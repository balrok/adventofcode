i="""33
14
18
20
45
35
16
35
1
13
18
13
50
44
48
6
24
41
30
42"""

numbers = [int(x) for x in i.split()]

import itertools
for n in range(1,21): print sum(sum(c) == 150 for c in itertools.combinations(numbers, n))
