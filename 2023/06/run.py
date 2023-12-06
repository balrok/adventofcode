import re

inp= open("input.txt").read().strip().split("\n")
#data= open("e").read().strip().split("\n")
t=tuple(map(int, re.split("\s+", inp[0])[1:]))
d=tuple(map(int, re.split("\s+", inp[1])[1:]))

t2=int(inp[0].split(":")[1].replace(" ", ""))
d2=int(inp[1].split(":")[1].replace(" ", ""))

def check(hold, time, dist):
    return (time - hold) * hold > dist

def mul_res(res):
    v = 1
    for i in res:
        v*=i
    return v

res = []
for l in range(0, len(t)):
    c = 0
    for h in range(0, t[l]):
        if check(h, t[l], d[l]):
            c += 1
        elif c > 0:
            break
    res += [c]

print(mul_res(res))


c = 0
for h in range(0, t2):
    if check(h, t2, d2):
        c += 1
    elif c > 0:
        break
print(c)
