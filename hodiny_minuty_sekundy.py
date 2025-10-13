sekudny = int(input())

minuty = sekudny // 60
sekundy = sekudny % 60

hodiny = minuty // 60
minuty = minuty % 60

print(hodiny, minuty, sekundy)