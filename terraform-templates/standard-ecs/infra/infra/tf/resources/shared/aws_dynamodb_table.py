#!/bin/python


def run():
    from .. import variables
    import localvars

    for key, value in localvars.lvar.iteritems():
        exec(key + ' = ' + 'value')
    for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

    block = {
        # 'aws_dynamodb_table': {
        #     'AlmHygieneProductionCustomers': {
        #         'name': 'AlmHygieneProductionCustomers',
        #         'read_capacity': 5,
        #         'write_capacity': 5,
        #         'hash_key': 'id',
        #         'stream_enabled': False,
        #         'attribute': [
        #             {
        #                 'name': "id",
        #                 'type': "S"
        #             },
        #             {
        #                 'name': "clientId-index",
        #                 'type': "S"
        #             },
        #             {
        #                 'name': "clientId",
        #                 'type': "S"
        #             }
        #         ],
        #         'global_secondary_index': {
        #             'name': 'household_id',
        #             'hash_key': 'clientId-index',
        #             'projection_type': 'ALL',
        #             'range_key': 'clientId',
        #             'write_capacity': 5,
        #             'read_capacity': 5
        #         },
        #         'lifecycle': {
        #             'ignore_changes': [
        #                 "write_capacity",
        #                 "read_capacity"
        #             ]
        #         }
        #     },
        #     'AlmHygieneProductionPolicies': {
        #         'name': 'AlmHygieneProductionPolicies',
        #         'read_capacity': 5,
        #         'write_capacity': 5,
        #         'hash_key': 'policy_number',
        #         'stream_enabled': False,
        #         'attribute': [
        #             {
        #                 'name': "policy_number",
        #                 'type': "S"
        #             },
        #             {
        #                 'name': "household_id",
        #                 'type': "S"
        #             },
        #             {
        #                 'name': "client_id",
        #                 'type': "S"
        #             }
        #         ],
        #         'global_secondary_index': [
        #             {
        #                 'name': 'household_id-index',
        #                 'hash_key': 'household_id',
        #                 'projection_type': 'ALL',
        #                 'write_capacity': 5,
        #                 'read_capacity': 5
        #             },
        #             {
        #                 'name': 'client_id-index',
        #                 'hash_key': 'client_id',
        #                 'projection_type': 'ALL',
        #                 'write_capacity': 5,
        #                 'read_capacity': 5
        #             }
        #         ],
        #         'lifecycle': {
        #             'ignore_changes': [
        #                 "write_capacity",
        #                 "read_capacity"
        #             ]
        #         }
        #     },
        #     'AlmHygieneStageCustomers': {
        #         'name': 'AlmHygieneStageCustomers',
        #         'read_capacity': 5,
        #         'write_capacity': 5,
        #         'hash_key': 'id',
        #         'stream_enabled': False,
        #         'attribute': [
        #             {
        #                 'name': "id",
        #                 'type': "S"
        #             },
        #             {
        #                 'name': "clientId-index",
        #                 'type': "S"
        #             },
        #             {
        #                 'name': "clientId",
        #                 'type': "S"
        #             }
        #         ],
        #         'global_secondary_index': {
        #             'name': 'household_id',
        #             'hash_key': 'clientId-index',
        #             'projection_type': 'ALL',
        #             'range_key': 'clientId',
        #             'write_capacity': 5,
        #             'read_capacity': 5
        #         },
        #         'lifecycle': {
        #             'ignore_changes': [
        #                 "write_capacity",
        #                 "read_capacity"
        #             ]
        #         }
        #     },
        #     'AlmHygieneStagePolicies': {
        #         'name': 'AlmHygieneStagePolicies',
        #         'read_capacity': 5,
        #         'write_capacity': 5,
        #         'hash_key': 'policy_number',
        #         'stream_enabled': False,
        #         'attribute': [
        #             {
        #                 'name': "policy_number",
        #                 'type': "S"
        #             },
        #             {
        #                 'name': "household_id",
        #                 'type': "S"
        #             }
        #         ],
        #         'global_secondary_index': {
        #             'name': 'household_id',
        #             'hash_key': 'policy_number',
        #             'projection_type': 'ALL',
        #             'range_key': 'household_id',
        #             'write_capacity': 5,
        #             'read_capacity': 5
        #         },
        #         'lifecycle': {
        #             'ignore_changes': [
        #                 "write_capacity",
        #                 "read_capacity"
        #             ]
        #         }
        #     }
        # }
    }
    return block
