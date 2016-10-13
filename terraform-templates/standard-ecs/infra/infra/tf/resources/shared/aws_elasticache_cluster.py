#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        # 'aws_elasticache_cluster': {
        #     plat_name.lower() + "-" + mservice + "-ec": {
        #         'cluster_id': plat_name.lower() + "-" + mservice + "-ec",
        #         'engine': 'redis',
        #         'node_type': 'cache.t2.micro',
        #         'num_cache_nodes': '1',
        #         'parameter_group_name': plat_name.lower() + "-" + mservice + "-ec",
        #         'port': 6379,
        #         'subnet_group_name': plat_name.lower() + "-" + mservice + "-ec",
        #         'security_group_ids': [
        #             "${aws_security_group." + ec2_sg + ".id}",
        #         ],
        #         'apply_immediately': True,
        #         'availability_zone': az['a']
        #     },
        #     plat_name.lower() + "-" + mservice + "-ec-m": {
        #         'cluster_id': plat_name.lower() + "-" + mservice + "-ec-m",
        #         'engine': 'memcached',
        #         'node_type': 'cache.t2.micro',
        #         'num_cache_nodes': '1',
        #         'parameter_group_name': plat_name.lower() + "-" + mservice + "-ec-m",
        #         'port': 11211,
        #         'subnet_group_name': plat_name.lower() + "-" + mservice + "-ec",
        #         'security_group_ids': [
        #             "${aws_security_group." + ec2_sg + ".id}",
        #         ],
        #         'apply_immediately': True,
        #         'az_mode': "single-az",
        #         'availability_zone': az['a']
        #     }
        # }
    }
    return block
