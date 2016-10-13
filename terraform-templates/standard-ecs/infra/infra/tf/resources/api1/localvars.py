#!/bin/python
import time
import os
from .. import variables

for key, value in variables.var.iteritems():
        exec(key + ' = ' + 'value')

lvar = {}


def localdir():
        str1 = os.path.dirname(os.path.realpath(__file__))
        str2 = str1.split('/')
        n = len(str2)
        return str2[n-1]


lvar['mservice'] = localdir()
lvar['iport'] = "8033"

lvar['mservice_stage'] = lvar['mservice'] + '_stage'
lvar['cw_prefix'] = plat_name + "-" + lvar['mservice'].upper() + "-"
lvar['cw_prefix_stage'] = plat_name + "-" + lvar['mservice'].upper() + "-Stage-"
lvar['elb'] = plat_name + "-" + lvar['mservice'].upper()
lvar['elb_stage'] = plat_name + "-" + lvar['mservice'].upper() + "-Stage"
lvar['elb_int'] = plat_name + "-" + lvar['mservice'].upper() + "-INT"
lvar['elb_int_stage'] = plat_name + "-" + lvar['mservice'].upper() + "-Stage-INT"
lvar['asg'] = plat_name + "-" + lvar['mservice'].upper() + "-ASG"
lvar['asg_stage'] = plat_name + "-" + lvar['mservice'].upper() + "-ASG-STAGE"
lvar['ec2_lc'] = plat_name + "-" + lvar['mservice'].upper() + "-LC"
lvar['ec2_lc_prefix'] = lvar['ec2_lc'] + "-"
lvar['ec2_lc_stage'] = plat_name + "-" + lvar['mservice'].upper() + "-LC-Stage"
lvar['ec2_lc_stage_prefix'] = lvar['ec2_lc_stage'] + "-"
lvar['ec2_lc_prefix_stamped'] = lvar['ec2_lc_prefix'] + str(int(time.time()))
lvar['ec2_sg'] = plat_name + "-" + lvar['mservice'].upper() + "-SG"
lvar['ec2_sg_stage'] = plat_name + "-" + lvar['mservice'].upper() + "-SG-STAGE"
lvar['elb_sg'] = plat_name + "-" + lvar['mservice'].upper() + "-ELB-SG"
lvar['elb_sg_stage'] = plat_name + "-" + lvar['mservice'].upper() + "-ELB-SG-STAGE"
lvar['rds_db_sg'] = plat_name + "-" + lvar['mservice'].upper() + "-DB-SG"
lvar['r53'] = lvar['mservice'] + '.' + plat_name.lower() + '.' + root_domain

lvar['rds_0'] = plat_name.lower() + lvar['mservice'] + 'db0'
lvar['rds_1'] = plat_name.lower() + lvar['mservice'] + 'db1'
lvar['rds_stage'] = plat_name.lower() + lvar['mservice'] + 'db0-stage'
lvar['rds_slaves'] = plat_name.lower() + lvar['mservice'] + 'db'
lvar['rds_0_full'] = lvar['rds_0'] + rds_suffix
lvar['rds_1_full'] = lvar['rds_1'] + rds_suffix
lvar['cd_prod'] = plat_name + "-" + lvar['mservice'].upper() + "-Prod"
lvar['cd_stage'] = plat_name + "-" + lvar['mservice'].upper() + "-Stage"
lvar['deploy_cfg'] = "CodeDeployDefault.AllAtOnce"

lvar['ldocs'] = {}
cwd = os.getcwd()
for f in os.listdir(cwd + "/tf/resources/" + lvar['mservice'] + "/ldocs"):
    lvar['ldocs'][f] = open(cwd + "/tf/resources/" + lvar['mservice'] + "/ldocs/" + f).read()

f1 = open('tf/resources/' + lvar['mservice'] + '/ldocs/plat_name.sh', 'w+')
f1.write("echo \"plat_name='" + plat_name + "'\" > /etc/plat_name.sh")
f1.close()
