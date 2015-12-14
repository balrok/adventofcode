i="""Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds."""

T = 2503

rs = []

for l in i.split("\n"):
	ls = l.split(" ")
	r = {}
	r["name"] = ls[0]
	r["speed"] = int(ls[3])
	r["fly"] = int(ls[6])
	r["rest"] = int(ls[13])
	print r
	rs.append(r)

for r in rs:
	cycles = T // (r["fly"] + r["rest"])
	remaining_seconds = T % (r["fly"] + r["rest"])
	travelled = cycles * r["fly"] * r["speed"]
	print cycles, remaining_seconds, travelled
	remaining_seconds = min(remaining_seconds, r["fly"])
	travelled += remaining_seconds * r["speed"]
	print travelled
