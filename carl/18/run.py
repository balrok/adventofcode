a={0:[(1,0)[i=="^"]for i in open("input").read().strip()]}
def get_type(x,y,z):
    return (1,0)[x==y!=z or y==z!=x]

for t in 40,400000:
    for i in range(t-1):
        b = a[i]
        a[i+1]=[get_type(1,b[0],b[1])]+[get_type(b[j],b[j+1],b[j+2])for j in range(len(b)-2)]+[get_type(b[-2],b[-1],1)]
    print(sum(map(sum,a.values())))
