i = list("hepxcrrq")
def inc(s):
	c = True
	pos = len(s)-1
	while True:
		if s[pos]== "z":
			s[pos] = "a"
			pos -= 1
		else:
			s[pos] = chr(ord(s[pos])+1)
			break
	return s

def valid(s):
	p = "_"
	d = "_"
	cl = 0
	chain = False
	double = False
	for c in s:
		if c == "i" or c == "o" or c == "l":
			return False
		if ord(p) + 1 == ord(c):
			cl += 1
			if cl == 2:
				chain = True
		else:
			cl = 0
		if p == c and c != d:
			if d != "_":
				double = True
			d = c
		p = c
	return double and chain


for x in xrange(1324557):
	if valid(i):
		print x, "".join(i), "valid: ", valid(i)
	i = inc(i)
