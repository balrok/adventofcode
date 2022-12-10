#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
outs = {}
for i in range(500):
    outs["ut %d"%i]=[]
    outs["ot %d"%i]=[]
z=min,max
a = open("input").read()
for v,b in re.findall("e (\d+).*(.. \d+)", a):
    outs[b].append(int(v))
search=True
for _ in range(100):
    for b in outs:
        if len(outs[b])>1:
            r=re.findall(b+" .*(.. \d+) .*(.. \d+)",a)[0]
            for i in 0,1:
                if z[i](outs[b]) not in outs[r[i]]:
                    outs[r[i]].append(z[i](outs[b]))
        if 61 in outs[b] and 17 in outs[b]:
            s1=b
            search=False
#print(outs)
s2=outs["ut 0"][0]*outs["ut 1"][0]*outs["ut 2"][0]
print(s1[3:]+"\n%d"%s2)
