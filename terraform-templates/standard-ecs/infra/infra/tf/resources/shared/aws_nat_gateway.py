#!/bin/python
from .. import variables


def run():
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        'aws_nat_gateway': {
            vpc_natgw: {
                'allocation_id': "${aws_eip." + vpc_natgw_eip + ".id}",
                'subnet_id': "${aws_subnet." + vpc_subnet_nat['name'] + ".id}"
            }
        }
    }
    return block
