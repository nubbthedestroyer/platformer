#!/bin/python

import os
import simplejson as json
import sys
from os import path

# Add relative path so we can import the base defined variables.
app_path = path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ))
sys.path.append(app_path)

import variables

# bring base defined variables into scope.
for key, value in variables.var.iteritems():
    exec(key + ' = ' + 'value')

def localdir():
    str1 = os.path.dirname(os.path.realpath(__file__))
    str2 = str1.split('/')
    n = len(str2)
    return str2[n - 2]

block = {
    "builders": [
        {
            "type": "amazon-ebs",
            "source_ami": "ami-fce3c696", # or whatever the current ubuntu image
            "region": "us-east-1",
            "instance_type": "t2.large",
            "iam_instance_profile": "packer",
            "ssh_username": "ubuntu",
            "ami_name": plat_name + "-" + localdir() + "-{{timestamp}}",
            "vpc_id": '<your_vpc>',     # packer VPC
            "subnet_id": '<your_subnet>',    # packer subnet
            "associate_public_ip_address": True,
            "ami_description": "@author: Packer",
            "tags": {
                "platform" : plat_name
            }
        }
    ],
    "provisioners": [
        {
            "type": "shell",
            "execute_command": "echo '' | sudo -S su - root -c '{{ .Path }}'",
            "scripts": [
                "plat_name.sh",
                "prebake.sh"
            ]
        }
    ]
}

f1 = open('packer-config.json', 'w+')
f1.write(json.dumps(block, indent=4, sort_keys=True))
f1.close()