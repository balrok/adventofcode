y=z=0
for l in open("input.txt").readlines():
 p=l.rfind("-");q=['']*9
 for i in map(chr,range(97,123)):q[8-l[:p].count(i)]+=i
 c=-int(l[p:-8]);y+=c*("".join(q)[:5]in l[p:])
 if(ord(l[0])-97+c)%26==13:z=c
print y,"\n",z
