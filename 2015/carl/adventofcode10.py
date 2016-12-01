import re
import time
import itertools

start = time.time()
s="1113222113"

# re implementation - medium fast
def repl1(s):
    new = []
    #f = re.finditer(r"(\d)\1*", s) this is a bit slower than the next
    f = re.finditer(r"1+|2+|3+", s)
    for m in f:
        a=m.group(0)
        new.append(str(len(a)))
        new.append(a[0])
    return "".join(new)

def repl6(s):
    new = []
    #f = re.finditer(r"(\d)\1*", s) this is a bit slower than the next
    f = re.findall(r"1+|2+|3+", s)
    for a in f:
        new.append(str(len(a)))
        new.append(a[0])
    return "".join(new)


# pure replace implementation - fast
def repl2(s):
    return s.replace('111', 'h') .replace('11', 'g') .replace('1', 'f') .replace('222', 'l') .replace('22', 'k') .replace('2', 'j') .replace('333', 'p') .replace('33', 'o') .replace('3', 'n') .replace('f', '11') .replace('g', '21') .replace('h', '31') .replace('j', '12') .replace('k', '22') .replace('l', '32') .replace('n', '13') .replace('o', '23') .replace('p', '33')


# using itertools - slow
def repl3(s):
    new = []
    f = ["".join(grp) for num, grp in itertools.groupby(s)]
    for a in f:
        new.append(str(len(a)))
        new.append(a[0])
    return "".join(new)

# pure replace implementation with micro-optimization
def repl4(s):
    return s.replace('111', 'h') .replace('11', 'g') .replace('1', '11') .replace('222', 'l') .replace('22', 'k') .replace('2', '12') .replace('333', 'p') .replace('33', 'o') .replace('3', '13') .replace('g', '21') .replace('h', '31') .replace('k', '22') .replace('l', '32') .replace('o', '23') .replace('p', '33')

# pure re implementation - slow
def repl5f(m):
    return str(len(m.group(0))) + m.group(1)
def repl5(s):
    return re.sub(r'(\d)\1*', repl5f, s)

for i in range(50):
    s = repl4(s)
    print i, len(s), time.time()-start #,s
