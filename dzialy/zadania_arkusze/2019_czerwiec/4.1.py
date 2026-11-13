def czy_pierwsza(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


with open("liczby.txt") as file:
    for line in file:
        liczba = int(line)
        if 100 <= liczba <= 5000 and czy_pierwsza(liczba):
            print(liczba)
