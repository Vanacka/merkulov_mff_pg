def suma(mince, vys, zbyva_zaplatit):
    if zbyva_zaplatit == 0:
        print(vys)
        return
    for i, m in enumerate(mince):
        if m <= zbyva_zaplatit:
            # Kdyz se m nezmenilo, tak neodrstranuji nic kdyz se zmenilo m, tak odstranim ze seznamu vsechny vetsi mince nez m
            suma(mince[i:], vys + str(m) + " ", zbyva_zaplatit - m)


pocet_typu_minci = int(input())
mince = [int(m) for m in input().split()]
zbyva_zaplatit = int(input())

suma(mince, "", zbyva_zaplatit)
