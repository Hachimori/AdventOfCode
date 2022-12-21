#!/usr/bin/env python

def read():
    ret = {}
    while 1:
        try:
            var, expr = raw_input().split(':')
            ret[var] = expr.split()
        except EOFError:
            break
    return ret
        

def calc(var, var2expr):
    expr = var2expr[var]
    
    if var == 'humn':
        return (1.0, 0.0)
    elif len(expr) == 1:
        return (0.0, float(expr[0]))
    else:
        var1, op, var2 = expr

        # a[0] * humn + a[1]
        a = calc(var1, var2expr)

        # b[0] * humn + b[1]
        b = calc(var2, var2expr)

        if op == '+':
            return (a[0] + b[0], a[1] + b[1])
        elif op == '-':
            return (a[0] - b[0], a[1] - b[1])
        elif op == '*':
            if a[0] != 0 and b[0] != 0:
                print "???"
            elif a[0] != 0:
                return (a[0] * b[1], a[1] * b[1])
            else:
                return (b[0] * a[1], b[1] * a[1])
        else:
            if b[0] != 0 or b[1] == 0:
                print "???"
            return (a[0] / b[1], a[1] / b[1])
        

def work(var2expr):
    var1, var2 = var2expr['root'][0], var2expr['root'][2]

    # a[0] * humn + a[1]
    a = calc(var1, var2expr)

    # b[0] * humn + b[1]
    b = calc(var2, var2expr)

    # a[0] * humn + a[1] = b[0] * humn + b[1]
    # humn = (b[1] - a[1]) / (a[0] - b[0])
    print "%20f" % ((b[1] - a[1]) / (a[0] - b[0]))


if __name__ == "__main__":
    work(read())
