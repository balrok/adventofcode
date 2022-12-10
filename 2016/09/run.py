#!/usr/bin/env python
# -*- coding: utf-8 -*-
d=open("input.txt").read().strip()
#d="X(8x2)(3x3)ABCY" #18
#d="(6x1)(1x3)A" #6
#d="A(2x2)BCD(2x2)EFG" #11
#d="A(1x5)BC" # 7
def run(d):
    c=0
    while True:
        x=d.find("(",c)
        y=d.find(")",x)
        if x<0:break
        chars,repeat=map(int,d[x+1:y].split("x"))
        d=d[:x] + repeat * d[y+1:y+1+chars] + d[y+1+chars:]
        c=x+repeat*chars
    print(len(d))
    return d
run(d)

a=[("X(8x2)(3x3)ABCY","X(3x3)ABC(3x3)ABCY"), #18
("(6x1)(1x3)A","(1x3)A"), #6
("A(2x2)BCD(2x2)EFG","ABCBCDEFEFG"),
("A(2x2)BC(2x2)EFZ","ABCBCEFEFZ"), #carl
("(2x2)BC(2x2)EFZ","BCBCEFEFZ"), #carl
("(5x2)(2x2)EFZ","(2x2)(2x2)EFZ"), #carl
("(6x2)(2x2)EFZ","(2x2)E(2x2)EFZ"), #carl
("A(1x5)BC","ABBBBBC")] # 7
for d in a:
    if run(d[0]) != d[1]:
        print(d[0], run(d[0]), d[1])

