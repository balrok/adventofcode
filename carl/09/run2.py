#!/usr/bin/env python
# -*- coding: utf-8 -*-
d=open("input.txt").read().strip()
def run(d):
    l=0
    while True:
        x=d.find("(")
        y=d.find(")",x)
        if x<0:return l+len(d)
        chars,repeat=map(int,d[x+1:y].split("x"))
        z = run(d[y+1:y+1+chars][:])
        l+=z*repeat+len(d[:x])
        d=d[y+1+chars:]
    return l
print(run(d))
