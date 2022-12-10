import re
o=[]
p=[]
i=0
for l in open("input"):i+=1;q,r=map(int,re.findall("( \d+)",l));o+=[(r+i)%q];p+=[q]
q=o[:]+[(i+1)%11]
def s(o,p):
 i=0
 while any(o):
  i+=1
  for c in range(len(o)):o[c]=(o[c]+1)%p[c]
 return i
print s(o[:],p),"\n",s(o+[(i+1)%11],p+[11])
