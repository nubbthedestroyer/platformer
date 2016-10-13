#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_iam_policy_attachment': {
            plat_name + "-IR" + "-Attachment": {
                'name': plat_name + "-IR" + "-Attachment",
                'roles': [
                    plat_name + "-IR"
                ],
                'policy_arn': "${aws_iam_policy." + plat_name + "-IR-Policy" + ".arn}",
                'depends_on': [
                    "aws_iam_role." + plat_name + "-IR",
                    "aws_iam_policy." + plat_name + "-IR-Policy",
                    "aws_iam_role." + plat_name + "-SR",
                    "aws_iam_policy." + plat_name + "-SR-Policy"
                ]
            },
            plat_name + "-SR" + "-Attachment": {
                'name': plat_name + "-SR" + "-Attachment",
                'roles': [
                    plat_name + "-SR"
                ],
                'policy_arn': "${aws_iam_policy." + plat_name + "-SR-Policy" + ".arn}",
                'depends_on': [
                    "aws_iam_role." + plat_name + "-IR",
                    "aws_iam_policy." + plat_name + "-IR-Policy",
                    "aws_iam_role." + plat_name + "-SR",
                    "aws_iam_policy." + plat_name + "-SR-Policy"
                ]
            }
        }
    }
    return block

