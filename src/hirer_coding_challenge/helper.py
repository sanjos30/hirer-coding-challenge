#!/usr/bin/python

import os, json

def read_spark_config_file(filepath:str) -> dict:
    """ read the spark json config and return a dict
    """

    if isinstance(filepath, str) and os.path.exists(filepath):
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    else:
        print("Input file is invalid or does not exist {}", filepath)

