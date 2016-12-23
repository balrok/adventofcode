#!/usr/bin/env python
# -*- coding: utf-8 -*-

import md5
input = open("input").read().strip()

longest=0
shortest=(99,)

dirs="UDLR"
todo=[(0,0,0,input)]
count=0
while len(todo):
    count+=1
    x,y,steps,inp = todo.pop()
    if x==y==3:
        if steps < shortest[0]:
            shortest = (steps, inp[len(input):])
        longest=max(longest, steps)
        continue
    c = md5.new(inp).hexdigest()
    for d,dx,dy in ((0,0,-1),(1,0,1),(2,-1,0),(3,1,0)):
        if x+dx<0 or x+dx>3 or c[d]<"b" or y+dy<0 or y+dy>3:continue
        todo.append((x+dx,y+dy,steps+1,inp+dirs[d]))


print(shortest[1])
print(longest)
