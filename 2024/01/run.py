d=list(map(lambda x: list(map(int, x.split("   "))), open("input.txt").readlines()))
l=sorted([i[0] for i in d])
r=sorted([i[1] for i in d])
s=0
s2=0
for i in range(len(l)):
    s+=abs(l[i]-r[i])
    s2+=l[i] * sum([1 for x in r if x == l[i]])
print(s)
print(s2)
