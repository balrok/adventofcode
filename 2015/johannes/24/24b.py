i = """1
2
3
7
11
13
17
19
23
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113"""

p = [int(x) for x in i.split()]

s = sum(p)/4

import itertools
from operator import mul
x = float("inf")
for c in itertools.combinations(p,4):
	if sum(c) == s:
		x = min(x, reduce(mul, c, 1))
print x
