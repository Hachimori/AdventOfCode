#!/usr/bin/env python

def read():
    return raw_input()


def work(txt):
    for i in range(len(txt) - 3):
        if len(set(txt[i:i+4])) == 4:
            print i + 4
            break
        
            
if __name__ == "__main__":
    work(read())
