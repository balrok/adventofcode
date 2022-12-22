d=set(map(lambda x: tuple(map(int, x.split(","))), open("input.txt").read().rstrip().split("\n")))

def part1():
    q=0
    for c in d:
        a=6
        for x in (-1,1):
            if (c[0]+x, c[1], c[2]) in d:
                a-=1
            if (c[0], c[1]+x, c[2]) in d:
                a-=1
            if (c[0], c[1], c[2]+x) in d:
                a-=1
        q+=a
    return q
print(part1())

def add(xyz1, xzy2):
    return (xyz1[0]+xzy2[0],xyz1[1]+xzy2[1],xyz1[2]+xzy2[2])
def isout(xyz, xyzmin, xyzmax):
    for i in range(3):
        if xyz[i]<xyzmin[i]:
            return True
        if xyz[i]>xyzmax[i]:
            return True
    return False

def part2():
    xyzmin=(min(x[0]-1 for x in d), min(x[1]-1 for x in d), min(x[2]-1 for x in d))
    xyzmax=(max(x[0]+1 for x in d), max(x[1]+1 for x in d), max(x[2]+1 for x in d))

    q=0
    searched=set()
    tosearch=set([xyzmin])
    while tosearch:
        p=tosearch.pop()
        searched.add(p)
        a=0
        for x in ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)):
            pp=add(p,x)
            if pp in d:
                a+=1
            elif not isout(pp,xyzmin,xyzmax) and pp not in searched:
                tosearch.add(pp)
        q+=a
    return q
print(part2())
