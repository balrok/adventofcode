d=list(map(int, list(open("input.txt").read().strip())))
disk=[]
idx=0
is_file=True
spaces = []
data = []
for e in d:
    if is_file:
        data += [(len(disk), e)]
        disk += [idx] * e
        idx += 1
    else:
        spaces += [(len(disk), e)]
        disk += [-1] * e
    is_file = not is_file
m_idx = idx

disk1 = disk[:]
while True:
    try:
        first_free = disk1.index(-1)
    except:
        break
    while True:
        d = disk1[len(disk1) - 1]
        del disk1[len(disk1) - 1]
        if d != -1:
            disk1[first_free] = d
            break
print(sum([i*v for i,v in enumerate(disk1)]))

for i in range(len(data)-1, -1, -1):
    d = data[i]
    for si, s in enumerate(spaces):
        if s[1] >= d[1] and s[0] < d[0]:
            for j in range(s[0], s[0] + d[1]):
                disk[j] = disk[d[0]]
            for j in range(d[0], d[0] + d[1]):
                disk[j] = -1
            spaces[si] = (s[0] + d[1], s[1] - d[1])
            break
print(sum([i*v for i,v in enumerate(disk) if v > 0]))
