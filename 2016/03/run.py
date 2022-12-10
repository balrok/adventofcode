#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = open("input.txt").read()
m = [int(s) for s in d.split()]
c = [x+y>z and x+z>y and z+y>x for x,y,z in zip(m[::3], m[1::3], m[2::3]) ]
e=[]
for i in range(3):
    e += [x+y>z and x+z>y and z+y>x for x,y,z in zip(m[i::9], m[3+i::9], m[6+i::9]) ]
print(sum(c))
print(sum(e))
