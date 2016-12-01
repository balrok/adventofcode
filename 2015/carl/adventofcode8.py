import re

def task1(s):
    c_code = 0
    c_memo = 0
    for a in s.split("\n"):
        c_code += len(a)
        real = a[1:-1]
        real = real.replace("\\\\", "a")
        real = re.sub(r"\\x[0-9a-f]{2}", "a", real)
        real = re.sub(r"\\.", "a", real)
        c_memo += len(real)
        print len(a), len(real), a[1:-1]
        print len(a), len(real), real
    print c_code, c_memo, c_code-c_memo

def task2(s):
    c_code = 0
    c_memo = 0
    for a in s.split("\n"):
        if a =="":
            continue
        c_code += len(a)
        real = a
        real = real.replace('"', "aa")
        real = real.replace("'", "aa")
        real = real.replace("\\", "aa")
        c_memo += len(real)+2
        print len(a), len(real)+2, a
        print len(a), len(real)+2, real
    print c_code, c_memo, c_memo-c_code

with open("input8") as f:
    s = f.read()
    task2(s)
