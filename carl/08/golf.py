import re
d=[["."]*50]*6
for l in open("input.txt"):exec'''n,m=list(map(int,re.findall("(\d+)",l)));k="r"
%s
%s
k="c"
%s
%s
n,m=m,n
%s
%s'''%(('if l[7]==k:d[n]=d[n][-m:]+d[n][:-m]','if l[1]<"f":d[:m]=[["#"]*n+list(x[n:])for x in d[:m]]','d=zip(*d)')*2)
s="\n".join(map("".join,d))
print s.count("#"),"\n",s
