#!/usr/bin/env python3

"""
Environment:
  MacBook Pro
  Apple M3 Max
  64 GB RAM

$ time ./009-2.py < input.txt
6448168620520
./009-2.py < input.txt  5.50s user 0.02s system 99% cpu 5.536 total
"""

def read():
    return list(map(int, input()))


def work(vList):
    nId = 0
    buf = [] # (length, id)

    for (idx, v) in enumerate(vList):
        if idx % 2 == 0:
            buf.append((v, nId))
            nId += 1
        else:
            buf.append((v, -1))

    rIdx = len(buf) - 1
    while rIdx >= 0:
        while rIdx >= 0 and (buf[rIdx][0] == 0 or buf[rIdx][1] == -1):
            rIdx -= 1

        for i in range(rIdx):
            if buf[i][1] != -1:
                continue

            if buf[i][0] >= buf[rIdx][0]:
                (leng, id) = buf[rIdx]
                buf[rIdx] = (leng, -1)
                buf = buf[:i] + [(leng, id)] + [(buf[i][0] - leng, -1)] + buf[i+1:]
                rIdx += 1
                break
        rIdx -= 1

    vList = []
    for (leng, id) in buf:
        vList += leng * [id]

    ans = 0
    for (idx, v) in enumerate(vList):
        if v >= 0:
            ans += idx * v
    print(ans)


if __name__ == "__main__":
    work(read())
