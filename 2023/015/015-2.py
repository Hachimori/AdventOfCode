#!/usr/bin/env python

def read():
    return raw_input().split(',')


def calc(s):
    ret = 0
    for ch in s:
        ret = (ret + ord(ch)) * 17 % 256
    return ret


def add(keyValList, key, val):
    for kv in keyValList:
        if kv[0] == key:
            kv[1] = val
            return
    keyValList.append([key, val])


def remove(keyValList, key):
    for (idx, kv) in enumerate(keyValList):
        if kv[0] == key:
            del keyValList[idx]
            return


def work(sList):
    hash2keyValList = [[] for hash in range(256)]

    for s in sList:
        if s.find('=') >= 0:
            key, val = s.split('=')
            val = int(val)
            add(hash2keyValList[calc(key)], key, val)
        else:
            key = s.split('-')[0]
            remove(hash2keyValList[calc(key)], key)

    ans = 0
    for hash in range(256):
        for (idx, kv) in enumerate(hash2keyValList[hash]):
            ans += (hash + 1) * (idx + 1) * kv[1]
    print ans


if __name__ == "__main__":
    work(read())
