#!/usr/bin/env python3
# -*- coding: utf-8 -*-

move = {"U":(-1,0),"D":(1,0),"L":(0,-1),"R":(0,1)}
# sample: 1985
# input: 19636
def solve1(d):
    x=1
    y=1
    for line in d:
        for char in line.strip():
            x+=move[char][0]
            x=max(0,x)
            x=min(2,x)
            y+=move[char][1]
            y=max(0,y)
            y=min(2,y)
        print(x*3+y+1,end="")
    print("")

field_min = [2,1,0,1,2]
field_max = [2,3,4,3,2]
letters=[
    ["_","_","1","_","_"],
    ["_","2","3","4","_"],
    ["5","6","7","8","9"],
    ["_","A","B","C","_"],
    ["_","_","D","_","_"],
]
# sample: 5DB3
# input: 3CC43
def solve2(d):
    x=2
    y=0
    for line in d:
        for char in line.strip():
            x+=move[char][0]
            x=max(field_min[y],x)
            x=min(field_max[y],x)
            y+=move[char][1]
            y=max(field_min[x],y)
            y=min(field_max[x],y)
        print(letters[x][y],end="")

with open("input.txt") as f:
#with open("sample.txt") as f:
    d = f.readlines()
    solve1(d)
    solve2(d)
