<h1 align="center">2017 Czerwiec</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs123/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

## 4.1

```py
import re


def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        return True
    return False


count = 0

with open("MIN-DANE-2017/punkty.txt") as file:
    for line in file:
        line = re.split('\W+', line.strip())
        if is_prime(int(line[0])) and is_prime(int(line[1])):
            print(int(line[0]), int(line[1]))
            count += 1
print(count)

```

## 4.2

```py
import re


def is_anagram(x, y):
    x = set(sorted(list(x)))
    y = set(sorted(list(y)))
    if x == y:
        return True
    return False


count = 0

with open("MIN-DANE-2017/punkty.txt") as file:
    for line in file:
        line = re.split('\W+', line.strip())
        if is_anagram(line[0], line[1]):
            print(line[0], line[1])
            count += 1
print(count)

```

## 4.3

```py
import math
import re
from operator import itemgetter

lista = []
odleglosci = []


def odleglosc(x1, y1, x2, y2):
    return (x1, y1), (x2, y2), int(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


count = 0

with open("MIN-DANE-2017/punkty.txt") as file:
    for line in file:
        line = re.split('\W+', line.strip())
        lista.append(line)

for i in range(len(lista)):

    x1 = int(lista[i][0])
    y1 = int(lista[i][1])

    for j in range(1, len(lista)):
        odleglosci.append(odleglosc(x1, y1, int(lista[j][0]), int(lista[j][1])))

odleglosci.sort(key=itemgetter(2))

print(odleglosci[-1])

```

## 4.4

```py
import re

inside = 0
na_boku = 0
poza = 0

with open("MIN-DANE-2017/punkty.txt") as file:
    for line in file:
        line = re.split('\W+', line.strip())
        x = int(line[0])
        y = int(line[1])
        # print(x,y)
        if x < 5000 and y < 5000:
            inside += 1
        elif (x == 5000 or x == -5000) or (y == 5000 or y == -5000):
            na_boku += 1
        elif (x > 5000 or x < -5000) or (y > 5000 or y < -5000):
            poza += 1

print(inside, na_boku, poza)

```
