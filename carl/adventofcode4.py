import hashlib

a="bgvyzdsv"

s = 609043

for s in range(0,10000000):
    if hashlib.md5(a+str(s)).hexdigest().startswith("00000"):
        print s
for s in range(1000000,10000000):
    if hashlib.md5(a+str(s)).hexdigest().startswith("000000"):
        print s
