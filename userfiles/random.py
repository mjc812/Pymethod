def c():
    i = 3

def b():
    i = 3
    while (i != 0) :
        i -= 1
        c()

def a():
    if (0) :
        b()
    else :
        b()

a()