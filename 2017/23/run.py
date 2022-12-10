# set X Y sets register X to the value of Y.
# sub X Y decreases register X by the value of Y.
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
# jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
# 
script = list(map(lambda x:x.split(" "), open("input.txt").read().rstrip().split("\n")))

def run(debug):
    vars={"a":debug,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0}
    print(script)
    pointer = 0

    def num(char):
        if char in vars:
            return vars[char]
        return int(char)
    c=0
    q=0
    while pointer < len(script):
        l = script[pointer]
        if l[0] == "set":
            if l[1]=="f" and l[2]=="0":
                pointer += 10
                q+=1
                print(q)
                continue
            vars[l[1]] = num(l[2])
            pointer += 1
        elif l[0] == "sub":
            vars[l[1]] -= num(l[2])
            pointer += 1
        elif l[0] == "mul":
            c+=1
            vars[l[1]] *= num(l[2])
            pointer += 1
        elif l[0] == "jnz":
            if num(l[1]) != 0:
                pointer += num(l[2])
            else:
                pointer += 1
    return c, vars
#print(run(0)[0])
print(run(1)[1]["h"])
vars = run(1)[1]
# 1000 too high
# 5001 too low
print(vars)
