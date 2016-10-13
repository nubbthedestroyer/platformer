#!/usr/bin/env bash
set -e

branch="${1}"
platform="${2}"
mservice="${3}"
port="${4}"
stage="${5}"
cwd=`dirname $0`

# ensure we have enough params to run
if [[ -z ${branch} || -z ${platform}  || -z ${mservice}  || -z ${port}  || -z ${stage} ]]; then
    echo "Missing a required param! [branch: ${branch}], [platform: ${platform},  [mservice: ${mservice}], [port: ${port}], [stage: ${stage}]"
    exit 1
fi

# BUILD BELOW #