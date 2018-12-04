
def func():
    input = sorted([str(x.strip()) for x in open("input.txt",'r')])
    guards = {}
    sleeping = 0
    for x in input:
        if "begins" in x:
          current_guard = x.split(" ")[3]
          if current_guard not in guards.keys():
            guards[x.split(" ")[3]] = [0 for x in range(00,60)]
        if "asleep" in x:
            sleeping = int(x[15:17])
        if "wakes" in x:
            for y in range(sleeping,int(x.split(" ")[1][3:5])):
                guards[current_guard][y] += 1
    g = (sorted(guards.keys(), key = lambda g : -sum(guards[g]))[0])
    guard_array = guards[g]
    minute = guard_array.index(max(guard_array))
    print(int(g[1:])*minute)


func()
