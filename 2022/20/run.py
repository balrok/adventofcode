dd=list(enumerate(map(int,open("input.txt").read().rstrip().split("\n"))))

def mov(idx,el,d):
    if el[1]==0:
        return
    del d[idx]
    nidx=(idx+el[1]+len(d))%len(d)
    d.insert(nidx,el)

d=dd[:]
for el in d[:]:
    idx=d.index(el)
    mov(idx,el,d)

for idx0,el in enumerate(d):
    if el[1]==0:
        break
print(sum([d[(idx0+1000)%len(d)][1],d[(idx0+2000)%len(d)][1],d[(idx0+3000)%len(d)][1]]))
#4224

dd=[(el[0],el[1]*811589153)for el in dd]
d=dd[:]
for _ in range(10):
    for el in dd[:]:
        idx=d.index(el)
        mov(idx,el,d)
for idx0,el in enumerate(d):
    if el[1]==0:
        break
print(sum([d[(idx0+1000)%len(d)][1],d[(idx0+2000)%len(d)][1],d[(idx0+3000)%len(d)][1]]))
