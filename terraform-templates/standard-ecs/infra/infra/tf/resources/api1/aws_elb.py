#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_elb': {
            elb: {
                'name': elb,
                'subnets': [
                    "${aws_subnet." + vpc_subnet_elba['name'] + ".id}",
                    "${aws_subnet." + vpc_subnet_elbb['name'] + ".id}"
                ],
                'access_logs': {
                    'bucket': s3_elb_log,
                    'bucket_prefix': elb,
                    'interval': 5
                },
                'listener': [
                    {
                        'instance_port': iport,
                        'instance_protocol': 'http',
                        'lb_port': 80,
                        'lb_protocol': 'http'
                    },
                    {
                        'instance_port': iport,
                        'instance_protocol': 'http',
                        'lb_port': 443,
                        'lb_protocol': 'https',
                        'ssl_certificate_id': ssl
                    }
                ],
                'health_check': {
                    'healthy_threshold': 2,
                    'unhealthy_threshold': 2,
                    'timeout': 4,
                    'target': "TCP:" + iport,
                    'interval': 5
                },
                'cross_zone_load_balancing': True,
                'connection_draining': True,
                'connection_draining_timeout': 60,
                'security_groups': [
                    "${aws_security_group." + elb_sg + ".id}"
                ]
            },
            elb_stage: {
                'name': elb_stage,
                'subnets': [
                    "${aws_subnet." + vpc_subnet_elba['name'] + ".id}",
                    "${aws_subnet." + vpc_subnet_elbb['name'] + ".id}"
                ],
                'access_logs': {
                    'bucket': s3_elb_log,
                    'bucket_prefix': elb_stage,
                    'interval': 5
                },
                'listener': [
                    {
                        'instance_port': iport,
                        'instance_protocol': 'http',
                        'lb_port': 80,
                        'lb_protocol': 'http'
                    },
                    {
                        'instance_port': iport,
                        'instance_protocol': 'http',
                        'lb_port': 443,
                        'lb_protocol': 'https',
                        'ssl_certificate_id': ssl
                    }
                ],
                'health_check': {
                    'healthy_threshold': 2,
                    'unhealthy_threshold': 2,
                    'timeout': 4,
                    'target': "TCP:" + iport,
                    'interval': 5
                },
                'cross_zone_load_balancing': True,
                'connection_draining': True,
                'connection_draining_timeout': 60,
                'security_groups': [
                    "${aws_security_group." + elb_sg_stage + ".id}"
                ]
            }
        }
    }
    return block
