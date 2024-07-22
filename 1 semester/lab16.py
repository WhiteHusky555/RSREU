from math import log
def f(x):
    return (x*x*x)/2-log(abs(x))-1

x0=float(input('x0: '))
xn=float(input('xn: '))
hx=float(input('hx: '))
a=x0
b=x0+hx
ya=f(a)
yb=f(b)
while (((ya*yb)>0) and (b<xn+hx/2)):
    a=a+hx
    b=b+hx
    ya=f(a)
    yb=f(b)
if b<(xn+hx/2):
    print(a, b)
else:
    print('нет')
#print(f(-0.4), f(-0.3), f(-0.4)*f(-0.3))+