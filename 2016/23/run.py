#!/usr/bin/env python3
# -*- coding: utf-8 -*-

regs = {}


def get_instr():
    instr = []
    for l in open("input"):
        val2=0
        if l[:3] == "jnz":
            type="j"
            val1,val2 = l[4:].split()
            if val1<"a":val1=int(val1)
            if val2<"a":val2=int(val2)
        if l[:3] == "cpy":
            type="c"
            val1,val2 = l[4:].split()
            if val1<"a":val1=int(val1)
            if val2<"a":val2=int(val2)
        if l[:3] == "inc":
            type="i"
            val1 = l[-2:-1]
        if l[:3] == "dec":
            type="d"
            val1 = l[-2:-1]
        if l[:3] == "tgl":
            type="t"
            val1 = l[-2:-1]
        instr.append([type, val1, val2])
    return instr

def get_val(x):
    if isinstance(x,int): return x
    else: return regs[x]

for a in 7,12:
    for i in "abcd": regs[i]=0
    regs["a"]=a
    i=0
    instr=get_instr()
    count=0
    lastjumps={}
    while i<len(instr):
        t,x,y = instr[i]
        if t=="i":
            regs[x]+=1
        if t=="d":
            regs[x]-=1
        if t=="c":
            #error
            if isinstance(y, int): i+=1; continue
            #int
            if isinstance(x, int): regs[y]=x
            #reg
            else: regs[y]=regs[x]
        if t=="j":
            if (isinstance(x, int) and x!=0) or regs[x]!=0:
                y=get_val(y)
                if y>0: y-=1
                if y==-5:
                    z = zip(*instr[i+y:i+1])
                    # this is not a hack - it is called peeophole optimization
                    # detect a pattern and optimize it
                    if z[0]==tuple("cidjdj"):
                        # sanity checks - not required when golfing
                        if z[1][-1]==z[1][-2] and z[2][0]==z[1][2]==z[1][3] and z[2][3]==-2 and z[1][4]==z[1][5]:
                            m1 = z[1][4]
                            regs[z[1][1]] += get_val(m1) * get_val(z[1][0])
                            regs[m1] = 0
                            i+=1
                            continue
                i += y
                continue
        if t=="t":
            q=regs[x]+i
            if q>=0 and q <len(instr):
                if instr[q][0]=="d": instr[q][0]="i"
                elif instr[q][0]=="t": instr[q][0]="i"
                elif instr[q][0]=="i": instr[q][0]="d"
                elif instr[q][0]=="j": instr[q][0]="c"
                elif instr[q][0]=="c": instr[q][0]="j"
        i+=1
        count+=1
        if count%1000000==0:
            print(i,instr,regs)
    print(regs["a"])
    #print(instr)
