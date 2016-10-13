#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_cloudwatch_log_group': {
            plat_name + '-Log-Group': {
                'name': plat_name.lower(),
                'retention_in_days': 14
            }
        }
    }
    return block
