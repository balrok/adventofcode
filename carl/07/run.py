#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import regex as re
d = open("input.txt").readlines()

m=lambda x:not not re.search(r"\[[^\]]*(.)(?!\1)(.)\2\1", x)
m2=lambda x:not not re.search(r"(^|\])[^\[]*(.)(?!\2)(.)\3\2", x)
m3=lambda x:not x[0] and x[1]
print(sum(map(m3,zip(map(m,d),map(m2,d)))))

inside=lambda x:".".join(re.findall(r"\[([^\]]*?)\]",x))
outside=lambda x:".".join([i[0] for i in re.findall(r"([^\[\]]*)(\[|$)",x)])
m4=lambda x:[i[1]+i[0]+i[1] for i in re.findall(r"(.)(?!\1)(\w)\1", x, overlapped=True)]
m5=lambda x:not not re.search(r"("+"|".join(["1"]+x[1])+")", x[0])
#print(sum(map(m5,zip(map(inside,d),map(m4,map(outside, d))))))
for i in zip(map(m4,map(outside,d)),map(m5,zip(map(inside,d),map(m4,map(outside, d))))):
 print(i)
