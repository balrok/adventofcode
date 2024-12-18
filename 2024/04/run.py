

d=list(map(list, open("input.txt").read().split("\n")))

def get(row, col):
    if row >= len(d) or row < 0:
        return "."
    if col >= len(d[row]) or col <0:
        return "."
    return d[row][col]

def find(row, col):
    s = 0
    if d[row][col] != "X":
        return 0
    if get(row+1,col+1) == "M" and get(row-1,col+1) == "A" and get(row+3,col) == "S":
        s+=1
    if get(row,col+1) == "M" and get(row,col+2) == "A" and get(row,col+3) == "S":
        s+=1
    if get(row-1,col) == "M" and get(row-2,col) == "A" and get(row-3,col) == "S":
        s+=1
    if get(row,col-1) == "M" and get(row,col-2) == "A" and get(row,col-3) == "S":
        s+=1
    if get(row+1,col+1) == "M" and get(row+2,col+2) == "A" and get(row+3,col+3) == "S":
        s+=1
    if get(row-1,col-1) == "M" and get(row-2,col-2) == "A" and get(row-3,col-3) == "S":
        s+=1
    if get(row+1,col-1) == "M" and get(row+2,col-2) == "A" and get(row+3,col-3) == "S":
        s+=1
    if get(row-1,col+1) == "M" and get(row-2,col+2) == "A" and get(row-3,col+3) == "S":
        s+=1
    return s

def find2(row, col):
    s = 0
    if d[row][col] != "A":
        return 0
    c = (get(row-1, col-1), get(row-1,col+1), get(row+1,col-1),get(row+1,col+1))
    if c.count("M") != 2 or c.count("S") != 2:
        return 0
    if c[0] == c[3]:
        return 0
    if c[1] == c[2]:
        return 0
    return 1

s=0
s2=0
for row in range(len(d)):
    for col in range(len(d[row])):
        s+=find(row,col)
        s2+=find2(row,col)
print(s)
print(s2)
