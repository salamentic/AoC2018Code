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