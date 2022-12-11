from typing import List, Tuple

class Monkey:
    num: int
    items: List[int]
    operation_old_old: bool = False
    operation_old_times_num: int = 0
    operation_old_plus_num: int = 0
    test_div: int = 1
    test_true_monkey: int = 0
    test_false_monkey: int = 0
    inspected:int = 0
    mod: int = 0
    is_part1 = True

    def __repr__(self):
        s = f"M{self.num} [{self.items}] "
        if self.operation_old_old:
            s += "old*old"
        elif self.operation_old_plus_num:
            s += f"old+{self.operation_old_plus_num}"
        else:
            s += f"old*{self.operation_old_times_num}"
        s += f" /{self.test_div}? {self.test_true_monkey} : {self.test_false_monkey}"
        return s

    def operate(self, item):
        if self.operation_old_old:
            return item * item
        elif self.operation_old_times_num:
            return item * self.operation_old_times_num
        elif self.operation_old_plus_num:
            return item + self.operation_old_plus_num

    def inspect_all(self, monkeys:List):
        """ modifies the input "monkeys" """
        for _ in range(len(self.items)):
            item, throw = monkeys[m].inspect()
            #print(self.num, item, throw)
            #input()
            monkeys[throw].items.append(item)

    def inspect(self) -> Tuple[int, int]:
        self.inspected += 1
        item = self.items[0]
        #print(self.num, item)
        #input()
        self.items = self.items[1:]
        item = self.operate(item)
        if self.is_part1:
            item = item // 3
        item %= self.mod
        if item % self.test_div == 0:
            return item, self.test_true_monkey
        return item, self.test_false_monkey

def parse(is_part1 = True) -> List[Monkey]:
    monkeys:List[Monkey] = []
    monkey:Monkey
    for l in open("input.txt").read().rstrip().split("\n"):
        if not l:
            continue
        if l[0] == "M":
            monkey = Monkey()
            monkey.is_part1 = is_part1
            monkey.num = len(monkeys)
            monkeys.append(monkey)
        elif l[2] == "S":
            monkey.items = list(map(int, l.split(": ")[1].split(", ")))
        elif l[2] == "O":
            if "old * old" in l:
                monkey.operation_old_old = True
            elif "*" in l:
                monkey.operation_old_times_num = int(l.split(" ")[-1])
            elif "+" in l:
                monkey.operation_old_plus_num = int(l.split(" ")[-1])
            else:
                print("ERROR", l)
        elif l[2] == "T":
            m = int(l.split(" ")[-1])
            monkey.test_div = m
        elif l[4] == "I":
            m = int(l.split(" ")[-1])
            if "true" in l:
                monkey.test_true_monkey = m
            if "false" in l:
                monkey.test_false_monkey = m
    mul = 1
    for m in monkeys:
        mul *= m.test_div
    for m in monkeys:
        m.mod = mul
    return monkeys

monkeys = parse()
for _ in range(20):
    for m in range(len(monkeys)):
        monkeys[m].inspect_all(monkeys)
a=sorted([m.inspected for m in monkeys])
print(a[-1]*a[-2])

monkeys = parse(False)
for i in range(10_000):
    for m in range(len(monkeys)):
        monkeys[m].inspect_all(monkeys)
a=sorted([m.inspected for m in monkeys])
print(a[-1]*a[-2])
