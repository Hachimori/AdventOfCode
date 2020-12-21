#!/usr/bin/env python

import re


def read():
    line2ingredientList = []
    line2allergenList = []
    
    try:
        while 1:
            line = raw_input()
            m = re.search(r"(.*)\((.*)\)", line)
            line2ingredientList.append(m.group(1).split())
            line2allergenList.append(m.group(2)[9:].split(', '))
    except EOFError:
        pass

    return line2ingredientList, line2allergenList


def work((line2ingredientList, line2allergenList)):
    allergen = set(sum([allergenList for allergenList in line2allergenList], []))
    ingredient = set(sum([ingredientList for ingredientList in line2ingredientList], []))

    a2iCandi = {}
    for a in allergen:
        a2iCandi[a] = ingredient

    for i in range(len(line2ingredientList)):
        ingredientList = line2ingredientList[i]
        allergenList = line2allergenList[i]
        
        for aller in allergenList:
            a2iCandi[aller] = [ing  for ing in a2iCandi[aller] if ing in ingredientList]


    a2i = []
    for i in range(len(a2iCandi)):
        for (aller, ingList) in a2iCandi.items():
            if len(ingList) == 1:
                matchedIng = ingList[0]
                a2i.append((aller, matchedIng))

                for ingList2 in a2iCandi.values():
                    if matchedIng in ingList2:
                        ingList2.remove(matchedIng)
                a2iCandi.pop(aller)
                
                break
            
    a2i.sort()
    print ",".join([ing for (aller, ing) in a2i])
        

if __name__ == "__main__":
    work(read())
