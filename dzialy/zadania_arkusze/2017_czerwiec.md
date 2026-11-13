<h1 align="center">Matura 2017 — czerwiec (termin dodatkowy), poziom rozszerzony</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2017-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2017-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2017-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2017-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

```py
import math


def sitko(n):
    czyjest = [False] * (n + 1)   # indeksy 1..n
    j = 1
    while j * j < n:
        j += 1
    wykonania = {}                # i -> liczba wykonań wiersza (*)
    for i in range(2, j + 1):
        kw = i * i
        poz = kw
        wykonania[i] = 0
        while poz <= n:
            czyjest[poz] = True   # (*)
            wykonania[i] += 1
            poz += kw
    return j, czyjest, wykonania


def czy_kwadratowa(k, czyjest):
    # k = a*b^2 + c*d^2 (b, d > 1) <=> k = x + (k - x), gdzie czyjest[x] i czyjest[k - x]
    for x in range(1, k):
        if czyjest[x] and czyjest[k - x]:
            return True
    return False


# 1.1
for n, k in [(10, 9), (10, 5), (100, 10), (100, 75)]:
    j, czyjest, wykonania = sitko(n)
    print(n, k, j, czyjest[k])

# 1.2
j, czyjest, wykonania = sitko(100)
for i in [2, 3, 5, 9]:
    print(i, wykonania[i])
razem = sum(wykonania.values())
print("razem:", razem)
print("ln 100:", math.log(100) > razem)
print("100:", 100 > razem)
print("100 * (1/2^2 + ... + 1/10^2):", 100 * sum(1 / i ** 2 for i in range(2, 11)) > razem)
print("sqrt(100):", math.sqrt(100) > razem)

# 1.3
print([k for k in range(1, 101) if czy_kwadratowa(k, czyjest)])
```
**Odpowiedź:** 1.1: (10, 9): j = 4, prawda; (10, 5): 4, fałsz; (100, 10): 10, fałsz; (100, 75): 10, prawda. 1.2: i = 2: 25, 3: 11, 5: 4, 9: 1; większe od łącznej liczby wykonań: 100 oraz 100 · (1/2² + … + 1/10²). 1.3: funkcja `czy_kwadratowa`.

## 2.1 i 2.2

```py
def REG(w, n):
    if n == 1:
        return 1
    m = n // 2                      # dla n nieparzystego to (n - 1) / 2
    for i in range(m):              # w[i] porównujemy z w[n + 1 - i] (tu indeksy od 0)
        if w[i] != w[n - 1 - i]:
            return 0
    return 1 + REG(w[:m], m)


# 2.1
for w in ["BABBAB", "BABBBB", "BAAAAB", "B", "BBB", "AAAAAAAA"]:
    print(w, REG(w, len(w)))
```
**Odpowiedź:** 2.1: 3, 0, 1, 1, 2, 4. 2.2: wynikiem jest 1; w[i] ≠ w[n + 1 - i]; wynikiem jest 1 + REG(x, m).

## 3.1 i 3.2

```py
A = int("00010110100", 2)
B = int("000330", 4)
C = int("078", 16)

# 3.1
print(A, B, C)
print(A % 6 == 0 and B % 6 == 0 and C % 6 == 0)
print((A - B) % 60 == 0 and (A - C) % 60 == 0 and (B - C) % 60 == 0)

# 3.2 - szukamy wartości pasujących do wzorców; po tym samym czasie t od pierwszego odczytu
# wszystkie zegary przesunęły się o tyle samo minut (pomijamy przejście przez północ)
def pasuje(liczba, wzorzec, podstawa):
    cyfry = "0123456789ABCDEF"
    zapis = ""
    for _ in range(len(wzorzec)):
        zapis = cyfry[liczba % podstawa] + zapis
        liczba //= podstawa
    if liczba > 0:
        return False
    for z, w in zip(zapis, wzorzec):
        if w != "X" and z != w:
            return False
    return True


for t in range(0, 24 * 60):
    if pasuje(A + t, "000110100XX", 2) and pasuje(B + t, "001XX2", 4) and pasuje(C + t, "X96", 16):
        print(bin(A + t)[2:].zfill(11), A + t)
        print(B + t, C + t)
```
**Odpowiedź:** 3.1: F, P, P (A = 180, B = 60, C = 120). 3.2: A: 00011010010, B: 001122, C: 096.

## 4.1

```py
def czy_pierwsza(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


licznik = 0

with open("punkty.txt") as file:
    for line in file:
        x, y = map(int, line.split())
        if czy_pierwsza(x) and czy_pierwsza(y):
            licznik += 1

print(licznik)
```
**Odpowiedź:** 18

## 4.2

