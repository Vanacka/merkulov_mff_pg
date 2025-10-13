vstup = input()
pocet_radku, pocet_sloupcu = vstup.split()
matrix = []
minimum = -1

pocet_radku = int(pocet_radku)
pocet_sloupcu = int(pocet_sloupcu)

for i in range(pocet_radku):
    radek = []
    cisla = input().split()
    for cislo in cisla:
        cislo = int(cislo)
        radek.append(cislo)
        if minimum < 0:
            minimum = cislo
        if minimum > 0 and cislo < minimum:
            minimum = cislo
    matrix.append(radek)

for i in range(pocet_radku):
    for j in range(pocet_sloupcu):
        print(matrix[i][j] - minimum, end=" ")
    print()
