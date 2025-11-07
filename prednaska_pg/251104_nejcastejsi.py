zbyvajici_slova = []
def precti_slovo():
    #global zbyvajici_slova
    while zbyvajici_slova == []:
        #zbyvajici_slova = input().split()
        zbyvajici_slova.extend(input().split())
    return zbyvajici_slova.pop(0)

slova = []
pocty = []
def zapocitej_slovo_stara(slovo):
    if slovo not in slova:
        slova.append(slovo)
        pocty.append(0)
    pocty[slova.index(slovo)] += 1

slovnik = {"...": 0}
def zapocitej_slovo(slovo):
    if slovo not in slovnik:
        slovnik[slovo] = 0
    slovnik[slovo] += 1


def najdi_vrat_a_znic_nejcastejsi_slovo():
    kolik = -1
    for slovo in slovnik:
        if slovnik[slovo] > kolik:
            kolik = slovnik[slovo]
            nejcastejsi_slovo = slovo
    slovnik[nejcastejsi_slovo] = -1
    return (kolik, nejcastejsi_slovo)

KONEC = "KONEC"

slovo = precti_slovo()
while slovo != KONEC:
    zapocitej_slovo(slovo)
    slovo = precti_slovo()

for i in range(20):
    print(najdi_vrat_a_znic_nejcastejsi_slovo())