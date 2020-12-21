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

    nonAllergenIngredient = []
    for ing in ingredient:
        if ing not in sum([i for i in a2iCandi.values()], []):
            nonAllergenIngredient.append(ing)

    cnt = 0
    for ing in nonAllergenIngredient:
        cnt += sum(ing in ingList for ingList in line2ingredientList)
    print cnt
        

if __name__ == "__main__":
    work(read())
