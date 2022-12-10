#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
d = open("input").readlines()
floors=[[],[],[],[]]
conv={}
c=1
for j in re.findall(" (\w*)-compatible", "".join(d)):
    c+=1
    conv[j]=c
for i in range(4):
    floors[i] = [conv[j]for j in re.findall(" (\w*)-compatible", d[i])]
    floors[i] += [-conv[j]for j in re.findall(" (\w*) generator", d[i])]
def ii(f):
    if not f: return True
    hasgen = False
    haschip= False
    for i in f:
        if i<0: hasgen=True
        if i>0 and -i not in f:
            haschip=True
        if hasgen and haschip:
            return False
    if hasgen and haschip:
        return False
    return True

def find_a_star(floors, win):
    todo = []
    closed=set()
    todo.append((floors,0,0))
    while True:
        floors,c, steps = todo.pop(0)
        if len(floors[3])==win:
            return steps
        new=[]
        for i in floors[c]:
            for j in floors[c]:
                if i<j:new.append([i,j])
        for i in floors[c]:
            new.append([i])
        for m in (1,-1):
            if not 0<=c+m<len(floors):continue
            found = False
            for it in new[::m]:
                if found and len(it)==1 and m>0:break#prune
                if found and len(it)==2 and m<0:break#prune
                tm = floors[c+m]+it # add
                tc = [x for x in floors[c] if x not in it] # remove
                if ii(tc) and ii(tm):
                    n=[x[:]for x in floors]
                    n[c]  =tc
                    n[c+m]=tm
                    # nn is pruning by pairs of chip-generator
                    nn = [[f for f in range(4)if v in n[f]]+[f for f in range(4)if -v in n[f]]for v in range(win)]
                    nn = str(c+m)+str(sorted(nn))
                    if nn not in closed:
                        found = True
                        closed.add(nn)
                        todo.append((n,c+m,steps+1))
print(find_a_star(floors,10))
floors[0]+=[7,-7,8,-8]
print(find_a_star(floors,14))
