n="1"
m="0"
l="x"
d=open("input").read()
for q in 272,35651584:
 while len(d)<q:d+=m+d.replace(n,l).replace(m,n).replace(l,m)[::-1];e=d[:q]
 while len(e)%2<1:e=["01"[e[i]==e[i+1]]for i in range(0,len(e)-1,2)]
 print"".join(e)
