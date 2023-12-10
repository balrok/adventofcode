data = []
start = (0, 0)
for row, l in enumerate(open("input.txt").read().strip().split("\n")):
    data += [l]
    if "S" in l:
        start = (row, l.index("S"))


def nxt(r, c, r2, c2):
    cur = data[r][c]
    # print(cur)
    if cur == "-":
        return r, c + (c - c2)
    if cur == "|":
        return r + (r - r2), c
    if cur == "F":
        if r != r2:
            return r, c + 1
        return r + 1, c
    if cur == "J":
        if r != r2:
            return r, c - 1
        return r - 1, c
    if cur == "7":
        if c != c2:
            return r + 1, c
        return r, c - 1
    if cur == "L":
        if c != c2:
            return r - 1, c
        return r, c + 1
    if cur == ".":
        assert False


def get_ins_r(r, c, r2, c2):
    if r > r2:
        return r2, c2 - 1
    if r < r2:
        return r2, c2 + 1
    if c > c2:
        return r2 + 1, c2
    if c < c2:
        return r2 - 1, c2


def get_ins_l(r, c, r2, c2):
    if r > r2:
        return r2, c2 + 1
    if r < r2:
        return r2, c2 - 1
    if c > c2:
        return r2 - 1, c2
    if c < c2:
        return r2 + 1, c2


def val(r, c):
    return r > 0 and c > 0 and r < len(data) and c < len(data[0])


def sur(r, c):
    yield (r - 0.5, c)
    yield (r + 0.5, c)
    yield (r, c - 0.5)
    yield (r, c + 0.5)
    yield (r - 0.5, c - 0.5)
    yield (r - 0.5, c + 0.5)
    yield (r + 0.5, c - 0.5)
    yield (r + 0.5, c + 0.5)


r, c = start
if data[r - 1][c] == "|":
    pos = (r - 1, c)
elif data[r + 1][c] == "|":
    pos = (r + 1, c)
elif data[r][c - 1] == "-":
    pos = (r, c - 1)
elif data[r][c + 1] in "-7":
    pos = (r, c + 1)
m = set()
ins1 = set()
ins2 = set()
step = 1
lst = start
m.add(pos)
m.add(((pos[0] + lst[0]) / 2, (pos[1] + lst[1]) / 2))
while pos != start:
    tmp = nxt(*pos, *lst)
    lst = pos
    pos = tmp
    step += 1
    m.add(pos)
    m.add(((pos[0] + lst[0]) / 2, (pos[1] + lst[1]) / 2))
    i = get_ins_r(*pos, *lst)
    if val(*i):
        ins1.add(i)
    i = get_ins_l(*pos, *lst)
    if val(*i):
        ins2.add(i)
    if pos == start:
        break
for x in m:
    if x in ins1:
        ins1.remove(x)
    if x in ins2:
        ins2.remove(x)


# fill up the inside/outside data by moving around a
def fill(ins):
    inl = list(ins)
    c = 0
    while c < len(inl):
        x = inl[c]
        for i in sur(*x):
            if not val(*i):
                return []
            if i not in m and i not in ins:
                ins.add(i)
                inl += [i]
        c += 1
    return ins


ins1 = fill(ins1)
ins2 = fill(ins2)


print("part 1:", step // 2)
print(
    "part 2:",
    max(
        len([i for i in ins1 if int(i[0]) == i[0] and int(i[1]) == i[1]]),
        len([i for i in ins2 if int(i[0]) == i[0] and int(i[1]) == i[1]]),
    ),
)
