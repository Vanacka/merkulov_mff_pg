pole = []
max = 0

while True:
    cislo = int(input())
    if cislo == -1:
        break
    else:
        pole.append(cislo)

if len(pole) > 1:
    if pole[1] >= pole[0]:
        max = pole[1]
    else:
        max = pole[0]

    for i in range(1, len(pole) - 1):
        if pole[i] >= max:
            max = pole[i]

    print(max)
else:
    print(pole[0])