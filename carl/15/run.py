import re

def solve(ps, pms):
    i=0
    r=range(len(ps))
    # speedup
    pmax = max(pms)
    pmax_idx = pms.index(pmax)
    while ps[pmax_idx]:
        i+=1
        for c in r:
            ps[c]=(ps[c]+1)%pms[c]
    while any(ps):
        i+=pmax
        for c in r:
            ps[c]=(ps[c]+pmax)%pms[c]
    return i

ps = []
pms = []
i=0
for l in open("input"):
    i+=1
    pmax,p = map(int,re.findall("( \d+)", l))
    ps += [(p+i)%pmax]
    pms += [pmax]
print solve(ps[:], pms[:])
i+=1
ps += [i%11]
pms += [11]
print solve(ps, pms)
