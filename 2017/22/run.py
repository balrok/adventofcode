grid={}
maxr=0
maxc=0
for r,l in enumerate(open("input.txt").read().rstrip().split("\n")):
    for c,o in enumerate(l):
        grid[(r,c)] = o
        maxr=max(r,maxr)
        maxc=max(c,maxc)

turnleft = {
    (-1, 0) : (0, -1),
    (0, -1) : (1, 0),
    (1, 0) : (0, 1),
    (0, 1) : (-1, 0),
}
turnright = {
    (-1, 0) : (0, 1),
    (0, -1) : (-1, 0),
    (1, 0) : (0, -1),
    (0, 1) : (1, 0),
}
facing = (-1, 0) # initially facing upwards
virus = (maxr//2, maxc//2)
infection_counter = 0
def wakeup():
    global virus, facing, grid, infection_counter
    cur = grid.get(virus, ".")
    if cur == "#":
        facing = turnright.get(facing)
    else:
        facing = turnleft.get(facing)
    if cur == ".":
        grid[virus] = "#"
        infection_counter+=1
    else:
        grid[virus] = "."
    virus = (virus[0] + facing[0], virus[1] + facing[1])

for _ in range(10000):
    wakeup()
print(infection_counter)













grid={}
maxr=0
maxc=0
for r,l in enumerate(open("input.txt").read().rstrip().split("\n")):
    for c,o in enumerate(l):
        grid[(r,c)] = o
        maxr=max(r,maxr)
        maxc=max(c,maxc)

turnleft = {
    (-1, 0) : (0, -1),
    (0, -1) : (1, 0),
    (1, 0) : (0, 1),
    (0, 1) : (-1, 0),
}
turnright = {
    (-1, 0) : (0, 1),
    (0, -1) : (-1, 0),
    (1, 0) : (0, -1),
    (0, 1) : (1, 0),
}
facing = (-1, 0) # initially facing upwards
virus = (maxr//2, maxc//2)
infection_counter = 0


#    Clean nodes become weakened.
#    Weakened nodes become infected.
#    Infected nodes become flagged.
#    Flagged nodes become clean.


#    Modify the state of the current node, as described above.
#    The virus carrier moves forward one node in the direction it is facing.

def wakeup():
    global virus, facing, grid, infection_counter
    cur = grid.get(virus, ".")
    if cur == "#":
        facing = turnright.get(facing)
    elif cur == ".":
        facing = turnleft.get(facing)
    elif cur == "F":
        facing = (-facing[0], -facing[1])

    if cur == ".":
        grid[virus] = "W"
    elif cur == "W":
        grid[virus] = "#"
        infection_counter+=1
    elif cur == "#":
        grid[virus] = "F"
    elif cur == "F":
        grid[virus] = "."
    virus = (virus[0] + facing[0], virus[1] + facing[1])

for _ in range(10000000):
    wakeup()
print(infection_counter)
