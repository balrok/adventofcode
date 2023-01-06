from collections import defaultdict
m=set()
r=0
for l in open("input.txt").read().rstrip().split("\n"):
    r+=1
    for c in range(len(l)):
        if l[c]=="#":
            m.add((r,c))
print(m)

def m_north(elf,n,ne,nw,s,se,sw,w,e):
    return (elf[0]-1,elf[1])if n+ne+nw==0 else None
def m_south(elf,n,ne,nw,s,se,sw,w,e):
    return (elf[0]+1,elf[1])if s+se+sw==0 else None
def m_west(elf,n,ne,nw,s,se,sw,w,e):
    return (elf[0],elf[1]-1)if w+nw+sw==0 else None
def m_east(elf,n,ne,nw,s,se,sw,w,e):
    return (elf[0],elf[1]+1)if e+ne+se==0 else None
movers=[m_north,m_south,m_west,m_east]

def consider_and_move(m, iteration, part2):
    moves = {}
    proposals = defaultdict(lambda:0)
    nomove=0
    for elf in m:
        n=(elf[0]-1,elf[1]) in m
        ne=(elf[0]-1,elf[1]+1) in m
        nw=(elf[0]-1,elf[1]-1) in m
        s=(elf[0]+1,elf[1]) in m
        se=(elf[0]+1,elf[1]+1) in m
        sw=(elf[0]+1,elf[1]-1) in m
        w=(elf[0],elf[1]-1) in m
        e=(elf[0],elf[1]+1) in m
        # If no other Elves are in one of those eight positions, the Elf does not do anything
        if n+ne+nw+s+se+sw+w+e == 0:
            moves[elf]=elf
            proposals[elf]+=1
            nomove+=1
            continue
        for i in range(4):
            goal = movers[(i+iteration)%4](elf,n,ne,nw,s,se,sw,w,e)
            if goal is not None:
                #print("found",i,elf)
                moves[elf] = goal
                proposals[goal]+=1
                break
        else:
            goal = elf
            moves[elf] = goal
            proposals[goal]+=1
    m2 = set()
    for elf in m:
        goal = moves[elf]
        if proposals[goal] == 1:
            #print("moving", elf)
            m2.add(goal)
        else:
            #print("stay", elf, proposals[goal], goal)
            nomove+=1
            m2.add(elf)
    if part2 and nomove==len(m):
        raise Exception("part2:"+str(iteration+1))
    return m2

def minmax(m):
    rows = [e[0] for e in m]
    cols = [e[1] for e in m]
    return (min(rows),max(rows),min(cols),max(cols))

def printmap(m):
    mm=minmax(m)
    for r in range(mm[0],mm[1]+1):
        for c in range(mm[2],mm[3]+1):
            print([".","#"][(r,c) in m], end="")
        print()
def emptytiles(m):
    mm=minmax(m)
    r=abs(mm[0]-mm[1])+1
    c=abs(mm[2]-mm[3])+1
    return r*c-len(m)

part1 = m.copy()
for i in range(1000000):
    part1 = consider_and_move(part1, i,True)
    if i == 9:
        print(emptytiles(part1))
#printmap(part1)
# 6642 too high
print(emptytiles(part1))
