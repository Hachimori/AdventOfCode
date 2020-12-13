#!/usr/bin/env python

def read():
    departAt = int(raw_input())
    busList = [int(s) for s in raw_input().split(',') if s != 'x']
    return departAt, busList


def work((departAt, busList)):
    minV = 1 << 30
    busId = -1
    
    for bus in busList:
        waitUntil = departAt + (bus - departAt % bus) % bus
        if minV > waitUntil:
            minV = waitUntil
            busId = bus

    print busId * (minV - departAt)


if __name__ == "__main__":
    work(read())
