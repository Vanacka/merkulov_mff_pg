def kino (kasa, sto, dvesto, vys):
    if sto + dvesto == 0:
        print(vys)
        return
    if sto > 0:
        kino (kasa, sto - 1, dvesto, vys + "100 ")
    if dvesto > sto:
        kino (kasa, sto, dvesto - 1, vys + "200 ")

kino(0, 4, 4, "")