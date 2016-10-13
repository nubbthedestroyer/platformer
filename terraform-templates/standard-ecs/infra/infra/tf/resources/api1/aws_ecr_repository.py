#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_ecr_repository': {
            plat_name.lower() + "-" + mservice + "-prod": {
                'name': plat_name.lower() + "-" + mservice + "-prod"
            },
            plat_name.lower() + "-" + mservice + "-stage": {
                'name': plat_name.lower() + "-" + mservice + "-stage"
            }
        }
    }
    return block
