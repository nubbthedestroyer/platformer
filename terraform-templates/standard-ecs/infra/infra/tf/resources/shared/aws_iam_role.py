#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_iam_role': {
            plat_name + "-IR": {
                'name': plat_name + "-IR",
                'assume_role_policy': docs['iam_ir']
            },
            plat_name + "-SR": {
                'name': plat_name + "-SR",
                'assume_role_policy': docs['iam_sr']
            }
        }
    }
    return block
