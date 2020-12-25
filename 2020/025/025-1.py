#!/usr/bin/env python

MAX_LOOP = 20201227
MOD = 20201227

def read():
    pub1 = int(raw_input())
    pub2 = int(raw_input())
    return pub1, pub2


def modpow(p, n):
    if n == 0: return 1
    t = modpow(p, n / 2)
    return t * t % MOD if n % 2 == 0 else t * t * p % MOD


def work((pub1, pub2)):
    loopSize1, loopSize2 = 0, 0
    
    for i in range(MAX_LOOP):
        if modpow(7, i) == pub1:
            loopSize1 = i
            break

    # for i in range(MAX_LOOP):
    #     if modpow(7, i) == pub2:
    #         loopSize2 = i
    #         break

    print modpow(pub2, loopSize1) #, modpow(pub1, loopSize2)
        
    
if __name__ == "__main__":
    work(read())
