def z(x, y):
    while x>y:
        if x%2==0 and x//2>=y:
            x//=2
            print(':2')
        elif x-1>=y:
            x-=1
            print('-1')
        if x==y:
            break
x1=int(input())
y1=int(input())
z(x1, y1)