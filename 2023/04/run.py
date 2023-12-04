import re

def matches(left, right):
    return len(set(right).intersection(left))


def score(s):
    if s == 0:
        return 0
    f = 1
    for _ in range(1, s):
        f += f
    return f


lines = open("input.txt").read().strip().split("\n")
copies = [1] * len(lines)
idx = 0
s = 0
for line in lines:
    _, right = line.split(": ")
    left, right = right.split("|")
    left = tuple(map(int, re.split("\\s+", left.strip())))
    right = tuple(map(int, re.split("\\s+", right.strip())))
    m = matches(left, right)
    s += score(m)
    for i in range(idx + 1, min(idx + 1 + m, len(copies))):
        copies[i] += copies[idx]
    idx += 1
print(s)
print(sum(copies))
