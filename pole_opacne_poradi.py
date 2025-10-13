pole = []
vstup = int(input())

while vstup != -1:
    pole.append(vstup)
    vstup = int(input())

for i in range(len(pole) - 1, -1, -1):
    print(pole[i])