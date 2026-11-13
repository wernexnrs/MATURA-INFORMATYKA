def czy_pierwsza(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


with open("pierwsze.txt") as file:
    for line in file:
        liczba = line.strip()
        if czy_pierwsza(int(liczba[::-1])):
            print(liczba)
