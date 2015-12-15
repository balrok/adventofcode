s="""Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
s="""Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8"""


def prod(iterable):
    p= 1
    for n in iterable:
        if n < 0:
            return 0
        p *= n
    return p

class Ingredient:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = []
        for i in attributes:
            self.attributes.append(int(i))

    def getScore(self, x):
        for i in self.attributes:
            yield i*x

    def __repr__(self):
        return str(self.__dict__)

import re
def constructIngredients(s):
    ing = []
    for a in s.split("\n"):
        t = a.split(" ")
        atts = re.findall(r"(-?\d+)",a)
        ing.append(Ingredient(t[0][:-1], atts))
    return ing

def genPermutations(amount):
    p = []
    if amount == 4:
        for a in xrange(101):
            s=a
            for b in xrange(101-s):
                s=a+b
                for c in xrange(101-s):
                    s=a+b+c
                    d = 100-s
                    p.append((a,b,c,d))
    elif amount == 2:
        for a in xrange(101):
            s=a
            b = 100-s
            p.append((a,b))
    else:
        assert(False)
    return p

def task1(ing, task2=False):
    perm = genPermutations(len(ing))
    l = len(ing[0].attributes)
    best = []
    for p in perm:
        score = [0] * l
        ci = 0
        for i in ing:
            cj=0
            for j in i.getScore(p[ci]):
                score[cj] += j
                cj+=1
            ci+=1
        score_int = prod(score[:-1])
        if task2:
            if score[-1] == 500:
                best.append(score_int)
        else:
            best.append(score_int)
    return best

def task2(ing):
    return task1(ing, True)

import pprint
ing = constructIngredients(s)
pprint.pprint(ing)
print max(task1(ing))
print max(task2(ing))
