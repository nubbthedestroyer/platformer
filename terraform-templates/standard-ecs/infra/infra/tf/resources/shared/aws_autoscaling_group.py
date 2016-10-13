#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_autoscaling_group': {
            plat_name + "-" + mservice.upper() + "-ECS-ASG": {
                'availability_zones': [az['a'], az['b']],
                'name': plat_name + "-" + mservice.upper() + "-ECS-ASG",
                'max_size': 8,
                'min_size': 0,
                'desired_capacity': 3,
                'health_check_grace_period': 1100,
                'default_cooldown': 5,
                'health_check_type': 'EC2',
                'force_delete': True,
                'launch_configuration': "${aws_launch_configuration." + plat_name + "-" + mservice.upper() + "-LC" + ".name}",
                'vpc_zone_identifier': [
                    "${aws_subnet." + vpc_subnet_a['name'] + ".id}",
                    "${aws_subnet." + vpc_subnet_b['name'] + ".id}"
                ],
                'tag': [
                    {
                        'key': 'Name',
                        'value': plat_name.lower() + "-" + mservice.lower() + "-ecs-asg-node",
                        'propagate_at_launch': True
                    },
                    {
                        'key': 'Platform',
                        'value': plat_name.upper(),
                        'propagate_at_launch': True
                    }
                ],
            },
            plat_name + "-" + mservice.upper() + "-ECS-ASG-STAGE": {
                'availability_zones': [az['a'], az['b']],
                'name': plat_name + "-" + mservice.upper() + "-ECS-ASG-STAGE",
                'max_size': 4,
                'min_size': 0,
                'desired_capacity': 1,
                'health_check_grace_period': 1100,
                'default_cooldown': 5,
                'health_check_type': 'EC2',
                'launch_configuration': "${aws_launch_configuration." + plat_name + "-" + mservice.upper() + "-LC-STAGE" + ".name}",
                'vpc_zone_identifier': [
                    "${aws_subnet." + vpc_subnet_a['name'] + ".id}",
                    "${aws_subnet." + vpc_subnet_b['name'] + ".id}"
                ],
                'tag': [
                    {
                        'key': 'Name',
                        'value': plat_name.lower() + "-" + mservice.lower() + "-ecs-asg-stage-node",
                        'propagate_at_launch': True
                    },
                    {
                        'key': 'Platform',
                        'value': plat_name.upper(),
                        'propagate_at_launch': True
                    }
                ]
            },
        }
    }

    return block
