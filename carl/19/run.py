inp=int(open("input").read())
o = list(range(1,inp+1))
d=o[:]
l=inp
for c in range(100):
    # l==3: so d wil not get empty
    d = ((l==3) + (1-l%2))*[d[0]] + d[2::2]
    l = len(d)
    if l<=1:
        break
print(d, "iterations: ",c)

d=o[:]
i = 0
l = len(d)
for c in range(100):
    g = (i+l/2)%l
    # this is a bit slower because I can't break the list comprehension
    # q=set([g]+[(i+(2*y)+((l-y)/2))%l for y in range(1,(l+1)/2)if((i+(2*y)+((l-y)/2))%l) > g])
    q = set([g])
    for y in range(1,int(l/1.5)):
        s = (i+(2*y)+((l-y)/2))%l
        if s <= g:
            break
        q.add(s)
    d = [x for z,x in enumerate(d)if z not in q]
    i=(i+(len(q)))%l
    l=len(d)
    if l<=1:break
print(d, "iterations: ",c)
