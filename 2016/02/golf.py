f=7*"0"
l=f+"10002340567890ABC000D"+f+"1230045600789"+f
x=41
n=20
i=k="\n"
for c in open("input.txt").read():
 t=(6-11**(c>"T"),2-3**(c<"M"))["K"<c<"S"]
 if c<f:i+=l[n];k+=l[x]
 else:x+=t*(l[x+t]>f);n+=t*(l[n+t]>f)
print k,i
