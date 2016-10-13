#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_ecs_service': {
            plat_name + "-" + mservice.upper() + "-Service": {
                'name': plat_name + "-" + mservice.upper() + "-Service",
                'cluster': plat_name + "-ECS-Cluster",
                'task_definition': "${aws_ecs_task_definition." + plat_name + "-" + mservice.upper() + "-ECS-Task-Def" + ".arn}",
                'desired_count': "3",
                'deployment_maximum_percent': "200",
                'deployment_minimum_healthy_percent': "10",
                'iam_role': plat_name + "-SR",
                'depends_on': ["aws_iam_policy." + plat_name + "-SR-Policy"],
                'load_balancer': {
                    'elb_name': elb,
                    'container_name': plat_name.lower() + "-" + mservice + "-prod",
                    'container_port': iport
                },
                'lifecycle': {
                    'ignore_changes': [
                        "task_definition"
                    ]
                }
            },
            plat_name + "-" + mservice.upper() + "-Service-Stage": {
                'name': plat_name + "-" + mservice.upper() + "-Service-Stage",
                'cluster': plat_name + "-ECS-Cluster-Stage",
                'task_definition': "${aws_ecs_task_definition." + plat_name + "-" + mservice.upper() + "-ECS-Task-Def-Stage" + ".arn}",
                'desired_count': "1",
                'deployment_maximum_percent': "200",
                'deployment_minimum_healthy_percent': "10",
                'iam_role': plat_name + "-SR",
                'depends_on': ["aws_iam_policy." + plat_name + "-SR-Policy"],
                'load_balancer': {
                    'elb_name': elb_stage,
                    'container_name': plat_name.lower() + "-" + mservice + "-stage",
                    'container_port': iport
                },
                'lifecycle': {
                    'ignore_changes': [
                        "task_definition"
                    ]
                }
            }
        }
    }
    return block
