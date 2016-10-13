#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        # 'aws_elasticache_security_group': {
        #     plat_name.lower() + "-" + mservice + "-ec": {
        #         'name': plat_name.lower() + "-" + mservice + "-ec",
        #         'description': plat_name.lower() + "-" + mservice + "-ec",
        #         'security_group_names': [
        #             "${aws_security_group." + ec2_sg + ".id}"
        #         ]
        #     }
        # }
    }
    return block
