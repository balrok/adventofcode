for p in (1,2):
    s=0
    for l in open("input.txt").read().rstrip().split("\n"):
        if p==2:
            l=l.replace("one","o1e")
            l=l.replace("two","t2o")
            l=l.replace("three","t3e")
            l=l.replace("four","f4r")
            l=l.replace("five","f5e")
            l=l.replace("six","s6x")
            l=l.replace("seven","s7n")
            l=l.replace("eight","e8t")
            l=l.replace("nine","n9e")
        w=[int(i) for i in l if i in "123456789"]
        s+=10*w[0]+w[-1]
    print(str(p) + ":" + str(s))

