#!/usr/bin/env bash

branch="${1}"
platform="${2}"
mservice="${3}"
port="${4}"
stage="${5}"
ecr_host="${6}"
cwd=`dirname $0`
cluster=${platform^}-ECS-Cluster
ecsservice=${platform^}-${mservice^^}-Service
dockerfile=Dockerfile.${mservice}
docker_build_host="docker.example.com"

# ensure we have enough params to run
if [[ -z ${branch} || -z ${platform}  || -z ${mservice}  || -z ${port}  || -z ${stage} ]]; then
    echo "Missing a required param! [branch: ${branch}], [platform: ${platform},  [mservice: ${mservice}], [port: ${port}], [stage: ${stage}]"
    exit 1
fi

# Custom string postfix added manually for now.
if [[ "${stage}" == "stage" ]]; then
    cluster="${cluster}-Stage"
    ecsservice="${ecsservice}-Stage"
fi

# Start deploy logic
echo "[Info]: Branch is : ${branch}"

set -e

cmd="`aws ecr get-login --region us-east-1`"
fullcmd=`echo "$cmd" | sed -e "s/docker/docker \-H tcp\:\/\/${docker_build_host}\:4243/g"`

echo "Setting some container def variables..."
cat infra/task-definition-template-${mservice}.json |\
sed \
    -e "s/platname/${platform}/g" \
    -e "s/mservice/${mservice}/g" \
    -e "s/thisenv/${stage}/g" \
    -e "s/thisport/${port}/g" \
    > infra/task-definition-finished-${mservice}.json

echo "Logging into Travis-Docker node..."
$fullcmd

if [[ ! -f "${cwd}/../${dockerfile}" ]]; then
    if [[ -f "${cwd}/../Dockerfile" ]]; then
        dockerfile="Dockerfile"
    else
        error "[Missing Docker File]::[${dockerfile}]"
        exit 1
    fi
fi

echo "Building image from ${dockerfile}..."
docker -H tcp://${docker_build_host}:4243 build -t ${platform}-${mservice}-${stage} -f ${dockerfile} .

echo "Tagging built image..."
docker -H tcp://${docker_build_host}:4243 tag ${platform}-${mservice}-${stage}:latest ${ecr_host}/${platform}-${mservice}-${stage}:latest
CURRENT_VERSION=$(git describe --abbrev=0) && docker -H tcp://${docker_build_host}:4243 tag ${platform}-${mservice}-${stage}:latest ${ecr_host}/${platform}-${mservice}-${stage}:${CURRENT_VERSION}

echo "Pushing image..."
docker -H tcp://${docker_build_host}:4243 push ${ecr_host}/${platform}-${mservice}-${stage}:latest
[[ ! -z "${CURRENT_VERSION}" ]] && docker -H tcp://${docker_build_host}:4243 push ${ecr_host}/${platform}-${mservice}-${stage}:${CURRENT_VERSION}

echo "Creating ECS deployment... cluster:" ${cluster}
aws ecs register-task-definition --region "us-east-1" --family ${platform}-${mservice}-${stage} --cli-input-json file://infra/task-definition-finished-${mservice}.json
aws ecs update-service --region "us-east-1" --cluster ${cluster} --service ${ecsservice} --task-definition ${platform}-${mservice}-${stage}