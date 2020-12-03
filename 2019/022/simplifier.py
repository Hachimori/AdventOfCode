#!/usr/bin/env python

def myPow(p, n, mod):
    if n == 0:
        return 1
    t = myPow(p, n / 2, mod)
    if n % 2 == 0:
        return t * t % mod
    else:
        return t * t * p % mod

"""
CARD = 10007
LOOP = 1
POS = 2019
"""

CARD = 119315717514047
LOOP = 101741582076661
POS = 2020


instructionList = []
while True:
    try:
        s = raw_input()
    except:
        break
    instructionList.append(s)


mul = 1
add = 0
for instruction in instructionList[::-1]:
    if instruction[0] == 'c':
        # cut
        n = int(instruction.split()[-1])

        if n < 0:
            n = CARD + n
        add += n

    elif instruction[5] == 'i':
        mul *= -1
        add = - add - 1
    else:
        n = int(instruction.split()[-1])
        mul = mul * myPow(n, CARD - 2, CARD) % CARD
        add = add * myPow(n, CARD - 2, CARD) % CARD


# (1) CARD = 10007
#   -> idx * 6150 + 5038
#
# (2) CARD = 119315717514047
#   -> idx * 3237733208034 + 43667402712944
print "idx * %d + %d" % (mul % CARD, add % CARD)
