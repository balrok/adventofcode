for t in 40,400000:
 a=[i<"^"for i in open("input").read().strip()];s=0
 for i in range(t):s+=sum(a);a=[x==y for x,y in zip([1]+a,a[1:]+[1])]
 print s
