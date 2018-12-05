import timeit
import string

input = ([str(x.strip()) for x in open("input.txt", 'r')])

def p1(arg):
    line = list(arg)
    stack = []
    for x in (line):
        if(len(stack) ==0 ):
            stack.append(x)
        else:
            if(stack[-1] == x.swapcase()):
                    stack.pop()
            else:
                stack.append(x)
    return len(stack)

def p2(arg):
    m = len(arg)
    for x in string.ascii_lowercase:
        temp = ((arg).replace(x,"").replace(x.upper(),"").strip())
        m = min(m,p1(temp))
    print(m)

print((p1(input[0])))
p2(input[0])