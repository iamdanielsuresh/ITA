#!/usr/bin/env python3
import re

def rearrene_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    print(result)
    print(result[0])
    print(result[1])
    print(result[2])
    if result is None:
        return name
    return "{} {}".format(result[2],result[1])
