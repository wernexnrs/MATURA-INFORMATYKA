lista = []
liczba = 0
i = 0

while liczba <= 100000:
    liczba = 3 ** i
    lista.append(liczba)
    i += 1

count = 0

with open("Dane_PR/liczby.txt") as file:
    for line in file:
        line = int(line.strip())
        if line in lista:
            count += 1
print(count)