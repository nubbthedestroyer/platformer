#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_route_table': {
            vpc_rt: {
                'vpc_id': VPC['id'],
                'route': [
                    # {
                    #     'cidr_block': "0.0.0.0/0",
                    #     'gateway_id': VPC['igw']
                    # },
                    {
                        'cidr_block': "0.0.0.0/0",
                        'nat_gateway_id': "${aws_nat_gateway." + vpc_natgw + ".id}"
                    },
                    {
                        'cidr_block': "207.7.117.122/32",
                        'gateway_id': VPC['igw']
                    },
                    {
                        'cidr_block': "207.7.117.124/32",
                        'gateway_id': VPC['igw']
                    },
                    {
                        'cidr_block': "54.83.32.174/32",
                        'gateway_id': VPC['igw']
                    },
                    {
                        'cidr_block': "98.173.145.114/32",
                        'gateway_id': VPC['igw']
                    },
                    {
                        'cidr_block': "54.163.226.2/32",   # newetl server external
                        'gateway_id': VPC['igw']
                    },
                    {
                        'cidr_block': "10.58.93.152/32",   # newetl server internal
                        'gateway_id': VPC['igw']
                    },
                    {
                        'cidr_block': "54.225.132.202/32",  # edum 4
                        'gateway_id': VPC['igw']
                    },
                    {
                        'cidr_block': "54.89.203.205/32",   # edum 3
                        'gateway_id': VPC['igw']
                    },
                    {
                        'cidr_block': "54.225.15.54/32",    # edum 2
                        'gateway_id': VPC['igw']
                    },
                    {
                        'cidr_block': "174.129.154.33/32",  # edum 1
                        'gateway_id': VPC['igw']
                    },
                    {
                        'cidr_block': "65.127.24.220/32",
                        'nat_gateway_id': "${aws_nat_gateway." + vpc_natgw + ".id}"
                    },
                    {
                        'cidr_block': "65.127.24.221/32",
                        'nat_gateway_id': "${aws_nat_gateway." + vpc_natgw + ".id}"
                    }
                ],
                'tags': {
                    'Name': vpc_rt
                }
            },
            vpc_rt_nat: {
                'vpc_id': VPC['id'],
                'route': [
                    {
                        'cidr_block': "0.0.0.0/0",
                        'gateway_id': VPC['igw']
                    }
                ],
                'tags': {
                    'Name': vpc_rt_nat
                }
            }
        }
    }
    return block
