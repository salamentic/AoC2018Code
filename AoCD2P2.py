import itertools
def func():
    list = [str(x.strip()) for x in open("input.txt",'r')]
    for string,string2 in itertools.product(list,list):
        answer = [x for x,y in zip(string,string2) if x==y]
        if(len(string2) - len(answer) == 1):
            print("".join(answer))
            break
func()
