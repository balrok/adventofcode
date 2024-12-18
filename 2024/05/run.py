d=open("input.txt").read().strip().split("\n\n")
f=list(map(lambda x: list(map(int, x.split("|"))), d[0].split("\n")))
l=list(map(lambda x: list(map(int, x.split(","))), d[1].split("\n")))
s=0
s2=0
for i in l:
    ok = True
    for zz in range(20):
        change = False
        for ff in f:
            if ff[0] in i and ff[1] in i:
                if i.index(ff[0]) > i.index(ff[1]):
                    ok = False
                    idx0 = i.index(ff[0])
                    idx1 = i.index(ff[1])
                    i[idx0] = ff[1]
                    i[idx1] = ff[0]
                    change = True
        if not change:
            break
    if ok:
        s += i[len(i)//2]
    else:
        s2 += i[len(i)//2]
print(s)
print(s2)
