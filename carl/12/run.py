#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# cpy x y copies x (either an integer or the value of a register) into register y.
# inc x increases the value of register x by one.
# dec x decreases the value of register x by one.
# jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.
# 
# 
# cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a
# 
# The above code would set register a to 41, increase its value by 2, decrease its value by 1, and then skip the last dec a (because a is not zero, so the jnz a 2 skips it), leaving register a at 42. When you move past the last instruction, the program halts.

regs = {}
for i in range(-100,100):
    regs[str(i)]=i
for i in "abcd":
    regs[i]=0
instr = open("input").readlines()

def run(regs):
    c=0
    while True:
        if c >= len(instr):
            break
        l = instr[c]
        if l[:3] == "cpy":
            x,y = l[4:].split()
            regs[y]=regs[x]
        if l[:3] == "inc":
            regs[l[-2:-1]]+=1
        if l[:3] == "dec":
            regs[l[-2:-1]]-=1
        if l[:3] == "jnz":
            x,y = l[4:].split()
            if regs[x]!=0:
                c += regs[y]
            else:
                c+=1
            if regs[x]<0:
                c+=1
        else:
            c+=1
    return regs
s1 = {k:v for k,v in regs.items()}
print(run(s1)["a"])
regs["c"]=1
print(run(regs)["a"])
