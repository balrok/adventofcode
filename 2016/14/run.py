#!/usr/bin/env python
# -*- coding: utf-8 -*-

import md5
import re
import pickle
salt = "abc%d"
salt = "ihaygndm%d"
def f(salt, stretch):
    i = 0
    keys = []
    found = 0
    result = []
    try:
        cache = pickle.load(open("cache%d"%stretch, "rb"))
    except:
        cache = {}
    while True:
        s = salt%i
        if s in cache:
            c = cache[s]
        else:
            c = md5.new(s).hexdigest()
            for z in range(stretch):
                c = md5.new(c).hexdigest()
            cache[s] = c
        rem  = []
        for k in keys:
            if k[1]+1000<i:
                rem.append(k)
                continue
            if k[0] in c:
                print("found at ",i,k)
                result += [k[1]]
                found += 1
                if found == 80:
                    pickle.dump(cache,open("cache%d"%stretch, "wb"))
                    return sorted(result)
                rem.append(k)
        for k in rem:
            keys.remove(k)
        k = re.search(r"(.)\1\1",c)
        if k:
            keys.append((5*k.group(1), i))
        i+=1
    return result

print(f(salt,0)[63])
#19883 too low
#20076 too high
#20346 too high
print(f(salt,2016)[63])
