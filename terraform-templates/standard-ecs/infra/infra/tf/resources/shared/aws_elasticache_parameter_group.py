#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_elasticache_parameter_group': {
            plat_name.lower() + "-" + mservice + "-ec": {
                'name': plat_name.lower() + "-" + mservice + "-ec",
                'family': 'redis2.8',
                'description': plat_name.lower() + "-" + mservice + "-ec"
            },
            plat_name.lower() + "-" + mservice + "-ec-m": {
                'name': plat_name.lower() + "-" + mservice + "-ec-m",
                'family': 'memcached1.4',
                'description': plat_name.lower() + "-" + mservice + "-ec-m"
            }
        }
    }
    return block
