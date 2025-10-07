def ker(pocet_radku):
    for i in range(1, pocet_radku + 1):
        pocet_hvezdicek = i + (i - 1)
        pocet_tecek = pocet_radku - i
        print("."*pocet_tecek + "*"*pocet_hvezdicek + "."*pocet_tecek)

ker(int(input()))