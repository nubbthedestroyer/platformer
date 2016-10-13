#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_launch_configuration': {
            plat_name + "-" + mservice.upper() + "-LC": {
                'name_prefix': plat_name + "-LC-",
                'image_id': "ami-be991fa9",
                'instance_type': "m4.xlarge",
                'iam_instance_profile': "${aws_iam_instance_profile." + plat_name + "-IR" + ".arn}",
                'key_name': ssh_key_pair,
                'user_data': ldocs['userdata.sh'],
                'security_groups': [
                    "${aws_security_group." + ec2_sg + ".id}"
                ],
                'associate_public_ip_address': True,
                'lifecycle': {
                    'create_before_destroy': True
                },
                'depends_on': [
                    "aws_iam_instance_profile." + plat_name + "-IR",
                    "aws_iam_instance_profile." + plat_name + "-SR"
                ]
            },
            plat_name + "-" + mservice.upper() + "-LC-STAGE": {
                'name_prefix': plat_name + "-LC-Stage-",
                'image_id': "ami-be991fa9",
                'instance_type': 'm3.medium',
                'iam_instance_profile': "${aws_iam_instance_profile." + plat_name + "-IR" + ".arn}",
                'key_name': ssh_key_pair,
                'user_data': ldocs['userdata-stage.sh'],
                'security_groups': [
                    "${aws_security_group." + ec2_sg + ".id}"
                ],
                'associate_public_ip_address': True,
                'lifecycle': {
                    'create_before_destroy': True
                },
                'depends_on': [
                    "aws_iam_instance_profile." + plat_name + "-IR",
                    "aws_iam_instance_profile." + plat_name + "-SR"
                ]
            }
        }
    }
    return block