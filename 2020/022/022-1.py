#!/usr/bin/env python


def read():
    cards1 = []
    cards2 = []

    for i in range(2):
        raw_input()
        while 1:
            s = raw_input()
            if len(s) == 0:
                break
            (cards1 if i == 0 else cards2).append(int(s))
    
    return cards1, cards2


def work((cards1, cards2)):

    while cards1 and cards2:
        if cards1[0] > cards2[0]:
            cards1.append(cards1[0])
            cards1.append(cards2[0])
        else:
            cards2.append(cards2[0])
            cards2.append(cards1[0])
        del cards1[0]
        del cards2[0]

    score = 0
    if not cards1:
        cards1 = cards2
    for (idx, val) in enumerate(cards1):
        score += val * (len(cards1) - idx)
    print score
    
        
if __name__ == "__main__":
    work(read())
