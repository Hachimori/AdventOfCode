#!/usr/bin/env python

def read():
    lines = []    
    while 1:
        line = raw_input()
        if not line:
            break
        lines.append(line)
    return lines, raw_input()


def createMaze(lines):
    maze = []
    
    col = max(len(line) for line in lines)
    for line in lines:
        maze.append(line + ' ' * (col - len(line)))

    return maze


def createMove(moveStr):
    move = []
    for i in range(len(moveStr)):
        if moveStr[i].isalpha():
            move.append(moveStr[i])
        elif move and move[-1].isdigit():
            move[-1] += moveStr[i]
        else:
            move.append(moveStr[i])
        
    for i in range(len(move)):
        if move[i].isdigit():
            move[i] = int(move[i])
    
    return move


def getNextRC(r, c, to, row, col, maze):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    rr = r
    cc = c
    while 1:
        nr = (rr + row + dr[to]) % row
        nc = (cc + col + dc[to]) % col
            
        if maze[nr][nc] == '.' or maze[nr][nc] == '#':
            return (nr, nc)

        rr = nr
        cc = nc
        

    
def work((lines, moveStr)):
    maze = createMaze(lines)
    moves = createMove(moveStr)
    row, col = len(maze), len(maze[0])
                
    r = 0
    c = maze[0].index('.')
    to = 0

    for move in moves:
        if move == 'R':
            to = (to + 1) % 4
        elif move == 'L':
            to = (to + 3) % 4
        else:
            for _ in range(move):
                nr, nc = getNextRC(r, c, to, row, col, maze)
                if maze[nr][nc] == '#':
                    break
                r, c = nr, nc
                
    print (r + 1) * 1000 + (c + 1) * 4 + to
    
    
if __name__ == "__main__":
    work(read())
