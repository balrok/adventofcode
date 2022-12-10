import re
o={}
f=".*(.. \d+)"
s="ut %d"
r=range
for i in r(300):o[s%i]=set();o["ot %d"%i]=set()
a=open("input").read()
for v,b in re.findall("e (\d+)"+f, a):o[b].add(int(v))
for _ in r(90):
 for b in o:
  p=o[b]
  if len(p)>1:y,z=re.findall(b+(" "+f)*2,a)[0];o[y].add(min(p));o[z].add(max(p))
  if(61 in p)*(17 in p):n=b
m=1
for i in r(3):m*=o[s%i].pop()
print(n[3:]+"\n%d"%m)
