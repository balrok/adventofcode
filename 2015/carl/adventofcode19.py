import time
start = time.time()

mapping = []
# reverse the mapping and sort by length
mapping_reverse = []

def read(s):
    mode = 0
    for line in s.split("\n"):
        if line == "":
            mode += 1
        if mode == 0:
            mapping.append(line.split(" => "))
        if mode == 1:
            text = line
    return mapping, text
        

def gen_molecules(text):
    molecules = set()
    for m in mapping:
        # go over all m[0] in string text:
        for new_text in iter_molecules(m, text):
            molecules.add(new_text)
    return molecules

    
def iter_molecules(from_to, text):
    pos = 0
    while True:
        pos_n = text[pos:].find(from_to[0])
        if pos_n == -1:
            break
        pos += pos_n
        new_text = text[:pos]+text[pos:].replace(from_to[0], from_to[1], 1)
        yield new_text
        pos += len(from_to[0])
        if pos >= len(text):
            break

best_depth = 999
def gen_all_texts_backwards(text, depth, mapping, goal):
    global best_depth
    if depth > best_depth:
        return
    if text == goal:
        if depth < best_depth:
            print "found"
            print best_depth, depth
            best_depth = depth
    elif len(text) == 1:
        return
    for m in mapping:
        for new_text in iter_molecules(m, text):
            gen_all_texts_backwards(new_text, depth+1, mapping, goal)


def run(s, task2=False):
    mapping, text = read(s)
    mapping.sort(key = lambda s: len(s[1]))
    for m in mapping:
        mapping_reverse.append((m[1],m[0]))
    if not task2:
        molecules = gen_molecules(text)
        print len(molecules)
    else:
        print mapping_reverse
        mapping_reverse.reverse()
        gen_all_texts_backwards(text, 0, mapping_reverse, "e")



with open("input19") as f:
    s = f.read()
    run(s)
    run(s, True)
