#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_cloudwatch_metric_alarm': {
            cw_prefix + "ELB-Latency-High": {
                'alarm_name': cw_prefix + "ELB-Latency",
                'comparison_operator': "GreaterThanOrEqualToThreshold",
                'evaluation_periods': "3",
                'metric_name': "Latency",
                'namespace': "AWS/ELB",
                'period': "60",
                'statistic': "Average",
                'threshold': "10",
                'dimensions': {
                    'LoadBalancerName': "${aws_elb." + elb + ".name}"
                },
                'alarm_description': cw_prefix + "ELB-Latency-High" + "-Over3secsfor3mins",
                'alarm_actions': [
                    sns
                ],
                'ok_actions': [
                    sns
                ]
            },
            # cw_prefix + "ELB-HealthyHosts-Low": {
            #     'alarm_name': cw_prefix + "ELB-HealthyHosts-Low",
            #     'comparison_operator': "LessThanOrEqualToThreshold",
            #     'evaluation_periods': "3",
            #     'metric_name': "HealthyHostCount",
            #     'namespace': "AWS/ELB",
            #     'period': "60",
            #     'statistic': "Average",
            #     'threshold': "0.5",
            #     'dimensions': {
            #         'LoadBalancerName': "${aws_elb." + elb + ".name}"
            #     },
            #     'alarm_description': cw_prefix + "ELB-HealthyHosts-Low" + "-Below1for3mins",
            #     'alarm_actions': [
            #         sns
            #     ],
            #     'ok_actions': [
            #         sns
            #     ]
            # },
            # cw_prefix + "ELB-UnHealthyHosts-High": {
            #     'alarm_name': cw_prefix + "ELB-UnHealthyHosts-High",
            #     'comparison_operator': "GreaterThanOrEqualToThreshold",
            #     'evaluation_periods': "3",
            #     'metric_name': "UnHealthyHostCount",
            #     'namespace': "AWS/ELB",
            #     'period': "60",
            #     'statistic': "Average",
            #     'threshold': "1.5",
            #     'dimensions': {
            #         'LoadBalancerName': "${aws_elb." + elb + ".name}"
            #     },
            #     'alarm_description': cw_prefix + "ELB-UnHealthyHosts-High" + "-Over1for3mins",
            #     'alarm_actions': [
            #         sns
            #     ],
            #     'ok_actions': [
            #         sns
            #     ]
            # },
            cw_prefix + "ELB-5xx-High": {
                'alarm_name': cw_prefix + "ELB-5xx-High",
                'comparison_operator': "GreaterThanOrEqualToThreshold",
                'evaluation_periods': "3",
                'metric_name': "HTTPCode_Backend_5XX",
                'namespace': "AWS/ELB",
                'period': "60",
                'statistic': "Average",
                'threshold': "10",
                'dimensions': {
                    'LoadBalancerName': "${aws_elb." + elb + ".name}"
                },
                'alarm_description': cw_prefix + "ELB-5xx-High" + "-Over10for3mins",
                'alarm_actions': [
                    sns
                ],
                'ok_actions': [
                    sns
                ]
            },
            cw_prefix + "ELB-4xx-High": {
                'alarm_name': cw_prefix + "ELB-4xx-High",
                'comparison_operator': "GreaterThanOrEqualToThreshold",
                'evaluation_periods': "3",
                'metric_name': "HTTPCode_Backend_4XX",
                'namespace': "AWS/ELB",
                'period': "60",
                'statistic': "Average",
                'threshold': "10",
                'dimensions': {
                    'LoadBalancerName': "${aws_elb." + elb + ".name}"
                },
                'alarm_description': cw_prefix + "ELB-4xx-High" + "-Over10for3mins",
                'alarm_actions': [
                    sns
                ],
                'ok_actions': [
                    sns
                ]
            },
            cw_prefix + "ELB-SurgeQueueLength-High": {
                'alarm_name': cw_prefix + "ELB-SurgeQueueLength-High",
                'comparison_operator': "GreaterThanOrEqualToThreshold",
                'evaluation_periods': "3",
                'metric_name': "SurgeQueueLength",
                'namespace': "AWS/ELB",
                'period': "60",
                'statistic': "Average",
                'threshold': "10",
                'dimensions': {
                    'LoadBalancerName': "${aws_elb." + elb + ".name}"
                },
                'alarm_description': cw_prefix + "ELB-SurgeQueueLength-High" + "-Over10for3mins",
                'alarm_actions': [
                    sns
                ],
                'ok_actions': [
                    sns
                ]
            },
            # cw_prefix + "RDS-CpuUtilization-High": {
            #     'alarm_name': cw_prefix + "RDS-CpuUtilization-High",
            #     'comparison_operator': "GreaterThanOrEqualToThreshold",
            #     'evaluation_periods': "5",
            #     'metric_name': "CPUUtilization",
            #     'namespace': "AWS/RDS",
            #     'period': "60",
            #     'statistic': "Average",
            #     'threshold': "90",
            #     'dimensions': {
            #         'LoadBalancerName': "${aws_db_instance." + rds_0 + ".name}"
            #     },
            #     'alarm_description': cw_prefix + "RDS-CpuUtilization-High" + "-Over90for5mins",
            #     'alarm_actions': [
            #         sns
            #     ],
            #     'ok_actions': [
            #         sns
            #     ]
            # },
            # cw_prefix + "RDS-FreeStorageSpace-Low": {
            #     'alarm_name': cw_prefix + "RDS-FreeStorageSpace-Low",
            #     'comparison_operator': "LessThanOrEqualToThreshold",
            #     'evaluation_periods': "1",
            #     'metric_name': "FreeStorageSpace",
            #     'namespace': "AWS/RDS",
            #     'period': "60",
            #     'statistic': "Average",
            #     'threshold': "10000000000",
            #     'dimensions': {
            #         'LoadBalancerName': "${aws_db_instance." + rds_0 + ".name}"
            #     },
            #     'alarm_description': cw_prefix + "RDS-FreeStorageSpace-Low" + "-Under10GB",
            #     'alarm_actions': [
            #         sns
            #     ],
            #     'ok_actions': [
            #         sns
            #     ]
            # },
            # cw_prefix + "RDS-DatabaseConnections-High": {
            #     'alarm_name': cw_prefix + "RDS-DatabaseConnections-High",
            #     'comparison_operator': "GreaterThanOrEqualToThreshold",
            #     'evaluation_periods': "5",
            #     'metric_name': "DatabaseConnections",
            #     'namespace': "AWS/RDS",
            #     'period': "60",
            #     'statistic': "Average",
            #     'threshold': "300",
            #     'dimensions': {
            #         'LoadBalancerName': "${aws_db_instance." + rds_0 + ".name}"
            #     },
            #     'alarm_description': cw_prefix + "RDS-FreeStorageSpace-Low" + "-Under10GB",
            #     'alarm_actions': [
            #         sns
            #     ],
            #     'ok_actions': [
            #         sns
            #     ]
            # },
            # cw_prefix + "RDS-FreeableMemory-High": {
            #     'alarm_name': cw_prefix + "RDS-FreeableMemory-High",
            #     'comparison_operator': "LessThanOrEqualToThreshold",
            #     'evaluation_periods': "5",
            #     'metric_name': "FreeableMemory",
            #     'namespace': "AWS/RDS",
            #     'period': "60",
            #     'statistic': "Average",
            #     'threshold': "1000000000",
            #     'dimensions': {
            #         'LoadBalancerName': "${aws_db_instance." + rds_0 + ".name}"
            #     },
            #     'alarm_description': cw_prefix + "RDS-FreeableMemory-Low" + "-Under1GB",
            #     'alarm_actions': [
            #         sns
            #     ],
            #     'ok_actions': [
            #         sns
            #     ]
            # },
            cw_prefix_stage + "ELB-Latency-High": {
                'alarm_name': cw_prefix_stage + "ELB-Latency",
                'comparison_operator': "GreaterThanOrEqualToThreshold",
                'evaluation_periods': "3",
                'metric_name': "Latency",
                'namespace': "AWS/ELB",
                'period': "60",
                'statistic': "Average",
                'threshold': "10",
                'dimensions': {
                    'LoadBalancerName': "${aws_elb." + elb_stage + ".name}"
                },
                'alarm_description': cw_prefix_stage + "ELB-Latency-High" + "-Over3secsfor3mins",
                'alarm_actions': [
                    sns
                ],
                'ok_actions': [
                    sns
                ]
            },
            # cw_prefix_stage + "ELB-HealthyHosts-Low": {
            #     'alarm_name': cw_prefix_stage + "ELB-HealthyHosts-Low",
            #     'comparison_operator': "LessThanOrEqualToThreshold",
            #     'evaluation_periods': "3",
            #     'metric_name': "HealthyHostCount",
            #     'namespace': "AWS/ELB",
            #     'period': "60",
            #     'statistic': "Average",
            #     'threshold': "0.5",
            #     'dimensions': {
            #         'LoadBalancerName': "${aws_elb." + elb_stage + ".name}"
            #     },
            #     'alarm_description': cw_prefix_stage + "ELB-HealthyHosts-Low" + "-Below1for3mins",
            #     'alarm_actions': [
            #         sns
            #     ],
            #     'ok_actions': [
            #         sns
            #     ]
            # },
            # cw_prefix_stage + "ELB-UnHealthyHosts-High": {
            #     'alarm_name': cw_prefix_stage + "ELB-UnHealthyHosts-High",
            #     'comparison_operator': "GreaterThanOrEqualToThreshold",
            #     'evaluation_periods': "3",
            #     'metric_name': "UnHealthyHostCount",
            #     'namespace': "AWS/ELB",
            #     'period': "60",
            #     'statistic': "Average",
            #     'threshold': "1.5",
            #     'dimensions': {
            #         'LoadBalancerName': "${aws_elb." + elb_stage + ".name}"
            #     },
            #     'alarm_description': cw_prefix_stage + "ELB-UnHealthyHosts-High" + "-Over1for3mins",
            #     'alarm_actions': [
            #         sns
            #     ],
            #     'ok_actions': [
            #         sns
            #     ]
            # },
            cw_prefix_stage + "ELB-5xx-High": {
                'alarm_name': cw_prefix_stage + "ELB-5xx-High",
                'comparison_operator': "GreaterThanOrEqualToThreshold",
                'evaluation_periods': "3",
                'metric_name': "HTTPCode_Backend_5XX",
                'namespace': "AWS/ELB",
                'period': "60",
                'statistic': "Average",
                'threshold': "10",
                'dimensions': {
                    'LoadBalancerName': "${aws_elb." + elb_stage + ".name}"
                },
                'alarm_description': cw_prefix_stage + "ELB-5xx-High" + "-Over10for3mins",
                'alarm_actions': [
                    sns
                ],
                'ok_actions': [
                    sns
                ]
            },
            cw_prefix_stage + "ELB-4xx-High": {
                'alarm_name': cw_prefix_stage + "ELB-4xx-High",
                'comparison_operator': "GreaterThanOrEqualToThreshold",
                'evaluation_periods': "3",
                'metric_name': "HTTPCode_Backend_4XX",
                'namespace': "AWS/ELB",
                'period': "60",
                'statistic': "Average",
                'threshold': "10",
                'dimensions': {
                    'LoadBalancerName': "${aws_elb." + elb_stage + ".name}"
                },
                'alarm_description': cw_prefix_stage + "ELB-4xx-High" + "-Over10for3mins",
                'alarm_actions': [
                    sns
                ],
                'ok_actions': [
                    sns
                ]
            },
            cw_prefix_stage + "ELB-SurgeQueueLength-High": {
                'alarm_name': cw_prefix_stage + "ELB-SurgeQueueLength-High",
                'comparison_operator': "GreaterThanOrEqualToThreshold",
                'evaluation_periods': "3",
                'metric_name': "SurgeQueueLength",
                'namespace': "AWS/ELB",
                'period': "60",
                'statistic': "Average",
                'threshold': "10",
                'dimensions': {
                    'LoadBalancerName': "${aws_elb." + elb_stage + ".name}"
                },
                'alarm_description': cw_prefix_stage + "ELB-SurgeQueueLength-High" + "-Over10for3mins",
                'alarm_actions': [
                    sns
                ],
                'ok_actions': [
                    sns
                ]
            },
        }
    }

    return block
