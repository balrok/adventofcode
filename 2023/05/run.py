seeds = tuple()
data = []
current = ""
c = 0
for line in open("input.txt").read().strip().split("\n"):
    if line.startswith("seeds:"):
        seeds = tuple(map(int, line.split(": ")[1].split(" ")))
    elif ":" in line:
        current = c  # line[:-1]
        c += 1
        data += [[]]
    elif len(line) == 0:
        continue
    else:
        split = tuple(map(int, line.split(" ")))
        data[current] += [split]


def do_map(inp, m):
    res = []
    for l in m:
        if l[1] <= inp and l[1] + l[2] > inp:
            res += [inp + l[0] - l[1]]
    return res


state = seeds[:]
for m in data:
    next_state = []
    for s in state:
        next_state += do_map(s, m)
    state = next_state

print(min(state))


def range_intersect(x, y):
    return range(max(x.start, y.start), min(x.stop, y.stop))


def do_map_r(inp, m):
    res = []
    for l in m:
        r = range(l[1], l[1] + l[2])
        intersect = range_intersect(inp, r)
        if len(intersect) != 0:
            add = l[0] - l[1]
            res += [range(intersect.start + add, intersect.stop + add)]
    return res


state = []
for s in range(0, len(seeds), 2):
    state += [range(seeds[s], seeds[s] + seeds[s + 1])]
for m in data:
    next_state = []
    for s in state:
        next_state += do_map_r(s, m)
    state = next_state
print(min(map(lambda x: x.start, state)))
