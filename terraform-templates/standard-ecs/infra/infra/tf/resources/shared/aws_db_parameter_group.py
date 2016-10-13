#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_db_parameter_group': {
            plat_name.lower() + mservice.lower() + 'db': {
                'name': plat_name.lower() + mservice.lower() + "db",
                'family': "mysql5.6",
                'description': plat_name.lower() + mservice.lower() + "db",
                'parameter': [
                    {
                        'name': 'max_connections',
                        'value': '100000'
                    }
                ]
            },
        }
    }
    return block