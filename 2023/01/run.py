for p in (1, 2):
    s = 0
    for line in open("input.txt", encoding="utf-8").read().rstrip().split("\n"):
        if p == 2:
            line = line.replace("one", "o1e")
            line = line.replace("two", "t2o")
            line = line.replace("three", "t3e")
            line = line.replace("four", "f4r")
            line = line.replace("five", "f5e")
            line = line.replace("six", "s6x")
            line = line.replace("seven", "s7n")
            line = line.replace("eight", "e8t")
            line = line.replace("nine", "n9e")
        w = [i for i in line if i in "123456789"]
        s += int(w[0] + w[-1])
    print(str(p) + ":" + str(s))
