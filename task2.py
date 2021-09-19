import math

file=input('Введите название файла, связанного с окружностью: ')
findings = open(file).read().splitlines()
coordinates=findings[0].split(' ')

file2=input('Введите название файла, связанного с точками: ')
points = open(file2).read().splitlines()

r = int(findings[1])               #радиус
a = int(coordinates[0])   #координаты центра окружности
b = int(coordinates[1])

for i in points:
    coordin_points = i.split(' ')
    coordin_points = [int(item) for item in coordin_points]
    x = int(coordin_points[0])
    y = int(coordin_points[1])
    if math.sqrt(x - a) + math.sqrt(y - b) < math.sqrt(r):
        print('1') #Эта точка внутри окружности
    elif math.sqrt(x - a) + math.sqrt(y - b) == math.sqrt(r):
        print('0') #Эта точка лежит на окружности
    else:
        print('2') #Эта точка снаружи окружности


