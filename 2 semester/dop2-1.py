from math import sqrt
A=[12, 13, 423, 5364, 4354, 243, 2435, 435, 2435, 243, 2435, 435, 0, -1, 2, 7, 17]
len=0
for x in A:
    len+=1
A1=[0]*len
A2=[0]*len
A3=[0]*len
a1=0
a2=0
a3=0
for x in A:
    if abs(x)%2==0:
        A1[a1]=x
        a1+=1
    else:
        A2[a2]=x
        a2+=1
    if abs(x)<=3:
        A3[a3]=x
        a3+=1
    else:
        for i in range(2, int(round(sqrt(abs(x))+1))):
            if abs(x)%i==0:
                break
            if i==int(round(sqrt(abs(x)))):
                    A3[a3] = x
                    a3+=1
A1=A1[:(a1)]
A2=A2[:(a2)]
A3=A3[:(a3)]
min1=A1[0]
min2=A2[0]
min3=A3[0]
print(A1, A2, A3)
for i in range(1, a1):
    if min1>A1[i]:
        min1=A1[i]
for i in range(1, a2):
    if min2>A2[i]:
        min2=A2[i]
for i in range(1, a3):
    if min3>A3[i]:
        min3=A3[i]
E=[0]*3
E[0]=min1
E[1]=min2
E[2]=min3
print(E)