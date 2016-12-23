#!/usr/bin/env python
# -*- coding: utf-8 -*-

import md5
import re
import multiprocessing
from functools import partial

salt = "ihaygndm%d"
salt = "abc%d"

def multi_md5(stretch, i):
    c = md5.new(salt%i).hexdigest()
    for z in range(stretch):
        c = md5.new(c).hexdigest()
    k = re.search(r"(.)\1\1",c)
    if k:
        k=k.group(1)
    e = re.findall(r"(.)\1\1\1\1",c)
    if k or e: return (i,(k,e))
    return (i,0)

def f(salt, stretch, pool):
    i = 0
    keys = []
    result = []
    u=1000
    idx=0
    m5=partial(multi_md5, stretch)
    while 1:
        for i,r in pool.imap(m5, range(i,i+u)):
            if not r:
                continue
            t3,t5 = r
            if t5: # has a 5er
                for k in keys[idx:]:
                    if k[1]+1000<i:
                        idx+=1
                        continue
                    if k[2]==0:continue
                    if k[0] in t5:
                        #print("found at ",i,k)
                        result += [k[1]]
                        if len(result) == 80:
                            return sorted(result)
                        k[2] = 0
            if t3: # has a 3er
                keys.append([t3, i, 1])
    return sorted(result)

pool = multiprocessing.Pool(multiprocessing.cpu_count())
print(f(salt,0,pool)[63])
print(f(salt,2016,pool)[63])
#pool.close()
#pool.join()
