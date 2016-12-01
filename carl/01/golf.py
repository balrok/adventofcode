#!/usr/bin/env python3
move = ((0,-1),(-1,0),(0,1),(1,0))
def solve1(d:str):
    pos=(0,0)
    curdir = 0
    for m in d.split(", "):
        curdir = (curdir+{"L":-1,"R":1}[m[0]])%4
        pos = (pos[0]+int(m[1:])*move[curdir][0], pos[1]+int(m[1:])*move[curdir][1])
    print("solution1: "+str(abs(pos[0]) + abs(pos[1])))
def solve2(d:str):
    pos = (0,0)
    curdir = 0
    visited = [pos]
    for m in d.split(", "):
        curdir = (curdir+{"L":-1,"R":1}[m[0]])%4
        for _ in range(int(m[1:])):
            pos = (pos[0] + move[curdir][0], pos[1] + move[curdir][1])
            if pos in visited:
                return print("Solution2: " + str(abs(pos[0]) + abs(pos[1])))
            visited.append(pos)
solve1(open("input.txt").read().strip())
solve2(open("input.txt").read().strip())
