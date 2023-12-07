from functools import cmp_to_key


def typ(hand):
    count = {}
    for i in order:
        count[i] = 0
    joker = 0
    if order.endswith("J"):
        joker = hand.count("J")
        hand = hand.replace("J", "")
    for i in hand:
        count[i] += 1
    count = list(count.values())
    count[count.index(max(count))] += joker
    if 5 in count:
        return 6
    if 4 in count:
        return 5
    if 3 in count and 2 in count:
        return 4
    if 3 in count:
        return 3
    if count.count(2) == 2:
        return 2
    if 2 in count:
        return 1
    return 0


def compare(item1, item2):
    if item1[0] == item2[0]:
        return 0
    if order.index(item1[0][0]) > order.index(item2[0][0]):
        return -1
    if order.index(item1[0][0]) < order.index(item2[0][0]):
        return 1
    return compare((item1[0][1:], 1), (item2[0][1:], 1))


def score():
    hands = {i: [] for i in range(7)}
    for line in inp:
        s = line.split(" ")
        hands[typ(s[0])] += [(s[0], int(s[1]))]
    res = 0
    c = 0
    for i in hands:
        hands[i].sort(key=cmp_to_key(compare))
        for s in hands[i]:
            c += 1
            res += c * s[1]
    return res


inp = open("input.txt").read().strip().split("\n")
order = "AKQJT98765432"
print(score())
order = "AKQT98765432J"
print(score())
