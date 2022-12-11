class State:
    def __init__(self):
        self.writ = [0,0]
        self.move = [0,0]
        self.cont = [0,0]
    def run(self, tape, cursor):
        val = tape.get(cursor, 0)
        tape[cursor] = self.writ[val]
        cursor += self.move[val]
        return cursor, self.cont[val]

def parse():
    states = []
    start = 0
    diag = 0
    state = None
    condition = 0
    for l in open("input.txt").read().split("\n"):
        if not l:
            continue
        l=l[:-1]
        s = l.split(" ")
        if l[0] == "B":
            start = ord(l[-1]) - 65
        elif l[0] == "P":
            diag = int(s[-2])
        elif l[0] == "I":
            state = State()
            states.append(state)
            condition = 0
        elif l[6] == "W":
            state.writ[condition] = int(l[-1])
        elif l[6] == "M":
            state.move[condition] = (-1,1)[l[-2]=="h"]
        elif l[6] == "C":
            state.cont[condition] = ord(l[-1]) - 65
            condition = 1
    return states, start, diag

tape = {}
cursor = 2
states, current, diag = parse()
for _ in range(diag):
    cursor, current = states[current].run(tape, cursor)
print(sum(tape.values()))
