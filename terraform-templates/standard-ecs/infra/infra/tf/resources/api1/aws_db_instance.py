#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        # 'aws_db_instance': {
        #     rds_0: {
        #         'identifier': rds_0,
        #         'allocated_storage': "10",
        #         'engine': "mysql",
        #         'engine_version': "5.6.27",
        #         'instance_class': "db.m3.medium",
        #         'username': "root",
        #         'password': "keikahLi5bu5Fae3",
        #         'db_subnet_group_name': "${aws_db_subnet_group." + plat_name.lower() + ".name}",
        #         'parameter_group_name': "${aws_db_parameter_group." + plat_name.lower() + mservice.lower() + "db.name}",
        #         'multi_az': True,
        #         'publicly_accessible': True,
        #         'vpc_security_group_ids': [
        #             "${aws_security_group." + rds_db_sg + ".id}"
        #         ],
        #         'storage_encrypted': True,
        #         'apply_immediately': True,
        #         'skip_final_snapshot': True,
        #         'final_snapshot_identifier': rds_0 + "-final",
        #         'maintenance_window': "Sat:09:00-Sat:09:30",
        #         'backup_window': "08:00-08:30",
        #         'backup_retention_period': "35",
        #         'tags': {
        #             'Platform': plat_name.upper()
        #         }
        #     },
        #     rds_1: {
        #         'identifier': rds_1,
        #         'allocated_storage': "100",
        #         'replicate_source_db': rds_0,
        #         'instance_class': "db.r3.xlarge",
        #         'name': plat_name.lower() + mservice.lower() + "db",
        #         'parameter_group_name': "${aws_db_parameter_group." + plat_name.lower() + mservice.lower() + "db.name}",
        #         'publicly_accessible': True,
        #         'vpc_security_group_ids': [
        #             "${aws_security_group." + rds_db_sg + ".id}"
        #         ],
        #         'storage_encrypted': True,
        #         'apply_immediately': True,
        #         'skip_final_snapshot': False,
        #         'final_snapshot_identifier': rds_1 + "-final",
        #         'maintenance_window': "Sat:09:00-Sat:09:30",
        #         'backup_window': "08:00-08:30",
        #         'backup_retention_period': "35",
        #         'tags': {
        #             'Platform': plat_name.upper()
        #         }
        #     },
        # }
    }
    return block
