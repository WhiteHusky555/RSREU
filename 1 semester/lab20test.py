from math import erfc, exp, pi, sqrt, pow
from time import perf_counter_ns

def fuct(x):
    c=1
    if x>1:
        while x>1:
            c*=x
            x-=1
        return c
    if x==1 or x==0:
        return 1

def CUSTOMerfc(x):
    a=1#*exp(-x*x)/(x*sqrt(pi))
    s=1
    n=1
    while True:
        a1=a
        a*=(-1)*(2*n+1)*(2*n+2)/((n+1)*(4*x*x))
        s+=a
        n+=1
        if abs(a-a1)<eps:
            break
        s*=exp(-x*x)/(x*sqrt(pi))
        return s

def CUSTOMerfc2(x):
    a=1
    s=1
    n=1
    while True:
        a1=a
        a=(pow(-1, n)*fuct(2*n)/(fuct(n)*pow(2*x, 2*n)))
        s+=a
        n+=1
        if abs(a-a1)<eps:
            break
        return s*exp(-x*x)/(x*sqrt(pi))

def customerf(x):
    return (2/(sqrt(pi)))*(x-x*x*x/3+pow(x, 5)/10 - pow(x, 7)/42 + pow(x, 9)/216)

def CUSTOMerfc3(x):
    a=(-1)/(2*x*x)
    s=a
    n=2
    if x<0:
        a*=-1
    while True:
        a1=a
        a*=-(2*n-1)/(2*x*x)
        n+=1
        s+=a
        if abs(a) < eps:
            break
        return (s+1)*exp(-x*x)/(x*sqrt(pi))


x=float(input('Введите х: '))
start_time = perf_counter_ns()
a1=erfc(x)
print(f'a1: {a1}')
current_time = perf_counter_ns()
print(current_time-start_time)
start_time = perf_counter_ns()
eps=0.0001
a2=CUSTOMerfc(x)
print(f'a2: {a2}')
current_time = perf_counter_ns()
print(current_time-start_time)
start_time = perf_counter_ns()
a3=1-customerf(x)
print(F'a3: {a3}')
current_time = perf_counter_ns()
print(current_time-start_time)
start_time = perf_counter_ns()
a4=CUSTOMerfc2(x)
print(f'a4: {a4}')
current_time = perf_counter_ns()
print(current_time-start_time)
start_time = perf_counter_ns()
a5=CUSTOMerfc3(x)
print(f'a5: {a5}')
current_time = perf_counter_ns()
print(current_time-start_time)