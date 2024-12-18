import re
d=open("input.txt").read()
def mul(a,b):
    return a*b
print(eval("+".join(re.findall("mul\([0-9]+,[0-9]+\)", d))))
print(eval("+".join(re.findall("mul\([0-9]+,[0-9]+\)", re.sub("don't\(\).*?do\(\)", "", d.replace("\n",""))))))
