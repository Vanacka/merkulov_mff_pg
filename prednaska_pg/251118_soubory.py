f = open("251118_soubory.py")
g = open("kopie.py", "w", encoding="utf-8")


radek = f.readline()

while radek != "":
    g.write(radek)
    print(radek, end="")
    radek = f.readline()
print("---koneček---")

g = open("cisla.txt", "w")
for i in range(1_000_000):
    g.write(f"{i}\n")
g.close()