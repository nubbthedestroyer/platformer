#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_ecs_cluster': {
            plat_name + "-ECS-Cluster": {
                'name': plat_name + "-ECS-Cluster"
            },
            plat_name + "-ECS-Cluster-Stage": {
                'name': plat_name + "-ECS-Cluster-Stage"
            }
        }
    }
    return block
