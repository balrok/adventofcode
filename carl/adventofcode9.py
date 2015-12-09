import itertools

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)

def task1(s):
    nodes = set()
    edges = dict()
    for a in s.split("\n"):
        if a == "":
            continue
        x = a.split(" ")
        nodes.add(x[0])
        nodes.add(x[2])
        edges[(x[0], x[2])] = int(x[4])
        edges[(x[2], x[0])] = int(x[4])
    #import pprint
    #pprint.pprint(nodes)
    #pprint.pprint(edges)
    perm = itertools.permutations(nodes)
    #print(len(list(perm)))
    plength = []
    for i in perm:
        length = 0
        for p in pairwise(i):
            length += edges[tuple(p)]
        plength.append(length)
    print min(plength)
    print max(plength)


with open("input9") as f:
    s = f.read()
    task1(s)
