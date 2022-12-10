s="""jio a, +16
inc a
inc a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +23
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7"""

commands = []

for line in s.split("\n"):
    cmd = line.replace(",","").split(" ")
    try:
        cmd[-1] = int(cmd[-1])
    except:
        pass
    commands.append(cmd)



def cmd_hlf(r,_):
    return r/2, 1
def cmd_tpl(r,_):
    return r*3, 1
def cmd_inc(r,_):
    return r+1, 1
def cmd_jmp(r,o):
    return r,o
def cmd_jie(r,o):
    return r,(o,1)[r%2]
def cmd_jio(r,o):
    return r,(o,1)[r!=1]

cmd_mapping = {
    'hlf':cmd_hlf,
    'tpl':cmd_tpl,
    'inc':cmd_inc,
    'jmp':cmd_jmp,
    'jie':cmd_jie,
    'jio':cmd_jio,
}
def exe(cmd, reg=[0,0]):
    param1 = None
    param2 = None
    r = None
    if cmd[1] == "a":
        r = 0
    if cmd[1] == "b":
        r = 1
    func = cmd_mapping[cmd[0]]

    if cmd[1] == "a":
        param1 = reg[0]
    elif cmd[1] == "b":
        param1 = reg[1]
    else:
        param1 = cmd[1]

    try:
        param2 = cmd[2]
    except:
        pass
    if r is not None:
        reg[r], next_line = func(param1, param2)
        reg[r] = max(reg[r],0)
    else:
        if cmd[0] == "jmp":
            _, next_line = func(None, param1)
        else:
            _, next_line = func(param1, param2)
    return reg, next_line

import pprint
pprint.pprint(commands)
def run(current_line, reg):
    for i in range(10000):
        try:
            cmd = commands[current_line]
        except:
            break
        cmd_str = ""
        for cmd_s in cmd:
            try:
                cmd_str+=" "+cmd_s
            except:
                cmd_str+=" "+`cmd_s`
        #print("%02d: %02d %02d %s" %(current_line, reg[0], reg[1], cmd_str))
        reg, next_line = exe(cmd, reg)
        current_line += next_line
        #input("%02d: %02d %02d" %(current_line, reg[0], reg[1]))
    return reg

print "task1"
print run(0, [0,0])
print "task2"
print run(0, [1,0])
