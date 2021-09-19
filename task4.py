file=input('Введите название файла: ')
x = open(file).read().splitlines()
x = [int(item) for item in x]
total=sum(x)
quantity=len(x)
avg=round(total/quantity)
y=[]
for i in x:
    y.append(i-avg)
print(sum(i if i>=0 else -i for i in y))
