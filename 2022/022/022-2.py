#!/usr/bin/env python
#
# It took 29 min to run.
#

import copy
import sys

sys.setrecursionlimit(30000)

SZ = 50 # 4
BOTTOM = 0
RIGHT = 1
TOP = 2
LEFT = 3
FRONT = 4
BACK = 5
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]



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


def swapFace(faceIdx1, faceIdx2, cube, cubePt):
    for r in range(SZ):
        for c in range(SZ):
            cube[faceIdx1][r][c], cube[faceIdx2][r][c] = cube[faceIdx2][r][c], cube[faceIdx1][r][c]
            cubePt[faceIdx1][r][c], cubePt[faceIdx2][r][c] = cubePt[faceIdx2][r][c], cubePt[faceIdx1][r][c]

def rotateFaceRight(face, facePt):
    buf = [[' ' for c in range(SZ)] for r in range(SZ)]
    '''
    for r in range(SZ):
        for c in range(SZ):
            buf[c][SZ - 1 - r] = face[r][c]
    for r in range(SZ):
        for c in range(SZ):
            face[r][c] = buf[r][c]
    '''    
    for r in range(SZ):
        for c in range(SZ):
            buf[c][SZ - 1 - r] = facePt[r][c]
    for r in range(SZ):
        for c in range(SZ):
            facePt[r][c] = buf[r][c]


def rotateFaceLeft(face, facePt):
    rotateFaceRight(face, facePt)
    rotateFaceRight(face, facePt)
    rotateFaceRight(face, facePt)

def rotateCubeRight(cube, cubePt):
    swapFace(BOTTOM, RIGHT, cube, cubePt)
    swapFace(RIGHT, TOP, cube, cubePt)
    swapFace(TOP, LEFT, cube, cubePt)    
    rotateFaceLeft(cube[FRONT], cubePt[FRONT])
    rotateFaceRight(cube[BACK], cubePt[BACK])

    rotateFaceLeft(cube[RIGHT], cubePt[RIGHT])
    rotateFaceLeft(cube[RIGHT], cubePt[RIGHT])
    rotateFaceLeft(cube[TOP], cubePt[TOP])
    rotateFaceLeft(cube[TOP], cubePt[TOP])


def rotateCubeLeft(cube, cubePt):
    rotateCubeRight(cube, cubePt)
    rotateCubeRight(cube, cubePt)
    rotateCubeRight(cube, cubePt)

def rotateCubeFront(cube, cubePt):
    swapFace(BOTTOM, FRONT, cube, cubePt)
    swapFace(FRONT, TOP, cube, cubePt)
    swapFace(TOP, BACK, cube, cubePt)
    rotateFaceRight(cube[RIGHT], cubePt[RIGHT])
    rotateFaceLeft(cube[LEFT], cubePt[LEFT])

def rotateCubeBack(cube, cubePt):
    rotateCubeFront(cube, cubePt)
    rotateCubeFront(cube, cubePt)
    rotateCubeFront(cube, cubePt)

def setByCubePt(cubeR, cubeC, cube, cubePt, val):
    r, c = cubePt[BOTTOM][cubeR][cubeC]
    cube[BOTTOM][r][c] = val

def getByCubePt(cubeR, cubeC, cube, cubePt):
    r, c = cubePt[BOTTOM][cubeR][cubeC]
    return cube[BOTTOM][r][c]


def dfs(mazeR, mazeC, cubeR, cubeC, cube, cubePt, visited, maze):
    visited[mazeR][mazeC] = True

    setByCubePt(cubeR, cubeC, cube, cubePt, (mazeR, mazeC))
    '''
    for i in range(6):
        print ["BOTTOM", "RIGHT", "TOP", "LEFT", "FRONT", "BACK"][i]
        for r in range(SZ):
            for c in range(SZ):
                rr, cc = cubePt[i][r][c]
                print cube[i][rr][cc],
            print ""
        print ""
    print ""
    
    for i in range(6):
        print ["BOTTOM", "RIGHT", "TOP", "LEFT", "FRONT", "BACK"][i]
        for r in range(SZ):
            for c in range(SZ):
                print cubePt[i][r][c],
            print ""
        print ""
    print " ------ "
    print " ------ "
    print " ------ "
    print ""
    '''
    
    for i in range(4):
        mazeNR = mazeR + dr[i]
        mazeNC = mazeC + dc[i]
        cubeNR = cubeR + dr[i]
        cubeNC = cubeC + dc[i]
        
        if not (0 <= mazeNR < len(maze) and 0 <= mazeNC < len(maze[0])):
            continue

        if maze[mazeNR][mazeNC] == ' ':
            continue
        
        if visited[mazeNR][mazeNC]:
            continue

        if cubeNR == -1:
            rotateCubeBack(cube, cubePt)
            dfs(mazeNR, mazeNC, SZ - 1, cubeNC, cube, cubePt, visited, maze)
            rotateCubeFront(cube, cubePt)
        elif cubeNR == SZ:
            rotateCubeFront(cube, cubePt)
            dfs(mazeNR, mazeNC, 0, cubeNC, cube, cubePt, visited, maze)
            rotateCubeBack(cube, cubePt)
        elif cubeNC == -1:
            rotateCubeLeft(cube, cubePt)
            dfs(mazeNR, mazeNC, cubeNR, SZ - 1, cube, cubePt, visited, maze)
            rotateCubeRight(cube, cubePt)
        elif cubeNC == SZ:
            rotateCubeRight(cube, cubePt)
            dfs(mazeNR, mazeNC, cubeNR, 0, cube, cubePt, visited, maze)
            rotateCubeLeft(cube, cubePt)
        else:
            dfs(mazeNR, mazeNC, cubeNR, cubeNC, cube, cubePt, visited, maze)


