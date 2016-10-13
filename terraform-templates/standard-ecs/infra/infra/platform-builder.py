#!/bin/python
import pprint
import simplejson as json
import tf.resources.variables as setvars
import os


pp = pprint.PrettyPrinter(indent=4)
#############################################
# Use this script to create the AWS resources json template
# required for a standard platform.
# NOTE: Does not create VPC aspects yet.
#############################################

# set resources
for key, value in setvars.var.iteritems():
    exec(key + ' = ' + 'value')


def addit(data, res):
    if not setvars.tvar['resource']:
        setvars.tvar['resource'].update(data)
    else:
        if res not in setvars.tvar['resource'].keys():
            setvars.tvar['resource'].update(data)
        else:
            d1 = setvars.tvar['resource'][res]
            d2 = data[res]
            d3 = dict(d1.items() + d2.items())
            setvars.tvar['resource'][res].update(d3)

temp = {}
for subdir, dirs, files in os.walk('./tf/resources'):
    for d in dirs:
        print("Building " + d)
        for subdir, dirs, files in os.walk('./tf/resources/' + d):
            if 'ldocs' not in subdir:
                for f in files:
                    if "__init__.py" not in f:
                        if 'localvars.py' not in f:
                            if '.pyc' not in f:
                                print("Adding " + f)
                                modname = f.split('.')[0]
                                temp[modname] = __import__('tf.resources.' + d + '.' + modname, globals(), locals(), ['run'], -1)
                                data = temp[modname].run()
                                res = modname
                                addit(data, res)

f1 = open('./infra.tf.json', 'w+')
f1.write(json.dumps(setvars.tvar, indent=4, sort_keys=True))
f1.close()

