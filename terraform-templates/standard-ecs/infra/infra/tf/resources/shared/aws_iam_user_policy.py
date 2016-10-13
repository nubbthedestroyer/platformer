#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_iam_user_policy': {
            plat_name + '-User-Policy': {
                'name': plat_name + '-User-Policy',
                'user': plat_name + '-User',
                'policy': docs['iam_user_policy'],
                'depends_on': [
                    "aws_iam_user." + plat_name + '-User'
                ]
            }
        }
    }
    return block
