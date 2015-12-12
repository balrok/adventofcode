import json
import pprint


def countNumbers(d):
    c = 0
    if isinstance(d, dict):
        for x in d.values():
            c += countNumbers(x)
    elif isinstance(d, list):
        for x in d:
            c += countNumbers(x)
    elif isinstance(d, int):
        c = d
    return c

def countNumbers2(d):
    c = 0
    if isinstance(d, dict):
        if "red" in d.values():
            return 0
        for x in d.values():
            c += countNumbers2(x)
    elif isinstance(d, list):
        for x in d:
            c += countNumbers2(x)
    elif isinstance(d, int):
        c = d
    return c

def task1(d):
    pprint.pprint(d)
    print countNumbers(d)
    print countNumbers2(d)

with open("input12") as f:
    d = json.load(f)
    task1(d)
