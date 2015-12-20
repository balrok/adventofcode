
n = 33100000
def presents(n):
	result = n
	for i in xrange(2, n//2 + 1):
		if n % i == 0 and n // i <= 50:
			result += i
	return result*11

step = 2**5*3**2*5
p,h = 0,step
while p < n:
	p = presents(h)
	if p >= n:
		print "house", h, "has", p, "presents"
	h += step


