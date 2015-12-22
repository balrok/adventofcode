wr = """Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""

ar = """Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
NoArmor       0     0       0"""

rr ="""Damage1    25     1       0
Damage2    50     2       0
Damage3   100     3       0
Defense1   20     0       1
Defense2   40     0       2
Defense3   80     0       3
NoRing      0     0       0"""

w = {}
a = {}
r = {}

for x in wr.split("\n"):
	w[x.split()[0]] = x.split()[1:]

for x in ar.split("\n"):
	a[x.split()[0]] = x.split()[1:]

for x in rr.split("\n"):
	r[x.split()[0]] = x.split()[1:]



def win(di, ai, hpi, dm, am, hpm):
	hpm -= max(di-am, 1)
	while hpm > 0:
		hpi -= max(dm-ai, 1)
		if hpi <= 0:
			return False
		hpm -= max(di-am, 1)
	return True

mn = float("inf")
mx = 0
for wx in w:
	for ax in a:
		for rx1 in r:
			for rx2 in r:
				if rx1 != rx2 or rx1 == "NoRing":
					cost = int(w[wx][0]) + int(a[ax][0]) + int(r[rx1][0]) + int(r[rx2][0])
					damage = int(w[wx][1]) + int(a[ax][1]) + int(r[rx1][1]) + int(r[rx2][1])
					armor = int(w[wx][2]) + int(a[ax][2]) + int(r[rx1][2]) + int(r[rx2][2])
					if win(damage, armor, 100, 9, 2, 103):
						if cost < mn:
							mn = cost
					else:
						if cost > mx:
							mx = cost

print "mn", mn
print "mx", mx
