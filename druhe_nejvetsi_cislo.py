maximum = int(input())
druhe_maximum = int(input())

while druhe_maximum == maximum:
    druhe_maximum = int(input())

if druhe_maximum > maximum:
    maximum, druhe_maximum = druhe_maximum, maximum

a = int(input())

while a != -1:
    if a > maximum:
        druhe_maximum = maximum
        maximum = a
    elif a > druhe_maximum and a != maximum:
        druhe_maximum = a
    a = int(input())

print(druhe_maximum)