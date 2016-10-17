#!/bin/bash

# set -e
# set -x

############################
#### Cluster name here: ####
source /etc/plat_name.sh
############################

echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) universe"

sudo apt-get update
sudo apt-get -y install ruby2.0
sudo apt-get -y install htop
sudo apt-get -y install unzip
sudo apt-get -y install python-pip
sudo apt-get -y install python
sudo apt-get -y install python-dev libwww-perl libcrypt-ssleay-perl libswitch-perl libdatetime-perl
sudo pip install awscli

#################################
#### Install apt-get-waiter #####
#################################
read -r -d '' aptgetwaiter << EOM
#!/bin/python
import fcntl


def is_dpkg_active():
    with open('/var/lib/dpkg/lock', 'w') as handle:
        try:
            fcntl.lockf(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return False
        except IOError:
            return True


print(is_dpkg_active())
EOM

echo "$aptgetwaiter" > /tmp/apt-get-waiter
chmod +x /tmp/apt-get-waiter

function waitforapt () {
    echo "Waiting for apt-get to be available."
    test="$(python /tmp/apt-get-waiter)"
    breaker="False"
    while [ "$breaker" == "False" ]; do
        test="$(python /tmp/apt-get-waiter)"
        if [ "$test" == "True" ]; then
            echo -n "."
        elif [ "$test" == "False" ]; then
            echo "Starting apt-get or dpkg install"
            breaker="True"
        fi
        sleep 4
    done
}

###############################
#### Cloudmon Provisioning ####
###############################
function cloudmoninstall () {
    (mkdir -p /etc/scripts
    cd /etc/scripts/
    curl http://aws-cloudwatch.s3.amazonaws.com/downloads/CloudWatchMonitoringScripts-1.2.1.zip -O
    unzip CloudWatchMonitoringScripts-1.2.1.zip
    rm CloudWatchMonitoringScripts-1.2.1.zip
    cd aws-scripts-mon
    mv * /etc/scripts/
    chmod +x /etc/scripts/*.pl
    chmod +x /etc/scripts/*.pm
    crontab -l > crontabbackup
    job1="*/1 * * * * /etc/scripts/mon-put-instance-data.pl --mem-util --mem-used --mem-avail --auto-scaling=only"
    cat <(fgrep -i -v "${job1}" <(crontab -l)) <(echo "$job1") | crontab -
    job2="*/1 * * * * /etc/scripts/mon-put-instance-data.pl --disk-space-util --disk-path=/ --auto-scaling=only"
    cat <(fgrep -i -v "${job2}" <(crontab -l)) <(echo "$job2") | crontab -
    cd) 2>&1 | tee -a /var/log/cloud-init-output-cloudmon.log
}

cloudmoninstall


function usercreate () {
    user="${1}"
    sshkey="${2}"
    sudo useradd -m -d /home/${user} -s /bin/bash -U ${user} &&
    sudo mkdir -p /home/${user}/.ssh &&
    sudo touch /home/${user}/.ssh/authorized_keys &&
    sudo echo $sshkey > /home/${user}/.ssh/authorized_keys &&
    sudo chmod 644 /home/${user}/.ssh/authorized_keys &&
    sudo chmod 755 /home/${user}/.ssh &&
    sudo adduser ${user} sudo &&
    sudo adduser ${user} admin &&
    sudo adduser ${user} adm
}

usercreate "user1" "<users ssh public key>"

read -r -d '' sudoers << EOM
Defaults        env_reset
Defaults        mail_badpass
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
root    ALL=(ALL:ALL) ALL
%admin ALL=(ALL) NOPASSWD:ALL
%sudo   ALL=(ALL:ALL) NOPASSWD:ALL
EOM

echo "$sudoers" > /etc/sudoers

##########################
#### App config block ####
##########################

read -r -d '' logs_configer << 'FULLEOM'
#!/bin/bash

source /etc/plat_name.sh

host_log_dir='/ecs/webdata/'

mkdir -p ${host_log_dir}

rm -f /tmp/awslogs.conf

read -r -d '' general_config << EOM
[general]
state_file = /var/awslogs/state/agent-state
EOM
echo "${general_config}" > /tmp/awslogs.conf

read -r -d '' logmain_config << EOM

[/var/log/ecs/ecs-agent.log*]
datetime_format = %b %d %H:%M:%S
file = /var/log/ecs/ecs-agent.log*
buffer_duration = 5000
log_stream_name = /var/log/ecs/ecs-agent.log
initial_position = end_of_file
log_group_name = ${plat_name,,}

[/var/log/syslog]
datetime_format = %b %d %H:%M:%S
file = /var/log/syslog
buffer_duration = 5000
log_stream_name = /var/log/syslog
initial_position = end_of_file
log_group_name = ${plat_name,,}

[/var/log/authlog]
datetime_format = %b %d %H:%M:%S
file = /var/log/authlog
buffer_duration = 5000
log_stream_name = /var/log/authlog
initial_position = end_of_file
log_group_name = ${plat_name,,}

[/var/log/cloud-init-output.log]
datetime_format = %b %d %H:%M:%S
file = /var/log/cloud-init-output.log
buffer_duration = 5000
log_stream_name = /var/log/cloud-init-output.log
initial_position = start_of_file
log_group_name = ${plat_name,,}
EOM

echo "${logmain_config}" >> /tmp/awslogs.conf

count=1
for folder in $(find ${host_log_dir} -type d); do
    for file in $(find ${folder} -type f); do
        filename="$(basename ${file})"
	log="${filename%.*}"
	read -r -d '' log_config << EOM

[${log}]
datetime_format = %b %d %H:%M:%S
file = ${file}
buffer_duration = 5000
log_stream_name = ${file}
initial_position = end_of_file
log_group_name = ${plat_name,,}
EOM
        echo "${log_config}" >> /tmp/awslogs.conf
    done
done


cd
curl --silent https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-agent-setup.py -O
sudo python ./awslogs-agent-setup.py --region us-east-1 --non-interactive --configfile=/tmp/awslogs.conf

service awslogs restart
FULLEOM

echo "$logs_configer" > /etc/logs_configer.sh
chmod +x /etc/logs_configer.sh

job="*/5 * * * * /etc/logs_configer.sh"
cat <(fgrep -i -v "${job}" <(crontab -l)) <(echo "$job") | crontab -

waitforapt && apt-get install -y apt-transport-https ca-certificates
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list
waitforapt && apt-get update
waitforapt && apt-get purge -y lxc-docker
apt-cache policy docker-engine
waitforapt && apt-get install -y linux-image-extra-$(uname -r)
waitforapt && apt-get install -y docker-engine