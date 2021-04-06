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
