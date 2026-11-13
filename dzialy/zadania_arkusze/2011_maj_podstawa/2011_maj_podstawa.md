<h1 align="center">Matura 2011 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2011-maj-matura-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2011-maj-matura-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2011-maj-matura-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2011-maj-matura-podstawowa-odpowiedzi.pdf)

## 1a i 1b

```py
print(len(bin(14400)[2:]))  # liczba pól zegara
print(int("1111110100100", 2) // 60)  # liczba minut
```
**Odpowiedź:** a) 14 pól; b) 135 minut

## 1c

```py
def liczba_jedynek(s):
    l = 0
    while s > 0:
        if s % 2 == 1:
            l += 1
        s = s // 2
    return l


print(liczba_jedynek(3600), liczba_jedynek(5400))
```
**Odpowiedź:** dla 3600 → 4, dla 5400 → 5

## 2a

```py
def algorytm(n):
    i = 2
    while True:
        if i >= n:
            return "TAK"
        if n % i == 0:
            return "NIE"
        i += 1


for n in [25, 37, 41, 49]:
    print(n, algorytm(n))
```
**Odpowiedź:** 25 NIE, 37 TAK, 41 TAK, 49 NIE; b) F, P, P, F

## 2c

```py
def rozklad(n):
    czynniki = []
    i = 2
    while n > 1:
        while n % i == 0:
            czynniki.append(i)
            n = n // i
        i += 1
    return czynniki


for n in [42, 17, 36]:
    print(n, rozklad(n))
```
**Odpowiedź:** 42 → 2, 3, 7; 17 → 17; 36 → 2, 2, 3, 3

## 4a

```py
parzyste = 0
nieparzyste = 0

with open("hasla.txt") as file:
    for line in file:
        haslo = line.strip()
        if len(haslo) % 2 == 0:
            parzyste += 1
        else:
            nieparzyste += 1

print(parzyste, nieparzyste)
```
**Odpowiedź:** 105 haseł ma parzystą liczbę znaków, 95 nieparzystą

## 4b

```py
with open("hasla.txt") as file:
    for line in file:
        haslo = line.strip()
        if haslo == haslo[::-1]:
            print(haslo)
```
**Odpowiedź:** dompmod, grafarg, kajak, komok, matam, mpoopm, mpouiuopm, oddo, omo, pokop, plkjjklp, pokkop, plolp

## 4c

```py
with open("hasla.txt") as file:
    for line in file:
        haslo = line.strip()
        for i in range(1, len(haslo)):
            if ord(haslo[i - 1]) + ord(haslo[i]) == 220:
                print(haslo)
                break
```
**Odpowiedź:** amodda, damod, damodd, dompmod, edamo, edamod, isksad, iughd, … (54 hasła)

## 6a

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
uczniowie = []

with open("test.txt") as file:
    next(file)
    for line in file:
        uczniowie.append(list(map(int, line.split())))

for pytanie in range(1, 26):
    poprawne = 0
    for uczen in uczniowie:
        poprawne += uczen[pytanie]
    if poprawne > len(uczniowie) / 2:
        print(pytanie)
```
**Odpowiedź:** 2, 9, 12, 18, 19, 20, 22

## 6b

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
wyniki = []

with open("test.txt") as file:
    next(file)
    for line in file:
        odpowiedzi = list(map(int, line.split()))
        wyniki.append(sum(odpowiedzi[1:]))

srednia = sum(wyniki) / len(wyniki)
count = 0
for wynik in wyniki:
    if wynik > srednia:
        count += 1

print(count)
```
**Odpowiedź:** 55

## 6c

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
bardzo_dobre = 0
niedostateczne = 0

with open("test.txt") as file:
    next(file)
    for line in file:
        odpowiedzi = list(map(int, line.split()))
        procent = sum(odpowiedzi[1:]) / 25 * 100
        if procent > 90:
            bardzo_dobre += 1
        if procent <= 30:
            niedostateczne += 1

print("bardzo dobre:", bardzo_dobre, "niedostateczne:", niedostateczne)
```
**Odpowiedź:** bardzo dobre: 1, niedostateczne: 6

## 6d

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
with open("test.txt") as file:
    next(file)
    for line in file:
        odpowiedzi = list(map(int, line.split()))
        if odpowiedzi[5] == 1 and odpowiedzi[15] == 1 and odpowiedzi[25] == 1:
            print(odpowiedzi[0])
```
**Odpowiedź:** 2, 45, 65, 70, 79

## 6e

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
epoki = ["prehistoria", "starożytność", "średniowiecze", "historia nowożytna", "historia najnowsza"]
poprawne = [0] * 5

with open("test.txt") as file:
    next(file)
    for line in file:
        odpowiedzi = list(map(int, line.split()))
        for pytanie in range(1, 26):
            poprawne[(pytanie - 1) // 5] += odpowiedzi[pytanie]

for i in range(5):
    print(epoki[i], poprawne[i])
```
**Odpowiedź:** prehistoria 278, starożytność 263, średniowiecze 281, historia nowożytna 320, historia najnowsza 298 (wykres kolumnowy wykonuje się w arkuszu kalkulacyjnym)
