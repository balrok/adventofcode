a=[[(s.count(l),l)for l in s]for s in zip(*open("input.txt").readlines())];print"".join(zip(*map(max,a)+map(min,a))[1])
