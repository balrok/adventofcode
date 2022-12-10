#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
def do(s,d=1):
    s=list(s)
    for ll, t,i,c in instr[::d]:
        j=[int(q)if q<"a"else s.index(q)for q in i][:2]
        x=j[0]
        y=j[1]
        if t == "rev": s[x:y+1] = s[x:y+1][::-1]
        if t == "rot":
            if d<0:
                if not ll and c:
                    q=x
                    for w in range(len(s)):
                        x=(x-1)%len(s)
                        if(x+(x>=4))%len(s)==w:break
                    x=(w+1)%len(s)
                if ll:
                    x*=-1
            else:
                if not ll:
                    if c: x=(x+1+(x>=4))%len(s)
                    x*=-1
            s = s[x:]+s[:x]
        if t == "swa": s[x],s[y]=s[y],s[x]
        if d<0:
            x,y=y,x
        if t == "mov": s.insert(y,s.pop(x))
    return "".join(s)
instr=[("left" in line, line[:3],re.findall(" (\w|\d)\s",line)+[0],line[7]=="b")for line in open("input")]
print(do("abcdefgh"))
print(do("fbgdceah",-1))
