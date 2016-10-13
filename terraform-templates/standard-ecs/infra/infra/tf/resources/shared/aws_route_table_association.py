#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_route_table_association': {
            vpc_rt_assoc_a: {
                'subnet_id': "${aws_subnet." + vpc_subnet_a['name'] + ".id}",
                'route_table_id': "${aws_route_table." + vpc_rt + ".id}"
            },
            vpc_rt_assoc_b: {
                'subnet_id': "${aws_subnet." + vpc_subnet_b['name'] + ".id}",
                'route_table_id': "${aws_route_table." + vpc_rt + ".id}"
            },
            vpc_rt_nat_assoc: {
                'subnet_id': "${aws_subnet." + vpc_subnet_nat['name'] + ".id}",
                'route_table_id': "${aws_route_table." + vpc_rt_nat + ".id}"
            },
            vpc_rt_assoc_elba: {
                'subnet_id': "${aws_subnet." + vpc_subnet_elba['name'] + ".id}",
                'route_table_id': "${aws_route_table." + vpc_rt_nat + ".id}"
            },
            vpc_rt_assoc_elbb: {
                'subnet_id': "${aws_subnet." + vpc_subnet_elbb['name'] + ".id}",
                'route_table_id': "${aws_route_table." + vpc_rt_nat + ".id}"
            }
        }
    }
    return block
