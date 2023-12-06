#!/usr/bin/env python

def read():
    timeList = map(int, raw_input().split()[1:])
    distanceList = map(int, raw_input().split()[1:])
    return timeList, distanceList


def calc(time, distance):
    cnt = 0
    for t in range(time):
        cnt += t * (time - t) > distance
    return cnt


def work((timeList, distanceList)):
    ans = 1
    for i in range(len(timeList)):
        ans *= calc(timeList[i], distanceList[i])
    print ans


if __name__ == "__main__":
    work(read())
