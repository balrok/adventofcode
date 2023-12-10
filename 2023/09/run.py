data = []
for l in open("input.txt").read().strip().split("\n"):
    data += [list(map(int, l.split(" ")))]

su = 0
su2 = 0
for oasis in data:
    rep = []
    rep += [oasis[:]]
    while any(map(lambda x: x != 0, rep[-1])):
        n = []
        for idx in range(1, len(rep[-1])):
            n += [rep[-1][idx] - rep[-1][idx - 1]]
        rep += [n]

    q = 0
    for i in range(len(rep) - 1, -1, -1):
        q += rep[i][-1]
    su += q

    q = 0
    for i in range(len(rep) - 1, -1, -1):
        q = rep[i][0] - q
    su2 += q
print(su)
print(su2)
