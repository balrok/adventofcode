

def code(rr, rc):
	r = c = 1
	v = 20151125
	while r != rr or c != rc:
		v = (v * 252533) % 33554393
		if r == 1:
			r = c + 1
			c = 1
		else:
			r -= 1
			c += 1
	return v

print code(3010,3019)

