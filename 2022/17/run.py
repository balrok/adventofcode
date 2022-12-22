import pprint

patterns = [
    # -
    [(0,0),(0,1),(0,2),(0,3)],
    [
        # +
        (0,1),(-1,0),(-1,1),(-1,2),(-2,1)
    ],
    [
        # L
        (0,0),(0,1),(0,2),(-1,2),(-2,2)
    ],
    [
        # I
        (0,0),(-1,0),(-2,0),(-3,0)
    ],
    [
        # #
        (0,0),(0,1),(-1,0),(-1,1)
    ],
]

pprint.pprint(patterns)

wind=list(open("input.txt").read().rstrip())
field = [["#"]*7]
cur_p = 0 # pattern
cur_w = 0 # wind
new = True

seen={}
def get_new_row_col():
    global field
    x=7
    for l in field:
        if "#" in l:
            break
        x-=1
    if x > 0:
        for i in range(x):
            field = [["."]*7] + field
    return (3,2)

def add(rc1, rc2):
    return (rc1[0]+rc2[0], rc1[1]+rc2[1])

def is_overlapping(pattern, prc, field):
    for p in pattern:
        c=add(prc,p)
        if c[0]>=0:
            if c[1]<0 or c[1] > 6:
                return True
            if field[c[0]][c[1]] == "#":
                return True
    return False

def pp(field):
    print(10*"-")
    for l in field:
        print("".join(l))

def write(field,prc,pattern,s):
    len_before=0
    i=0
    for l in field:
        i+=1
        if "#" in l:
            len_before=len(field)-i
            break
    for p in pattern:
        t=add(prc,p)
        field[t[0]][t[1]]=s
    i=0
    for l in field:
        i+=1
        if "#" in l:
            return(len(field)-i-len_before)

stopped = 0
l=0
while True:
    if new:
        prc = get_new_row_col()
        pattern=patterns[cur_p]
        cur_p += 1
        cur_p %= 5
        new=False
    w = wind[cur_w]
    cur_w += 1
    cur_w %= len(wind)
    if w==">":
        prc=add(prc,(0,1))
        if is_overlapping(pattern, prc, field):
            prc=add(prc,(0,-1))
    elif w=="<":
        prc=add(prc,(0,-1))
        if is_overlapping(pattern, prc, field):
            prc=add(prc,(0,1))
    prc=add(prc,(1,0))
    if is_overlapping(pattern, prc, field):
        prc=add(prc,(-1,0))
        new=True
        l += write(field,prc,pattern,"#")
        stopped += 1
        state=(cur_w, cur_p)
        if stopped > len(wind) and state in seen:
            sstopped = stopped - seen[state][0]
            slen = l - seen[state][1]
            if stopped+sstopped<1000000000000:
                l+=slen
                stopped+=sstopped
        seen[state] = (stopped, l)
        if stopped == 2022:
            print(2022, l)
        if stopped == 1000000000000:
            print(1000000000000, l)
            break
