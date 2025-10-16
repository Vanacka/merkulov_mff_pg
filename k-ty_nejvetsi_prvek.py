'''
Na vstupu je posloupnost navzájem různých celých čísel, každé na samostatném řádku, ukončená
−
1
−1. Dále následuje číslo
K
K.

Najděte a vypište
K
K-té největší číslo.

Testování: Všechny vstupy, na kterých budeme vaše řešení testovat, budou obsahovat nejvýše
10
 
000
10000 čísel, každé v rozsahu
0
0 do
1
 
000
 
000
 
000
1000000000. Pro číslo
K
K bude platit
1
≤
K
≤
100
1≤K≤100 a navíc
K
K pochopitelně nepřekročí počet všech čísel. Tyto nerovnosti nemusíte v programu kontrolovat, uvádíme je jen pro informaci, abyste věděli, jaké vstupy očekávat.

Nápověda: Čísla nechcete řadit podle velikosti. Zejména nepoužívejte zabudované funkce sort a sorted.
'''


vstup = int(input())
posloupnost = []

while vstup != -1:
    posloupnost.append(vstup)
    vstup = int(input())

k = int(input())


for i in range(k - 1):
    maximum = max(posloupnost)
    posloupnost.remove(maximum)

print(max(posloupnost))