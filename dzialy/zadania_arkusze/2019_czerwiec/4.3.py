def waga(liczba):
    while liczba >= 10:
        suma = 0
        for cyfra in str(liczba):
            suma += int(cyfra)
        liczba = suma
    return liczba


ile = 0

with open("pierwsze.txt") as file:
    for line in file:
        if waga(int(line)) == 1:
            ile += 1

print(ile)
