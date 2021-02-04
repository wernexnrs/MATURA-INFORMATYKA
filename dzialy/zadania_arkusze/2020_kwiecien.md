<h1 align="center">2020 Kwiecień</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs123/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

## 4.1

```py
lista = luki = []
with open("dane\dane4.txt") as file:
    for line in file:
        line = int(line.strip())
        lista.append(line)

wartownik = lista[0]
for i in lista[1:]:
    wynik = abs(wartownik - i)
    luki.append(wynik)
    wartownik = i

print(min(luki))
print(max(luki))
```

## 4.2

```py
lista, luki, max_list = [], [], []

with open("dane/dane4.txt") as file:
    for line in file:
        line = int(line.strip())
        lista.append(line)

for i in range(len(lista)):
    luki.append(abs(lista[i - 1] - lista[i]))

longest = count = 1

for i in range(len(luki)):
    if luki[i - 1] == luki[i]:
        count += 1
    else:
        count = 1
    max_list.append(count)

print(max(max_list) + 1)
print("poczatek", lista[max_list.index(max(max_list)) - max(max_list)])
print("koniec", lista[max_list.index(max(max_list))])

```

## 4.3

```py
from collections import Counter

lista = luki = []

with open("dane/dane4.txt") as file:
    for line in file:
        line = int(line.strip())
        lista.append(line)

for i in range(1, len(lista)):
    luki.append(abs(lista[i - 1] - lista[i]))

print(Counter(luki))

```
