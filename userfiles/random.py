def a():
    b()

class A:
    def foo():
        x = 1
    def bar():
        y = 2

def b():
    z = 1

class B:
    def baz():
        x = 1
    def qux():
        y = 2

a()

def c():
    z = 1
