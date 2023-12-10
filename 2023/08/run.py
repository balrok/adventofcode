inp = open("input.txt").read().strip().split("\n")
instr = inp[0]
nodes = {}
for l in inp[2:]:
    s = l.split(" = ")
    nodes[s[0]] = tuple(s[1][1:-1].split(", "))

point = 0
cur = "AAA"
while cur != "ZZZ":
    cur = nodes[cur][(instr[point % len(instr)] == "R")]
    point += 1
print(point)

cur_l = [i for i in nodes if i[-1] == "A"]
z = [0] * len(cur_l)
for idx, cur in enumerate(cur_l):
    point = 0
    while cur[-1] != "Z":
        cur = nodes[cur][(instr[point % len(instr)] == "R")]
        point += 1
    z[idx - 1] = point
import math

print(math.lcm(*z))
