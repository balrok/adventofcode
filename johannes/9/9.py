j="""Faerun to Tristram = 65
Faerun to Tambi = 129
Faerun to Norrath = 144
Faerun to Snowdin = 71
Faerun to Straylight = 137
Faerun to AlphaCentauri = 3
Faerun to Arbre = 149
Tristram to Tambi = 63
Tristram to Norrath = 4
Tristram to Snowdin = 105
Tristram to Straylight = 125
Tristram to AlphaCentauri = 55
Tristram to Arbre = 14
Tambi to Norrath = 68
Tambi to Snowdin = 52
Tambi to Straylight = 65
Tambi to AlphaCentauri = 22
Tambi to Arbre = 143
Norrath to Snowdin = 8
Norrath to Straylight = 23
Norrath to AlphaCentauri = 136
Norrath to Arbre = 115
Snowdin to Straylight = 101
Snowdin to AlphaCentauri = 84
Snowdin to Arbre = 96
Straylight to AlphaCentauri = 107
Straylight to Arbre = 14
AlphaCentauri to Arbre = 46"""

t = []
m = {}

for r in j.split("\n"):
	x = r.split(" ")
	t1 = x[0]
	t2 = x[2]
	d  = int(x[4])
	m[(t1,t2)] = d
	m[(t2,t1)] = d
	if not t1 in t:
		t.append(t1)
	if not t2 in t:
		t.append(t2)

def f(t1, t2, trav):
	if len(t2) == 0:
		return (t1,trav)
	else:
		mi = ([], float("inf"))
		for tx in t2:
			tra = t1[:]
			tra.append(tx)
			rem = t2[:]
			rem.remove(tx)
			trav2 = trav + m[(t1[-1],tx)]
			tmi = f(tra, rem, trav2)
			if tmi[1] < mi[1]:
				mi = tmi
	return mi

mi = ([], float("inf"))
for tx in t:
	nt = t[:]
	nt.remove(tx)
	tmi = f([tx], nt, 0)
	if tmi[1] < mi[1]:
		mi = tmi

print mi
