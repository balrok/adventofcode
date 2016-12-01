import time
from multiprocessing import Process, Queue
start = time.time()
try:
    range = xrange
except:
    pass

find_num = 33100000


# https://de.wikibooks.org/wiki/Primzahlen:_Programmbeispiele
def pgen():
    ''' ... generates the sequence of all primes: 2,3,5,7,11 ... 
    '''
    p=2
    f=1
    while(True):
        if f%p%2:
            yield p
        p+=1
        f*=(p-2)
primes = []
primegen = pgen()
for i in range(0, 1000):
    primes.append(primegen.next())
print "generated %d primes" % len(primes)

def get_primes(n):
    while True:
        if primes[-1]**2 < n:
            for i in range(0, 100):
                primes.append(primegen.next())
            print "generated 100 more primes"
        else:
            break
    return primes

# http://stackoverflow.com/questions/12421969/finding-all-divisors-of-a-number-optimization
def factorize(n):
    for p in primes:
        if p**2 > n: break
        i = 0
        while n % p == 0:
            n //= p
            i+=1
        if i > 0:
            yield (p, i)
    if n > 1:
        yield (n, 1)

def divisors(factors):
    div = [1]
    for (p, r) in factors:
        div = [d * p**e for d in div for e in range(r + 1)]
    return div

def get_divisors(n):
    f = factorize(n)
    return divisors(f)



def get_divisors_slow(n):
    for i in range(1,n+1):
        if n%i == 0:
            yield i


def get_presents(n,mm=find_num):
    return sum(get_divisors(n))
# test:
for i in range(10):
    print("test",i,get_presents(i))


def find_present_house(range_start, range_end, queue):
    for i in range(range_start, range_end):
        if i % 50000==0:
            print(time.time()-start, i)
        if get_presents(i) >= find_num:
            print i
            queue.put(i)
            return


def task1():
    tasks = processors*[0]
    q = Queue()

    range_start = 0 
    step = 500000
    while q.empty():
        for i in range(processors):
            range_end = range_start + step
            p = Process(target=find_present_house, args=(range_start,range_end,q))
            p.start()
            tasks[i] = p
            range_start += step
        for i in range(processors):
            tasks[i].join()
    print "result(s):"
    while not q.empty():
        val = q.get()
        print val, get_presents(val), find_num



def task2():
    houses = {}
    elf_num = 0
    # 776160 was the solution of the first
    while True:
        elf_num += 1
        if elf_num % 10000 == 0:
            print elf_num
        c = 0
        house_num = 0
        while c < 50:
            house_num += elf_num
            c+=1
            try:
                houses[house_num] += 11*elf_num
            except:
                houses[house_num] = 11*elf_num
        if houses[elf_num] > find_num:
            print (elf_num, houses[elf_num], find_num)
            return



processors = 8
find_num /= 10
task1()
find_num *= 10
#task2()        
