#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
x,y=50,6
#x,y=7,3
display = [["." for i in range(x)]for j in range(y)]
c=0
for l in open("input.txt").readlines():
    i = list(map(int,re.findall("(\d+)",l)))
    if l[1] == "e":
        for u in range(i[0]): 
            for v in range(i[1]):
                display[v][u] = "#"
    elif l[7]=="r":
        for z in range(i[1]):
            display[i[0]].insert(0,display[i[0]][-1])
            del(display[i[0]][-1])
    elif l[7]=="c":
        for z in range(i[1]):
            t = display[-1][i[0]]
            for u in range(y-2, -1, -1):
                display[u+1][i[0]] = display[u][i[0]]
            display[0][i[0]] = t

print("\n".join(["".join(row)for row in display]).count("#"))
print("\n".join(["".join(row)for row in display]))
