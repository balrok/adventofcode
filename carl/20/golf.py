o=0
a=[]
while o<2**32:
 for l in open("input"):
  s,e=map(int,l.split("-"))
  if s<=o<=e:o=e+1;break
 else:a+=[o];o+=1
print min(a),"\n",len(a)
