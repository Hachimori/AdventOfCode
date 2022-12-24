#!/usr/bin/env python

UP = 1
RIGHT = 2
DOWN = 4
LEFT = 8


def gcd(a, b):
    if b == 0: return a
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a / gcd(a, b) * b


def read():
    state = []
    while 1:
        try:
            line = raw_input()
            state.append([])
            for ch in line:
                if ch == '.':
                    state[-1].append(0)
                elif ch == '^':
                    state[-1].append(UP)
                elif ch == '>':
                    state[-1].append(RIGHT)
                elif ch == 'v':
                    state[-1].append(DOWN)
                elif ch == '<':
                    state[-1].append(LEFT)
                elif ch == '#':
                    state[-1].append(-1)
        except EOFError:
            break
    return state


def makeState(LOOP, row, col, origState):
    state = [[[0 for c in range(col)] for r in range(row)] for loop in range(LOOP)]
    state[0] = origState
    
    for loop in range(1, LOOP):
        for r in range(row):
            for c in range(col):
                if origState[r][c] == -1:
                    state[loop][r][c] = -1
                    continue
                if state[loop - 1][r][c] & UP:
                    state[loop][row - 2 if r == 1 else r - 1][c] |= UP
                if state[loop - 1][r][c] & RIGHT:
                    state[loop][r][1 if c == col - 2 else c + 1] |= RIGHT
                if state[loop - 1][r][c] & DOWN:
                    state[loop][1 if r == row - 2 else r + 1][c] |= DOWN
                if state[loop - 1][r][c] & LEFT:
                    state[loop][r][col - 2 if c == 1 else c - 1] |= LEFT

    return state


def work(origState):
    row = len(origState)
    col = len(origState[0])
    LOOP = lcm(row - 2, col - 2)
    
    state = makeState(LOOP, row, col, origState)

    '''
    for i in range(LOOP):
        for r in range(row):
            for c in range(col):
                print "%4d" % state[i][r][c],
            print ""
        print ""
    print ""
    '''
    
    # cost[loop][row][col] := min cost
    cost = [[[10 ** 10 for k in range(col)] for j in range(row)] for i in range(LOOP)]

    Q = [(0, 0, 1)]
    cost[0][0][1] = 0
    
    while Q:
        loop, r, c = Q[0]
        del Q[0]
        
        if r == row - 1 and c == col - 2:
            print cost[loop][r][c]
            break
        
        dr = [-1, 0, 1, 0, 0]
        dc = [0, 1, 0, -1, 0]

        for i in range(5):
            nexLoop = (loop + 1) % LOOP
            nr = r + dr[i]
            nc = c + dc[i]
            
            if not (0 <= nr < row and 0 <= nc < col):
                continue
            
            if state[nexLoop][nr][nc] == 0 and cost[nexLoop][nr][nc] > cost[loop][r][c] + 1:
                cost[nexLoop][nr][nc] = cost[loop][r][c] + 1
                Q.append((nexLoop, nr, nc))
            

if __name__ == "__main__":
    work(read())
