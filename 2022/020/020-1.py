#!/usr/bin/env python


def read():
    ret = []
    order = 0
    while 1:
        try:
            ret.append((int(raw_input()), order))
            order += 1
        except EOFError:
            break
    return ret


def work((valOrderList)):
    n = len(valOrderList)
    
    for (val, order) in valOrderList[:]:
        idx = valOrderList.index((val, order))

        if (idx + val) % n == idx:
            continue
        elif val > 0:
            toMove = valOrderList[idx]
            del valOrderList[idx]

            cutIdx = (idx + val) % (n - 1)
            valOrderList = valOrderList[:cutIdx] + [toMove] + valOrderList[cutIdx:]
            
        elif val < 0:
            toMove = valOrderList[idx]
            del valOrderList[idx]

            cutIdx = (idx + val) % (n - 1)

            if cutIdx == 0:
                valOrderList += [toMove]
            else:
                cutIdx = (idx + val) % (n - 1)
                valOrderList = valOrderList[:cutIdx] + [toMove] + valOrderList[cutIdx:]


    zeroIdx = 0
    for (idx, (val, order)) in enumerate(valOrderList):
        if val == 0:
            zeroIdx = idx
            break
    
    a = valOrderList[(zeroIdx + 1000) % n]
    b = valOrderList[(zeroIdx + 2000) % n]
    c = valOrderList[(zeroIdx + 3000) % n]
    
    print a[0] + b[0] + c[0]


if __name__ == "__main__":
    work(read())