```py
licznik = 0

with open("punkty.txt") as file:
    for line in file:
        x, y = line.split()
        # cyfropodobne - zbiory użytych cyfr są równe (porównujemy zbiory, nie listy)
        if set(x) == set(y):
            licznik += 1

print(licznik)
```
**Odpowiedź:** 5

## 4.3

```py
import math

punkty = []
with open("punkty.txt") as file:
    for line in file:
        x, y = map(int, line.split())
        punkty.append((x, y))

najwieksza = -1  # kwadrat odległości - porównujemy bez pierwiastka
for i in range(len(punkty)):
    for j in range(i + 1, len(punkty)):
        x1, y1 = punkty[i]
        x2, y2 = punkty[j]
        kwadrat = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if kwadrat > najwieksza:
            najwieksza = kwadrat
            para = (punkty[i], punkty[j])

print(para[0], para[1], round(math.sqrt(najwieksza)))
```
**Odpowiedź:** (9901, 593) i (35, 9583), odległość 13348

## 4.4

```py
wewnatrz = na_boku = na_zewnatrz = 0

with open("punkty.txt") as file:
    for line in file:
        x, y = map(int, line.split())
        # kwadrat K: -5000 <= x, y <= 5000 (bok 10000, środek w (0, 0))
        if abs(x) < 5000 and abs(y) < 5000:
            wewnatrz += 1
        elif abs(x) <= 5000 and abs(y) <= 5000:
            na_boku += 1
        else:
            na_zewnatrz += 1

print(wewnatrz, na_boku, na_zewnatrz)
```
**Odpowiedź:** a) 249, b) 2, c) 749

## 5.1

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
def amortyzacja(rok, cena, przebieg):
    czasowa = cena * 5 * (2017 - rok) // 100
    zuzycie = cena * 2 * (przebieg // 100000) // 100
    return czasowa, zuzycie


najmniejsza = None
with open("transport.txt") as file:
    next(file)
    for line in file:
        model, rok, cena, nr, przebieg, remont = line.strip().split("\t")
        czasowa, zuzycie = amortyzacja(int(rok), int(cena), int(przebieg))
        wartosc = int(cena) - czasowa - zuzycie

        # a)
        if nr == "ERA 092 TR":
            print(model, wartosc, czasowa, zuzycie)

        # b)
        if najmniejsza is None or wartosc < najmniejsza:
            najmniejsza = wartosc
            najtanszy = (model, nr, wartosc)

print(*najtanszy)
```
**Odpowiedź:** a) wartość 43 610 zł, amortyzacja czasowa 40 050 zł, z przebiegu 5 340 zł; b) DAF LF45, ERA 132 TR, 17 390 zł

## 5.2

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
liczba = {}
suma_przebiegow = {}

with open("transport.txt") as file:
    next(file)
    for line in file:
        model, rok, cena, nr, przebieg, remont = line.strip().split("\t")
        marka = model.split()[0]
        liczba[marka] = liczba.get(marka, 0) + 1
        suma_przebiegow[marka] = suma_przebiegow.get(marka, 0) + int(przebieg)

for marka in sorted(liczba):
    print(marka, liczba[marka], round(suma_przebiegow[marka] / liczba[marka]))
```
**Odpowiedź:** DAF 30 / 273 240, Iveco 12 / 657 434, MAN 18 / 289 637, Mercedes 17 / 486 546, Renault 17 / 519 936, Scania 17 / 557 118, Volvo 23 / 307 130 (+ wykres kolumnowy)

## 5.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
zestawienie = {}  # (rok, marka) -> liczba samochodów
marki = set()

with open("transport.txt") as file:
    next(file)
    for line in file:
        model, rok, cena, nr, przebieg, remont = line.strip().split("\t")
        marka = model.split()[0]
        marki.add(marka)
        zestawienie[(int(rok), marka)] = zestawienie.get((int(rok), marka), 0) + 1

marki = sorted(marki)
print("rok", *marki)
for rok in range(2006, 2016):
    print(rok, *[zestawienie.get((rok, marka), 0) for marka in marki])
```
**Odpowiedź:** np. 2006: Iveco 5; 2009: DAF 2, Iveco 2, MAN 4, Mercedes 4, Renault 2, Scania 4, Volvo 8; … (pełna tabela z programu)

## 5.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
from datetime import date

samochody = []

with open("transport.txt") as file:
    next(file)
    for line in file:
        model, rok, cena, nr, przebieg, remont = line.strip().split("\t")
        r, m, d = map(int, remont.split("-"))
        dni = (date(2017, 1, 1) - date(r, m, d)).days
        samochody.append((dni, model, nr))

samochody.sort(reverse=True)
for dni, model, nr in samochody[:4]:
    print(model, nr, dni)
```
**Odpowiedź:** Mercedes Atego ERA 112 TR 722, Iveco Strails ERA 212 TR 708, Iveco Strails ERA 213 TR 708, Iveco Trakker Euro5 ERA 214 TR 708
