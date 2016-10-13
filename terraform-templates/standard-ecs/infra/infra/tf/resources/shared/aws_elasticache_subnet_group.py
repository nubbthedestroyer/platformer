#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_elasticache_subnet_group': {
            plat_name.lower() + "-" + mservice + "-ec": {
                'name': plat_name.lower() + "-" + mservice + "-ec",
                'description': plat_name.lower() + "-" + mservice + "-ec",
                'subnet_ids': [
                    "${aws_subnet." + vpc_subnet_a['name'] + ".id}",
                    "${aws_subnet." + vpc_subnet_b['name'] + ".id}"
                ]
            }
        }
    }
    return block
