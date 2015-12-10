import re

s="1113222113"
def repl(s):
    new = []
    f = re.finditer(r"(\d)\1*", s)
    for m in f:
        a=m.group(0)
        new.append(str(len(a)))
        new.append(a[0])
    return "".join(new)

for i in range(40):
    s = repl(s)
print s, len(s)
for i in range(10):
    s = repl(s)
print s, len(s)
