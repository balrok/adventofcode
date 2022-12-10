# solution for part2 was to convert the program to python and hand-optimize it

a=1
b=c=d=e=f=g=h=0

b=81
c=b
if a==1:
	b*=100
	b+=100000
	c=b
	c+=17000

while True:
	f=1
	for d in range(2,b):
		for e in range(2,b):
			if d*e == b:
				f=0
				break
			e+=1
			if d*e > b:
				break
		if f == 0:
			break
	if f == 0:
		h+=1
	if b == c:
		print(h)
		break
	b+=17
