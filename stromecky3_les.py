seznam = []
max_x = 0
max_y = 0
vstup = input().split()
seznam.append(vstup)

while True:
    vstup = input().split()
    if vstup == []:
        break
    seznam.append(vstup)

for i in range(len(seznam)):
    if int(seznam[i][0]) + int(seznam[i][2]) * 2 - 1 > max_x:
        max_x = int(seznam[i][0]) + int(seznam[i][2]) * 2 - 1
    if int(seznam[i][1]) + int(seznam[i][3]) + int(seznam[i][2]) > max_y:
        max_y = int(seznam[i][1]) + int(seznam[i][3]) + int(seznam[i][2])
    seznam[i][0] = int(seznam[i][0])
    seznam[i][1] = int(seznam[i][1])
    seznam[i][2] = int(seznam[i][2])
    seznam[i][3] = int(seznam[i][3])

pole = [[False for _ in range(max_x)] for _ in range(max_y)]


def strom(pocet_radku_ker, pocet_radku_kmen, x, y):
    global pole
    for i in range(pocet_radku_ker):
        for j in range(i + i + 1):
            pocet_tecek = pocet_radku_ker - i - 1
            pole[i + y][pocet_tecek + j + x] = True

    for i in range(pocet_radku_kmen):
        pole[i + y + pocet_radku_ker][((pocet_radku_ker + pocet_radku_ker - 1) // 2) + x] = True

for i in range(len(seznam)):
    pocet_radku_ker = seznam[i][2]
    pocet_radku_kmen = seznam[i][3]
    x = seznam[i][0]
    y = seznam[i][1]
    strom(pocet_radku_ker, pocet_radku_kmen, x, y)

for i in range(max_y):
    for j in range(max_x):
        if pole[i][j] == True:
            print("*", end="")
        else:
            print(".", end="")
    print()