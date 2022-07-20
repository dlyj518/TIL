x = 0
def f1():
    x = 1
    def f2():
        nonlocal x
        x = 2
    print(x)
    f2()
    print(x)
print(x)
f1()
print(x)