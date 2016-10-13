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
            mservice: {
                'zone_id': r53_zone_id,
                'name': mservice + '.' + plat_name.lower() + '.' + root_domain,
                'type': 'A',
                'alias': {
                    'name': "${aws_elb." + elb + ".dns_name}",
                    'zone_id': "${aws_elb." + elb + ".zone_id}",
                    'evaluate_target_health': True
                }
            },
            mservice_stage: {
                'zone_id': r53_zone_id,
                'name': mservice.lower() + '.stage.' + plat_name.lower() + '.' + root_domain,
                'type': 'A',
                'alias': {
                    'name': "${aws_elb." + elb_stage + ".dns_name}",
                    'zone_id': "${aws_elb." + elb_stage + ".zone_id}",
                    'evaluate_target_health': True
                }
            },
            rds_0: {
                'zone_id': r53_zone_id,
                'name': "db0." + mservice + '.' + plat_name.lower() + '.' + root_domain,
                'type': 'CNAME',
                'ttl': 60,
                'records': [
                    rds_0_full
                ]
            },
            rds_slaves: {
                'zone_id': r53_zone_id,
                'name': "db." + mservice + '.' + plat_name.lower() + '.' + root_domain,
                'type': 'CNAME',
                'ttl': 60,
                'records': [
                    rds_0_full
                ]
            },
            'rds_0_1': {
                'zone_id': r53_zone_id,
                'name': plat_name.lower() + mservice.lower() + 'db0' + '.' + root_domain,
                'type': 'CNAME',
                'ttl': 60,
                'records': [
                    rds_0_full
                ]
            },
            'rds_slaves_1': {
                'zone_id': r53_zone_id,
                'name': "db." + mservice.lower() + '.' + plat_name.lower() + '.' + root_domain,
                'type': 'CNAME',
                'ttl': 60,
                'records': [
                    rds_0_full
                ]
            }
        }
    }
    return block