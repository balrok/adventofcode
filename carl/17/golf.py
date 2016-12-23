import md5
i=open("input").read().strip()
l=[]
t=[(1,1,0,"")]
while t:x,y,s,j=t.pop();g=x+y>7;l+=[(s,j)]*g;t+=[(v,w,s+1,j+d)for c,d,v,w in zip(md5.new(i+j).hexdigest(),"UDLR",(x,x,x-1,x+1),(y-1,y+1,y,y))if(5>v>0)*(c>"a")*(5>w>0)*(1-g)]
print min(l)[1],"\n",max(l)[0]
