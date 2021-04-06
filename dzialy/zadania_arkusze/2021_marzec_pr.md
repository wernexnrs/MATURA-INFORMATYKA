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

dni = []

for line in lista:
    dni.append(line[1])

zestawienie = dict()

for line in lista:
    if line[1] not in zestawienie:
        zestawienie[line[1]] = list()
    zestawienie[line[1]].extend([line[0]])

for k, v in zestawienie.items():
    print(k, v)
```
