import itertools
def func():
    list = [str(x.strip()) for x in open("input.txt",'r')]
    sums = {0}
    sum = 0
    for x in itertools.cycle(list):
        sum += x
        if sum in sums:
            print(sum); break
        sums.add(sum)
func()
