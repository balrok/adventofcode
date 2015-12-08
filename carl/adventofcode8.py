import re

def task1(s):
    c_code = 0
    c_memo = 0
    for a in s.split("\n"):
        c_code += len(a)
        real = a[1:-1]
        real = re.sub(r"\\x[0-9a-f]*", "a", real)
        real = re.sub(r"\\x[0-9a-f]{2}", "a", real)
        real = re.sub(r"\\.", "a", real)
        c_memo += len(real)
        if "\\" in real:
            print real
        print len(a), len(real), a[1:-1]
        print len(a), len(real), real
    print c_code, c_memo, c_code-c_memo


with open("input8") as f:
    s = f.read()
    task1(s)
