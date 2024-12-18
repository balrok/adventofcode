def safe(l):
    last = l[0]
    for i in l[1:]:
        diff = abs(i-last)
        if diff < 1 or diff > 3:
            return False
        last = i
    if l == sorted(l):
        return True
    if l == sorted(l, reverse=True):
        return True
    return False

def safe2(l):
    for i in range(0, len(l)):
        l2 = l[:]
        del l2[i]
        if safe(l2):
            return True
    return False

print(sum(map(safe, map(lambda x: list(map(int, x.split(" "))), open("input.txt").readlines()))))
print(sum(map(safe2, map(lambda x: list(map(int, x.split(" "))), open("input.txt").readlines()))))

