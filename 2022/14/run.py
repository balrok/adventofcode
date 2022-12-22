pour=(500,0)

m={}
smallest=500
highest=500
lowest=0
for l in open("input.txt").read().rstrip().split("\n"):
    last=None
    for c in [list(map(int,i.split(",")))for i in l.split(" -> ")]:
        if c[0]<smallest:
            smallest = c[0]
        if c[0]>highest:
            highest = c[0]
        if c[1]>lowest:
            lowest = c[1]
        if last is not None:
            if last[1]==c[1]:
                for i in range(min(last[0],c[0]),max(last[0],c[0])+1):
                    m[(i,c[1])]="#"
            else:
                for i in range(min(last[1],c[1]),max(last[1],c[1])+1):
                    m[(c[0],i)]="#"
        last=c

def printm():
    for r in range(lowest+1):
        for c in range(smallest,highest+1):
            p=(c,r)
            if p in m:
                print(m[p],end="")
            else:
                print(".",end="")
        print("")
    print("")

def sandfall(sand):
    while True:
        if (sand[0],sand[1]+1) in m:
            if (sand[0]-1,sand[1]+1) in m:
                if (sand[0]+1,sand[1]+1) in m:
                    return sand
                else:
                    sand = (sand[0]+1,sand[1]+1)
            else:
                sand = (sand[0]-1,sand[1]+1)
        else:
            sand = (sand[0],sand[1]+1)
        if sand[1]>lowest:
            raise Exception

def putsand():
    q=sandfall(pour)
    if q==pour:
        raise Exception("aa")
    m[q]="o"

for k in range(100000):
    try:
        putsand()
    except:
        print(k)
        break
#printm()

for i in range(-1000,1000):
    m[(i, lowest + 2)] = "#"
lowest += 2
for i in range(k,1000000):
    try:
        putsand()
    except:
        print(i+1)
        break
#printm()
