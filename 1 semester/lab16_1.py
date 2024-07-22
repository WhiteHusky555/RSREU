from math import log
def f(x):
    return (x*x*x)/2-log(abs(x))-1

def hord(a, b):
    ya = f(a)
    yb = f(b)
    eps = 1e-3
    s=0
    x = a
    while True:
        print(x, f(x))
        s += 1
        x = a - ((b - a) / (yb - ya)) * ya
        y = f(x)
        if y * ya < 0:
            b = x
            yb = y
        else:
            a = x
            ya = y
        if abs(f(x)) < eps:
            break
    return x,s

a=float(input('a: '))
b=float(input('b: '))
x,s = hord(a,b)
print(x)
print(s)