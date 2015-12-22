import time
start = time.time()
try:
    range = xrange
except:
    pass

find_num = 3310000

import math
def get_divisors(n):
    yield 1
    yield n
    sq = int(math.sqrt(n))
    yield sq
    for i in reversed(range(2, sq-1)):
        if n % i == 0:
            yield i
            yield int(n/i)

def get_presents(n,mm=find_num):
    sq = int(math.sqrt(n))
    s = 1+n+sq
    for i in reversed(range(2, sq-1)):
        if n % i == 0:
            s+=i+n/i
            if s >mm:
                return -1
    return s

print(list(get_divisors(9)))
def get_presents0(house):
    return sum(get_divisors(house))*10

# test:
for i in range(10):
    print("test",get_presents(i))

for i in range(560000, find_num):
    if i % 10000==0:
        print(time.time()-start, i)
    if get_presents(i) == find_num:
        print("found", i)
