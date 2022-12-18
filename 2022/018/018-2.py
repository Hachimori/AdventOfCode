#!/usr/bin/env python

def read():
    ret = set([])
    while 1:
        try:
            line = raw_input()
            ret.add(tuple(map(int, line.split(','))))
        except EOFError:
            break
    return ret


def work(xyzSet):
    minX, minY, minZ = 10**10, 10**10, 10**10
    maxX, maxY, maxZ = -10**10, -10**10, -10**10
    for (x, y, z) in xyzSet:
        minX = min(minX, x)
        minY = min(minY, y)
        minZ = min(minZ, z)
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        maxZ = max(maxZ, z)

    minX -= 1
    minY -= 1
    minZ -= 1
    maxX += 1
    maxY += 1
    maxZ += 1
    
    cnt = 0
    Q = [(minX, minY, minZ)]
    visited = set([])
    
    while Q:
        x, y, z = Q[0]
        del Q[0]

        dx = [0, 1, 0, -1, 0, 0]
        dy = [-1, 0, 1, 0, 0, 0]
        dz = [0, 0, 0, 0, -1, 1]
        
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if not (minX <= nx <= maxX and minY <= ny <= maxY and minZ <= nz <= maxZ):
                continue
            elif (nx, ny, nz) in visited:
                continue
            elif (nx, ny, nz) in xyzSet:
                cnt += 1
            else:
                visited.add((nx, ny, nz))
                Q.append((nx, ny, nz))
                
    print cnt


if __name__ == "__main__":
    work(read())
