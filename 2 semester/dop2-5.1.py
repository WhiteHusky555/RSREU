def okr(x, y, r):
    k = False
    if x * x + y * y - r * r <= 0:
        k = True
    return k


def obl1(x, y):
    k = False
    if (y >= 0 and x >= 0) and (y <= x) and (y >= x * x):
        k = True
    return k


def obl2(x, y):
    k = False
    if (y <= 0 and x <= 0) and (y <= x):
        k = True
    return k

def f1(coords):
    k=len(coords)
    extra = [0] * k
    extra1 = 0
    for i in range(k):
        if okr(coords[i][0], coords[i][1], r) == True:
            if obl1(coords[i][0], coords[i][1]) == True:
                extra[i] = 1
                extra1+=1
    coords_f1 = [[0] * 2 for i in range(extra1)]
    f1 = 0
    for i in range(k):
        if extra[i] == 1:
            coords_f1[f1][0], coords_f1[f1][1] = coords[i][0], coords[i][1]
            f1 += 1
    return coords_f1

def f2(coords):
    k = len(coords)
    extra = [0] * k
    extra2 = 0
    for i in range(k):
        if okr(coords[i][0], coords[i][1], r) == True:
            if obl2(coords[i][0], coords[i][1]) == True:
                extra[i] = 2
                extra2 += 1
    coords_f2 = [[0] * 2 for i in range(extra2)]
    f2 = 0
    for i in range(k):
        if extra[i] == 2:
            coords_f2[f2][0], coords_f2[f2][1] = coords[i][0], coords[i][1]
            f2 += 1
    return coords_f2

r = float(input('Введите размер радиуса окружности: '))
while r <= 0:
    r = float(input('Повторите ввод радиуса: '))
while True:
    k = int(input('Введите количество точек, область которых необходимо определить: '))
    if k >= 1:
        break
coords = [[0] * 2 for i in range(k)]
for i in range(k):
    coords[i][0] = float(input(f'Введите значение х {i + 1}-й точки: '))
    coords[i][1] = float(input(f'Введите значение y {i + 1}-й точки: '))
coords_f1=f1(coords)
coords_f2=f2(coords)
print(f'Точки, пренадлежащие первой области:\n{coords_f1}\nТочки, пренадлежащие второй области:\n{coords_f2}')