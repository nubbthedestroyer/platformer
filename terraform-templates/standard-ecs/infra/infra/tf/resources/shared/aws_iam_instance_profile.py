#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_iam_instance_profile': {
            plat_name + "-IR": {
                'name': plat_name + "-IR",
                'roles': [
                    plat_name + "-IR"
                ],
                'depends_on': [
                    "aws_iam_role." + plat_name + "-IR",
                    "aws_iam_policy." + plat_name + "-IR-Policy",
                    "aws_iam_role." + plat_name + "-SR",
                    "aws_iam_policy." + plat_name + "-SR-Policy",
                ]
            },
            plat_name + "-SR": {
                'name': plat_name + "-SR",
                'roles': [
                    plat_name + "-SR"
                ],
                'depends_on': [
                    "aws_iam_role." + plat_name + "-IR",
                    "aws_iam_policy." + plat_name + "-IR-Policy",
                    "aws_iam_role." + plat_name + "-SR",
                    "aws_iam_policy." + plat_name + "-SR-Policy",
                ]
            }
        }
    }
    return block
