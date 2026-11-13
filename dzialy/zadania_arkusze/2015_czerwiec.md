<h1 align="center">2015 czerwiec</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2015-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2015-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2015-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2015-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1

```py
def na_u2(liczba, n=8):
    # dla liczby ujemnej zapisujemy 2^n + liczba (bit znaku ma wagę -2^(n-1))
    if liczba < 0:
        liczba += 2 ** n
    return bin(liczba)[2:].zfill(n)


def z_u2(zapis):
    n = len(zapis)
    return -int(zapis[0]) * 2 ** (n - 1) + int(zapis[1:], 2)


print(na_u2(93), na_u2(-42))
print(na_u2(z_u2("00101011") + z_u2("10011011")))
```
**Odpowiedź:** 93 = (01011101)U2, -42 = (11010110)U2, suma = (11000110)U2

## 1.2

```py
def przeciwna(a):
    # a - napis an-1 ... a1 a0, indeks i liczony od prawej (a0 to ostatni znak)
    n = len(a)
    b = ["0"] * n
    i = 0
    while a[n - 1 - i] == "0":       # krok 2
        b[n - 1 - i] = "0"
        i += 1
    b[n - 1 - i] = a[n - 1 - i]      # krok 3
    i += 1                           # krok 4
    while i < n:                     # krok 5
        if a[n - 1 - i] == "0":
            b[n - 1 - i] = "1"
        else:
            b[n - 1 - i] = "0"
        i += 1
    return "".join(b)


print(przeciwna("1111001001110000"))
# pętla z kroku 2 nie wykona się, gdy a0 = 1, np.:
print(przeciwna("0000000000000001"))
# 7 negacji w kroku 5: ostatnia jedynka na pozycji 8, czyli xxxxxxx100000000, np.:
print(przeciwna("0000000100000000"))
```
**Odpowiedź:** 0000110110010000; brak obrotów pętli z kroku 2: dowolna liczba postaci xxxxxxxxxxxxxxx1; 7 negacji: xxxxxxx100000000

## 2.1

```py
a, b = 5, 15
C = [2, 3, 5, 6, 9, 10, 11, 13, 14, 15, 17, 19, 20, 23, 24]

# dla a <= b: a, b, c tworzą triadę <=> b - a < c < b + a
triady = []
for c in C:
    if b - a < c < b + a:
        triady.append(c)

print(triady)
print(len(triady))
```
**Odpowiedź:** b - a < c, b + a > c; 6 wartości: 11, 13, 14, 15, 17, 19

## 2.2

```py
def ile_triad(c):
    # c[0] < c[1]; c1, c2, ck tworzą triadę <=> c2 - c1 < ck < c2 + c1
    minimum = c[1] - c[0]
    maksimum = c[1] + c[0]
    licznik = 0
    for ck in c:
        if minimum < ck < maksimum:
            licznik += 1
    return licznik


print(ile_triad([5, 15, 2, 3, 6, 9, 10, 11, 13, 14, 17, 19, 20, 23, 24]))
```
**Odpowiedź:** liczba elementów ck spełniających c2 - c1 < ck < c2 + c1 (dla przykładu z 2.1: 6)

## 4.1

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
from datetime import date, timedelta

miesiace = {}  # (rok, miesiąc) -> [kostka, orzech, miał]
dzien = date(2014, 10, 15)

with open("piastek.txt") as file:
    for line in file:
        if not line.strip():
            continue
        dostawa = list(map(int, line.split()))
        klucz = (dzien.year, dzien.month)
        if klucz not in miesiace:
            miesiace[klucz] = [0, 0, 0]
        for i in range(3):
            miesiace[klucz][i] += dostawa[i]
        dzien += timedelta(days=1)

for (rok, miesiac), tony in miesiace.items():
    print(rok, miesiac, *tony)
```
**Odpowiedź:** (kostka, orzech, miał) 10: 1742 1658 915, 11: 2756 2884 1750, 12: 2696 2749 1586, 1: 2990 2870 1646, 2: 2579 2651 1252, 3: 3332 3026 1360, 4: 1365 966 706

## 4.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
ceny = [685, 620, 380]  # kostka, orzech, miał [zł/t]
koszt = 0

with open("piastek.txt") as file:
    for line in file:
        dostawa = list(map(int, line.split()))
        for i in range(len(dostawa)):
            koszt += dostawa[i] * ceny[i]

print(koszt)
```
**Odpowiedź:** 25 880 280 zł

## 4.4, 4.5 i 4.6

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
from datetime import date, timedelta

dostawy = []
with open("piastek.txt") as file:
    for line in file:
        if line.strip():
            dostawy.append(list(map(int, line.split())))

spalanie = [200, 260, 320]      # dzienne zużycie: 200, 1,3 * 200, 1,6 * 200

magazyn = [80, 80, 80]
dni_palenia = [0, 0, 0]
podtrzymanie = 0
pierwszy_mial = None
dzien = date(2014, 10, 15)

