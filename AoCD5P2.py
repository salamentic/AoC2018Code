import string
from AoCD5P1 import p1

input = ([str(x.strip()) for x in open("input.txt", 'r')])

def p2(arg):
    m = len(arg)
    for x in string.ascii_lowercase:
        temp = ((arg).replace(x,"").replace(x.upper(),"").strip())
        m = min(m,p1(temp))
    print(m)