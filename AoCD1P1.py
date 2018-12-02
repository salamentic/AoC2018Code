def func():
    list = [int(x.strip()) for x in open("input.txt",'r')]
    print(sum(list))

func()
