import sys

def get_light_board(s):
    board = []
    for line in s.split("\n"):
        if line=="":
            continue
        row = []
        for c in line:
            row.append((1,0)[c=="."])
        board.append(row)
    return board




def step(board):
    # watch my british english :)
    cmax = len(board[0])
    rmax = len(board)
    # what a silly thing: for two dimensional lists this is an array with a lot of references everywhere:
    # neighbours = [[0]*cmax]*rmax
    # so use this instead
    neighbours = [[0 for col in range(cmax)] for row in range(rmax)]


    def count_neighbours(rid, cid):
        n = [
            (rid-1,cid),(rid,cid-1),(rid-1,cid-1),
            (rid+1,cid),(rid,cid+1),(rid+1,cid+1),
            (rid+1,cid-1),(rid-1,cid+1)
            ]
        n = filter(lambda x: x[0]>=0 and x[1]>=0 and x[0]<rmax and x[1]<cmax, n)
        count = 0
        for i in n:
            count += board[i[0]][i[1]]
        return count

    for rid in range(rmax):
        for cid in range(cmax):
            neighbours[rid][cid] = count_neighbours(rid, cid)
    change = False
    for rid in range(rmax):
        for cid in range(cmax):
            if board[rid][cid] == 1:
                if neighbours[rid][cid] not in (2,3):
                    board[rid][cid] = 0
                    change = True
            else:
                if neighbours[rid][cid] == 3:
                    board[rid][cid] = 1
                    change = True
    return change

def print_board(board):
    for r in board:
        for c in r:
            sys.stdout.write(".#"[c])
        print ""

def light4corners(board):
    cmax = len(board[0])-1
    rmax = len(board)-1
    board[0][0] = 1
    board[rmax][0] = 1
    board[rmax][cmax] = 1
    board[0][cmax] = 1

def run(s, task2=False):
    board = get_light_board(s)
    change = True
    counter = 0
    if task2:
        light4corners(board)
    print_board(board)
    #import pprint
    #pprint.pprint(board)
    import time
    start = time.time()
    while True:
        counter += 1
        change = step(board)
        if task2:
            light4corners(board)
        print time.time()-start, counter, sum(map(sum, board))
        if not change or counter == 100:
            break
with open("input18") as f:
    s = f.read()
    #run(s)
    run(s, True)