for dostawa in dostawy:
    for i in range(3):
        magazyn[i] += dostawa[i]

    spalono = False
    for i in range(3):          # najpierw kostka, potem orzech, na końcu miał
        if magazyn[i] >= spalanie[i]:
            magazyn[i] -= spalanie[i]
            dni_palenia[i] += 1
            if i == 2 and pierwszy_mial is None:
                pierwszy_mial = dzien
            spalono = True
            break
    if not spalono:
        podtrzymanie += 1

    dzien += timedelta(days=1)

print("4.4", *dni_palenia)
print("4.5", pierwszy_mial)
print("4.6", podtrzymanie)
```
**Odpowiedź:** 4.4: kostka 87, orzech 64, miał 29 dni; 4.5: 2014-10-18; 4.6: 3 dni

## 5.1

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
wykroczenia = {}  # kod -> (nazwa, mandat, punkty)
mandaty = []      # (pesel, data, kod)
kierowcy = {}     # pesel -> (data prawa jazdy, miasto)

with open("wykroczenia.txt") as file:
    next(file)
    for line in file:
        kod, nazwa, mandat, punkty = line.strip().split("\t")
        wykroczenia[kod] = (nazwa, int(mandat), int(punkty))

with open("mandaty.txt") as file:
    next(file)
    for line in file:
        pesel, data, kod = line.strip().split("\t")
        mandaty.append((pesel, data, kod))

with open("kierowcy.txt") as file:
    next(file)
    for line in file:
        pesel, data_pj, miasto = line.strip().split("\t")
        kierowcy[pesel] = (data_pj, miasto)

ile = {}
for pesel, data, kod in mandaty:
    ile[kod] = ile.get(kod, 0) + 1

kod = max(ile, key=ile.get)
print(wykroczenia[kod][0], ile[kod])
```
**Odpowiedź:** Przekroczenie dopuszczalnej prędkości o 21 - 30 km/h, 77 razy

## 5.2

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
wykroczenia = {}  # kod -> (nazwa, mandat, punkty)
mandaty = []      # (pesel, data, kod)
kierowcy = {}     # pesel -> (data prawa jazdy, miasto)

with open("wykroczenia.txt") as file:
    next(file)
    for line in file:
        kod, nazwa, mandat, punkty = line.strip().split("\t")
        wykroczenia[kod] = (nazwa, int(mandat), int(punkty))

with open("mandaty.txt") as file:
    next(file)
    for line in file:
        pesel, data, kod = line.strip().split("\t")
        mandaty.append((pesel, data, kod))

with open("kierowcy.txt") as file:
    next(file)
    for line in file:
        pesel, data_pj, miasto = line.strip().split("\t")
        kierowcy[pesel] = (data_pj, miasto)

punkty = {}
for pesel, data, kod in mandaty:
    if kierowcy[pesel][0][:4] == "2013":
        punkty[pesel] = punkty.get(pesel, 0) + wykroczenia[kod][2]

for pesel in punkty:
    if punkty[pesel] > 20:
        print(pesel, punkty[pesel])
```
**Odpowiedź:** 81011159031 32, 80062465997 27, 81011807736 26

## 5.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
wykroczenia = {}  # kod -> (nazwa, mandat, punkty)
mandaty = []      # (pesel, data, kod)
kierowcy = {}     # pesel -> (data prawa jazdy, miasto)

with open("wykroczenia.txt") as file:
    next(file)
    for line in file:
        kod, nazwa, mandat, punkty = line.strip().split("\t")
        wykroczenia[kod] = (nazwa, int(mandat), int(punkty))

with open("mandaty.txt") as file:
    next(file)
    for line in file:
        pesel, data, kod = line.strip().split("\t")
        mandaty.append((pesel, data, kod))

with open("kierowcy.txt") as file:
    next(file)
    for line in file:
        pesel, data_pj, miasto = line.strip().split("\t")
        kierowcy[pesel] = (data_pj, miasto)

for kod in wykroczenia:
    if "naruszenie zakazu" in wykroczenia[kod][0].lower():
        print(wykroczenia[kod][0])
```
**Odpowiedź:** 9 wykroczeń, np. Naruszenie zakazu postoju przed lub za przejazdem kolejowym, Naruszenie zakazu wyprzedzania na skrzyżowaniach, …

## 5.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
wykroczenia = {}  # kod -> (nazwa, mandat, punkty)
mandaty = []      # (pesel, data, kod)
kierowcy = {}     # pesel -> (data prawa jazdy, miasto)

with open("wykroczenia.txt") as file:
    next(file)
    for line in file:
        kod, nazwa, mandat, punkty = line.strip().split("\t")
        wykroczenia[kod] = (nazwa, int(mandat), int(punkty))

with open("mandaty.txt") as file:
    next(file)
    for line in file:
        pesel, data, kod = line.strip().split("\t")
        mandaty.append((pesel, data, kod))

with open("kierowcy.txt") as file:
    next(file)
    for line in file:
        pesel, data_pj, miasto = line.strip().split("\t")
        kierowcy[pesel] = (data_pj, miasto)

