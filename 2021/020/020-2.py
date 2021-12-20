#!/usr/bin/env python

def read():
    int2ch = raw_input()
    
    raw_input()

    img = []
    
    try:
        while 1:
            img.append(list(raw_input()))
    except EOFError:
        pass

    return int2ch, img


def work((int2ch, img)):
    LOOP = 50

    for _ in range(LOOP):
        row, col = len(img), len(img[0])
        for r in range(row):
            img[r] = ['.'] + ['.'] + img[r] + ['.'] + ['.']
        img.insert(0, ['.'] * (col + 4))
        img.insert(0, ['.'] * (col + 4))
        img.append(['.'] * (col + 4))
        img.append(['.'] * (col + 4))
        
    
    for _ in range(LOOP):
        nexImg = [['.' for c in range(len(img[0]))] for r in range(len(img))]
        
        for r in range(len(img) - 2):
            for c in range(len(img[0]) - 2):
                total = 0
                for i in range(3):
                    for j in range(3):
                        total <<= 1
                        if img[r + i][c + j] == '#':
                            total += 1
                nexImg[r][c] = int2ch[total]

        img = nexImg

    cnt = 0
    for r in range(len(img) - LOOP * 2):
        for c in range(len(img[0]) - LOOP * 2):
            if img[r][c] == '#':
                cnt += 1
    print cnt
    

if __name__ == "__main__":
    work(read())
