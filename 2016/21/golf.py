import re
for s,m in("abcdefgh",1),("fbgdceah",-1):
 for p,t,i in[(l[7],l[0],re.findall(" (\D|\d)\s",l)+[0])for l in open("input")][::m]:
	s=list(s);x,y=[int(q)if q<"a"else s.index(q)for q in i][:2]
	if"r "==t+p:s[x:y+1]=s[x:y+1][::-1]
	elif"r"==t:x=(x,((x+1+(x>3))%8,[1,1,6,2,7,3,0,4][x])[m<0])[p<"c"]*(m,m*-1)[p!="l"];s=s[x:]+s[:x]
	if"r"<t:s[x],s[y]=s[y],s[x]
	if m<0:x,y=y,x
	if"n">t:s.insert(y,s.pop(x))
 print"".join(s)
