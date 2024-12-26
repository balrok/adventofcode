d=list(map(lambda x:list(map(int,list(x))),open("input.txt").read().strip().split("\n")))

def sget(point):
    row=point[0]
    col=point[1]
    if row <0 or row >= len(d) or col < 0 or col>=len(d[0]):
        return -1
    return d[row][col]

def find_heads(row, col, path=None):
    if path is None:
        path = []
    path = path[:] + [(row,col)]
    n = set()
    c = d[row][col]
    point = (row-1, col)
    if sget(point) == c+1:n.add(point)
    point = (row+1, col)
    if sget(point) == c+1:n.add(point)
    point = (row, col-1)
    if sget(point) == c+1:n.add(point)
    point = (row, col+1)
    if sget(point) == c+1:n.add(point)

    if c == 8:
        return (n, set(tuple(path[:] + [i]) for i in n))
    r = set()
    s = set()
    for i in n:
        t = find_heads(i[0], i[1], path)
        for j in t[0]:
            r.add(j)
        for j in t[1]:
            s.add(j)
    return (r,s)

s = 0
s2=0
for row in range(len(d)):
    for col in range(len(d[0])):
        if d[row][col] == 0:
            res = find_heads(row, col)
            s += len(res[0])
            s2 += len(res[1])
print(s)
print(s2)
