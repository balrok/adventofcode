#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    d = ""
    with open("input.txt") as i:
    #with open("sample.txt") as i:
        d = i.read().strip()
    solve1(d)
    solve2(d)

def solve1(d:str):
    up = 0
    right = 0
    curdir = "U"
    for m in d.split(", "):
        dir = m[0]
        steps = int(m[1:])
        curdir = get_cur_dir(curdir, dir)
        if curdir == "L":
            right -= steps
        elif curdir == "R":
            right += steps
        elif curdir == "U":
            up += steps
        elif curdir == "D":
            up -= steps
        else:
            print(dir)
    print("solution1: "+str(abs(up) + abs(right)))


def get_cur_dir(curdir:str, dir:str):
    r = {
        "L":{
            "U":"L",
            "L":"D",
            "D":"R",
            "R":"U",
        },
        "R":{
            "U":"R",
            "R":"D",
            "D":"L",
            "L":"U",
        }
    }
    return r[dir][curdir]


def solve2(d:str):
    visited = []
    startpos = [500, 500]
    pos = startpos[:]
    curdir = "U"
    count = 0
    visited.append(pos[:])
    for m in d.split(", "):
        count += 1
        dir = m[0]
        steps = int(m[1:])
        curdir = get_cur_dir(curdir, dir)
        move = { "L": (0, -1), "R": (0, +1), "U": (-1, 0), "D": (+1, 0), }
        found = False
        for _ in range(steps):
            pos[0] += move[curdir][0]
            pos[1] += move[curdir][1]
            if pos in visited:
                print("Solution2: " + str(abs(startpos[0]-pos[0]) + abs(startpos[1]-pos[1])))
                print("after %d steps" % len(visited))
                found = True
                break
            visited.append(pos[:])
        if found:
            break

if __name__ == "__main__":
    main()
