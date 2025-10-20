def n_to_dec(n, cislo) -> int:
    vysledek = 0
    i = 0
    for cislice in reversed(cislo):
        vysledek += int(cislice)* (n**i)
        i += 1
    return vysledek

def dec_to_n(n, cislo) -> int:
    seznam_vysledku = []
    vysledek = ""
    while cislo > 0:
        seznam_vysledku.append(cislo % n)
        cislo = cislo // n

    for cislice in reversed(seznam_vysledku):
        vysledek += str(cislice)
    return int(vysledek)


vstup = input().split()
rozdeleni = []
skupina = []
i = 0

while i < len(vstup):
    if (i + 1) % 5 == 0:
        skupina.append(int(vstup[i]))
        rozdeleni.append(skupina)
        skupina = []
        i += 1
    else:
        skupina.append(vstup[i])
        i += 1

for i in range(len(rozdeleni)):
    prvni = n_to_dec(int(rozdeleni[i][0]), rozdeleni[i][1])
    druhy = n_to_dec(int(rozdeleni[i][2]), rozdeleni[i][3])
    soucet = dec_to_n(rozdeleni[i][4], prvni + druhy)
    rozdil = dec_to_n(rozdeleni[i][4], prvni - druhy)
    soucin = dec_to_n(rozdeleni[i][4], prvni * druhy)
    podil = dec_to_n(rozdeleni[i][4], prvni // druhy)
    print(soucet)
    print(rozdil)
    print(soucin)
    print(podil)