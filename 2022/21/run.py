d=open("input.txt").read().rstrip().split("\n")
n=[]
for l in d:
 l=l.replace(": ","=lambda:")
 if len(l)>20:l=l.replace(" ","()",1)+"()"
 if "root"in l: n.insert(0,l)
 else: n+=[l]
exec(";".join(n)+";print(int(root()))")

n+=[n[0].replace("+",">").replace("root","g")]
n[0]=n[0].replace("+","==")
p2 = ";".join(n)+"\ni=1;s=9**9;humn=lambda:i;gt=g()\nwhile not root():\n i+=s\n if gt!=g():gt=g();s*=-1/9;\nprint(int(i))"
exec(p2)
