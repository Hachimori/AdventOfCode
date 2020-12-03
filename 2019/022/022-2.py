#!/usr/bin/env python

"""
CARD = 10007
LOOP = 1
POS = 2019
"""

CARD = 119315717514047
LOOP = 101741582076661
POS = 2020

def matMul(a, b):
    ret = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] = (ret[i][j] + a[i][k] * b[k][j]) % CARD
    return ret


def matPow(p, n):
    if n == 0:
        return [[1, 0], [0, 1]]

    t = matPow(p, n / 2)
    
    if n % 2 == 0:
        return matMul(t, t)
    else:
        return matMul(matMul(t, t), p)
    

"""
mat = [[6150, 5038],
       [   0,    1]]
"""

mat = [[ 3237733208034, 43667402712944],
       [             0,              1]]

    
ret = matPow(mat, LOOP)

print (ret[0][0] * POS + ret[0][1]) % CARD
