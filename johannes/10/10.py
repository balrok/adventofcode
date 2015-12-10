i = "1113222113"
for x in range(50):
	s = ""
	n = i[0]
	c = 0
	for d in i:
		if d == n:
			c += 1
		else:
			s += str(c)
			s += str(n)
			n = d
			c = 1
	s += str(c) + str(n)
	i = s
	print str(x + 1) + ": " + str(len(i))
