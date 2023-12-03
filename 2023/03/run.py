def get_num(line, x):
    num = ""
    for i in range(x, -1, -1):
        if line[i].isdigit():
            num = line[i] + num
        else:
            break
    for i in range(x + 1, len(line)):
        if line[i].isdigit():
            num += line[i]
        else:
            break
    if num == "":
        return None
    return int(num)


def get_adjacent(grid, row, col):
    return set(
        [
            grid.get(row - 1, {}).get(col - 1),
            grid.get(row - 1, {}).get(col),
            grid.get(row - 1, {}).get(col + 1),
            grid.get(row + 1, {}).get(col - 1),
            grid.get(row + 1, {}).get(col),
            grid.get(row + 1, {}).get(col + 1),
            grid.get(row, {}).get(col - 1),
            grid.get(row, {}).get(col + 1),
        ]
    )


grid = {}
row = col = 0
for line in open("input.txt").read().strip().split("\n"):
    grid[row] = {}
    for col in range(0, len(line)):
        if line[col].isdigit():
            grid[row][col] = get_num(line, col)
        elif line[col] == ".":
            continue
        else:
            grid[row][col] = line[col]
    row += 1

r = s = 0
for row in range(0, len(grid)):
    for col in grid[row]:
        if not isinstance(grid[row][col], int):
            s += sum([i for i in get_adjacent(grid, row, col) if isinstance(i, int)])
        if grid[row][col] == "*":
            mul = 1
            c = 0
            for i in get_adjacent(grid, row, col):
                if isinstance(i, int):
                    c += 1
                    mul *= i
            if c == 2:
                r += mul

print(s)
print(r)
