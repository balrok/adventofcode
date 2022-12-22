from functools import lru_cache
bps=[]
for l in open("input.txt").read().rstrip().split("\n"):
    ll=l.split(" ")
    bps+=[((int(ll[6]),0,0,0),(int(ll[12]),0,0,0),(int(ll[18]),int(ll[21]),0,0),(int(ll[27]),0,int(ll[30]),0))]

def add(xyz1, xzy2):
    return (xyz1[0]+xzy2[0],xyz1[1]+xzy2[1],xyz1[2]+xzy2[2],xyz1[3]+xzy2[3])
def sub(xyz1, xzy2):
    return (xyz1[0]-xzy2[0],xyz1[1]-xzy2[1],xyz1[2]-xzy2[2],xyz1[3]-xzy2[3])

@lru_cache(maxsize=90)
def m(minutes,r2):
    h=r=0
    for m in range(minutes):
        h+=r
        if not r2:
            r2 = True
        else:
            r+=1
    return h

def h1(bp,res,rob,minutes):
    res=res[3]
    r=rob[3]
    r2=rob[2]
    # no geode and no obsidian -> skip all where geode-amount is over minutes
    if r==0 and r2==0 and bp[3][2]>minutes*3:
        return -1
    h=res+r*minutes
    h+=m(minutes,r2>0)
    return h

def buyable(bp,res,r):
    if res[0]<bp[r][0]:
        return False
    if r==2:
        return res[1]>=bp[r][1]
    if r==3:
        return res[2]>=bp[r][2]
    return True

robs={0:(1,0,0,0),1:(0,1,0,0),2:(0,0,1,0),3:(0,0,0,1)}
def h2(bp,res,rob,minutes):
    rob=list(rob)
    res=list(res)
    b=[False,False,False,False]
    for _ in range(minutes):
        b[0]=b[0]or buyable(bp,res,0)
        b[1]=b[1]or buyable(bp,res,1)
        b[2]=b[2]or buyable(bp,res,2)
        b[3]=b[3]or buyable(bp,res,3)
        res[0]+=rob[0]
        res[1]+=rob[1]
        res[2]+=rob[2]
        res[3]+=rob[3]
        rob[0]+=b[0]
        rob[1]+=b[1]
        rob[2]+=b[2]
        rob[3]+=b[3]
    return res[3]

def sim(bp,res,rob,minutes,g_best,mm,searched):
    s=(res,rob,minutes)
    if s in searched:
        return g_best
    searched.add(s)
    res2=add(res,rob)
    best=res2[3]
    minutes -= 1
    if minutes==0:
        return best
    if h2(bp,res,rob,minutes+1)<=g_best:
        return g_best
    for r in range(3,-1,-1):
        # don't build if res-cost are lower anyway
        if r==2 and rob[2]==bp[3][2]:
            continue
        if r==1 and rob[1]==bp[2][1]:
            continue
        if r==0 and rob[0]==mm:
            continue
        if buyable(bp,res,r):
            res3=sub(res2,bp[r])
            rob3=add(rob,robs[r])
            nbest=sim(bp, res3,rob3,minutes,g_best,mm,searched)
            if nbest>best:
                best = nbest
                g_best = max(g_best,best)
            # geode is always the best to buy
            if r==3:
                return best
        # last minute, so no further calc required
        if minutes==1:
            return add(res2,rob)[3]
    nbest=sim(bp, res2,rob, minutes,g_best,mm,searched)
    if nbest>best:
        best = nbest
        g_best = max(g_best,best)
    return best

def ssim(bp,minutes,g_best):
    i=bp[0]
    bp=bp[1]
    mm=max(bp[2][0],bp[1][0],bp[0][0],bp[3][0])
    return i, sim(bp,(0,0,0,0),(1,0,0,0),minutes,g_best,mm,set())
s = 0
s2 = 1
for bp in enumerate(bps):
    i,r=ssim(bp,24,0)
    s+=(i+1)*r
    if bp[0]<3:
        i,r=ssim(bp,32,r)
        s2*=r
print(s,s2)
