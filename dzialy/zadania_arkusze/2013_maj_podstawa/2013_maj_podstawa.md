<h1 align="center">Matura 2013 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2013-maj-matura-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2013-maj-matura-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2013-maj-matura-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2013-maj-matura-podstawowa-odpowiedzi.pdf)

## 1a

```py
def sposob1(a, x):
    mnozenia = 0
    dodawania = 0
    W = 0
    i = 0
    while i <= 4:
        sk = a[i]
        j = 4 - i
        while j > 0:
            sk = sk * x
            mnozenia += 1
            j = j - 1
        W = W + sk
        dodawania += 1
        i = i + 1
    return W, mnozenia, dodawania


print(sposob1([1, 2, 3, 4, 5], 2))
```
**Odpowiedź:** liczba mnożeń – 10, liczba dodawań – 5

## 1b

```py
def sposob2(a, x):  # schemat Hornera
    mnozenia = 0
    dodawania = 0
    W = a[0]
    i = 0
    while i < 4:
        i = i + 1
        W = W * x + a[i]
        mnozenia += 1
        dodawania += 1
    return W, mnozenia, dodawania


print(sposob2([1, 2, 3, 4, 5], 2))
```
**Odpowiedź:** a) i ← i + 1; b) W ← W * x + a[i]; liczba mnożeń – 4, liczba dodawań – 4

## 2a i 2c

```py
def algorytm(N):
    wypisane = []
    d = 2
    while N >= d:
        if N % d == 0:
            wypisane.append(d)
            N = N // d
        else:
            d = d + 1
    return wypisane


for N in [36, 120, 675]:
    print(N, algorytm(N))

print(len(algorytm(2 ** 100)))
```
**Odpowiedź:** a) 36 → 2, 2, 3, 3; 120 → 2, 2, 2, 3, 5; 675 → 3, 3, 3, 5, 5; b) czynniki pierwsze liczby N; c) dla N = 2<sup>100</sup> zostanie wypisanych 100 liczb

## 2d

```py
def czynniki_pary(N):
    a = 2
    b = 0
    while N >= a:
        if N % a == 0:
            b = b + 1
            N = N // a
        else:
            if b > 0:
                print(a, b)
            a = a + 1
            b = 0
    print(a, b)


czynniki_pary(225)
czynniki_pary(784)
```
**Odpowiedź:** 225 → (3, 2), (5, 2); 784 → (2, 4), (7, 2)

## 4a

```py
parzyste = 0

with open("napisy.txt") as file:
    for line in file:
        napis = line.strip()
        if len(napis) % 2 == 0:
            parzyste += 1

print(parzyste)
```
**Odpowiedź:** 504

## 4b

```py
count = 0

with open("napisy.txt") as file:
    for line in file:
        napis = line.strip()
        if napis.count("0") == napis.count("1"):
            count += 1

print(count)
```
**Odpowiedź:** 110

## 4c

```py
zera = 0
jedynki = 0

with open("napisy.txt") as file:
    for line in file:
        napis = line.strip()
        if napis.count("0") == len(napis):
            zera += 1
        if napis.count("1") == len(napis):
            jedynki += 1

print("same zera:", zera, "same jedynki:", jedynki)
```
**Odpowiedź:** same zera – 32, same jedynki – 50

## 4d

```py
dlugosci = [0] * 17

with open("napisy.txt") as file:
    for line in file:
        napis = line.strip()
        dlugosci[len(napis)] += 1

for k in range(2, 17):
    print(k, dlugosci[k])
```
**Odpowiedź:** 2: 43, 3: 38, 4: 37, 5: 57, 6: 53, 7: 68, 8: 78, 9: 103, 10: 83, 11: 90, 12: 86, 13: 81, 14: 68, 15: 59, 16: 56

## 5a

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
with open("Hobby.txt") as file:
    for line in file:
        id_hobby, hobby = line.split()
        if hobby[0] == "k":
            print(hobby)
```
**Odpowiedź:** kulturystyka, kolekcjonerstwo, krzyżówki

## 5b

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
hobby = {}

with open("Hobby.txt") as file:
    for line in file:
        id_hobby, nazwa = line.split()
        hobby[id_hobby] = nazwa

osoby = set()
with open("Ma_Hobby.txt") as file:
    for line in file:
        id_wpisu, id_osoba, id_hobby = line.split()
        if hobby[id_hobby] == "majsterkowanie":
            osoby.add(id_osoba)

print(len(osoby))
```
**Odpowiedź:** 7 osób

## 5c

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
hobby = {}
osoby = {}

with open("Hobby.txt") as file:
    for line in file:
        id_hobby, nazwa = line.split()
        hobby[id_hobby] = nazwa

with open("Osoby.txt", encoding="cp1250") as file:
    for line in file:
        id_osoba, imie, nazwisko = line.split()
        osoby[id_osoba] = (nazwisko, imie)

