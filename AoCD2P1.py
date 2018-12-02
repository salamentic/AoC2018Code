def func():
    list = [str(x.strip()) for x in open("input.txt",'r')]
    c2 = 0;c3=0;
    for x in list:
        list1 = [x.count(y) for y in x];
        if 2 in list1:c2+=1
        if 3 in list1:c3+=1
    print(c2*c3)
func()
