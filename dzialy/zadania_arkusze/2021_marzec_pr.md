# 4.1
```py
from collections import Counter

panstwa = []
with open("Dane_2103/galerie.txt") as file:
    for line in file:
        line = line.strip()
        kod_kraju, miasto, *liczby = line.split()

        panstwa.append(kod_kraju)

with open("Dane_2103/wynik4_1.tx.txt", "w") as file2:
    for k, v in Counter(panstwa).items():
        file2.write(k + " " + str(v) + "\n")

```

# 4.2a
```py
with open("Dane_2103/galerie.txt") as file:
    with open("Dane_2103/wynik4_2a.txt", "w") as file2:
        for line in file:
            line = line.strip()
            kod_kraju, miasto, *liczby = line.split()

            liczby = list(map(int, filter(lambda a: a != '0', liczby)))
            wymiary = [a * b for a, b in zip(liczby[::2], liczby[1::2])]
            file2.write(miasto + " " + str(sum(wymiary)) + " " + str(len(wymiary)) + "\n")

```

# 4.2b
```py
lista = []

with open("Dane_2103/galerie_przyklad.txt") as file:
    for line in file:
        line = line.strip()
        kod_kraju, miasto, *liczby = line.split()

        liczby = list(map(int, filter(lambda a: a != '0', liczby)))
        wymiary = [a * b for a, b in zip(liczby[::2], liczby[1::2])]
        lista.append((miasto, sum(wymiary)))

maxi = sorted(lista, key=lambda x: x[1], reverse=True)[0]
mini = sorted(lista, key=lambda x: x[1])[0]

with open("Dane_2103/wynik4_2b.txt", "w") as file2:
    file2.write(maxi[0] + " " + str(maxi[1]) + "\n")
    file2.write(mini[0] + " " + str(mini[1]) + "\n")

```

# 4.3
```py
lista = []

with open("Dane_2103/galerie_przyklad.txt") as file:
    for line in file:
        line = line.strip()
        kod_kraju, miasto, *liczby = line.split()

        liczby = list(map(int, filter(lambda a: a != '0', liczby)))
        wymiary = [a * b for a, b in zip(liczby[::2], liczby[1::2])]
        lista.append((miasto, len(set(wymiary))))

maxi = sorted(lista, key=lambda x: x[1], reverse=True)[0]
mini = sorted(lista, key=lambda x: x[1])[0]

with open("Dane_2103/wynik4_3.txt", "w") as file2:
    file2.write(maxi[0] + " " + str(maxi[1]) + "\n")
    file2.write(mini[0] + " " + str(mini[1]) + "\n")

```

# 5.1
```py
from collections import Counter

lista = []

with open("Dane_2103/telefony.txt") as file:
    for line in file:
        line = line.strip().split()
        lista.append(line)

del lista[0]
numery = []

for line in lista:
    numery.append(line[0])

print(sorted(list(Counter(numery).items()), key=lambda x: x[1], reverse=True)[:3])

```

# 5.2
```py
# bez wykresu, nie ma matplotlib 
lista = []

with open("Dane_2103/telefony.txt") as file:
    for line in file:
        line = line.strip().split()
        lista.append(line)

del lista[0]

zestawienie = dict()

for line in lista:
    if line[1] not in zestawienie:
        zestawienie[line[1]] = list()
    zestawienie[line[1]].extend([line[0]])

for k, v in zestawienie.items():
    komorkowe = 0
    stacjonarne = 0
    for i in v:
        if len(i) == 7:
            stacjonarne += 1
        elif len(i) == 8:
            komorkowe += 1

    print(k, komorkowe, stacjonarne)


```
