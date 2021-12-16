#!/usr/bin/env python

class Packet:

    def __init__(self, version, typeID, literal, subPacketList):
        self.version = version
        self.typeID = typeID
        
        # If typeID is 4, then, literal >= 0
        # Otherwise, literal == -1
        self.literal = literal

        # If typeID is 4, then, subPacketList is empty
        self.subPacketList = subPacketList

    
    def output(self, depth):
        print "%s (version: %d, typeID: %d, literal: %d)" % \
          ("  " * depth, self.version, self.typeID, self.literal)

        for subPacket in self.subPacketList:
            subPacket.output(depth + 1)

    
    def calc(self):
        ret = -1

        vList = [subpacket.calc() for subpacket in self.subPacketList]
        
        if self.typeID == 0: # sum
            ret = reduce(lambda x, y: x + y, vList)
        elif self.typeID == 1: # product
            ret = reduce(lambda x, y: x * y, vList)
        elif self.typeID == 2: # min
            ret = reduce(lambda x, y: min(x, y), vList)
        elif self.typeID == 3: # max
            ret = reduce(lambda x, y: max(x, y), vList)
        elif self.typeID == 4: # literal
            ret = self.literal
        elif self.typeID == 5: # greater than
            ret = vList[0] > vList[1]
        elif self.typeID == 6: # less than
            ret = vList[0] < vList[1]
        elif self.typeID == 7: # equals
            ret = vList[0] == vList[1]
        else:
            print "typeID: %d, ???" % self.typeID

        return ret
        

def read():
    return raw_input()


def binary2int(binary):
    return int("".join(map(str, binary)), 2)


idx = 0
def rec(binary):
    global idx
    
    version = binary2int(binary[idx:idx+3])
    typeID = binary2int(binary[idx+3:idx+6])
    
    idx += 6
    
    if typeID == 4:
        literal = 0
        while 1:
            toContinue = binary[idx]
            idx += 1
            literal = (literal << 4) + binary2int(binary[idx:idx+4])
            idx += 4
            if not toContinue:
                break
        return Packet(version, typeID, literal, [])
    else:
        lengthTypeID = binary[idx]
        idx += 1

        subPacketList = []
        if lengthTypeID == 0:
            bitLength = binary2int(binary[idx:idx+15])
            idx += 15
            baseIdx = idx
            while idx - baseIdx < bitLength:
                subPacketList.append(rec(binary))
        else:
            subpacketLength = binary2int(binary[idx:idx+11])
            idx += 11
            for i in range(subpacketLength):
                subPacketList.append(rec(binary))

        return Packet(version, typeID, -1, subPacketList)
        
    

def work(s):
    integer = int(s, 16)
    binaryStr = bin(integer)
    binaryStr = binaryStr[2:] # trim "0b"
    
    while len(binaryStr) < len(s) * 4:
        binaryStr = '0' + binaryStr
    
    binary = map(int, binaryStr)
    
    packet = rec(binary)
    
    # packet.output(0)

    print packet.calc()


if __name__ == "__main__":
    work(read())
