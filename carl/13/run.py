#!/usr/bin/env python
# -*- coding: utf-8 -*-
from heapq import heappop, heappush

#z=10
#s=10
z=int(open("input").read())
s=200
goal=(31,39)
field = [[(0,1)[bin(x*x + 3*x + 2*x*y + y + y*y+z).count("1")%2] for x in range(s)]for y in range(s)]
x=0
y=0
#from pprint import pprint
#pprint(field)


todo = []
closed={}
heappush(todo, (0,(1,1),0,[(1,1)]))
while True:
    _,move,steps,hist = heappop(todo)
    if field[move[1]][move[0]]:continue
    x,y = move
    if move == goal:
        #for m in hist:
        #    field[m[1]][m[0]] = "X"
        #pprint(field)
        print(steps)
        break
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        if x+dx<0:continue
        if y+dy<0:continue
        sc = abs(x+dx - goal[0]) + abs(y+dx - goal[1])
        move = (x+dx, y+dy)
        if closed.get(move,9999)>steps:
            #print("move to",move)
            closed[move]=steps
            heappush(todo,(sc,move,steps+1,hist+[move]))



todo = []
closed={}
heappush(todo, (0,(1,1),0,[(1,1)]))
while True:
    try:
        _,move,steps,hist = heappop(todo)
    except:
        break
    x,y = move
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        if x+dx<0:continue
        if y+dy<0:continue
        move = (x+dx, y+dy)
        if field[move[1]][move[0]]:continue
        if closed.get(move,49)>steps:
            closed[move]=steps
            heappush(todo,(0,move,steps+1,hist+[move]))
# too high: 440, 125
print(len(closed)+1)
