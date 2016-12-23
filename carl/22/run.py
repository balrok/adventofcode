#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from heapq import heappop, heappush
nodes = []
coords = []
index = {}
i=0
target = 0
for line in open("input"):
    if line[0]!="/":continue
    q=map(int,re.findall("(\d+)",line))
    c = (q[0],q[1])
    if q[1]==0:
        target = c
    nodes += [(q[4], q[3])]
    coords += [c]
    index[c]=i
    i+=1


def get_all_viable(nodes):
    n = []
    #nodes.sort(reverse=True)
    for i in range(len(nodes)):
        avail,used = nodes[i][:2]
        # Node A is not empty (its Used is not zero).
        if used == 0:continue
        for j in range(len(nodes)):
            nj=nodes[j]
            # Nodes A and B are not the same node.
            if nj[-2:]==nodes[i][-2:]:continue
            # The data on node A (its Used) would fit on node B (its Avail).
            if nj[0]>=used:
                n+=[(i,j)]
    return n
print(len(get_all_viable(nodes)))

def get_viable(nodes):
    n = []
    #nodes.sort(reverse=True)
    for i in range(len(nodes)):
        type = nodes[i]
        # Node A is not empty (its Used is not zero).
        if type != 1:continue
        ic = coords[i]
        for c in ((ic[0]+1,ic[1]),(ic[0]-1,ic[1]),(ic[0],ic[1]+1),(ic[0],ic[1]-1)):
            j = index.get(c)
            if j is not None:
                if nodes[j] == 0:
                # The data on node A (its Used) would fit on node B (its Avail).
                    n+=[(i,j)]
    return n


#print(is_neighboring((35,28),(35,27)))
c=set()
t=[]
def print_nodes(nodes, goal):
    print(nodes)
    for i in range(len(nodes)):
        ci = coords[i]
        if ci[1]==0:print""
        if ci==goal:print"G",
        #elif nodes[i][1]>80:print"#",
        #elif nodes[i][0]>60:print"_",
        elif nodes[i][1]>9:print"#",
        elif nodes[i][0]>=1:print"_",
        else:print".",
    print""
        
free = max(nodes)[0]

n2= []
for n in nodes:
    typ=1
    if n[1]>free:typ=2
    elif n[0]==free:typ=0
    n2+=[typ]
nodes = [n for n in n2]
heappush(t,(0,target,nodes,0))
while len(t):
    score,goal,nodes,s=heappop(t)
    if goal == (0,0):
        print(s)
        break
    for n in get_viable(nodes):
        i,j=n
        nn = nodes[:]
        nn[j],nn[i] = nn[i],nn[j]
        nt = goal
        ci = coords[i]
        if nt==ci:
            nt = coords[j]
        h = (nt, tuple(nn))
        if h not in c:
            c.add(h)
            score = 100*sum(nt) + abs(nt[0]-ci[0]) + abs(nt[1]-ci[1])
            heappush(t, (score, nt, nn, s+1))
