class Prvek:
    def __init__(self, x, dalsi):
        self.x = x
        self.dalsi = dalsi

def VytiskniLSS( p ):
    print( "LSS:", end=" " )
    while p!=None:
        print( p.x, end=" " )
        p = p.dalsi
    print(".")

def NactiLSS():
    """cte cisla z radku, dokud nenacte prazdny radek"""
    prvni = None
    posledni = None
    r = input()
    while r!="":
        radek = r.split()
        if len(radek)==0: # protoze ten test r!="" v RCDX neukoncil cyklus!
            break
        for s in radek:
            p = Prvek(int(s),None)
            if prvni==None:
                prvni = p
            else:
                posledni.dalsi = p
            posledni = p
        r = input()
    return prvni

#################################################

def UnionDestruct(a,b):
    """ destruktivni sjednoceni dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """
    if a is None:
        return b
    elif b is None:
        return a
    else:
        if a.x < b.x:
            seznam1 = a.dalsi
            seznam2 = b
            predchozi = a
            prvni_prvek = a
        elif a.x > b.x:
            seznam1 = a
            seznam2 = b.dalsi
            predchozi = b
            prvni_prvek = b
        else:
            seznam1 = a.dalsi
            seznam2 = b.dalsi
            predchozi = a
            prvni_prvek = a

        while seznam1 is not None and seznam2 is not None:
            if seznam1.x < seznam2.x:
                predchozi.dalsi = seznam1
                predchozi = seznam1
                seznam1 = seznam1.dalsi
            elif seznam1.x > seznam2.x:
                predchozi.dalsi = seznam2
                predchozi = seznam2
                seznam2 = seznam2.dalsi
            else:
                predchozi.dalsi = seznam1
                predchozi = seznam1
                seznam1 = seznam1.dalsi
                seznam2 = seznam2.dalsi
        if seznam1 is None:
            predchozi.dalsi = seznam2
        else:
            predchozi.dalsi = seznam1

    return prvni_prvek

#################################################

VytiskniLSS( UnionDestruct( NactiLSS(), NactiLSS() ) )
