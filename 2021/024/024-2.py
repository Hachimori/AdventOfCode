#!/usr/bin/env python

import random
import copy

debug = 0


def read():
    opList = []

    try:
        while 1:
            opList.append(raw_input().split())
    except EOFError:
        pass
    
    return opList


def work(opList, inpList):
    var2val = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    
    for op in opList:
        if op[0] == "inp":
            if debug: print "Set %d to %s" % (inpList[0], op[1])
            var2val[op[1]] = inpList[0]
            del inpList[0]
        elif op[0] == "add":
            if debug: print "Add %s to %s" % (op[2], op[1])
            if op[2].isdigit() or op[2].startswith('-'):
                var2val[op[1]] += int(op[2])
            else:
                var2val[op[1]] += var2val[op[2]]
        elif op[0] == "mul":
            if debug: print "Multiply %s with %s" % (op[1], op[2])
            if op[2].isdigit() or op[2].startswith('-'):
                var2val[op[1]] *= int(op[2])
            else:
                var2val[op[1]] *= var2val[op[2]]
        elif op[0] == "div":
            if debug: print "Divide %s by %s" % (op[1], op[2])
            if op[2].isdigit() or op[2].startswith('-'):
                var2val[op[1]] /= int(op[2])
            else:
                var2val[op[1]] /= var2val[op[2]]
        elif op[0] == "mod":
            if debug: print "%s %%= %s" % (op[1], op[2])
            if op[2].isdigit() or op[2].startswith('-'):
                var2val[op[1]] %= int(op[2])
            else:
                var2val[op[1]] %= var2val[op[2]]
        elif op[0] == "eql":
            if debug: print "%s = (%s == %s)" % (op[1], op[1], op[2])
            if op[2].isdigit() or op[2].startswith('-'):
                var2val[op[1]] = var2val[op[1]] == int(op[2])
            else:
                var2val[op[1]] = var2val[op[1]] == var2val[op[2]]

        if debug:
            print "Result:"
            print "  w = %d, x = %d, y = %d, z = %d" % \
              (var2val['w'], var2val['x'], var2val['y'], var2val['z'])
            print ""

    return True if var2val['z'] == 0 else False


if __name__ == "__main__":
    opList = read()

    """
    random.seed(0)
    
    for i in range(100000):
        work(opList, [random.randrange(1, 10) for _ in range(14)])
    """

    inp = [-1 for _ in range(14)]
    inp[0] = 1
    inp[1] = 1
    inp[2] = 8
    inp[3] = 1
    inp[4] = 5
    inp[5] = 6
    inp[6] = 7
    inp[7] = -1
    inp[8] = -1
    inp[9] = -1
    inp[10] = -1
    inp[11] = 1
    inp[12] = -1
    inp[13] = -1
    
    for v7 in range(1, 10):
        for v8 in range(1, 10):
            for v9 in range(1, 10):
                for v10 in range(1, 10):
                    for v12 in range(1, 10):
                        for v13 in range(1, 10):
                            inp[7] = v7
                            inp[8] = v8
                            inp[9] = v9
                            inp[10] = v10
                            inp[12] = v12
                            inp[13] = v13
                            if work(opList, copy.deepcopy(inp)):
                                print "".join(map(str, inp))
                                exit(0)

