<h1 align="center">2019 Czerwiec</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs123/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

## 4.1

```py
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False


with open("MIN-R2A1P-193_dane/liczby.txt") as file:
    for line in file:
        line = int(line)
        if is_prime(line) and line in range(100, 5001):
            print(line)

```

## 4.2

```py
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False


with open("MIN-R2A1P-193_dane/pierwsze.txt") as file:
    for line in file:
        line = line.strip()
        liczba = int(line[::-1])
        if is_prime(liczba):
            print(line)

```

## 4.3

```py
def waga(n=''):
    wynik = 0
    while len(str(n)) > 1:
        for char in n:
            char = int(char)
            wynik += char
        n = str(wynik)
        wynik = 0
    return n


count = 0

with open("MIN-R2A1P-193_dane/pierwsze_przyklad.txt") as file:
    for line in file:
        line = line.strip()
        if waga(line) == '1':
            count += 1
print(count)

```
