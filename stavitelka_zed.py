from merkulov_mff_pg import stavitelka as st

sirka = int(input())
vyska = int(input())

for i in range(vyska):
    if i % 2 == 0:
        for j in range(sirka):
            st.Kvadr(x=-(sirka/2)*2 + j + j*1.1 ,y=(vyska/2)-i*0.5 - i*0.1 ,z=0 , sx=2, sy=0.5, sz=1, barva=(1,1,0))
    else:
        for j in range(sirka):
            st.Kvadr(x=-(sirka/2)*2 + 1 + j + j*1.1 ,y=(vyska/2)-i*0.5 - i*0.1 ,z=0 , sx=2, sy=0.5, sz=1, barva=(1,1,0))

st.ZobrazScenu()