#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from string import ascii_lowercase

def main():
    d = ""
    with open("input.txt") as i:
    #with open("sample.txt") as i:
        d = i.readlines()
    solve1(d)

def solve1(d:str):
    s1=0
    for line in d:
        sline=line.split("-")
        x=sline.pop()
        s="".join(sline)
        q=[[] for _ in range(99)]
        for i in ascii_lowercase:
            q[s.count(i)]+=[i]
        p = "".join(["".join(x)for x in q[::-1]])
        if line[-7:-2]==p[:5]:
            code = int(x[:-8])
            s1+=code
            if "north" in "".join([ascii_lowercase[(ascii_lowercase.find(i)+code)%26] for i in s]):
                print("solution2: %d"%code)
    print("solution1: %d"%s1)
if __name__ == "__main__":
    main()
