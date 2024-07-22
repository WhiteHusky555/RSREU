x, y = str(input()).split(' ')
x=int(x)
y=int(y)
maxim=x*y
len_maxim=len(str(maxim))
list_f=[[0]*y for i in range(x)]
minin=1
for i in range(x):
    for j in range(y):
        list_f[i][j]=minin
        minin+=1
    if i%2==1:
        list_f[i].reverse()

for i in list_f:
    s=''
    for y in i:
        if y==i[0]:
            s=s+(len_maxim-len(str(y)))*' '+f'{y}'
        else:
            s=s+(4-len(str(y)))*' '+f'{y}'
    print(s)