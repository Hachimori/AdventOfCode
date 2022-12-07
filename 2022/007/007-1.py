#!/usr/bin/env python

import sys


class Directory:
    def __init__(self):
        self.files = []
        self.directories = []
    

def read():
    return sys.stdin.readlines()


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
    

def rec(current, dirTree):
    directory = dirTree[tuple(current)]
    sumFile = sum(directory.files)
    ans = 0

    for dirName in directory.directories:
        subSumFile, subAns = rec(current + [dirName], dirTree)
        sumFile += subSumFile
        ans += subAns

    if sumFile <= 100000:
        ans += sumFile

    return sumFile, ans
    
    
def work(lines):
    dirTree = getDirTree(lines)
    _, ans = rec([], dirTree)
    print ans


if __name__ == "__main__":
    work(read())
