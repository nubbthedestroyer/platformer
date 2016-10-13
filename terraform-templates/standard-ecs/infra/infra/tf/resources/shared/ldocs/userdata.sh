#!/bin/bash

############################
#### Cluster name here: ####
source /etc/plat_name.sh
############################

mkdir -p /ecs/webdata

#sleep 60

/usr/bin/docker run --name ecs-agent \
--detach=true \
--restart=on-failure:10 \
--volume=/var/run/docker.sock:/var/run/docker.sock \
--volume=/var/log/ecs/:/log \
--volume=/var/lib/ecs/data:/data \
--volume=/sys/fs/cgroup:/sys/fs/cgroup:ro \
--volume=/var/run/docker/execdriver/native:/var/lib/docker/execdriver/native:ro \
--publish=127.0.0.1:51678:51678 \
--env=ECS_LOGFILE=/log/ecs-agent.log \
--env=ECS_LOGLEVEL=debug \
--env=ECS_DATADIR=/data \
--env=ECS_CLUSTER=${plat_name}-ECS-Cluster \
--env=ECS_AVAILABLE_LOGGING_DRIVERS=[\"json-file\",\"awslogs\"] \
amazon/amazon-ecs-agent:latest

source /etc/plat_name.sh

read -r -d '' startecs << EOM
#!/bin/bash

#sleep 120

/usr/bin/docker rm ecs-agent || true
/usr/bin/docker run --name ecs-agent \\
--detach=true \\
--restart=on-failure:10 \\
--volume=/var/run/docker.sock:/var/run/docker.sock \\
--volume=/var/log/ecs/:/log \\
--volume=/var/lib/ecs/data:/data \\
--volume=/sys/fs/cgroup:/sys/fs/cgroup:ro \\
--volume=/var/run/docker/execdriver/native:/var/lib/docker/execdriver/native:ro \\
--publish=127.0.0.1:51678:51678 \\
--env=ECS_LOGFILE=/log/ecs-agent.log \\
--env=ECS_LOGLEVEL=info \\
--env=ECS_DATADIR=/data \\
--env=ECS_CLUSTER=${plat_name}-ECS-Cluster \\
--env=ECS_AVAILABLE_LOGGING_DRIVERS=["json-file","awslogs"] \\
amazon/amazon-ecs-agent:latest
EOM

echo "$startecs" > /etc/startecs.sh
chmod +x /etc/startecs.sh

job="@reboot /etc/startecs.sh"
cat <(fgrep -i -v "${job}" <(crontab -l)) <(echo "$job") | crontab -

job="@daily ntpdate ntp.ubuntu.com"
cat <(fgrep -i -v "${job}" <(crontab -l)) <(echo "$job") | crontab -