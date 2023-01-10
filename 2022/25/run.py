
def toint(num):
    c=0
    for i in range(len(num)):
        q=num[i]
        if q == "2" or q=="1"or q=="0":
            q=int(q)
        elif q=="-":
            q=-1
        elif q=="=":
            q=-2
        c+=pow(5,len(num)-i-1)*q
    return c

def tosnf(c,i):
    if c+2.5*pow(5,i)<0:
        return None
    if c > 2.5*pow(5,i):
        return None
    if c==0:
        if i>0:
            return "0"+tosnf(c,i-1)
        return "0"

    q=pow(5,i)*2
    if c-q>=0 or True:
        if i>0 and tosnf(c-q,i-1) is not None:
            return "2"+tosnf(c-q,i-1)
        if i==0 and c-q==0:
            return "2"
    q=pow(5,i)
    if c-q>=0 or True:
        if i>0 and tosnf(c-q,i-1) is not None:
            return "1"+tosnf(c-q,i-1)
        if i==0 and c-q==0:
            return "1"
    q=0
    if c-q>=0 or True:
        if i>0 and tosnf(c-q,i-1) is not None:
            return "0"+tosnf(c-q,i-1)
        if i==0 and c-q==0:
            return "0"

    q=-pow(5,i)
    if c-q>=0 or True:
        if i>0 and tosnf(c-q,i-1) is not None:
            return "-"+tosnf(c-q,i-1)
        if i==0 and c-q==0:
            return "-"
    q=-2*pow(5,i)
    if c-q>=0 or True:
        if i>0 and tosnf(c-q,i-1) is not None:
            return "="+tosnf(c-q,i-1)
        if i==0 and c-q==0:
            return "="
    return None

#print(toint("1121-1110-1=0"))
for i in range(21):
    print(i,tosnf(i,5))
print(tosnf(314159265,15))
print(tosnf(4890,15))

s=0
for l in open("input.txt").read().rstrip().split("\n"):
    s+=toint(l)
print(s)
print(tosnf(s,23))
