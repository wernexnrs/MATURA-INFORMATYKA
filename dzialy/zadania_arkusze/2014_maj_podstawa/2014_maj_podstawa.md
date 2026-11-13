<h1 align="center">Matura 2014 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2014-maj-matura-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2014-maj-matura-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2014-maj-matura-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2014-maj-matura-podstawowa-odpowiedzi.pdf)

## 1a i 1b

```py
def dzielniki(n):
    wynik = []
    d = 1
    while d <= n // 2:  # 1b: wystarczy sprawdzać do n div 2
        if n % d == 0:
            wynik.append(d)
        d = d + 1
    return wynik


for n in [6, 35, 56, 81]:
    print(n, *dzielniki(n))
```
**Odpowiedź:** a) 35 → 1 5 7; 56 → 1 2 4 7 8 14 28; 81 → 1 3 9 27; b) d ≤ n div 2

## 1c

```py
def doskonala_II_rzedu(n):
    iloczyn = 1
    d = 1
    while d <= n // 2:
        if n % d == 0:
            iloczyn = iloczyn * d
        d = d + 1
    if iloczyn == n:
        return "TAK"
    return "NIE"


for n in [6, 8, 10, 12, 16]:
    print(n, doskonala_II_rzedu(n))
```
**Odpowiedź:** np. 6 → TAK, 8 → TAK, 10 → TAK, 12 → NIE, 16 → NIE

## 2a i 2b

```py
def min_max_pary(a):
    n = len(a)
    i = 0
    while i < n - 1:
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
        i = i + 2
    return a


print(min_max_pary([45, 12, 7, 39, 20, 1]))
print(min_max_pary([21, 1, 56, 90, 8, 8, 19, 47]))
```
**Odpowiedź:** a) [12, 45, 7, 39, 1, 20], [1, 21, 56, 90, 8, 8, 19, 47]; b) a[i] ≤ a[i+1]

## 2c

```py
def min_max(a):
    n = len(a)
    i = 0
    while i < n - 1:
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
        i = i + 2
    mini = a[0]
    maks = a[1]
    i = 2
    while i < n - 1:
        if a[i] < mini:
            mini = a[i]
        if a[i + 1] > maks:
            maks = a[i + 1]
        i = i + 2
    return mini, maks


print(min_max([45, 12, 7, 39, 20, 1]))
print(min_max([21, 1, 56, 90, 8, 8, 19, 47]))
```
**Odpowiedź:** min ← a[1], max ← a[2], dopóki i < n: jeżeli a[i] < min, to min ← a[i]; jeżeli a[i+1] > max, to max ← a[i+1]

## 4a

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
dzialki = []

with open("DZIALKI.TXT") as file:
    next(file)  # pomijamy nagłówek
    for line in file:
        numer, powierzchnia, rodzaj, ulga = line.strip().split(";")
        dzialki.append((float(powierzchnia.replace(",", ".")), rodzaj))

print("min:", min(dzialki))
print("max:", max(dzialki))
```
**Odpowiedź:** min: 500,18 – siedliskowa (S); max: 1500 – rekreacyjna (X)

## 4b

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
liczba = {}
suma = {}

with open("DZIALKI.TXT") as file:
    next(file)
    for line in file:
        numer, powierzchnia, rodzaj, ulga = line.strip().split(";")
        liczba[rodzaj] = liczba.get(rodzaj, 0) + 1
        suma[rodzaj] = suma.get(rodzaj, 0) + float(powierzchnia.replace(",", "."))

for rodzaj in "RBSLX":
    print(rodzaj, liczba[rodzaj], round(suma[rodzaj] / liczba[rodzaj], 2))
```
**Odpowiedź:** R (rolna) 708 – 989,98; B (budowlana) 1775 – 999,59; S (siedliskowa) 964 – 986,12; L (leśna) 559 – 1016,75; X (rekreacyjna) 994 – 989,94

## 4c

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
from decimal import Decimal, ROUND_HALF_UP

stawka = {"R": "0.65", "B": "0.77", "S": "0.21", "L": "0.04", "X": "0.43"}
procent_ulgi = {"A": 20, "B": 50, "C": 90, "D": 0}


def zaokraglij(x):  # zaokrąglenie do grosza jak w arkuszu kalkulacyjnym
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


do_100 = 0
do_500 = 0
ponad_500 = 0

with open("DZIALKI.TXT") as file:
    next(file)
    for line in file:
        numer, powierzchnia, rodzaj, ulga = line.strip().split(";")
        podatek = zaokraglij(Decimal(powierzchnia.replace(",", ".")) * Decimal(stawka[rodzaj]))
        podatek = zaokraglij(podatek * (100 - procent_ulgi[ulga]) / 100)
        if podatek <= 100:
            do_100 += 1
        elif podatek <= 500:
            do_500 += 1
        else:
            ponad_500 += 1

print(do_100, do_500, ponad_500)
```
**Odpowiedź:** do 100 zł – 2096, ponad 100 zł do 500 zł – 2133, ponad 500 zł – 771 (wykres procentowy wykonuje się w arkuszu kalkulacyjnym)

## 5a

```py
count = 0

with open("PARY_LICZB.TXT") as file:
    for line in file:
        a, b = map(int, line.split())
        if a % b == 0 or b % a == 0:
            count += 1

print(count)
```
**Odpowiedź:** 10

## 5b

```py
def nwd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


count = 0

with open("PARY_LICZB.TXT") as file:
    for line in file:
        a, b = map(int, line.split())
        if nwd(a, b) == 1:
            count += 1

print(count)
```
**Odpowiedź:** 584

## 5c

```py
def suma_cyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    return suma


count = 0

with open("PARY_LICZB.TXT") as file:
    for line in file:
        a, b = line.split()
        if suma_cyfr(a) == suma_cyfr(b):
            count += 1

print(count)
```
**Odpowiedź:** 48
