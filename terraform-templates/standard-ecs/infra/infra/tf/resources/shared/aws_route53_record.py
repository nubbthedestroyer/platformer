#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_route53_record': {
            # rds_0: {
            #     'zone_id': r53_zone_id,
            #     'name': "db0." + mservice + '.' + plat_name.lower() + '.' + root_domain,
            #     'type': 'CNAME',
            #     'ttl': 60,
            #     'records': [
            #         "${aws_db_instance." + rds_0 + ".address}"
            #     ]
            # },
            # rds_slaves: {
            #     'zone_id': r53_zone_id,
            #     'name': "db." + mservice + '.' + plat_name.lower() + '.' + root_domain,
            #     'type': 'CNAME',
            #     'ttl': 60,
            #     'records': [
            #         "${aws_db_instance." + rds_0 + ".address}"
            #     ]
            # },
            # 'rds_0_1': {
            #     'zone_id': r53_zone_id,
            #     'name': plat_name.lower() + mservice.lower() + 'db0' + '.' + root_domain,
            #     'type': 'CNAME',
            #     'ttl': 60,
            #     'records': [
            #         "${aws_db_instance." + rds_0 + ".address}"
            #     ]
            # },
            # 'rds_slaves_1': {
            #     'zone_id': r53_zone_id,
            #     'name': "db." + mservice.lower() + '.' + plat_name.lower() + '.' + root_domain,
            #     'type': 'CNAME',
            #     'ttl': 60,
            #     'records': [
            #         "${aws_db_instance." + rds_0 + ".address}"
            #     ]
            # },
            # 'memcached': {
            #     'zone_id': r53_zone_id,
            #     'name': "memcached." + mservice.lower() + '.' + plat_name.lower() + '.' + root_domain,
            #     'type': 'CNAME',
            #     'ttl': 60,
            #     'records': [
            #         "${aws_elasticache_cluster." + plat_name.lower() + "-" + mservice + "-ec-m" + ".cache_nodes.0.address}"
            #     ]
            # },
            # 'memcached-cfg': {
            #     'zone_id': r53_zone_id,
            #     'name': "memcached-cfg." + mservice.lower() + '.' + plat_name.lower() + '.' + root_domain,
            #     'type': 'CNAME',
            #     'ttl': 60,
            #     'records': [
            #         "${aws_elasticache_cluster." + plat_name.lower() + "-" + mservice + "-ec-m" + ".configuration_endpoint}"
            #     ]
            # },
            # 'redis': {
            #     'zone_id': r53_zone_id,
            #     'name': "redis." + mservice.lower() + '.' + plat_name.lower() + '.' + root_domain,
            #     'type': 'CNAME',
            #     'ttl': 60,
            #     'records': [
            #         "${aws_elasticache_cluster." + plat_name.lower() + "-" + mservice + "-ec" + ".cache_nodes.0.address}"
            #     ]
            # }
        }
    }
    return block