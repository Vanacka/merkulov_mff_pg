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

def IntersectionDestruct(a,b):
    """ destruktivni prunik dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """

    if a is None or b is None:
        return None
    if a.x < b.x:
        seznam1 = a.dalsi
        seznam2 = b
        prvni_prvek = None
        posledni_prvek = None
    elif a.x > b.x:
        seznam1 = a
        seznam2 = b.dalsi
        prvni_prvek = None
        posledni_prvek = None
    else:
        seznam1 = a.dalsi
        seznam2 = b.dalsi
        predchozi = a
        prvni_prvek = a
        posledni_prvek = a

    while seznam1 is not None and seznam2 is not None:
        if seznam1.x < seznam2.x:
            seznam1 = seznam1.dalsi
        elif seznam1.x > seznam2.x:
            seznam2 = seznam2.dalsi
        else:
            if prvni_prvek is None:
                prvni_prvek = seznam1
                predchozi = seznam1
                posledni_prvek = seznam1
                seznam1 = seznam1.dalsi
                seznam2 = seznam2.dalsi
            else:
                predchozi.dalsi = seznam1
                predchozi = seznam1
                posledni_prvek = seznam1
                seznam1 = seznam1.dalsi
                seznam2 = seznam2.dalsi

    if posledni_prvek is not None:
        posledni_prvek.dalsi = None

    return prvni_prvek

#################################################

VytiskniLSS( IntersectionDestruct( NactiLSS(), NactiLSS() ) )
