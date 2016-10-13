#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_subnet': {
            vpc_subnet_a['name']: {
                'availability_zone': vpc_subnet_a['az'],
                'cidr_block': vpc_subnet_a['cidr'],
                'map_public_ip_on_launch': True,
                'vpc_id': vpc_subnet_a['vpc_id'],
                'tags': {
                    'Name': str(vpc_subnet_a['name'])
                }
            },
            vpc_subnet_b['name']: {
                'availability_zone': vpc_subnet_b['az'],
                'cidr_block': vpc_subnet_b['cidr'],
                'map_public_ip_on_launch': True,
                'vpc_id': vpc_subnet_b['vpc_id'],
                'tags': {
                    'Name': str(vpc_subnet_b['name'])
                }
            },
            vpc_subnet_nat['name']: {
                'availability_zone': vpc_subnet_nat['az'],
                'cidr_block': vpc_subnet_nat['cidr'],
                'map_public_ip_on_launch': True,
                'vpc_id': vpc_subnet_nat['vpc_id'],
                'tags': {
                    'Name': str(vpc_subnet_nat['name'])
                }
            },
            vpc_subnet_elba['name']: {
                'availability_zone': vpc_subnet_elba['az'],
                'cidr_block': vpc_subnet_elba['cidr'],
                'map_public_ip_on_launch': True,
                'vpc_id': vpc_subnet_elba['vpc_id'],
                'tags': {
                    'Name': str(vpc_subnet_elba['name'])
                }
            },
            vpc_subnet_elbb['name']: {
                'availability_zone': vpc_subnet_elbb['az'],
                'cidr_block': vpc_subnet_elbb['cidr'],
                'map_public_ip_on_launch': True,
                'vpc_id': vpc_subnet_elbb['vpc_id'],
                'tags': {
                    'Name': str(vpc_subnet_elbb['name'])
                }
            }
        }
    }
    return block
