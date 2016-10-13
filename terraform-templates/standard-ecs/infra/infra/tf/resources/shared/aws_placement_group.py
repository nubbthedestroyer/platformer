#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_placement_group': {
            aws_pg: {
                'name': aws_pg,
                'strategy': 'cluster'
            }
        }
    }
    return block

