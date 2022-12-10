#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from heapq import heappop, heappush
d = open("input").readlines()
conv={}
c=0
for j in re.findall(" (\w*)-compatible", "".join(d)):
    conv[j]=c
    c+=1
floors = 0
for i in range(4):
    for j in re.findall(" (\w*)-compatible", d[i]):
        floors |= 1<<conv[j] + 14*i
    for j in re.findall(" (\w*) generator", d[i]):
        floors |= 1<<conv[j]+7 + 14*i

def ii(f,i):
    i*=14
    #if f&127<<i+7:
    #    for j in range(7):
    #        if f&129<<i+j==1<<i+j:
    #            return False
    #return True
    return not(f&127<<i+7 and(\
       0 < f&129<<i+0 < 128<<i or\
       0 < f&129<<i+1 < 128<<i or\
       0 < f&129<<i+2 < 128<<i or\
       0 < f&129<<i+3 < 128<<i or\
       0 < f&129<<i+4 < 128<<i or\
       0 < f&129<<i+5 < 128<<i or\
       0 < f&129<<i+6 < 128<<i))

#-1 and 1 to know when to prune together with "found"
permutation=[(-1,1<<i|1<<j)for i in range(0,13)for j in range(i+1,14)]+[(1,1<<i)for i in range(0,14)]
def find_a_star(floors):
    todo = []
    closed=set()
    heappush(todo, (0,floors,0,0))
    while True:
        _,floors,c,steps = heappop(todo)
        if floors&(2**42-1)==0:# 42 = the answer to everything - even this puzzle
            return steps
        for m in (1,-1):
            if not 0<=c+m<4:continue
            found = False
            for l,it in permutation[::m]:
                if found and l==m:break#prune
                ic=it<<14*c
                if (floors & ic)!=ic:continue
                n = floors - ic + (it<<14*(c+m))
                if ii(n,c+m) and ii(n,c):
                    # nn is pruning by pairs of chip-generator
                    # chip gets level+4 and generator level+0
                    # create the sum of those two
                    # then sort by this
                    # filtering by &129 makes it faster - as the list contains no more 0-elements
                    nn = sorted([(f+4)*(n&1<<14*f+j>0)+f*(n&128<<14*f+j>0)for f in range(4)for j in range(7)if n&129<<14*f+j])
                    # create a single number by multiplying every element with a certain base
                    # single numbers are easier to look up in the set
                    n2 = c+m+sum([8**(1+j)*nn[j]for j in range(len(nn))])
                    #n2 = str(c+m)+str(nn)
                    if n2 not in closed:
                        found = True
                        closed.add(n2)
                        #f = bin(floors)
                        score = steps# + c + f[-14:].count("1")*1.9 + f[-28:-14].count("1")*1.4 + f[-42:-28].count("1")*0.9
                        heappush(todo, (score, n,c+m,steps+1))
#print(find_a_star(floors,4))
print(find_a_star(floors))
floors |= 1<<5 | 1<<12
floors |= 1<<6 | 1<<13
print(find_a_star(floors))
