#!/usr/bin/env python

CARD = 10007


instructionList = []
while True:
    try:
        s = raw_input()
    except:
        break
    instructionList.append(s)


deck = range(CARD)
for instruction in instructionList:
    if instruction[0] == 'c':
        # cut
        n = int(instruction.split()[-1])
        deck = deck[n:] + deck[:n]
    elif instruction[5] == 'i':
        # deal into new stack
        deck = deck[::-1]
    else:
        # deal with increment
        n = int(instruction.split()[-1])
        
        newDeck = [0 for i in range(CARD)]
        for i in range(CARD):
            newDeck[(i * n) % CARD] = deck[i]
        deck = newDeck


print deck.index(2019)
