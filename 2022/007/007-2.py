#!/usr/bin/env python

import sys


class Directory:
    def __init__(self):
        self.files = []
        self.directories = []
    

def read():
    return sys.stdin.readlines()


def getSpace(lines):
    space = 70000000
    for line in lines:
        if not line.startswith('$') and not line.startswith('dir'):
            space -= int(line.split()[0])
    return space
            

def getDirTree(lines):
    dirTree = {}
    current = []
    
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if line.startswith('$ cd'):
            dirName = line.split()[-1]
            if dirName == '..':
                del current[-1]
            elif dirName == '/':
                current = []
            else:
                current.append(dirName)
            idx += 1
                
        elif line.startswith('$ ls'):
            toPush = Directory()
            idx += 1
            while idx < len(lines) and not lines[idx].startswith('$'):
                elements = lines[idx].split()
                if elements[0] == 'dir':
                    toPush.directories.append(elements[1])
                else:
                    toPush.files.append(int(elements[0]))
                idx += 1
            dirTree[tuple(current)] = toPush
                
    return dirTree
    

def rec(current, dirTree, space):
    directory = dirTree[tuple(current)]
    sumFile = sum(directory.files)
    ans = 10 ** 10

    for dirName in directory.directories:
        subSumFile, subAns = rec(current + [dirName], dirTree, space)
        sumFile += subSumFile
        ans = min(ans, subAns)

    if space + sumFile >= 30000000:
        ans = min(ans, sumFile)

    return sumFile, ans
    
    
def work(lines):
    space = getSpace(lines)
    dirTree = getDirTree(lines)
    _, ans = rec([], dirTree, space)
    print ans


if __name__ == "__main__":
    work(read())
