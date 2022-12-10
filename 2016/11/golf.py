import re
import heapq as h
hp=h.heappush
r4=range(4)
d = open("input").readlines()
s=" (\w*)-co"
rf=re.findall
co={}
c=0
for j in rf(s,"".join(d)):c+=1;co[j]=c
l=[[co[j]for j in rf(s,d[i])]+[-co[j]for j in rf(" (\w*) gen",d[i])]for i in r4]
ii=lambda f:1-any(i<0 for i in f)*any(-i not in f for i in f if i>0)
for w in 10,14:
 cl={};t=[(l,0,0)];f=l
 while len(f[3])<w:
  f,c,s=t.pop(0);fc=f[c]
  for d in c+1,c-1:
   if(d<0)+(d>3):continue
   for it in[[i,j]for i in fc for j in fc if i<j]+[[i]for i in fc]:
    tm=f[d]+it;tc=[x for x in fc if x not in it]
    if ii(tc)*ii(tm):n=[x[:]for x in f];n[c]=tc;n[d]=tm;nn=`sorted([(d+g+5)*(v in n[g])+g*(-v in n[g])for g in r4 for v in range(9)])`;t+=[(n,d,s+1)]*cl.get(nn,1);cl[nn]=0;
 print s;l[0]+=[7,-7,8,-8]
