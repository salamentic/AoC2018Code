import itertools as it
import re
import numpy as np

list1 = [[0 for x in range(1000)] for y in range(1000)]
input = [str(x.strip()) for x in open("input.txt", 'r')]
global xcount
xcount = 0

def findSize(x):
    re1='.*?'	# Non-greedy match on filler
    re2='\\d+'	# Uninteresting: int
    re3='.*?'	# Non-greedy match on filler
    re4='\\d+'	# Uninteresting: int
    re5='.*?'	# Non-greedy match on filler
    re6='\\d+'	# Uninteresting: int
    re7='.*?'	# Non-greedy match on filler
    re8='(\\d+)'	# Integer Number 1
    re9='.*?'	# Non-greedy match on filler
    re10='(\\d+)'	# Integer Number 2

    rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10,re.IGNORECASE|re.DOTALL)
    m = rg.search(x)
    if m:
        int1=m.group(1)
        int2=m.group(2)
        return [int(int1),int(int2)]

def findCoords(x):
    re1 = '.*?'  # Non-greedy match on filler
    re2 = '(\\d+)'  # Integer Number 1
    re3 = '.*?'  # Non-greedy match on filler
    re4 = '\\d+'  # Uninteresting: int
    re5 = '.*?'  # Non-greedy match on filler
    re6 = '(\\d+)'  # Integer Number 1
    re7 = '.*?'  # Non-greedy match on filler
    re8 = '(\\d+)'  # Integer Number 2
    re9 = '.*?'  # Non-greedy match on filler
    re10 = '(\\d+)'  # Integer Number 2

    size = findSize(x)
    rg = re.compile(re1 + re2 + re3 + re4 + re5 + re6 + re7 + re8 + re9 + re10, re.IGNORECASE | re.DOTALL)
    m = rg.search(x)
    rg = re.compile(re3 + re4 + re5 + re6 + re7 + re8, re.IGNORECASE | re.DOTALL)
    m = rg.search(x)
    if m:
        int1 = m.group(1)
        int2 = m.group(2)
        return [int(int1),int(int2)]


def func():
    list3 =[]
    input = [str(x.strip()) for x in open("input.txt",'r')]
    xcounts = 0
    for x in input:
        overlaps = 0
        number = 0
        re1 = '.*?'  # Non-greedy match on filler
        re2 = '(\\d+)'  # Integer Number 1

        size = findSize(x)
        coords = findCoords(x)
        rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)
        m = rg.search(x)
        if m:
            number = m.group(1)
        for y in range(0,size[0]):
            for z in range(0, size[1]):
                if list1[coords[0]+y][coords[1] + z] != 0:
                    if list1[coords[0]+y][coords[1] + z]!='X':
                        xcounts += 1
                        zz =  list1[coords[0]+y][coords[1] + z] in list3
                        if int(list1[coords[0]+y][coords[1] + z]) in list3:
                            list3.remove(list1[coords[0]+y][coords[1] + z])
                    list1[coords[0]+y][coords[1] + z] = 'X'
                    overlaps+=1

                else:
                    list1[coords[0]+y][coords[1] + z] = int(number)
        if(overlaps == 0):
            list3.append(int(number))
    print(list3)



func()