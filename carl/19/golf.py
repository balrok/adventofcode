p=lambda:(i+(2*y)+(l-y)/2)%l
for m in 1,0:
 i=0;l=int(open("input").read());d=range(1,l+1)
 while l>1:
  y=0;g=p();q=set([p()for y in range(0,l/2)if p()>=g])
  d=([d[z]for z in range(l)if z not in q],((l==3)+(1-l%2))*[d[0]]+d[2::2])[m]
  i=(i+len(q))%l;l=len(d)
 print d[0]
