pole = []
vstup = int(input())

while vstup != -1:
    if vstup % 2 != 0:
        pole.append(vstup)
        vstup = int(input())
    else:
        print(vstup)
        vstup = int(input())

for i in range(len(pole)):
    print(pole[i])