liczba = {}
kwota = {}
for pesel, data, kod in mandaty:
    miesiac = int(data[5:7])
    liczba[miesiac] = liczba.get(miesiac, 0) + 1
    kwota[miesiac] = kwota.get(miesiac, 0) + wykroczenia[kod][1]

miesiac = min(liczba, key=liczba.get)
print(miesiac, liczba[miesiac], kwota[miesiac])
```
**Odpowiedź:** luty (2): 63 mandaty na łączną kwotę 12 750 zł

## 5.5

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
wykroczenia = {}  # kod -> (nazwa, mandat, punkty)
mandaty = []      # (pesel, data, kod)
kierowcy = {}     # pesel -> (data prawa jazdy, miasto)

with open("wykroczenia.txt") as file:
    next(file)
    for line in file:
        kod, nazwa, mandat, punkty = line.strip().split("\t")
        wykroczenia[kod] = (nazwa, int(mandat), int(punkty))

with open("mandaty.txt") as file:
    next(file)
    for line in file:
        pesel, data, kod = line.strip().split("\t")
        mandaty.append((pesel, data, kod))

with open("kierowcy.txt") as file:
    next(file)
    for line in file:
        pesel, data_pj, miasto = line.strip().split("\t")
        kierowcy[pesel] = (data_pj, miasto)

ukarani = set()
for pesel, data, kod in mandaty:
    ukarani.add(pesel)

miasta = {}
bez_mandatu = 0
for pesel in kierowcy:
    if pesel not in ukarani:
        bez_mandatu += 1
        miasto = kierowcy[pesel][1]
        miasta[miasto] = miasta.get(miasto, 0) + 1

print(bez_mandatu, max(miasta, key=miasta.get))
```
**Odpowiedź:** 190 kierowców, najwięcej z miasta Warszawa

## 6.1

```py
def sumy(liczba):
    # pozycje liczymy od prawej: cyfra jednostek ma pozycję 0
    parzyste = nieparzyste = 0
    for pozycja, cyfra in enumerate(reversed(liczba)):
        if pozycja % 2 == 0:
            parzyste += int(cyfra)
        else:
            nieparzyste += int(cyfra)
    return parzyste, nieparzyste


with open("kody.txt") as file, open("kody1.txt", "w") as wynik:
    for line in file:
        parzyste, nieparzyste = sumy(line.strip())
        wynik.write(f"{parzyste} {nieparzyste}\n")
```
**Odpowiedź:** plik kody1.txt (pierwsze wiersze: 10 13, 11 17, 17 16, …)

## 6.2

```py
kody = {}
with open("cyfra_kodkreskowy.txt") as file:
    next(file)
    for line in file:
        cyfra, kod = line.split()
        kody[cyfra] = kod


def sumy(liczba):
    # pozycje liczymy od prawej: cyfra jednostek ma pozycję 0
    parzyste = nieparzyste = 0
    for pozycja, cyfra in enumerate(reversed(liczba)):
        if pozycja % 2 == 0:
            parzyste += int(cyfra)
        else:
            nieparzyste += int(cyfra)
    return parzyste, nieparzyste


def cyfra_kontrolna(liczba):
    parzyste, nieparzyste = sumy(liczba)
    return str((10 - (3 * parzyste + nieparzyste) % 10) % 10)


with open("kody.txt") as file, open("kody2.txt", "w") as wynik:
    for line in file:
        k = cyfra_kontrolna(line.strip())
        wynik.write(f"{k} {kody[k]}\n")
```
**Odpowiedź:** plik kody2.txt (pierwsze wiersze: 7 10101011101110, 0 10101110111010, 3 11101110101010, …)

## 6.3

```py
kody = {}
with open("cyfra_kodkreskowy.txt") as file:
    next(file)
    for line in file:
        cyfra, kod = line.split()
        kody[cyfra] = kod


def sumy(liczba):
    # pozycje liczymy od prawej: cyfra jednostek ma pozycję 0
    parzyste = nieparzyste = 0
    for pozycja, cyfra in enumerate(reversed(liczba)):
        if pozycja % 2 == 0:
            parzyste += int(cyfra)
        else:
            nieparzyste += int(cyfra)
    return parzyste, nieparzyste


def cyfra_kontrolna(liczba):
    parzyste, nieparzyste = sumy(liczba)
    return str((10 - (3 * parzyste + nieparzyste) % 10) % 10)


with open("kody.txt") as file, open("kody3.txt", "w") as wynik:
    for line in file:
        liczba = line.strip()
        kod = "11011010"                                   # START
        for cyfra in liczba:
            kod += kody[cyfra]
        kod += kody[cyfra_kontrolna(liczba)] + "11010110"  # cyfra kontrolna i STOP
        wynik.write(kod + "\n")
```
**Odpowiedź:** plik kody3.txt (pierwszy wiersz to kod liczby 764321, taki jak w przykładzie z treści zadania)
