m=[list(i) for i in open("input.txt").read().rstrip().split("\n")]
start=(0,0)
goal=(0,0)
for r in range(len(m)):
    for c in range(len(m[r])):
        if m[r][c]=="S":
            start=(r,c)
        if m[r][c]=="E":
            goal=(r,c)


def pop_openlist_min(openlist):
    min_number = 9999
    min_index = 0
    for idx, l in enumerate(openlist):
        if l[1] < min_number:
            min_number = l[1]
            min_index = idx
    ret = openlist[min_index]
    del openlist[min_index]
    return ret

def astar():
    openlist = [(start, 0, [])]
    closedlist = set()
    while len(openlist) > 0:
        current_node, fval, path = pop_openlist_min(openlist)
        if current_node == goal:
            return path + [current_node]
        closedlist.add(current_node)
        expand_node(current_node, path, openlist, closedlist)
    return []

def expand_node(current_node, path, openlist, closedlist):
    neighbors = ((0,1),(0,-1),(1,0),(-1,0))
    current_char = m[current_node[0]][current_node[1]]
    if current_char == "S":
        current_char = "a"
    for n in neighbors:
        successor = (current_node[0]+n[0], current_node[1]+n[1])
        if successor[0] < 0 or successor[1]<0:
            continue
        if successor[0] >= len(m) or successor[1] >= len(m[0]):
            continue
        if successor in closedlist:
            continue
        successor_char = m[successor[0]][successor[1]]
        if successor_char == "E":
            successor_char = "z"
        if ord(current_char) < ord(successor_char) - 1:
            continue
        tentative_g = len(path) + 1
        better_exists = False
        existing_in_openlist = None
        for idx,l in enumerate(openlist):
            if l[0]==successor:
                existing_in_openlist = idx
                if tentative_g >= len(l[2]):
                    better_exists = True
                    break
        if better_exists:
            continue
        f = tentative_g + h(successor)
        if existing_in_openlist is not None:
            openlist[existing_in_openlist] = (successor, f, path[:] + [current_node])
        else:
            openlist.append((successor, f, path[:] + [current_node]))

def h(node):
    return abs(goal[0]-node[0]) + abs(goal[1]-node[1])

p=astar()
print(len(p)-1)
smallest_part2=[]
for r in range(len(m)):
    for c in range(len(m[r])):
        if m[r][c]=="a":
            start=(r,c)
            l = len(astar())-1
            if l == -1:
                continue
            smallest_part2+=[l]
print(min(smallest_part2))
