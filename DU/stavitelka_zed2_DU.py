from merkulov_mff_pg import stavitelka as st

def predni_zadni_zed(sirka, vyska, hloubka):
    for i in range(vyska):
        if i % 2 == 0:
            for j in range(sirka):
                st.Kvadr(x=-sirka + j + j*1.1, y=(vyska/2)-i*0.5 - i*0.1, z=hloubka , sx=2, sy=0.5, sz=1, barva=(1,1,0))
        else:
            for j in range(sirka):
                st.Kvadr(x=-sirka + 1.1 + j + j*1.1, y=(vyska/2)-i*0.5 - i*0.1, z=hloubka, sx=2, sy=0.5, sz=1, barva=(1,1,0))

        if i % 2 != 0:
            for j in range(sirka):
                st.Kvadr(x=-sirka + j + j*1.1, y=(vyska/2)-i*0.5 - i*0.1, z=-hloubka - hloubka*0.1, sx=2, sy=0.5, sz=1, barva=(1,1,0))
        else:
            for j in range(sirka):
                st.Kvadr(x=-sirka + 1.1 + j + j*1.1, y=(vyska/2)-i*0.5 - i*0.1, z=-hloubka - hloubka*0.1, sx=2, sy=0.5, sz=1, barva=(1,1,0))

def leva_prava_zed(sirka, vyska, hloubka):
    for i in range(vyska):
        if i % 2 == 0:
            for j in range(hloubka):
                st.Kvadr(x=sirka + sirka*0.1 - 0.5, y=(vyska/2) - i*0.6, z=hloubka - 0.5 - 2.1*j, sx=2, sy=0.5, sz=1, ry=90, barva=(3,0,1))
        else:
            for j in range(hloubka):
                st.Kvadr(x=sirka + sirka*0.1 - 0.5, y=(vyska/2) - i*0.6, z=hloubka - 1.6 - 2.1*j, sx=2, sy=0.5, sz=1, ry=90, barva=(3,0,1))

        if i % 2 != 0:
            for j in range(hloubka):
                st.Kvadr(x=-sirka - 0.5, y=(vyska/2) - i*0.6, z=hloubka - 0.5 - 2.1*j, sx=2, sy=0.5, sz=1, ry=90, barva=(3,0,1))
        else:
            for j in range(hloubka):
                st.Kvadr(x=-sirka - 0.5, y=(vyska/2) - i*0.6, z=hloubka - 1.6 - 2.1*j, sx=2, sy=0.5, sz=1, ry=90, barva=(3,0,1))


sirka = int(input())
vyska = int(input())
hloubka = int(input())

predni_zadni_zed(sirka, vyska, hloubka)
leva_prava_zed(sirka, vyska, hloubka)
st.ZobrazScenu()