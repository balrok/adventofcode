import time

start = time.time()
s=list("hepxcrrq")

def incr(s):
    s.reverse()
    for idx,c in enumerate(s):
        if c == "z":
            s[idx] = "a"
        # this checks the iol condition
        elif c=="h" or c=="n" or c=="k":
            s[idx] = chr(ord(c)+2)
            break
        else:
            s[idx] = chr(ord(c)+1)
            break
    s.reverse()
    return s

let = []
last = list("abc")
while True:
    let.append("".join(last))
    if last[-1]=="z":
        break
    last = last[1:]
    last.append(chr(ord(last[-1])+1))

def check3(s):
    for i in let:
        if i in s:
            return True
    return False

import re
def checkOverlap(s):
    return re.search(r"([a-z])\1.*([a-z])\2", s)

def checkiol(s):
    #return re.search(r"([iol])",s)
    return "i" in s or "o" in s or "l" in s


#s=list("ghijklmn")

c=0
while True:
    c+=1
    s = incr(s)
    ss = "".join(s)

    if checkiol(ss):
        continue
    if not check3(ss):
        continue
    if not checkOverlap(ss):
        continue
    print c, ss, time.time()-start
