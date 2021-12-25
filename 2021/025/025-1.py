#!/usr/bin/env python

def read():
    state = []

    try:
        while 1:
            state.append(list(raw_input()))
    except EOFError:
        pass

    return state


def work(state):
    row = len(state)
    col = len(state[0])
    step = 0
    
    while 1:
        updated = False
        
        step += 1

        checkCh = ['>', 'v']
        dr = [0, 1]
        dc = [1, 0]
        for loop in range(2):
            isMoving = [[False for j in range(col)] for i in range(row)]
            for r in range(row):
                for c in range(col):
                    if state[r][c] == checkCh[loop] and state[(r + dr[loop]) % row][(c + dc[loop]) % col] == '.':
                        isMoving[r][c] = True
                        updated = True

            for r in range(row):
                for c in range(col):
                    if isMoving[r][c]:
                        t = state[r][c]
                        state[r][c] = state[(r + dr[loop]) % row][(c + dc[loop]) % col]
                        state[(r + dr[loop]) % row][(c + dc[loop]) % col] = t

        if not updated:
            break

    print step


if __name__ == "__main__":
    work(read())
