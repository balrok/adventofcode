a=map(chr,range(97,123))
y=z=0
for l in open("input.txt").readlines():
 p=l.rfind("-");x=l[p+1:];s=l[:p];q=['']*99
 for i in a:q[s.count(i)]+=i
 c=int(x[:-8])*("".join(q[::-1])[:5]in x);y+=c;z+=c*("north"in"".join([a[(ord(i)-97+c)%26]for i in s]))
print y,"\n",z
