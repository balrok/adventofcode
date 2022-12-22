import re
from functools import lru_cache

valves={}
for l in open("input.txt").read().rstrip().split("\n"):
    g=re.findall("[A-Z]{2}|[0-9]+",l)
    valves[g[0]]=(int(g[1]),g[2:])
import pprint
pprint.pprint(valves)

def get_valve(node):
    for v in valve:
        if v[0]==node:
            return v

qq=set(k for k,v in valves.items()if v[0]>0)


@lru_cache(maxsize=500)
def h1(minute,closed):
    p=[valves[q][0] for q in closed]
    p=sorted(p,reverse=True)
    s=0
    i=0
    for pp in p:
        s+=minute*pp
        minute -= 3
        if minute<0:
            break
    return s

@lru_cache(maxsize=500)
def get_next(cur,goal):
    visited=set()
    tosearch = [[q] for q in valves[cur][1]]
    while len(tosearch) > 0:
        s = tosearch.pop(0)
        if s[-1] in visited:
            continue
        visited.add(s[-1])
        if s[-1] == goal:
            return s[0]
        tosearch.extend([s + [q] for q in valves[s[-1]][1] if q not in visited])

def search(node,snode,minute,pressure,closed):
    global g_best_pressure
    if pressure+h1(minute,tuple(closed)) < g_best_pressure:
        return pressure
    if minute<=0 or not closed:
        return pressure
    v=valves[node]
    if node == snode:
        best_pressure=pressure
        if node in closed:
            closed.remove(node)
            minute -= 1
            pressure += minute * v[0]
            best_pressure=pressure
            #print(minute,node,pressure)
        for nsnode in closed:
            n_pressure = search(node,nsnode,minute,pressure,closed.copy())
            best_pressure=max(n_pressure, best_pressure)
            g_best_pressure = max(best_pressure, g_best_pressure)
        return best_pressure
    else:
        n=get_next(node,snode)
        if n is None:
            return 0
        return search(n, snode, minute-1,pressure,closed)
g_best_pressure=0
print(search("AA","AA",30,0,qq))
import sys
# 2330 in 10s


@lru_cache(maxsize=500)
def h(minute,closed):
    p=[valves[q][0] for q in closed]
    p=sorted(p,reverse=True)
    s=0
    i=0
    for pp in p:
        s+=minute*pp
        minute -= 2
        if minute<0:
            break
    return s
g_best_pressure = 0
def search2(nodeA,snodeA,nodeB,snodeB,minute,pressure,closed):
    global g_best_pressure
    if pressure+h(minute,tuple(closed)) < g_best_pressure:
        return pressure
    if minute<=0 or len(closed) == 0:
        return pressure
    if nodeA == snodeA and nodeA in closed:
        closed = closed.copy()
        closed.remove(nodeA)
        pressure += (minute-1) * valves[nodeA][0]
        nextA = nodeA
    else:
        nextA=get_next(nodeA, snodeA)
    if nodeB == snodeB and nodeB in closed:
        closed = closed.copy()
        closed.remove(nodeB)
        pressure += (minute-1) * valves[nodeB][0]
        nextB = nodeB
    else:
        nextB=get_next(nodeB, snodeB)
    if nextA is None or nextB is None:
        print("MMM")
        return 0
    #path += [(minute,pressure,(nodeA,snodeA,nextA),(nodeB,snodeB))]

    minute -= 1
    best_pressure = pressure
    #best_path = path[:]
    g_best_pressure = max(best_pressure, g_best_pressure)
    if nodeA == snodeA and nodeB == snodeB:
        for nsnodeA in closed:
            for nsnodeB in closed:
                if nsnodeA ==nsnodeB:continue
                n_pressure = search2(nextA,nsnodeA,nextB,nsnodeB,minute,pressure,closed)
                best_pressure=max(n_pressure, best_pressure)
                g_best_pressure = max(best_pressure, g_best_pressure)
    elif nodeA == snodeA:
        for nsnodeA in closed:
            if nsnodeA ==snodeB:continue
            n_pressure= search2(nextA,nsnodeA,nextB,snodeB,minute,pressure,closed)
            best_pressure=max(n_pressure, best_pressure)
            g_best_pressure = max(best_pressure, g_best_pressure)
    elif nodeB == snodeB:
        for nsnodeB in closed:
            if nsnodeB ==snodeA:continue
            n_pressure= search2(nextA,snodeA,nextB,nsnodeB,minute,pressure,closed)
            best_pressure=max(n_pressure, best_pressure)
            g_best_pressure = max(best_pressure, g_best_pressure)
    else:
        n_pressure= search2(nextA,snodeA,nextB,snodeB,minute,pressure,closed)
        best_pressure=max(n_pressure, best_pressure)
        g_best_pressure = max(best_pressure, g_best_pressure)
    return best_pressure
best_pressure = 0
for nsnodeA in qq:
    for nsnodeB in qq:
        if nsnodeA==nsnodeB:continue
        n_pressure = search2("AA",nsnodeA,"AA",nsnodeB,26,0,qq)
        best_pressure=max(n_pressure, best_pressure)
        g_best_pressure = max(best_pressure, g_best_pressure)
# 2675
print(best_pressure)
