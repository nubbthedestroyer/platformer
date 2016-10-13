#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_db_subnet_group': {
            plat_name.lower(): {
                'name': plat_name.lower(),
                'description': plat_name.lower(),
                'subnet_ids': [
                    "${aws_subnet." + vpc_subnet_a['name'] + ".id}",
                    "${aws_subnet." + vpc_subnet_b['name'] + ".id}"
                ],
                'tags': {
                    'Name': plat_name.lower()
                }
            }
        }
    }
    return block