wynik = set()
with open("Ma_Hobby.txt") as file:
    for line in file:
        id_wpisu, id_osoba, id_hobby = line.split()
        if hobby[id_hobby] == "programowanie":
            wynik.add(osoby[id_osoba])

for nazwisko, imie in sorted(wynik):
    print(imie, nazwisko)
```
**Odpowiedź:** Zofia Augustowska, Sebastian Helski, Kornel Henrykowski, Jerzy Kielecki, Ewelia Lubelska, Wiktor Lubelski, Wiktor Pilski, Horacy Warszawski

## 5d

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
osoby = {}
hobby_osoby = {}

with open("Osoby.txt", encoding="cp1250") as file:
    for line in file:
        id_osoba, imie, nazwisko = line.split()
        osoby[id_osoba] = (nazwisko, imie)

with open("Ma_Hobby.txt") as file:
    for line in file:
        id_wpisu, id_osoba, id_hobby = line.split()
        if id_osoba not in hobby_osoby:
            hobby_osoby[id_osoba] = set()
        hobby_osoby[id_osoba].add(id_hobby)

wynik = []
for id_osoba in hobby_osoby:
    if len(hobby_osoby[id_osoba]) > 4:
        wynik.append(osoby[id_osoba])

for nazwisko, imie in sorted(wynik):
    print(nazwisko, imie)
```
**Odpowiedź:** Augustowska Anna, Augustowska Justyna, Augustowska Zofia, Augustowski Adam, Augustowski Kornel, Augustowski Sebastian, Augustowski Tomasz, Katowicka Paulina, Katowicki Grzegorz, Nadolicki Jan, Nyska Ewelina, Piotrkowska Katarzyna, Piotrkowski Andrzej, Polkowicka Dominika

## 5e

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
hobby = {}
ile_osob = {}

with open("Hobby.txt") as file:
    for line in file:
        id_hobby, nazwa = line.split()
        hobby[id_hobby] = nazwa

with open("Ma_Hobby.txt") as file:
    for line in file:
        id_wpisu, id_osoba, id_hobby = line.split()
        ile_osob[id_hobby] = ile_osob.get(id_hobby, 0) + 1

najwiecej = max(ile_osob.values())
for id_hobby in ile_osob:
    if ile_osob[id_hobby] == najwiecej:
        print(hobby[id_hobby])
```
**Odpowiedź:** agroturystyka, broń, kolekcjonerstwo, malarstwo, szydełkowanie

## 6a

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
fundusze = "ABCDEFGHIJKL"
sumy = [0] * 12
dni = 0

with open("historia.txt") as file:
    for line in file:
        dane = line.strip().replace(",", ".").split(";")
        ceny = list(map(float, dane[1:]))
        for i in range(12):
            sumy[i] += ceny[i]
        dni += 1

for i in range(12):
    print(fundusze[i], round(sumy[i] / dni, 2))
```
**Odpowiedź:** A 36,54; B 37,14; C 38,30; D 39,00; E 39,28; F 39,56; G 33,40; H 33,44; I 33,49; J 38,34; K 38,42; L 38,49

## 6b

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
count = 0

with open("historia.txt") as file:
    for line in file:
        dane = line.strip().replace(",", ".").split(";")
        ceny = list(map(float, dane[1:]))
        if min(ceny) > 33:
            count += 1

print(count)
```
**Odpowiedź:** 158

## 6c

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
wystapienia = {}

with open("historia.txt") as file:
    for line in file:
        dane = line.strip().split(";")
        for cena in dane[1:]:
            wystapienia[cena] = wystapienia.get(cena, 0) + 1

najczestsza = max(wystapienia, key=wystapienia.get)
print(najczestsza, wystapienia[najczestsza])
```
**Odpowiedź:** 42,98 – wystąpiła 8 razy

## 6d

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
fundusze = "ABCDEFGHIJKL"
najnizsza = [10 ** 9] * 12
najwyzsza = [0] * 12

with open("historia.txt") as file:
    for line in file:
        dane = line.strip().replace(",", ".").split(";")
        ceny = list(map(float, dane[1:]))
        for i in range(12):
            najnizsza[i] = min(najnizsza[i], ceny[i])
            najwyzsza[i] = max(najwyzsza[i], ceny[i])

for i in range(12):
    print(fundusze[i], najnizsza[i], najwyzsza[i])
```
**Odpowiedź:** (min, max) A 20,82 50,90; B 21,21 51,62; C 21,92 53,12; D 18,76 58,66; E 18,94 58,96; F 19,12 59,26; G 16,04 48,15; H 16,08 48,17; I 16,12 48,19; J 20,33 50,23; K 20,41 50,23; L 20,50 50,23 (wykres liniowy wykonuje się w arkuszu kalkulacyjnym)
