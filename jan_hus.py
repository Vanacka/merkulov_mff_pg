def vytvor_hus():
    f = open("Hus.txt", "w")
    for i in range(99):
        f.write("Mistr Jan Hus vynalezl háčky a čárky.\n")
    f.write("Mistr Jan Hus vynalezl háčky a čárky.")
    f.close()

vytvor_hus()

tabulka = {}
g = open("jan_hus.py", "r", encoding="utf-8")
radek = g.readline()

while radek != "":
    for pismeno in radek:
        if pismeno not in tabulka:
            tabulka[pismeno] = 1
        tabulka[pismeno] += 1
    radek = g.readline()

tabulka = sorted(tabulka.items(), key=lambda x: x[1], reverse=True)

for znak, pocet in tabulka:
    print(f"{znak} : {pocet}")
