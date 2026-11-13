from math import factorial

with open("liczby.txt") as file:
    for line in file:
        liczba = line.strip()
        suma = 0
        for cyfra in liczba:
            suma += factorial(int(cyfra))
        if suma == int(liczba):
            print(liczba)
