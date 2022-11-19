class randomclass:
    def foo() :
        morerandomclass.bar()

class morerandomclass:
    def bar() :
        e()

def e():
    i = 0

def d():
    randomclass.foo()

def c():
    d()

def b():
    i = 4
    while (i != 0) :
        i -= 1
        c()

def a():
    if (0) :
        b()
    else :
        b()

a() 