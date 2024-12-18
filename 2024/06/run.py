d=open("input.txt").read().strip()
m=[]
row=0
guard=None
for line in d.split("\n"):
    print(line)
    m+=[list(line)]
    if "^" in line:
        col=line.index("^")
        guard=(row,col)
    row+=1

def turn(di):
    if di == (-1,0): return (0,1)
    if di == (0,1): return (1,0)
    if di == (1,0): return (0,-1)
    if di == (0,-1): return (-1,0)

def run(guard, di):
    visited = set()
    visited2 = set()
    while True:
        visited.add(guard)
        if (guard, di) in visited2:
            return "loop"
        visited2.add((guard, di))
        for i in range(4):
            nguard = (guard[0] + di[0], guard[1] + di[1])
            if nguard[0]<0 or nguard[1] < 0 or nguard[0] >= len(m) or nguard[1] >= len(m[nguard[0]]):
                return visited
            if m[nguard[0]][nguard[1]] == "#":
                di = turn(di)
            else:
                guard = nguard
                break

print(len(run(guard, (-1, 0))))
c=0
for row in range(len(m)):
    for col in range(len(m[row])):
        if m[row][col] == ".":
            m[row][col] = "#"
            c+=run(guard, (-1,0)) == "loop"
            m[row][col] = "."
            print(c)

