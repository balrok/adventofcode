d=open("input.txt").read().strip()
def u(d,s=0,l=0):
 while 1:
	x=d.find("(")
	if x<0:return l+len(d)
	y=d.find(")",x);c,r=map(int,d[x+1:y].split("x"));y+=1;l+=len(d[:x])+r*(u(d[y:y+c]),c)[s];d=d[y+c:]
 return l
print `u(d,1)`+"\n"+`u(d)`
