import re
from heapq import heappop, heappush
n=[map(int,re.findall("(\d+)",l))for l in open("input")if l[0]=="/"]
p=1+[(q[1])for q in n[::-1]].index(0)
n=[(q[4],q[3])for q in n]
l=len(n)
g=l-p
c=[]
t=[]
f=max(n)[0]
heappush(t,(0,g,[((1,0)[a==f],2)[u>f]for a,u in n],0))
while g>0:
 _,g,n,s=heappop(t);j=n.index(0)
 for i in [i for i in[j+p,j-p]+[j-1]*(j%p>0)+[j+1]*(j%p<p-1)if l>i>=0 and n[i]==1]:
  m=n[:];m[j],m[i]=m[i],m[j];u=(g,j)[g==i];h=1000*i+u
  if h not in c:c+=[h];heappush(t,(i%p,u,m,s+1))
print(n.count(1))
print(s)
