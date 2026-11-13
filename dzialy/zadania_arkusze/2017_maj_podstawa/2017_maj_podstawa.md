<h1 align="center">Matura 2017 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2017-maj-matura-stara-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2017-maj-matura-stara-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2017-maj-matura-stara-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2017-maj-matura-stara-podstawowa-odpowiedzi.pdf)

## 1.1

```py
def szyfruj(s, k, n):
    d = len(s)
    szyfr = list(s)
    i = 1  # numeracja od 1 jak w treści
    while i <= d - k:
        szyfr[i - 1], szyfr[i + k - 1] = szyfr[i + k - 1], szyfr[i - 1]
        i = i + n
    return "".join(szyfr)


print(szyfruj("ataknadranem", 4, 2))
print(szyfruj("maturazinformatyki", 3, 5))
print(szyfruj("stokrotka", 1, 2))
```
**Odpowiedź:** ntdkaaeranam, uatmrnziafarmotyki, tskoorkta

## 1.2 i 1.3

```py
def odszyfruj(szyfr, k, n):
    d = len(szyfr)
    s = list(szyfr)
    i = 1
    while i <= d - k - n:  # szukamy ostatniej zamiany wykonanej przy szyfrowaniu
        i = i + n
    while i >= 1:  # wykonujemy zamiany w odwrotnej kolejności
        s[i - 1], s[i + k - 1] = s[i + k - 1], s[i - 1]
        i = i - n
    return "".join(s)


print(odszyfruj("eiindaezotinwezssyktpo", 2, 2))
```
**Odpowiedź:** pieniadzetoniewszystko; luki: dopóki i ≤ d − k − n, i ← i − n

## 2.1 i 2.2

```py
def pierwsza(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i = i + 1
    return True


def blizniacze(a):
    if pierwsza(a) and (pierwsza(a - 2) or pierwsza(a + 2)):
        return "TAK"
    return "NIE"


for a in [17, 5, 31, 41, 49]:
    print(a, pierwsza(a), pierwsza(a + 2), pierwsza(a - 2), blizniacze(a))
```
**Odpowiedź:** 31 → TAK (29), 41 → TAK (43), 49 → NIE

## 4.1

```py
count = 0

with open("liczby.txt") as file:
    for line in file:
        a, b, c = map(int, line.split())
        if a < b < c:
            count += 1

print(count)
```
**Odpowiedź:** 139

## 4.2

```py
def nwd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


suma = 0

with open("liczby.txt") as file:
    for line in file:
        a, b, c = map(int, line.split())
        suma += nwd(nwd(a, b), c)

print(suma)
```
**Odpowiedź:** 1404

## 4.3

```py
sumy_cyfr = []

with open("liczby.txt") as file:
    for line in file:
        suma = 0
        for znak in line.strip():
            if znak != " ":
                suma += int(znak)
        sumy_cyfr.append(suma)

najwieksza = max(sumy_cyfr)
print(sumy_cyfr.count(35), najwieksza, sumy_cyfr.count(najwieksza))
```
**Odpowiedź:** 4 wiersze z sumą 35; największa suma cyfr 88, wystąpiła 2 razy

## 5.1

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
wynajmy = {}

with open("wynajem.txt") as file:
    next(file)  # pomijamy nagłówek
    for line in file:
        przyjazd, wyjazd, energia, woda, typ = line.strip().split("\t")
        wynajmy[typ] = wynajmy.get(typ, 0) + 1

print(max(wynajmy, key=wynajmy.get))
```
**Odpowiedź:** domki 2-osobowe

## 5.2

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
from datetime import date

doby = {}

with open("wynajem.txt") as file:
    next(file)
    for line in file:
        przyjazd, wyjazd, energia, woda, typ = line.strip().split("\t")
        liczba_dob = (date.fromisoformat(wyjazd) - date.fromisoformat(przyjazd)).days
        doby[typ] = doby.get(typ, 0) + liczba_dob

for typ in sorted(doby):
    print(typ, doby[typ])
```
**Odpowiedź:** 2 – 2985, 3 – 2816, 4 – 2944, 5 – 2997, 6 – 3244

## 5.3

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
from datetime import date

oplaty = {}

with open("wynajem.txt") as file:
    next(file)
    for line in file:
        przyjazd, wyjazd, energia, woda, typ = line.strip().split("\t")
        liczba_dob = (date.fromisoformat(wyjazd) - date.fromisoformat(przyjazd)).days
        czynsz = 10 * int(typ) * liczba_dob
        oplata = czynsz + float(energia.replace(",", ".")) + float(woda.replace(",", "."))
        oplaty[typ] = oplaty.get(typ, 0) + oplata

for typ in sorted(oplaty, key=oplaty.get, reverse=True):
    print(typ, round(oplaty[typ], 2))
```
**Odpowiedź:** 6 – 196 335,25 zł; 5 – 151 509,94 zł; 4 – 119 478,24 zł; 3 – 86 170,73 zł; 2 – 61 401,00 zł

## 5.4

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
media = [0] * 13

with open("wynajem.txt") as file:
    next(file)
    for line in file:
        przyjazd, wyjazd, energia, woda, typ = line.strip().split("\t")
        miesiac = int(przyjazd[5:7])
        media[miesiac] += float(energia.replace(",", ".")) + float(woda.replace(",", "."))

for miesiac in range(1, 13):
    print(miesiac, round(media[miesiac], 2))
```
**Odpowiedź:** 1: 1078,32; 2: 611,15; 3: 565,22; 4: 322,96; 5: 299,66; 6: 568,59; 7: 628,60; 8: 531,33; 9: 1045,12; 10: 813,25; 11: 1107,80; 12: 893,16 (wykres kolumnowy wykonuje się w arkuszu kalkulacyjnym)
