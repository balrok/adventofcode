def d(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

data=list(map(lambda x: list(map(int,x.split(", "))),open("input.txt").read().rstrip().replace("Sensor at x=","")
    .replace(": closest beacon is at x=", ", ").replace("y=","").split("\n")))
m={}
sdist={}
xmin=0
xmax=0
for i in data:
    s=tuple(i[:2])
    b=tuple(i[2:4])
    sdist[s]=d(s,b)
    m[s]="S"
    m[b]="B"
    xmin=min([xmin,i[0],i[2]])
    xmax=max([xmax,i[0],i[2]])

f=0
for x in range(xmin*2, 2*xmax+1):
    p=(x,2000000)
    if p in m:
        continue
    for sensor,dist in sdist.items():
        if d(p,sensor)<=dist:
            f+=1
            break
print(f,xmin)

def part2():
    yinc=250000
    for ystart in range(-1, 4000001, yinc):
        x=-1
        jump0=0
        while x<4000001:
            x+=1
            #if x%100000==0:
            #    print(x,ystart)
            y=ystart
            yend=min(4000001,ystart+yinc+1)
            while y<yend:
                y+=1
                if y==ystart+1 and jump0>3:
                    jump0-=3
                    y+=jump0
                    if y>yend:
                        continue
                p=(x,y)
                if p in m:
                    continue
                q=[dist-d(p,sensor) for sensor,dist in sdist.items()]
                a=max(q)
                if a<0:
                    return x,y
                else:
                    if y==ystart+1:
                        jump0=a
                    y+=a
x,y=part2()
# 13267474686239
print(x*4000000 + y)
