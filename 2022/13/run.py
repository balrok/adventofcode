import functools
ll=list(map(eval, filter(str, open("input.txt").read().rstrip().split("\n"))))
def cmp(a, b):
    if isinstance(a,int) and isinstance(b,int):
        return (a > b) - (a < b)
    elif isinstance(a,list) and isinstance(b,list):
        for j in range(len(a)):
            if j == len(b):
                return 1
            r = cmp(a[j],b[j])
            if r != 0:
                return r
        return (-1,0)[len(a)==len(b)]
    elif isinstance(a,int):
        return cmp([a], b)
    return cmp(a, [b])
right=[]
for i in range(0,len(ll),2):
    a=ll[i]
    b=ll[i+1]
    if cmp(a,b)==-1:
        right+=[i//2+1]
print(sum(right))
ll+=[[[2]]]
ll+=[[[6]]]
ll=sorted(ll, key=functools.cmp_to_key(cmp))
print((ll.index([[2]])+1) * (ll.index([[6]])+1))
