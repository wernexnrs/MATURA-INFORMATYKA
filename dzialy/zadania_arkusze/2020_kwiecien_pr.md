<h1 align="center">2020 Kwiecień (próbna)</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2020-kwiecien-probna-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2020-kwiecien-probna-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2020-kwiecien-probna-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2020-kwiecien-probna-rozszerzona-odpowiedzi.pdf)

## 1.1

```py
# Liczba wywołań Rek zależy tylko od tego, w którą połowę przedziału p..k pójdzie rekurencja.
# Sprawdzamy obie możliwości w każdym kroku i wybieramy najmniejszą / największą liczbę wywołań.
def wywolania(p, k, wybierz):
    if p < k:
        s = (p + k) // 2
        return 1 + wybierz(wywolania(p, s, wybierz), wywolania(s + 1, k, wybierz))
    return 1


print("najmniejsza:", wywolania(5, 14, min))
print("największa:", wywolania(5, 14, max))
```

**Odpowiedź:** najmniejsza liczba wywołań 4, największa 5

## 1.2

```py
T = [1, 5, 8, 10, 12, 14, 19, 20, 23, 30, 38]


def Rek(x, p, k):
    print(f"Rek({x},{p},{k})")
    if p < k:
        s = (p + k) // 2
        if T[s - 1] >= x:  # tablica w treści jest numerowana od 1
            return Rek(x, p, s)
        else:
            return Rek(x, s + 1, k)
    else:
        if T[p - 1] == x:
            return p
        return -1


print("wynik:", Rek(7, 1, 11))
```

**Odpowiedź:** Rek(7,1,6), Rek(7,1,3), Rek(7,3,3) (1.3: D. logarytmiczna)

## 2.1 i 2.2

```py
def moda(n, T):
    najwiecej = 0
    for i in range(n):
        ile = 0
        for j in range(n):
            if T[j] == T[i]:
                ile += 1
        if ile > najwiecej:
            najwiecej = ile
            m = T[i]
    return m


print(moda(9, [2, 3, 4, 2, 3, 5, 2, 100, 67]))
# 2.1 - przykład 10-elementowego zestawu z trzema modami (maksymalnie mód może być 4)
print([1, 1, 1, 2, 2, 2, 3, 3, 3, 4])
```

**Odpowiedź:** 2.1: maksymalnie 4 mody, np. 1 1 1 2 2 2 3 3 3 4; 2.2: algorytm w kodzie (dla przykładu z treści moda = 2)

## 4.1

```py
with open("dane4.txt") as file:
    liczby = [int(line) for line in file]

luki = []
for i in range(1, len(liczby)):
    luki.append(abs(liczby[i] - liczby[i - 1]))

print(min(luki))
print(max(luki))
```

**Odpowiedź:** najmniejsza 1, największa 1056392131

## 4.2

```py
with open("dane4.txt") as file:
    liczby = [int(line) for line in file]

najdluzszy = 2
dlugosc = 2  # każde dwa kolejne elementy tworzą fragment regularny
poczatek, koniec = liczby[0], liczby[1]

for i in range(2, len(liczby)):
    if abs(liczby[i] - liczby[i - 1]) == abs(liczby[i - 1] - liczby[i - 2]):
        dlugosc += 1
    else:
        dlugosc = 2
    if dlugosc > najdluzszy:
        najdluzszy = dlugosc
        poczatek = liczby[i - dlugosc + 1]
        koniec = liczby[i]

print(najdluzszy, poczatek, koniec)
```

**Odpowiedź:** długość 17, początek 193134524, koniec 223545714

## 4.3

```py
with open("dane4.txt") as file:
    liczby = [int(line) for line in file]

krotnosc = {}
for i in range(1, len(liczby)):
    luka = abs(liczby[i] - liczby[i - 1])
    krotnosc[luka] = krotnosc.get(luka, 0) + 1

najwiecej = max(krotnosc.values())
print(najwiecej)
for luka in krotnosc:
    if krotnosc[luka] == najwiecej:
        print(luka)
```

**Odpowiedź:** krotność 31, luki 149 i 11

## 5.1

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
chlodne = cieple_bez_deszczu = cieple_z_deszczem = 0

