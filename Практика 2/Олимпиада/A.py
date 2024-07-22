stroka=str(input())
nech=0
ch=0
for i in range(len(stroka)):
    if i%2!=0:
        nech+=int(stroka[i])
    else:
        ch+= int(stroka[i])
ch=3*ch
if (nech+ch)%10==0:
    print('YES')
else:
    print('NO')


