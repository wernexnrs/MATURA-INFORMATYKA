from math import gcd

with open("liczby.txt") as file:
    liczby = [int(line) for line in file]

najdluzszy = 0

for i in range(len(liczby)):
    nwd = liczby[i]
    j = i
    # rozszerzamy ciąg zaczynający się od i, dopóki NWD wszystkich liczb jest większy od 1
    while j + 1 < len(liczby) and gcd(nwd, liczby[j + 1]) > 1:
        j += 1
        nwd = gcd(nwd, liczby[j])
    if j - i + 1 > najdluzszy:
        najdluzszy = j - i + 1
        pierwsza = liczby[i]
        dzielnik = nwd

print(pierwsza, najdluzszy, dzielnik)
