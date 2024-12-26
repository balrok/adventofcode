d=open("input.txt").read().strip().split("\n")
d=[list(l)for l in d]
antennas = {}
r_m = len(d)
c_m = len(d[0])
def in_bound(rc):
    return rc[0] >= 0 and rc[0] < r_m and rc[1] >= 0 and rc[1] < c_m
for row in range(r_m):
    for col in range(c_m):
        a = d[row][col]
        if a != ".":
            l = antennas.get(a, [])
            l += [(row, col)]
            antennas[a] = l
an = set()
for rc_l in antennas.values():
    for rc1 in rc_l:
        for rc2 in rc_l:
            if rc1 == rc2:
                continue
            rd = abs(rc1[0] - rc2[0])
            cd = abs(rc1[1] - rc2[1])
            q = rc1
            w = rc2
            if q[0] < w[0] and q[1] < w[1]:
                q = (q[0] - rd, q[1] - cd)
                w = (w[0] + rd, w[1] + cd)
            if q[0] >= w[0] and q[1] < w[1]:
                q = (q[0] + rd, q[1] - cd)
                w = (w[0] - rd, w[1] + cd)
            if q[0] < w[0] and q[1] >= w[1]:
                q = (q[0] - rd, q[1] + cd)
                w = (w[0] + rd, w[1] - cd)
            if q[0] >= w[0] and q[1] >= w[1]:
                q = (q[0] + rd, q[1] + cd)
                w = (w[0] - rd, w[1] - cd)
            an.add(q)
            an.add(w)
print(len(list(filter(in_bound, an))))


an = set()
for rc_l in antennas.values():
    for rc1 in rc_l:
        for rc2 in rc_l:
            if rc1 == rc2:
                continue
            rd = abs(rc1[0] - rc2[0])
            cd = abs(rc1[1] - rc2[1])
            q = rc1
            w = rc2
            for _ in range(400):
                an.add(q)
                an.add(w)
                if q[0] < w[0] and q[1] < w[1]:
                    q = (q[0] - rd, q[1] - cd)
                    w = (w[0] + rd, w[1] + cd)
                if q[0] >= w[0] and q[1] < w[1]:
                    q = (q[0] + rd, q[1] - cd)
                    w = (w[0] - rd, w[1] + cd)
                if q[0] < w[0] and q[1] >= w[1]:
                    q = (q[0] - rd, q[1] + cd)
                    w = (w[0] + rd, w[1] - cd)
                if q[0] >= w[0] and q[1] >= w[1]:
                    q = (q[0] + rd, q[1] + cd)
                    w = (w[0] - rd, w[1] - cd)
                if not in_bound(q) and not in_bound(w):
                    break
print(len(list(filter(in_bound, an))))
