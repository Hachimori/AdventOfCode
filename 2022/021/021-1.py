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
    if len(expr) == 1:
        return int(expr[0])
    else:
        var1, op, var2 = expr
        val1, val2 = calc(var1, var2expr), calc(var2, var2expr)
        return eval(str(val1) + op + str(val2))
        

def work(var2expr):
    print calc('root', var2expr)


if __name__ == "__main__":
    work(read())
