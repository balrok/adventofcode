l=7*[0]+[1,0,0,0,2,3,4,0,5,6,7,8,9,0,"A","B","C",0,0,0,"D"]+7*[0]
q=4*[0]+range(10)+5*[0]
x=9
n=20
i=k=""
for c in open("input.txt").read():
    if c=="\n":
        i+=str(l[n])
        k+=`q[x]`
        continue
    f,t=((2-3**(c>"T"),0),(0,(2-3**(c<"M"))))["K"<c<"S"]
    g=t+3*f
    t+=5*f
    if q[x+g]:x+=g
    if l[n+t]:n+=t
print k,"\n",i
