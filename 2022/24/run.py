from functools import lru_cache
from queue import PriorityQueue
d=open("input.txt").read().rstrip().split("\n")
m=set()
moves={}
maxr=0
maxc=0
for r in range(len(d)):
    for c in range(len(d[r])):
        q=d[r][c]
        p=(r-1,c-1)
        if q=="#":
            maxr=max(maxr,r-1)
            maxc=max(maxc,c-1)
        if q==">":
            m.add(p)
            moves[p]=(0,1)
        if q=="<":
            m.add(p)
            moves[p]=(0,-1)
        if q=="v":
            m.add(p)
            moves[p]=(1,0)
        if q=="^":
            m.add(p)
            moves[p]=(-1,0)

def add(a, b, bmult, mod0, mod1):
    return ((a[0] + b[0] * bmult) % mod0, (a[1] + b[1] * bmult) % mod1)

@lru_cache(maxsize=500)
def get_map(iteration):
    m2=set()
    for w in m:
        m2.add(add(w,moves[w],iteration,maxr,maxc))
    return m2

def print_map(mm):
    for r in range(maxr):
        for c in range(maxc):
            if (r,c) in mm:
                print("X", end="")
            else:
                print(".", end="")
        print()

def cost(pos, goal):
    return goal[0]-pos[0] + goal[1] - pos[1]


start=(-1,0)
end=(maxr,maxc-1)
def search(pos,goal,part2=False):
    part2counter=0
    visited = set()
    tosearch = PriorityQueue()
    tosearch.put((0,(1,(0,0))))
    while not tosearch.empty():
        prio,s = tosearch.get()
        pos=s[1]
        if s in visited:
            continue
        if pos==goal:
            if part2:
                tosearch = PriorityQueue()
                visited=set()
                part2counter+=1
                if part2counter==1:
                    goal=start
                if part2counter==2:
                    goal=end
                if part2counter==3:
                    return s[0]
            else:
                return s[0]
        if pos!=start and pos!=end and (pos[0]<0 or pos[1]<0 or pos[0]>=maxr or pos[1]>=maxc):
            continue
        visited.add(s)
        next_minute = s[0] + 1
        new = [
            (next_minute, (pos[0]+1,pos[1]+0)),
            (next_minute, (pos[0]+0,pos[1]+1)),
            (next_minute, (pos[0]-1,pos[1]+0)),
            (next_minute, (pos[0]+0,pos[1]-1)),
            (next_minute, pos)
        ]
        mm=get_map(s[0]+1)
        for n in new:
            if n not in visited and n[1] not in mm:
                tosearch.put((next_minute + cost(n[1], goal), n))
    return 0
print(search((-1,0), (maxr,maxc-1)))
print(search((-1,0), (maxr,maxc-1), True))
#print_map(get_map(0))
