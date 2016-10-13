#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_s3_bucket': {
            "elb-log-" + plat_name.lower(): {
                'bucket': "elb-log-" + plat_name.lower(),
                'acl': "public-read-write",
                'force_destroy': True
            },
            plat_name.lower(): {
                'bucket': plat_name.lower(),
                'force_destroy': False
            },
            plat_name.lower() + "-secure": {
                'bucket': plat_name.lower() + "-secure",
                'force_destroy': False
            }
        }
    }
    return block
