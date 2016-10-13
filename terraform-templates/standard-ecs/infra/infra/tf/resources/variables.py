#!/bin/python
import os
import simpleyaml as yaml
from os.path import expanduser

var = {}
tvar = {}


def setvars():
    global var
    global tvar

    var = {}
    tvar = {}
    tvar['resource'] = {}

    # AWS account ID
    # Needed for ECS implementations
    var['aws_account_id'] = "12345678910"

    # Set your platform name
    var['plat_name'] = "TemplateECS"

    # set the AWS region.
    var['region']   = "us-east-1"

    var['root_domain'] = 'example.com'

    # other configs needed
    var['instance_type'] = "t2.medium"
    var['ssh_key_pair'] = "cluster"
    var['VPC'] = {
        'name': 'MAIN-VPC',
        'id': 'vpc-dgye649g',
        'igw': 'igw-37fb6894'
    }
    var['az'] = {
        'a': 'us-east-1a',
        'b': 'us-east-1b',
        'c': 'us-east-1c',
        'd': 'us-east-1d',
        'e': 'us-east-1e'
    }

    # Route53 Stuff
    var['r53_zone_id'] = 'FSH64J9R67SHV5'

    # SNS alert ARN
    var['sns'] = "arn:aws:sns:us-east-1:12345678910:sns-topic"

    # SSL cert
    var['ssl'] = "arn:aws:acm:us-east-1:12345678910:certificate/<cert-id>"

    var['stamp'] = ''

    var['iam_user'] = var['plat_name'] + "-User"
    var['iam_user_policy'] = var['plat_name'] + "-User-Policy"
    var['iam_ir'] = var['plat_name'] + "-IR"
    var['iam_ir_profile'] = var['iam_ir'] + "-Profile"
    var['iam_ir_policy'] = var['plat_name'] + "-IR-Policy"
    var['iam_sr'] = var['plat_name'] + "-SR"
    var['iam_sr_profile'] = var['iam_sr'] + "-Profile"
    var['iam_sr_policy'] = var['plat_name'] + "-SR-Policy"
    var['s3_elb_log'] = "elb-log-" + var['plat_name'].lower()
    var['aws_pg'] = var['plat_name'] + "-PG"
    var['aws_vpc'] = var['VPC']['name']
    var['vpc_subnet_a'] = {
        'name': var['aws_vpc'] + "-" + var['plat_name'] + "-A",
        'az': var['az']['a'],
        'cidr': '10.99.110.0/24',
        'vpc_id': var['VPC']['id']
    }
    var['vpc_subnet_b'] = {
        'name': var['aws_vpc'] + "-" + var['plat_name'] + "-B",
        'az': var['az']['b'],
        'cidr': '10.99.111.0/24',
        'vpc_id': var['VPC']['id']
    }
    var['vpc_subnet_nat'] = {
        'name': var['aws_vpc'] + "-" + var['plat_name'] + "-NAT",
        'az': var['az']['a'],
        'cidr': '10.99.112.0/24',
        'vpc_id': var['VPC']['id']
    }
    var['vpc_subnet_elba'] = {
        'name': var['aws_vpc'] + "-" + var['plat_name'] + "-ELBA",
        'az': var['az']['a'],
        'cidr': '10.99.113.0/24',
        'vpc_id': var['VPC']['id']
    }
    var['vpc_subnet_elbb'] = {
        'name': var['aws_vpc'] + "-" + var['plat_name'] + "-ELBB",
        'az': var['az']['b'],
        'cidr': '10.99.114.0/24',
        'vpc_id': var['VPC']['id']
    }
    var['vpc_rt'] = var['VPC']['name'] + "-" + var['plat_name'] + "-RT"
    var['vpc_rt_assoc_a'] = var['VPC']['name'] + "-" + var['plat_name'] + "-RT-ASSOC-A"
    var['vpc_rt_assoc_b'] = var['VPC']['name'] + "-" + var['plat_name'] + "-RT-ACCOC-B"
    var['vpc_rt_assoc_elba'] = var['VPC']['name'] + "-" + var['plat_name'] + "-RT-ASSOC-ELBA"
    var['vpc_rt_assoc_elbb'] = var['VPC']['name'] + "-" + var['plat_name'] + "-RT-ACCOC-ELBB"
    var['vpc_rt_nat_assoc'] = var['VPC']['name'] + "-" + var['plat_name'] + "-RT-NAT-ASSOC"
    var['vpc_rt_nat'] = var['VPC']['name'] + "-" + var['plat_name'] + "-RT-NAT"
    var['vpc_rt_elba'] = var['VPC']['name'] + "-" + var['plat_name'] + "-RT-ELBA"
    var['vpc_rt_elbb'] = var['VPC']['name'] + "-" + var['plat_name'] + "-RT-ELBB"
    var['vpc_igw'] = var['VPC']['name'] + "-" + var['plat_name'] + "-IGW"
    var['vpc_natgw'] = var['VPC']['name'] + "-" + var['plat_name'] + "-NATGW"
    var['vpc_natgw_eip'] = var['VPC']['name'] + "-" + var['plat_name'] + "-NATGW-EIP"
    var['cd'] = {
        'app': var['plat_name'] + "-App",
        'deploy_cfg': "CodeDeployDefault.AllAtOnce"
    }

    # print(var)

    for key, value in var.iteritems():
        exec(key + ' = ' + 'value')

    # set tvar and base variables
    tvar['variable'] = {
        'ami': {
            'description': var['base_ami'],
            'default': {
                var['region']: var['base_ami']
            }
        }
    }

    tvar['provider'] = {
        'aws': {
            'region': var['region']
        }
    }

    # set aws resources to create and manage.
    var['docs'] = {}
    cwd = os.getcwd()
    cwd = cwd + "/docs"

    if (os.path.isdir(cwd)):
        for f in os.listdir(cwd):
            var['docs'][f] = open(cwd + "/" + f).read()
        # print(json.dumps(var, indent=4, sort_keys=True))
        # print(json.dumps(tvar, indent=4, sort_keys=True))


setvars()
