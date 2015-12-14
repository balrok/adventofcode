s="""Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
s="""Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds."""

class Deer:
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = int(speed)
        self.duration = int(duration)
        self.rest = int(rest)
        self.score = 0
        self.position = 0
        self.is_flying = True
        self.time = 0
        self.fly_counter = 0

    def dofly(self): 
        if not self.is_flying:
            self.is_flying = True
            self.time = 1
        self.position += self.speed

    def dorest(self): 
        if self.is_flying:
            self.is_flying = False
            self.time = 1

    def __repr__(self):
        ret = "%s (%d/%d - %d): %d %d %d" % (
                self.name, self.speed, self.duration, self.rest, self.position,
                self.is_flying, self.time)
        ret += " "+str(self.fly_counter)
        return ret

def constructDeers(s):
    deers = []
    for a in s.split("\n"):
        t = a.split(" ")
        deers.append(Deer(t[0], t[3], t[6], t[13]))
    return deers    



def findBest(deers):
    best = []
    for d in deers:
        best.append(d.position)
    return max(best) 

def task1(deers):
    for i in range(2503):
        for d in deers:
            d.time += 1
            if d.is_flying:
                if d.time > d.duration:
                    d.dorest()
                else: 
                    d.dofly()
            else:
                if d.time > d.rest:
                    d.dofly()
    return deers

def task2(deers):
    for i in range(2503):
        for d in deers:
            d.time += 1
            if d.is_flying:
                if d.time > d.duration:
                    d.dorest()
                else: 
                    d.dofly()
            else:
                if d.time > d.rest:
                    d.dofly()
        b = findBest(deers)
        for d in deers:
            if d.position == b:
                d.score += 1
    for d in deers:
        d.position = d.score
    return deers

import pprint

deers = constructDeers(s)
pprint.pprint(deers)
print findBest(task1(deers))
pprint.pprint(deers)

print "2nd"

deers = constructDeers(s)
pprint.pprint(deers)
print findBest(task2(deers))
pprint.pprint(deers)
# 5042 is too high
# 3069 is wrong

