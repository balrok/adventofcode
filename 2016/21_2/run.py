from typing import List,Dict

tmp=open("input.txt").read().strip().split("\n")
start_img=".#./..#/###"
def build_rules()->Dict[str,str]:
    rules={}
    for line in tmp:
        s=line.split(" => ")
        rules[s[0]]=s[1]
        img=s[0]
        for _ in range(2):
            for _ in range(3):
                if img not in rules:
                    rules[img]=s[1]
                img=rotate(img)
            img=flip(img)
    return rules

def rotate(img):
    a=img.split("/")
    if len(a)==3:
        return a[2][0]+a[1][0]+a[0][0]+"/"+ a[2][1]+a[1][1]+a[0][1]+"/"+ a[2][2]+a[1][2]+a[0][2]
    return a[1][0]+a[0][0]+"/"+ a[1][1]+a[0][1]

def flip(img):
    a=img.split("/")
    if len(a)==3:
        return a[0][::-1]+"/"+ a[1][::-1]+"/"+ a[2][::-1]
    return a[0][::-1]+"/"+ a[1][::-1]

def p(img):
    print(img.replace("/","\n"),img.count("#"))
    print("")

def divide(img:str) -> List[List[str]]:
    """divides a single string-image into a 2d img-array"""
    a=img.split("/")
    if len(a)%2==0:
        return [[a[r+0][c:c+2]+"/"+ a[r+1][c:c+2]for c in range(0,len(a),2)] for r in range(0,len(a),2)]
    return [[a[r+0][c:c+3]+"/"+ a[r+1][c:c+3]+"/"+a[r+2][c:c+3] for c in range(0,len(a),3)] for r in range(0,len(a),3)]

def join(dimg):
    """joins 2 dimensional img-array to a single string again"""
    return "".join([
        "".join([
            "".join([
                dimgrc.split("/")[i] for dimgrc in dimgr
            ])+"/"
            for i in range(0,dimg[0][0].count("/")+1)
        ])
        for dimgr in dimg
    ]).rstrip("/")

def run(img:str,it_amount:int):
    """run"""
    for _ in range(it_amount):
        dimg = divide(img)
        for row,dimgr in enumerate(dimg):
            for col,dimgrc in enumerate(dimgr):
                dimg[row][col]=rules.get(dimgrc)
        img = join(dimg)
    return img.count("#")

rules=build_rules()
assert 208 == run(start_img,5)
assert 2480380 == run(start_img,18)
