l=list(map(lambda x: (int(x[0]),int(x[1])), map(lambda x: x.split("/"), open("input.txt").read().rstrip().split("\n"))))
def search(pp,p,n):
    lbest = best = sum([sum(i) for i in p])
    longest = len(p)
    for v in pp:
        if n not in v:
            continue
        pp2 = pp[:]
        pp2.remove(v)
        newbest, newlbest, newlongest =search(pp2, p[:] + [v], (v[0],v[1])[v[0]==n])
        best=max(best, newbest)
        if newlongest > longest or (newlongest == longest and newlbest > lbest):
            longest = newlongest
            lbest = newlbest
    return best, lbest, longest
print(search(l[:], [], 0)[:2])
