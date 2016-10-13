#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_iam_policy': {
            plat_name + "-IR-Policy": {
                'name': plat_name + "-IR-Policy",
                'policy': docs['iam_ir_policy']
            },
            plat_name + "-SR-Policy": {
                'name': plat_name + "-SR-Policy",
                'policy': docs['iam_sr_policy'],
            }
        },
    }
    return block
