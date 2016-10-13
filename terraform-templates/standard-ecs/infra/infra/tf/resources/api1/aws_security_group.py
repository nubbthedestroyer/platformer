#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_security_group': {
            ec2_sg: {
                'name': ec2_sg,
                'description': ec2_sg,
                'vpc_id': VPC['id'],
                'ingress': [
                    {
                        'from_port': 80,
                        'to_port': 80,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    },
                    {
                        'from_port': 443,
                        'to_port': 443,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    },
                    {
                        'from_port': 22,
                        'to_port': 22,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            '0.0.0.0/0'       # VPN server
                        ],
                    },
                    {
                        'from_port': 0,
                        'to_port': 65535,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "10.32.0.0/16"
                        ]
                    },
                    {
                        'from_port': iport,
                        'to_port': iport,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0",
                        ],
                    }
                ],
                'egress': [
                    {
                        'from_port': 0,
                        'to_port': 65535,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    },
                ],
                'lifecycle': {
                    'create_before_destroy': True
                }
            },
            ec2_sg_stage: {
                'name': ec2_sg_stage,
                'description': ec2_sg_stage,
                'vpc_id': VPC['id'],
                'ingress': [
                    {
                        'from_port': 80,
                        'to_port': 80,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    },
                    {
                        'from_port': 443,
                        'to_port': 443,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    },
                    {
                        'from_port': 22,
                        'to_port': 22,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"       # VPN server
                        ],
                    },
                    {
                        'from_port': iport,
                        'to_port': iport,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0",
                        ],
                    }
                ],
                'egress': [
                    {
                        'from_port': 0,
                        'to_port': 65535,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    },
                ],
                'lifecycle': {
                    'create_before_destroy': True
                }
            },
            elb_sg: {
                'name': elb_sg,
                'description': elb_sg,
                'vpc_id': VPC['id'],
                'ingress': [
                    {
                        'from_port': 80,
                        'to_port': 80,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    },
                    {
                        'from_port': 443,
                        'to_port': 443,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    },
                    {
                        'from_port': 22,
                        'to_port': 22,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"
                        ],
                    },
                    {
                        'from_port': iport,
                        'to_port': iport,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0",
                        ],
                    }
                ],
                'egress': [
                    {
                        'from_port': 0,
                        'to_port': 65535,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    },
                ],
                'lifecycle': {
                    'create_before_destroy': True
                }
            },
            elb_sg_stage: {
                'name': elb_sg_stage,
                'description': elb_sg_stage,
                'vpc_id': VPC['id'],
                'ingress': [
                    {
                        'from_port': 80,
                        'to_port': 80,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    },
                    {
                        'from_port': 443,
                        'to_port': 443,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    },
                    {
                        'from_port': 22,
                        'to_port': 22,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"
                        ],
                    },
                    {
                        'from_port': 8000,
                        'to_port': 9000,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0",
                        ],
                    },
                    {
                        'from_port': 3333,
                        'to_port': 3333,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0",
                        ],
                    }
                ],
                'egress': [
                    {
                        'from_port': 0,
                        'to_port': 65535,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    },
                ],
                'lifecycle': {
                    'create_before_destroy': True
                }
            },
            rds_db_sg: {
                'name': rds_db_sg,
                'description': rds_db_sg,
                'vpc_id': VPC['id'],
                'ingress': [
                    {
                        'from_port': 3306,
                        'to_port': 3306,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "10.99.0.0/16"
                        ],
                    }
                ],
                'egress': [
                    {
                        'from_port': 0,
                        'to_port': 65535,
                        'protocol': "tcp",
                        'cidr_blocks': [
                            "0.0.0.0/0"  # everywhere
                        ]
                    }
                ]
            }
        }
    }
    return block