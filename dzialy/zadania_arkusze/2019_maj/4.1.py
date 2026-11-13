potegi_trojki = []
potega = 1
while potega <= 100000:
    potegi_trojki.append(potega)
    potega *= 3

ile = 0

with open("liczby.txt") as file:
    for line in file:
        if int(line) in potegi_trojki:
            ile += 1

print(ile)
