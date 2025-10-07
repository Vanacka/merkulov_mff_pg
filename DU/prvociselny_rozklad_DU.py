zadane_cislo = int(input())
cislo = zadane_cislo
prvocisla = [True] * (cislo + 1)
prvocisla[0] = False
prvocisla[1] = False
rozklad = []

# Vytvori seznam prvocisel
for i in range(2, cislo + 1):
    if prvocisla[i] == True:
        for j in range(i * i, cislo + 1, i):
            prvocisla[j] = False

# Vytvori prvociselny rozklad (zkouma pouze prvocisla)
delitel = 2
while delitel ** 2 <= cislo:
    if prvocisla[delitel] == True:
        while cislo % delitel == 0:
            rozklad.append(delitel)
            cislo = cislo // delitel
    delitel += 1
# Zapise posledni cislo rozkladu
if cislo > 1:
    rozklad.append(cislo)

# Vypise prvociselny rozklad
print(str(zadane_cislo) + "=" + "*".join(str(prvocislo) for prvocislo in rozklad))