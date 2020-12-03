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


# layerIdxDigit2cnt[layerIdx][digit] = cnt
layerIdxDigit2cnt = [[0 for j in range(10)] for i in range(len(layer))]
for layerIdx in range(len(layer)):
    for r in range(ROW):
        for c in range(COL):
            digit = int(layer[layerIdx][r][c])
            layerIdxDigit2cnt[layerIdx][digit] += 1


minZeroLayer = 0
for layerIdx in range(len(layer)):
    if layerIdxDigit2cnt[minZeroLayer][0] > layerIdxDigit2cnt[layerIdx][0]:
        minZeroLayer = layerIdx

print layerIdxDigit2cnt[minZeroLayer][1] * layerIdxDigit2cnt[minZeroLayer][2]
