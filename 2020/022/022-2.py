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


def play(cards1, cards2):
    visited = set([])
    
    while cards1 and cards2:
        if (tuple(cards1), tuple(cards2)) in visited:
            return [-1], []
        visited.add((tuple(cards1), tuple(cards2)))
    
        if cards1[0] <= len(cards1) - 1 and cards2[0] <= len(cards2) - 1:
            ret1, ret2 = play(cards1[1:cards1[0]+1], cards2[1:cards2[0]+1])
            isFstWin = len(ret1) > 0
        else:
            isFstWin = cards1[0] > cards2[0]

        if isFstWin:
            cards1.append(cards1[0])
            cards1.append(cards2[0])
        else:
            cards2.append(cards2[0])
            cards2.append(cards1[0])
        del cards1[0]
        del cards2[0]

    return cards1, cards2
        

def work((cards1, cards2)):
    ret1, ret2 = play(cards1, cards2)
    
    score = 0
    if not ret1:
        ret1 = ret2
    for (idx, val) in enumerate(ret1):
        score += val * (len(ret1) - idx)
    print score
    
        
if __name__ == "__main__":
    work(read())
