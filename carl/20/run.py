#!/usr/bin/env python
# -*- coding: utf-8 -*-
lowest = 0
allowed=[]
l = sorted([map(int,line.split("-"))for line in open("input")])
idx = 0
while 1:
    for s,e in l[idx:]:
        if s > lowest:
            break
        if lowest < e+1:
            lowest = e+1
        idx += 1
    if lowest >= 2**32:
        break
    allowed += [lowest]
    lowest += 1
print(min(allowed))
print(len(allowed))
