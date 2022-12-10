import re
f=re.findall
def d(s):
 s=list(s)
 for p,t,i,c in w:
	x,y=(i+[s.index(q)for q in c]+[0])[:2]
	if t=="re":s[x:y+1]=s[x:y+1][::-1]
	if t=="ro":
	 if c:x=(x+1+(x>=4))%8
	 if p<1:x*=-1
	 s=s[x:]+s[:x]
	if t=="sw":s[x],s[y]=s[y],s[x]
	if t=="mo":s.insert(y,s.pop(x))
 return "".join(s)
w=[("e l" in line,line[:2],map(int,f("(\d+)",line)),f(" (\w)\s",line))for line in open("input")]
g="fbgdceah"
from itertools import*
print d("abcdefgh"),"\n","".join([s for s in permutations(g)if d(s)==g][0])
