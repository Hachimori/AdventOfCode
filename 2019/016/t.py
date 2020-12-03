#!/usr/bin/env python

h = raw_input()*10000
i = (h[int(h[0:7]):])
for a in range(100):
    print(a)
    string = '' 
    e = 0
    while e < len(i):
        if e == 0:
            total = 0
            for f in i:
                total += int(f)
        elif e > 0:
            total -= int(i[e-1])
        string += str(total)[-1]
        e+=1
    i = string
print(i[0:8])     
