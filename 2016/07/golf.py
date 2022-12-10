import re
a=b=0
n="\n"
f=re.sub
m=lambda l:f(r"(.)(?!\1)(.)\2\1",n,l)<l
for l in open("input.txt").readlines():o=f("[^[]*]",n,l);i=f("(]|^)[^[]*",n,l);a+=0**m(i)*m(o);b+=any([y+x+y in i for x,y,z in zip(o,o[1:],o[2:])if z==x!=y])
print a,n,b
