#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
o=map(int, list(open("input").read().strip()))
o=open("input").read()
for q in 272,35651584:
    d=o[:]
    start = time.time()
    j=0
    while len(d)<q:
        j+=1
        print(j)
        #d+=[0]+[1^x for x in reversed(d)] # for ints: it takes 9 seconds
        #d+=[0]+[1^x for x in d[::-1]] # for ints: it takes 10 seconds
        #d+=[0]+map(lambda x:1^x,d[::-1]) # for ints it takes 13seconds
        d+="0"+d.replace("1","X").replace("0","1").replace("X","0")[::-1] # for strings 1.2 seconds
    d=d[:q]
    #d=map(int,d) - super slow
    #pairs = zip(d[::2],d[1::2]) -slow
    print("part 1 done: "+str(time.time()-start))

    start = time.time()
    j=0
    while 1:
        j+=1
        print(j)
        #d = map(lambda x:(0,1)[x[0]==x[1]],zip(d[::2],d[1::2])) - slow (30sec)
        #d = [(False,True)[d[i]==d[i+1]]for i in range(0,len(d)-1,2)] # for anything 24seconds
        #d = [("0","1")[d[i]==d[i+1]]for i in range(0,len(d)-1,2)] # for anything 16-17 seconds
        #d = [0+(d[i]==d[i+1])for i in range(0,len(d)-1,2)] # for anything 16 seconds (better than int()=24seconds)
        #d = [1-d[i]^d[i+1] for i in range(0,len(d)-1,2)] # for int in 15 seconds
        d = [(0,1)[d[i]==d[i+1]]for i in range(0,len(d)-1,2)] # for anything 15.5-17 seconds(string)
        if len(d)%2:
            break
        #pairs = zip(c[::2],c[1::2])
    print("part2 done: "+str(time.time()-start))
    print("result: "+"".join(map(str,d)))

# 10011010101001010 too high
