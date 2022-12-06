#!/usr/bin/env python

def read():
    return raw_input()


def work(txt):
    for i in range(len(txt) - 13):
        if len(set(txt[i:i+14])) == 14:
            print i + 14
            break
        
            
if __name__ == "__main__":
    work(read())
