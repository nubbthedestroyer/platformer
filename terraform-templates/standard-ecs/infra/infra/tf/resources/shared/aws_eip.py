#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_eip': {
            vpc_natgw_eip: {
                'vpc': True
            }
        }
    }
    return block

