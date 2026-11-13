def czy_pierwsza(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


with open("pary.txt") as file:
    for line in file:
        liczba = int(line.split()[0])
        if liczba > 4 and liczba % 2 == 0:
            # najmniejszy pierwszy składnik daje największą różnicę składników
            for p in range(3, liczba // 2 + 1, 2):
                if czy_pierwsza(p) and czy_pierwsza(liczba - p):
                    print(liczba, p, liczba - p)
                    break
