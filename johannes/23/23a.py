i = """
a = 0
b = 0

a += 1 # inc a
a *= 3 # tpl a
a *= 3 # tpl a
a *= 3 # tpl a
a += 1 # inc a
a *= 3 # tpl a
a += 1 # inc a
a *= 3 # tpl a
a += 1 # inc a
a += 1 # inc a
a *= 3 # tpl a
a += 1 # inc a
a += 1 # inc a
a *= 3 # tpl a
a += 1 # inc a
a += 1 # inc a
a *= 3 # tpl a
a += 1 # inc a
a += 1 # inc a
a *= 3 # tpl a
jmp +19
a *= 3 # tpl a
a *= 3 # tpl a
a *= 3 # tpl a
a *= 3 # tpl a
a += 1 # inc a
a += 1 # inc a
a *= 3 # tpl a
a += 1 # inc a
a *= 3 # tpl a
a += 1 # inc a
a += 1 # inc a
a *= 3 # tpl a
a += 1 # inc a
a += 1 # inc a
a *= 3 # tpl a
a += 1 # inc a
a *= 3 # tpl a
a *= 3 # tpl a
while a%2 == 1: # jio a, +8
	b += 1 # inc b
	if a%2 == 0: # jie a, +4
	a *= 3 # tpl a
	a += 1 # inc a
	jmp +2
	a /= 2 # hlf a
	# end while # jmp -7"""



i = """jio a, +22
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp +19
tpl a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7"""


reg = {}
reg["a"] = 1
reg["b"] = 0
prog = []
for l in i.split("\n"):
	prog.append(l.split())

x = 0
for cmd in prog:
	print x, cmd
	x+=1

pc = 0
while pc >= 0 and pc < len(prog):
	c = prog[pc]
	print pc, c, reg
	if c[0] == "hlf":
		reg[c[1]] /= 2
		pc += 1
	elif c[0] == "tpl":
		reg[c[1]] *= 3
		pc += 1
	elif c[0] == "inc":
		reg[c[1]] += 1
		pc += 1
	elif c[0] == "jmp":
		pc += int(c[1])
	elif c[0] == "jie":
		if reg[c[1][0]] % 2 == 0:
			pc += int(c[2])
		else:
			pc += 1
	elif c[0] == "jio":
		if reg[c[1][0]] == 1:
			pc += int(c[2])
		else:
			pc += 1

print reg

