def z(x):
    max_d=int(x**(1/2))+1
    list_d=[]
    q=2
    while q<=max_d:
        if x%q==0:
            list_d+=[q]
            x//=q
        else:
            q+=1
        if q==max_d:
            break
    return sorted(list_d)

x=int(input())
l_d=z(x)
if l_d==[]:
    print(f'{x} = {x}')
else:
    s=f'{x} ='
    for i in range(len((l_d))):
        s=s+f' {l_d[i]} *'
    print(s[:-2])
