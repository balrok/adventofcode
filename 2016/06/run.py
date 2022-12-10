#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1=""
s2=""
with open("input.txt") as d:
    s=zip(*d.read().split())
    for l in s:
        a=b=0
        c=d=999
        for i in l:
            if l.count(i)>a:
                a=l.count(i)
                b=i
            if l.count(i)<c:
                c=l.count(i)
                d=i
        s1+=b
        s2+=d
print(s1+"\n"+s2)
        
