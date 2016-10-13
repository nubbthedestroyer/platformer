#!/bin/python
import os

__all__ = []

for subdir, dirs, files in os.walk('./tf/resources'):
    for f in files:
        if "__init__.py" not in f:
            if "localvars.py" not in f:
                __all__.append(f.split('.')[0])
