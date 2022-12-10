z=int(open("input").read())+1
g=31,39
c={}
t=[(1,1,-1)]
while len(t):
 x,y,s=t.pop(0)
 for n,m in(x+1,y),(x-1,y),(x,y+1),(x,y-1):
  if(bin(n*n+3*n+2*n*m+m+m*m+z).count("1")%2)*(n>=0)*(m>=0)*(c.get((n,m),99)>s):c[n,m]=s;t+=[(n,m,s+1)]
e=w=1
for i in c:w+=c[i]<48;e+=c[i]*(i==g)
print e,"\n",w
