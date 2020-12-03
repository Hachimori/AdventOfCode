#!/usr/bin/env python

ROW = 6
COL = 25

s = raw_input()
layer = []

for (idx, ch) in enumerate(s):
    layerIdx = idx / (ROW * COL)
    layerRow = idx % (ROW * COL) / COL
    layerCol = idx % (ROW * COL) % COL
    
    if layerIdx >= len(layer):
        layer.append([[' ' for c in range(COL)] for r in range(ROW)])

    layer[layerIdx][layerRow][layerCol] = ch


    
ans = ''
for r in range(ROW):
    for c in range(COL):
        added = False
        for layerIdx in range(len(layer)):
            if layer[layerIdx][r][c] != '2':
                ans += ' ' if layer[layerIdx][r][c] == '0' else '#'
                added = True
                break
        if not added:
            ans += ' '
    ans += '\n'

print ans

