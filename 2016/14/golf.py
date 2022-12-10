import md5
import re
z=open("input").read(8)
for q in 1,2017:
 i=0;e=g=[]
 while len(g)<70:
  c=z+`i`;f=[]
  for _ in[0]*q:c=md5.new(c).hexdigest()
  for k,l in e:
   if k in c:g+=[l]
   elif l+999>i:f+=[(k,l)]
  e=f;k=re.findall(r"(.)\1\1",c)
  if k:e+=[(5*k[0][0],i)]
  i+=1
 print sorted(g)[63]
