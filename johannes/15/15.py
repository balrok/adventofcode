i = """Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8"""

ings = []

for l in i.split("\n"):
	ls = l.split(", ")
	ing = {}
	ing["cap"] = int(ls[0].split(" ")[2])
	ing["dur"] = int(ls[1].split(" ")[1])
	ing["fla"] = int(ls[2].split(" ")[1])
	ing["tex"] = int(ls[3].split(" ")[1])
	ing["cal"] = int(ls[4].split(" ")[1])
	ings.append(ing)

def score(ings):
	score = 1
	for part in ["cap", "dur", "fla", "tex"]:
		ts = 0
		for ing in ings:
			ts += ing["r"] * ing[part]
		if ts <= 0:
			return 0
		score *= ts
	return score

def cals(ings):
	c = 0
	for ing in ings:
		c += ing["r"] * ing["cal"]
	return c

mx = 0
cmx = 0
for f in xrange(0,101):
	for g in xrange(0,101-f):
		for h in xrange(0,101-f-g):
			i = 100 - f - g - h
			ings[0]["r"] = f
			ings[1]["r"] = g
			ings[2]["r"] = h
			ings[3]["r"] = i
			ts = score(ings)
			c = cals(ings)
			if mx < ts:
				mx = ts
			if cmx < ts and c == 500:
				cmx = ts

print mx, cmx
