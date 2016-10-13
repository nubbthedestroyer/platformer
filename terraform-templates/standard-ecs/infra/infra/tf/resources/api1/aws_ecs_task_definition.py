#!/bin/python


def run():
    from .. import variables
    import localvars
    import simplejson as json

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    container1 = [
        {
            "name": plat_name.lower() + "-" + mservice + "-prod",
            "image": aws_account_id + ".dkr.ecr.us-east-1.amazonaws.com/" + plat_name.lower() + "-" + mservice + "-prod:latest",
            "cpu": 7000,
            "memory": 6000,
            "portMappings": [
                {
                    "containerPort": int(iport),
                    "hostPort": int(iport),
                    "protocol": "tcp"
                }
            ],
            "mountPoints": [
                {
                    "containerPath": "/var/log/",
                    "sourceVolume": "webdata"
                }
            ],
            "essential": True
        }
    ]

    container2 = [
        {
            "name": plat_name.lower() + "-" + mservice + "-stage",
            "image": aws_account_id + ".dkr.ecr.us-east-1.amazonaws.com/" + plat_name.lower() + "-" + mservice + "-stage:latest",
            "cpu": 1024,
            "memory": 1024,
            "portMappings": [
                {
                    "containerPort": int(iport),
                    "hostPort": int(iport),
                    "protocol": "tcp"
                }
            ],
            "mountPoints": [
                {
                    "containerPath": "/var/log/",
                    "sourceVolume": "webdata"
                }
            ],
            "essential": True
        }
    ]

    block = {
        'aws_ecs_task_definition': {
            plat_name + "-" + mservice.upper() + "-ECS-Task-Def": {
                'family': plat_name.lower() + "-" + mservice + "-prod",
                'container_definitions': json.dumps(container1),
                "volume": [
                    {
                        "name": "webdata",
                        "host_path": "/ecs/webdata/" + mservice
                    }
                ],
            },
            plat_name + "-" + mservice.upper() + "-ECS-Task-Def-Stage": {
                'family': plat_name.lower() + "-" + mservice + "-stage",
                'container_definitions': json.dumps(container2),
                "volume": [
                    {
                        "name": "webdata",
                        "host_path": "/ecs/webdata/" + mservice
                    }
                ],
            }
        }
    }
    return block

