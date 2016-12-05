b=c=d=e=0;f=abs;g=[0,-1,0,1]
for m in open("input.txt").read().split(", "):e+=2-3**(m[0]=="R");exec"g+=[(c,d)]*(0**b);c+=g[e%4];d-=g[~e%4];b=(b,f(c)+f(d))[(c,d)in g];"*int(m[1:])
print f(c)+f(d),"\n",b
