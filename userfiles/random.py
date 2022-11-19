def a():
    b()

def b():
    print('in b()')

class A:
    def something():
        print("something")

a()