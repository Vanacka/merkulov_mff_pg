def strom(pocet_radku_ker, pocet_radku_kmen):
    for i in range(1, pocet_radku_ker + 1):
        pocet_hvezdicek = i + (i - 1)
        pocet_tecek = pocet_radku_ker - i
        print("."*pocet_tecek + "*"*pocet_hvezdicek + "."*pocet_tecek)
    for j in range(pocet_radku_kmen):
        print("."*(pocet_radku_ker - 1) + "*" + "."*(pocet_radku_ker - 1))

strom(int(input()), int(input()))