with open("pogoda.txt") as file:
    file.readline()  # nagłówek
    for line in file:
        temperatura, opady = line.split()
        temperatura = float(temperatura.replace(",", "."))
        opady = float(opady.replace(",", "."))
        if temperatura <= 15:
            chlodne += 1
        elif opady <= 0.6:
            cieple_bez_deszczu += 1
        else:
            cieple_z_deszczem += 1

print(chlodne, cieple_bez_deszczu, cieple_z_deszczem)
```

**Odpowiedź:** 88 dni (temperatura ≤ 15°C), 73 dni (temperatura > 15°C i opady ≤ 0,6), 22 dni (temperatura > 15°C i opady > 0,6)

## 5.2

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
import math
from datetime import date, timedelta

with open("pogoda.txt") as file:
    file.readline()
    dane = []
    for line in file:
        temperatura, opady = line.split()
        dane.append((float(temperatura.replace(",", ".")), float(opady.replace(",", "."))))

POJEMNOSC = 25000
stan = POJEMNOSC  # 31 marca o 21:00 zbiornik był pełen
dzien = date(2015, 4, 1)
dolewki = []  # (data, ile litrów dolano)

for temperatura, opady in dane:
    if opady > 0:
        stan = min(POJEMNOSC, stan + math.ceil(700 * opady))
    else:
        stan -= math.ceil(0.0003 * temperatura ** 1.5 * stan)
    if temperatura > 15 and opady <= 0.6:
        potrzeba = 12000 if temperatura <= 30 else 24000
        if stan < potrzeba:
            dolewki.append((dzien, POJEMNOSC - stan))
            stan = POJEMNOSC
        stan -= potrzeba
    dzien += timedelta(days=1)

print(dolewki[0])
print("razem dolano:", sum(ile for d, ile in dolewki))
```

**Odpowiedź:** 6 maja 2015 r., 13172 litrów (łącznie dolano 743 427 litrów)

## 5.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
import math
from datetime import date, timedelta

with open("pogoda.txt") as file:
    file.readline()
    dane = []
    for line in file:
        temperatura, opady = line.split()
        dane.append((float(temperatura.replace(",", ".")), float(opady.replace(",", "."))))

POJEMNOSC = 25000
stan = POJEMNOSC
dzien = date(2015, 4, 1)

for temperatura, opady in dane:
    if opady > 0:
        stan = min(POJEMNOSC, stan + math.ceil(700 * opady))
    else:
        stan -= math.ceil(0.0003 * temperatura ** 1.5 * stan)
    if temperatura > 15 and opady <= 0.6:
        potrzeba = 12000 if temperatura <= 30 else 24000
        if stan < potrzeba:
            stan = POJEMNOSC
        stan -= potrzeba
    print(dzien, stan)  # stan o 21:00 - dane do wykresu liniowego
    dzien += timedelta(days=1)
```

**Odpowiedź:** wykres liniowy stanu zbiornika o 21:00 w kolejnych dniach (od 2015-04-01 do 2015-09-30)

## 5.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
import math
from datetime import date, timedelta

with open("pogoda.txt") as file:
    file.readline()
    dane = []
    for line in file:
        temperatura, opady = line.split()
        dane.append((float(temperatura.replace(",", ".")), float(opady.replace(",", "."))))

POJEMNOSC = 25000
stan = POJEMNOSC
dzien = date(2015, 4, 1)
dolano = {miesiac: 0 for miesiac in range(4, 10)}

for temperatura, opady in dane:
    if opady > 0:
        stan = min(POJEMNOSC, stan + math.ceil(700 * opady))
    else:
        stan -= math.ceil(0.0003 * temperatura ** 1.5 * stan)
    if temperatura > 15 and opady <= 0.6:
        potrzeba = 12000 if temperatura <= 30 else 24000
        if stan < potrzeba:
            dolano[dzien.month] += POJEMNOSC - stan
            stan = POJEMNOSC
        stan -= potrzeba
    dzien += timedelta(days=1)

for miesiac, litry in dolano.items():
    m3 = math.ceil(litry / 1000)
    print(miesiac, litry, m3, round(m3 * 11.74, 2))
```

**Odpowiedź:** kwiecień 0 zł, maj 164,36 zł, czerwiec 1056,60 zł, lipiec 2559,32 zł, sierpień 3651,14 zł, wrzesień 1326,62 zł

## 6.1

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
def wczytaj(nazwa):
    with open(nazwa) as file:
        file.readline()  # nagłówek
        return [line.rstrip("\n").split("\t") for line in file if line.strip()]


