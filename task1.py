n=int(input('Введи число n: '))
m=int(input('Введи число m: '))

a=[]
b=[]

for i in range(1,m+1):
    a.append(i)
while a[0]!=a[-1]:
    for i in range(a[-1], n+1):
        b.append(i)
    if len(b)>m:
        b=b[:m+1]
    elif len(b)<m:
        for i in range(1,m-len(b)+1):
            b.append(i)
        for arr in b:
            a.append(arr)
        b.clear()
    elif len(b)==m:
        for arr in b:
            a.append(arr)
        b.clear()
a=a[::m]
print("".join(map(str, a)))





