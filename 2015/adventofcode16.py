solution = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1}

class Aunt(object):
    greater_ranges = ("cats", "trees")
    smaller_ranges = ("pomeranians", "goldfish")
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __repr__(self):
        s = "Aunt %d" % self.id
        s += str(self.__dict__)
        return s

    def equals(self, aunt, range=False):
        props = set(self.__dict__).intersection(set(aunt.__dict__))
        for prop in props:
            ret = None
            if range:
                if prop in self.greater_ranges:
                    ret = self.__getattribute__(prop) > aunt.__getattribute__(prop)
                elif prop in self.smaller_ranges:
                    ret = self.__getattribute__(prop) < aunt.__getattribute__(prop)
                
            if ret is None:
                ret = self.__getattribute__(prop) == aunt.__getattribute__(prop)
            if ret == False:
                return False
        return True

    def equals_ranges(self, aunt):
        props = set(self.__dict__).intersection(set(aunt.__dict__))
        for prop in props:
            if self.__getattribute__(prop) != aunt.__getattribute__(prop):
                return False
        return True


import re
import pprint
def get_aunts(s):
    aunts = []
    for line in s.split("\n"):
        if line == "":
            continue
        f = re.findall(r"^Sue (\d+)", line)
        properties = {"id": int(f[0])}
        f = re.findall(r"([a-z]+): (\d+)", line)
        for ff in f:
            properties[ff[0]] = int(ff[1])
        aunts.append(Aunt(**properties))
    return aunts

def task1(aunts, solution_aunt):
    for aunt in aunts:
        if aunt.equals(solution_aunt):
            return aunt
def task2(aunts, solution_aunt):
    for aunt in aunts:
        if aunt.equals(solution_aunt, True):
            return aunt





with open("input16") as f:
    s = f.read()
    aunts = get_aunts(s)
    pprint.pprint(aunts)
    solution_aunt = Aunt(**solution)
    print task1(aunts, solution_aunt)
    print task2(aunts, solution_aunt)
