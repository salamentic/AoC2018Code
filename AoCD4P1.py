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