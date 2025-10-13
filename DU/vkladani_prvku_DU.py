pocet_prvku1 = int(input())
posloupnost1 = []
posloupnost2 = []

for i in range(pocet_prvku1):
    prvek = int(input())
    posloupnost1.append(prvek)

pocet_prvku2 = int(input())

for i in range(pocet_prvku2):
    prvek = int(input())
    posloupnost2.append(prvek)

for i in range(pocet_prvku2):
    for j in range(pocet_prvku2 - i - 1):
        if posloupnost2[j] > posloupnost2[j + 1]:
            posloupnost2[j], posloupnost2[j + 1] = posloupnost2[j + 1], posloupnost2[j]

i = j = 0

while i < pocet_prvku1 and j < pocet_prvku2:
    if posloupnost2[j] <= posloupnost1[i]:
        print(posloupnost2[j])
        j += 1
    else:
        print(posloupnost1[i])
        i += 1

# Vypise zbytek prvni posloupnosti
while i < pocet_prvku1:
    print(posloupnost1[i])
    i += 1

# Vypise zbytek druhe posloupnosti
while j < pocet_prvku2:
    print(posloupnost2[j])
    j += 1