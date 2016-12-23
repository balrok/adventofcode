b=c=d=e=f=0;g=[0,-1,0,1]
for m in open("input.txt").read().split(", "):e+=2-3**(m[0]>"Q");exec"h=c,d;c+=g[e%4];d-=g[~e%4];b=(b,f)[h in g];g+=[h]*(0**b);f=abs(c)+abs(d);"*int(m[1:])
print f,"\n",b
