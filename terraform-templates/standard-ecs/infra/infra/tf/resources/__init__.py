#!/bin/python
import os

__all__ = []

for subdir, dirs, files in os.walk('./tf/resources'):
    for f in files:
        if "__init__.py" not in f:
            __all__.append(f.split('.')[0])

# __all__ = [
#     'aws_elb',
#     'aws_s3_bucket',
#     'aws_iam_role',
#     'aws_iam_policy'
# ]
