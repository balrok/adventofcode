import itertools
from functools import reduce
def combi(ll):
 for i in range(1,len(ll)-3):yield from itertools.combinations(ll,i)
def p(ll,t):
 s = sum(ll)/t
 if t==2:return True
 for a in combi(ll):
  if s==sum(a)and p(set(ll).difference(a),t-1):return reduce(lambda x,y:x*y, a)
ll=list(map(int,open("input.txt").read().strip().split("\n")))
print(p(ll,3),p(ll,4))
