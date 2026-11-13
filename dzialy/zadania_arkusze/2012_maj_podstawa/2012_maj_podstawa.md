<h1 align="center">Matura 2012 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2012-maj-matura-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2012-maj-matura-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2012-maj-matura-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2012-maj-matura-podstawowa-odpowiedzi.pdf)

## 1a i 1b

```py
poziomy = []


def fib(k, poziom=0):
    # zapamiętujemy argumenty wywołań na kolejnych poziomach drzewa
    if len(poziomy) <= poziom:
        poziomy.append([])
    poziomy[poziom].append(k)
    if k == 1 or k == 2:
        return 1
    return fib(k - 1, poziom + 1) + fib(k - 2, poziom + 1)


print("Fib(8) =", fib(8))
print("Fib(11) =", fib(11))

poziomy.clear()
fib(6)
for poziom in poziomy:  # drzewo wywołań dla Fib(6), poziom po poziomie
    print(*poziom)
```
**Odpowiedź:** a) Fib(8) = 21, Fib(11) = 89; b) drzewo: 6 / 5 4 / 4 3 3 2 / 3 2 2 1 2 1 / 2 1

## 1c

```py
def wyraz(k):
    a = [0, 1, 1]  # a[1] = a[2] = 1, a[0] nieużywane
    for i in range(3, k + 1):
        if i % 2 == 0:
            a.append(a[i - 1] + a[i - 2] + a[i - 3])
        else:
            a.append(a[i - 1])
    return a[k]


for k in range(1, 9):
    print(k, wyraz(k))
```
**Odpowiedź:** 1, 1, 1, 3, 3, 7, 7, 17 (zgodnie z tabelą w treści)

## 2a

```py
def algorytm(d):
    n = len(d)
    j = 0
    i = 1
    while i < n:
        if d[i - 1] > d[i]:  # większe(i, i+1), numeracja od 1
            j = j + 1
        i = i + 1
    return j


for d in [[5, 2, 1, 6], [2, 5, 1, 2], [1, 2, 3, 4], [4, 3, 2, 1]]:
    print(d, algorytm(d))
```
**Odpowiedź:** 2 (podane), 1, 0, 3

## 2b

```py
def najdrozszy(d):
    porownania = 0
    i = 1
    for k in range(2, len(d) + 1):
        porownania += 1
        if d[k - 1] > d[i - 1]:  # większe(k, i)
            i = k
    return i, porownania


print(najdrozszy([5, 2, 1, 6]))
print(najdrozszy(list(range(1000)))[1])
```
**Odpowiedź:** dla n = 1000 algorytm wykonuje 999 porównań

## 4a

```py
parzyste = 0

with open("cyfry.txt") as file:
    for line in file:
        if int(line) % 2 == 0:
            parzyste += 1

print(parzyste)
```
**Odpowiedź:** 495

## 4b

```py
def suma_cyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    return suma


najwieksza = ""
najmniejsza = ""

with open("cyfry.txt") as file:
    for line in file:
        liczba = line.strip()
        if najwieksza == "" or suma_cyfr(liczba) > suma_cyfr(najwieksza):
            najwieksza = liczba
        if najmniejsza == "" or suma_cyfr(liczba) < suma_cyfr(najmniejsza):
            najmniejsza = liczba

print("największa suma cyfr:", najwieksza)
print("najmniejsza suma cyfr:", najmniejsza)
```
**Odpowiedź:** największa suma cyfr: 187869866, najmniejsza suma cyfr: 10010

## 4c

```py
with open("cyfry.txt") as file:
    for line in file:
        liczba = line.strip()
        rosnace = True
        for i in range(1, len(liczba)):
            if liczba[i] <= liczba[i - 1]:
                rosnace = False
        if rosnace:
            print(liczba)
```
**Odpowiedź:** 2389, 23567, 123456789, 3468

## 5a i 5b

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
cena = [200, 200, 200]
najwyzsza = [200, 200, 200]
najnizsza = [10 ** 9, 10 ** 9, 10 ** 9]

with open("gielda.txt") as file:
    for line in file:
        zmiany = list(map(int, line.split()))
        for i in range(3):
            cena[i] += zmiany[i]
            najwyzsza[i] = max(najwyzsza[i], cena[i])
            najnizsza[i] = min(najnizsza[i], cena[i])

print("a)", "A:", cena[0], "B:", cena[1], "C:", cena[2])
print("b) max:", najwyzsza, "min:", najnizsza)
```
**Odpowiedź:** a) A – 221, B – 117, C – 198; b) max: A 264, B 210, C 223; min: A 167, B 62, C 97

## 5d

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
cena = [200, 200, 200]
krachy = 0
ostatni = []

with open("gielda.txt") as file:
    for line in file:
        zmiany = list(map(int, line.split()))
        for i in range(3):
            cena[i] += zmiany[i]
        if zmiany[0] < 0 and zmiany[1] < 0 and zmiany[2] < 0 and -sum(zmiany) > 20:
            krachy += 1
            ostatni = cena[:]

print(krachy, ostatni)
```
**Odpowiedź:** 6 krachów, ceny przy ostatnim krachu: A – 224, B – 163, C – 194

## 5e

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
cena = 200
rekord = 200
zmiany_rekordu = 0

with open("gielda.txt") as file:
    for line in file:
        cena += int(line.split()[0])
        if cena > rekord:
            rekord = cena
            zmiany_rekordu += 1

print(zmiany_rekordu)
```
**Odpowiedź:** 14 razy