klienci = wczytaj("klienci.txt")
zabiegi = wczytaj("zabiegi.txt")
wizyty = wczytaj("wizytydane.txt")
wizyty_zabiegi = wczytaj("wizytyzabiegi.txt")

cena = {z[0]: int(z[3]) for z in zabiegi}

for id_klienta, imie, nazwisko in klienci:
    if imie == "Alicja" and nazwisko == "Kowalska":
        szukany = id_klienta

jej_wizyty = set(w[0] for w in wizyty if w[3] == szukany)

suma = 0
for id_wizyty, kod in wizyty_zabiegi:
    if id_wizyty in jej_wizyty:
        suma += cena[kod]

print(suma)
```

**Odpowiedź:** 3841

## 6.2

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
def wczytaj(nazwa):
    with open(nazwa) as file:
        file.readline()
        return [line.rstrip("\n").split("\t") for line in file if line.strip()]


klienci = wczytaj("klienci.txt")
wizyty = wczytaj("wizytydane.txt")

ile_wizyt = {}
for id_wizyty, data, nr, id_klienta in wizyty:
    ile_wizyt[id_klienta] = ile_wizyt.get(id_klienta, 0) + 1

najczesciej = max(ile_wizyt, key=ile_wizyt.get)
for id_klienta, imie, nazwisko in klienci:
    if id_klienta == najczesciej:
        print(imie, nazwisko, ile_wizyt[id_klienta])
```

**Odpowiedź:** Johan Bor, 20 wizyt

## 6.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
def wczytaj(nazwa):
    with open(nazwa) as file:
        file.readline()
        return [line.rstrip("\n").split("\t") for line in file if line.strip()]


zabiegi = wczytaj("zabiegi.txt")
wizyty = wczytaj("wizytydane.txt")
wizyty_zabiegi = wczytaj("wizytyzabiegi.txt")

for z in zabiegi:
    if z[2] == "Magia Hawajow":
        kod_hawaje = z[0]

data_wizyty = {w[0]: w[1] for w in wizyty}

daty = []
for id_wizyty, kod in wizyty_zabiegi:
    if kod == kod_hawaje:
        daty.append(data_wizyty[id_wizyty])

print(len(daty))
for data in sorted(daty, reverse=True):
    print(data)
```

**Odpowiedź:** 21 wizyt: 2018-01-25, 2018-01-20, 2018-01-18, 2018-01-12, 2018-01-10, 2018-01-04, 2018-01-04, 2018-01-03, 2017-12-22, … , 2017-11-13

## 6.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
def wczytaj(nazwa):
    with open(nazwa) as file:
        file.readline()
        return [line.rstrip("\n").split("\t") for line in file if line.strip()]


zabiegi = wczytaj("zabiegi.txt")
wizyty = wczytaj("wizytydane.txt")
wizyty_zabiegi = wczytaj("wizytyzabiegi.txt")

makijaze = {}  # kod zabiegu -> cena
for z in zabiegi:
    if z[1] == "MAKIJAZ":
        makijaze[z[0]] = int(z[3])

wizyta = {w[0]: (w[1], w[3]) for w in wizyty}  # id_wizyty -> (data, id_klienta)

kobiety = set()
suma = 0
for id_wizyty, kod in wizyty_zabiegi:
    data, klient = wizyta[id_wizyty]
    if kod in makijaze and klient[0] == "X" and "2017-12-06" <= data <= "2018-01-15":
        kobiety.add(klient)
        suma += makijaze[kod] * 0.8

print(len(kobiety), suma)
```

**Odpowiedź:** 7 kobiet, łącznie 400 zł

## 6.5

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
def wczytaj(nazwa):
    with open(nazwa) as file:
        file.readline()
        return [line.rstrip("\n").split("\t") for line in file if line.strip()]


zabiegi = wczytaj("zabiegi.txt")
wizyty_zabiegi = wczytaj("wizytyzabiegi.txt")

wykonane = set(kod for id_wizyty, kod in wizyty_zabiegi)

for z in zabiegi:
    if z[1] == "FRYZJER MESKI" and z[0] not in wykonane:
        print(z[2])
```

**Odpowiedź:** Odsiwianie, Kuracja L'Oreal, Rytual Kerastase (dyscyplinujacy), Maska Masquargil
