#!/usr/bin/env python

def read():
    s = [ch if ch in '0123456789-' else ' ' for ch in raw_input()]
    return map(int, ''.join(s).split())


def work((x1, x2, y1, y2)):
    cnt = 0
    
    for initVX in range(0, 200):
        for initVY in range(-200, 200):
            vx = initVX
            vy = initVY
            x, y = 0, 0
            
            while 1:
                if vx == 0 and not (x1 <= x <= x2): break
                if vy < 0 and y < y1: break

                x += vx
                y += vy

                if vx > 0:
                    vx -= 1
                elif vx < 0:
                    vx += 1

                vy -= 1

                if x1 <= x <= x2 and y1 <= y <= y2:
                    cnt += 1
                    break
    
    print cnt


if __name__ == "__main__":
    work(read())