def createCube(maze):
    cube = [[[(-1, -1) for k in range(SZ)] for j in range(SZ)] for i in range(6)]
    cubePt = [[[(-1, -1) for k in range(SZ)] for j in range(SZ)] for i in range(6)]
    visited = [[False for c in range(len(maze[0]))] for r in range(len(maze))]


    for i in range(6):
        for j in range(SZ):
            for k in range(SZ):
                cubePt[i][j][k] = (j, k)
    
    initR = 0
    initC = maze[0].index('.')
    
    dfs(initR, initC, 0, 0, cube, cubePt, visited, maze)

    return cube, cubePt


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


def getNextRC(cubeR, cubeC, to, cube, cubePt):
    cubeNR = cubeR + dr[to]
    cubeNC = cubeC + dc[to]
    
    if cubeNR == -1:
        rotateCubeBack(cube, cubePt)
        cubeNR = SZ - 1
    elif cubeNR == SZ:
        rotateCubeFront(cube, cubePt)
        cubeNR = 0
    elif cubeNC == -1:
        rotateCubeLeft(cube, cubePt)
        cubeNC = SZ - 1
    elif cubeNC == SZ:
        rotateCubeRight(cube, cubePt)
        cubeNC = 0

    return cubeNR, cubeNC

    
def work((lines, moveStr)):
    maze = createMaze(lines)
    cube, cubePt = createCube(maze)
    moves = createMove(moveStr)
    row, col = len(maze), len(maze[0])

    '''
    for i in range(6):
        print ["BOTTOM", "RIGHT", "TOP", "LEFT", "FRONT", "BACK"][i]
        for r in range(SZ):
            for c in range(SZ):
                rr, cc = cubePt[i][r][c]
                print cube[i][rr][cc],
            print ""
        print ""
    print ""
    
    for i in range(6):
        print ["BOTTOM", "RIGHT", "TOP", "LEFT", "FRONT", "BACK"][i]
        for r in range(SZ):
            for c in range(SZ):
                print cubePt[i][r][c],
            print ""
        print ""
    print " ------ "
    print " ------ "
    print " ------ "
    print ""
    '''
    
    cubeR = 0
    cubeC = 0
    to = 0

    for move in moves:
        if move == 'R':
            to = (to + 1) % 4
        elif move == 'L':
            to = (to + 3) % 4
        else:
            for _ in range(move):
                backupCube = copy.deepcopy(cube)
                backupCubePt = copy.deepcopy(cubePt)

                cubeNR, cubeNC = getNextRC(cubeR, cubeC, to, cube, cubePt)
                mazeNR, mazeNC = getByCubePt(cubeNR, cubeNC, cube, cubePt)
                if maze[mazeNR][mazeNC] == '#':
                    cube = backupCube
                    cubePt = backupCubePt
                    break
                cubeR, cubeC = cubeNR, cubeNC
    
    if 0 <= cubeR + dr[to] < SZ and 0 <= cubeC + dc[to] < SZ:
        r1, c1 = getByCubePt(cubeR, cubeC, cube, cubePt)
        r2, c2 = getByCubePt(cubeR + dr[to], cubeC + dc[to], cube, cubePt)
        diffR, diffC = r2 - r1, c2 - c1
    else:
        r1, c1 = getByCubePt(cubeR - dr[to], cubeC - dc[to], cube, cubePt)
        r2, c2 = getByCubePt(cubeR, cubeC, cube, cubePt)
        diffR, diffC = r2 - r1, c2 - c1
    drdc2to = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}
    mazeR, mazeC = getByCubePt(cubeR, cubeC, cube, cubePt)
    print (mazeR + 1) * 1000 + (mazeC + 1) * 4 + drdc2to[(diffR, diffC)]
    
    
if __name__ == "__main__":
    work(read())
