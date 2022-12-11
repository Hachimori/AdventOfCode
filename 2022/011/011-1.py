#!/usr/bin/env python

class Monkey:
    def __init__(self):
        self.items = []
        self.ope = ""
        self.testDivisibility = -1
        self.testResultTarget = [0, 0]

    def inspect(self):
        ret = [] # [(target, newItem)]
        
        for item in self.items:
            old = item
            newItem = eval(self.ope)
            newItem /= 3
            
            divisibility = newItem % self.testDivisibility == 0
            ret.append((self.testResultTarget[divisibility], newItem))

        self.items = []
        return ret

    
def read():
    ret = []
    while True:
        try:
            raw_input() # Monkey x:
            monkey = Monkey()
            
            line = raw_input() # Starting items: x, x, x, ...
            monkey.items = map(int, line.split(':')[1].split(','))

            line = raw_input() # Operation: new = old ...
            monkey.ope = line.split('=')[1]

            line = raw_input() # Test: divisible by x
            monkey.testDivisibility = int(line.split()[-1])

            line = raw_input() # If true: throw to monkey x
            monkey.testResultTarget[1] = int(line.split()[-1])
            
            line = raw_input() # If false: throw to monkey x
            monkey.testResultTarget[0] = int(line.split()[-1])

            ret.append(monkey)

            raw_input() # blank line or EOF
        except EOFError:
            break
        
    return ret


def show(monkeys):
    for monkey in monkeys:
        print monkey.items
        print monkey.ope
        print monkey.testDivisibility
        print monkey.testResultTarget
        print ""
    print "---"


def work(monkeys):
    cntInspection = [0 for _ in range(len(monkeys))]
    
    for _ in range(20):
        for i in range(len(monkeys)):
            cntInspection[i] += len(monkeys[i].items)
            targetNewItemList = monkeys[i].inspect()

            for (target, newItem) in targetNewItemList:
                monkeys[target].items.append(newItem)
                
        # show(monkeys)

    a, b = sorted(cntInspection)[-2:]
    print a * b
    
        
if __name__ == "__main__":
    work(read())
