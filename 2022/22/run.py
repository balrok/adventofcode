row=1
m={}
start_pos=None
moves=[]
for l in open("input.txt").read().rstrip().split("\n"):
    if "R" in l:
        num=""
        for col in range(len(l)):
            c=l[col]
            if c=="R" or c=="L":
                moves+=[int(num)]
                moves+=[c]
                num=""
            else:
                num+=c
        moves+=[int(num)]
        #print(moves)
        break
    for col in range(len(l)):
        if l[col]!=" ":
            m[(row,col+1)]=l[col]
            if start_pos is None and l[col]==".":
                start_pos =(row,col+1,0)
    row+=1

def step(pos):
    if pos[2]==0: return (pos[0],pos[1]+1,pos[2])
    if pos[2]==1: return (pos[0]+1,pos[1],pos[2])
    if pos[2]==2: return (pos[0],pos[1]-1,pos[2])
    if pos[2]==3: return (pos[0]-1,pos[1],pos[2])
def stepback(pos):
    if pos[2]==0: return (pos[0],pos[1]-1,pos[2])
    if pos[2]==1: return (pos[0]-1,pos[1],pos[2])
    if pos[2]==2: return (pos[0],pos[1]+1,pos[2])
    if pos[2]==3: return (pos[0]+1,pos[1],pos[2])
def turn(t,pos):
    if t=="R": return (pos[0],pos[1],(pos[2]+1)%4)
    if t=="L": return (pos[0],pos[1],(pos[2]-1)%4)

def part1(pos):
    for move in moves:
        if isinstance(move, int):
            for _ in range(move):
                n=step(pos)
                # over the edge
                if (n[0],n[1]) not in m:
                    nb=n
                    while True:
                        nb2=stepback(nb)
                        if (nb2[0],nb2[1]) not in m:
                            break
                        nb=nb2
                    n=nb
                # into a wall
                if m[(n[0],n[1])]=="#":
                    break
                pos=n
        else:
            pos=turn(move,pos)
    print(1000*pos[0]+4*pos[1]+pos[2])

def reverse_look(pos):
    return (pos[0],pos[1],(pos[2]+2)%4)


wrap = {}
for c in range(0,50):
    # 1
    wrap[(0,51+c,3)]=(151+c,1,0)
    # 1-
    wrap[(151+c,0,2)]=(1,51+c,1)
    # 2
    wrap[(0,101+c,3)]=(200,1+c,3)
    # 2-
    wrap[(201,1+c,1)]=(1,101+c,1)
    # 3
    wrap[(1+c,151,0)]=(151-c,100,2)
    # 3-
    wrap[(101+c,101,0)]=(51-c,150,2)
    # 4
    wrap[(51,101+c,1)] = (51+c,100,2)
    # 4-
    wrap[(51+c,101,0)] = (50,101+c,3)
    # 5
    wrap[(51+c,50,2)] = (101,1+c,1)
    # 5-
    wrap[(100,1+c,3)] = (51+c,51,0)
    # 6
    wrap[(151,51+c,1)] = (151+c,50,2)
    # 6-
    wrap[(151+c,51,0)] = (150,51+c,3)
    # 7
    wrap[(1+c,50,2)] = (150-c,1,0)
    # 7-
    wrap[(101+c,0,2)] = (50-c,51,0)

def dostep(pos, checkaround=True):
    n=step(pos)
    #if checkaround:
    #    print(n)
    # over the edge
    if (n[0],n[1]) not in m:
        n2 = wrap[n]
        #q=stepback(n2)
        #qq= (q[0],q[1],(q[2]+2)%4)
        #if qq in wrap:
        #    qq2 = reverse_look(stepback(wrap[qq]))
        #    if checkaround:
        #        print("stepback %s -> %s vs %s/%s/%s/%s" % (str(n), str(n2), str(qq), wrap[qq], stepback(wrap[qq]), qq2))
        #    if qq2 != n:
        #        raise Exception("stepback broken")
        #    if checkaround:
        #        t=n2
        #        for _ in range(400):
        #            t=dostep(t,False)
        #        print("around %s->%s" % (n2, t))
        #        if n2 != t:
        #            raise Exception("around broken")
        #        t=reverse_look(n2)
        #        for _ in range(200):
        #            t=dostep(t,False)
        #        print("around2 %s->%s" % (reverse_look(n2), t))
        #        if n2 != reverse_look(t):
        #            raise Exception("around broken")
        #else:
        #    raise Exception("stepback broken2 %s -> %s vs %s" % (str(n), str(n2), str(q)))
        n = n2
    return n

def printturn(t):
    return [">","v", "<", "^"][t]

def printm(path):
    for r in range(1,201):
        for c in range(1,201):
            q=(r,c)
            if q in m:
                if m[q]=="#" and q in path: raise Exception("AAA")
                if q in path:
                    print(path[q],end="")
                else:
                    print(m[q],end="")
            else:
                if q in path: raise Exception("Mmm")
                print(" ",end="")
        print()

#part1(pos)
path={}
def part2(pos):
    global path
    c=0
    for i in range(len(moves)):
        move = moves[i]
        if isinstance(move, int):
            c+=1
            for x in range(move):
                n = dostep(pos)
                # into a wall
                if m[(n[0],n[1])]=="#":
                    break
                pos=n
                if x==0:
                    path[(pos[0],pos[1])]=str(c%10)
                elif i==len(moves)-1:
                    path[(pos[0],pos[1])]="X"
                else:
                    path[(pos[0],pos[1])]=printturn(pos[2])
        else:
            #if i%9==0:
            #    print(moves[i-1],moves[i])
            #    printm(path)
            #    path={}
            #    input()
            #print((pos[0],pos[1]))
            path[(pos[0],pos[1])]=move
            pos=turn(move,pos)
    print(1000*pos[0]+4*pos[1]+pos[2])
part1(start_pos)
part2(start_pos)
#print(moves)

#printm(path)
#print(len(moves))
