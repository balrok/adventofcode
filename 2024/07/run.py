d=[list(map(int, l.split(" "))) for l in open("input.txt").read().strip().replace(":", "").split("\n")]

def result(res, l, p2):
    a=res+l[0]
    b=res*l[0]
    if p2:
        c=int(str(res) + str(l[0]))
    if len(l) > 1:
        yield from result(a, l[1:], p2)
        yield from result(b, l[1:], p2)
        if p2:
            yield from result(c, l[1:], p2)
    else:
        yield a
        yield b
        if p2:
            yield c

def check(l, p2):
    for r in result(l[1], l[2:], p2):
        if r == l[0]:
            return True
    return False

s=0
s2=0
for l in d:
    if check(l, False):
        s+=l[0]
    if check(l, True):
        s2+=l[0]
print(s)
print(s2)
