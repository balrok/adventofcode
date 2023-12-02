#!/usr/bin/python3
def mul(vals):
    result = 1
    for val in vals:
        result *= val
    return result

def main():
    sum_possible = 0
    sum_min_cubes = 0
    for line in open("input.txt", encoding="utf-8").read().strip().split("\n"):
        game, sets = line.split(": ")
        game = int(game.split(" ")[1])
        possible = True
        mincubes = {"red": 1, "green": 1, "blue": 1}
        for play in sets.split(";"):
            allow = {"red": 12, "green": 13, "blue": 14}
            for single_play in play.split(", "):
                sp_data = single_play.strip().split(" ")
                if allow[sp_data[1]] < int(sp_data[0]):
                    possible = False
                mincubes[sp_data[1]] = max(mincubes[sp_data[1]], int(sp_data[0]))
        sum_min_cubes += mul(mincubes.values())
        if possible:
            sum_possible += game
    print(sum_possible)
    print(sum_min_cubes)


main()
