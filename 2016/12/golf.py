a,d="ad"
for m in 0,1:
 r={`i`:i for i in range(-9,99)};c=r[a]=r["b"]=r[d]=0;r["c"]=m;w=[(x[0],x.split()+[d])for x in open("input")]
 while c<len(w):
	k,z=w[c];x=r[z[1]];r[z[1]]+=(k=="i")-(k==d);y=z[2];c+=(1,r[y]+(x<0))[k=="j"and x!=0]
	if k<d:r[y]=x
 print r[a]
