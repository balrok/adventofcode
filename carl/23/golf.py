g=lambda x:r[x]if r.get(x)!=None else x
e=lambda x:int(x)if x<"a"else x
for a in 7,12:
 l=[[i[0][0],e(i[1]),e(i[2])]for i in [(l+" 0").split()for l in open("input")]]
 r={i:0 for i in"abcd"};r["a"]=a;i=0
 while i<len(l):
  t,x,y=l[i];v=g(x);w=g(y);z=zip(*l[i-5:i+1])
  if x!=v:r[x]+=(t=="i")-(t=="d")
  if"c"==t:r[y]=v
  if t=="t"and v+i>=0 and v+i<len(l):l[v+i][0]={"i":"d","j":"c","c":"j"}.get(l[v+i][0],"i")
  if t=="j"and v!=0:
   if w==-5 and z[0]==tuple("cidjdj"):r[z[1][1]]+=g(x)*g(z[1][0]);r[x]=0
   else:i+=w-(w>0)
  else:i+=1
 print(r["a"])
