<h1 align="center">2017 maj (stara formuła)</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ I](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2017/formula_do_2014/informatyka/MIN-R1_1P-172.pdf) --- [ARKUSZ II](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2017/formula_do_2014/informatyka/MIN-R2_1P-172.pdf) --- [DANE](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2017/formula_do_2014/informatyka/Dane_PR2.zip) --- [ODPOWIEDZI](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2017/formula_do_2014/zasady_oceniania/MIN-R1-S.pdf)

## 1.1 i 1.2

```py
def sortowanie(T, k):
    liczba_wystapien = [0] * (k + 1)       # indeksy 1..k
    for x in T:
        liczba_wystapien[x] += 1
    W = []
    for j in range(1, k + 1):
        for i in range(liczba_wystapien[j]):
            W.append(j)
    return liczba_wystapien[1:], W


def ranga(T, k, i):
    # i - numer elementu liczony od 1, jak w tresci zadania
    liczba_wystapien = [0] + sortowanie(T, k)[0]
    r = 0
    for j in range(1, T[i - 1]):           # j = 1 .. T[i]-1
        r += liczba_wystapien[j]
    return r


dane = [(5, [1, 2, 3, 4, 5, 1, 2, 3, 4, 4]), (10, [1, 3, 3, 5, 10]), (5, [5, 5, 5, 5, 5]), (4, [1, 2, 3, 1, 2, 3, 1, 1, 2, 3])]
for k, T in dane:
    print(sortowanie(T, k)[0])

T = [1, 2, 3, 4, 5, 1, 4, 3, 2, 5]
print(ranga(T, 5, 8), ranga(T, 5, 10), ranga(T, 5, 6))
```

**Odpowiedź:** 1.1: [2, 2, 2, 3, 1], [1, 0, 2, 0, 1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 5], [4, 3, 3, 0]; 1.2: `dla j = 1..T[i] - 1`

## 1.3

```py
def liczniki_mod(T, k):
    liczba_wystapien = [0] * (k + 1)
    for x in T:
        m = 1 + x % k
        liczba_wystapien[m] += 1
    w = liczba_wystapien[1]                # liczba elementow podzielnych przez k
    return liczba_wystapien[1:], w


T = [1, 2, 3, 4, 5, 1, 2, 3, 4, 4]
for k in [2, 3, 4, 5]:
    print(k, *liczniki_mod(T, k))
```

**Odpowiedź:** k=3: [2, 5, 3], k=4: [3, 3, 2, 2], k=5: [1, 2, 2, 2, 3]; w — liczba elementów ciągu T[1..n] podzielnych przez k

## 2.1 i 2.2

```py
def pentanacci(n):
    tab = [0, 1, 1, 2, 4]
    i = 5
    while i <= n:
        temp = tab[0] + tab[1] + tab[2] + tab[3] + tab[4]
        tab[i % 5] = temp
        i += 1
    return tab[n % 5]


for n in [5, 7, 9]:
    print(n, pentanacci(n))
```

**Odpowiedź:** p7 = 31, p9 = 120; luki: `i ≤ n`, `tab[i mod 5]`, `w ← tab[n mod 5]`

## 2.3

```py
def parzystosc(n):
    k = n % 6
    if k == 1 or k == 2:
        return 1
    return 0


# sprawdzenie z algorytmem z 2.2 (funkcja pentanacci)
def pentanacci(n):
    tab = [0, 1, 1, 2, 4]
    for i in range(5, n + 1):
        tab[i % 5] = sum(tab)
    return tab[n % 5]


print(all(parzystosc(n) == pentanacci(n) % 2 for n in range(100)))
```

**Odpowiedź:** k ← n mod 6; jeżeli k = 1 lub k = 2, to w ← 1, w przeciwnym razie w ← 0

## 4.1

```py
licznik = 0
najdluzszy = ""

with open("binarne.txt") as file:
    for line in file:
        napis = line.strip()
        polowa = len(napis) // 2
        if napis[:polowa] == napis[polowa:]:
            licznik += 1
            if len(napis) > len(najdluzszy):
                najdluzszy = napis

print(licznik, najdluzszy, len(najdluzszy))
```

**Odpowiedź:** 18; 00100101100011100010010110001110; 32

## 4.2

```py
licznik = 0
najkrotszy = None

with open("binarne.txt") as file:
    for line in file:
        napis = line.strip()
        poprawny = True
        for i in range(0, len(napis), 4):
            if int(napis[i:i + 4], 2) > 9:
                poprawny = False
        if not poprawny:
            licznik += 1
            if najkrotszy is None or len(napis) < najkrotszy:
                najkrotszy = len(napis)

print(licznik, najkrotszy)
```

**Odpowiedź:** 359; 4

## 4.3

```py
maks = 0

with open("binarne.txt") as file:
    for line in file:
        liczba = int(line.strip(), 2)
        if liczba <= 65535 and liczba > maks:
            maks = liczba

print(bin(maks)[2:], maks)
```

**Odpowiedź:** 1101011001100101, 54885

## 5.1, 5.2 i 5.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
from datetime import date, timedelta


def sezon(dostawa):
    dzien = date(2015, 9, 15)
    drewno = 550
    pierwszy_raz = None
    dostawy = 0
    wieczory_drewno = 0
    wieczory_gaz = 0
    ogrzewania_gazem_zamiast_drewnem = 0
    while dzien <= date(2016, 3, 31):
        dzien_tygodnia = dzien.weekday()    # 0 - poniedzialek, 4 - piatek, 5 i 6 - weekend
        if dzien_tygodnia == 4 and drewno < 100:
            drewno += dostawa
            dostawy += 1
        # rano - w weekend drewno (jesli jest), w dni robocze gaz
        if dzien_tygodnia >= 5:
            if drewno >= 26:
                drewno -= 26
            else:
                ogrzewania_gazem_zamiast_drewnem += 1
            if drewno < 100 and pierwszy_raz is None:
                pierwszy_raz = (dzien, "rano")
        # wieczor - zawsze drewno (jesli jest)
        if drewno >= 26:
            drewno -= 26
            wieczory_drewno += 1
        else:
            wieczory_gaz += 1
            ogrzewania_gazem_zamiast_drewnem += 1
        if drewno < 100 and pierwszy_raz is None:
            pierwszy_raz = (dzien, "wieczor")
        dzien += timedelta(days=1)
    return pierwszy_raz, dostawy, wieczory_drewno, wieczory_gaz, ogrzewania_gazem_zamiast_drewnem


pierwszy_raz, dostawy, wieczory_drewno, wieczory_gaz, _ = sezon(300)
print("5.1", pierwszy_raz[0], pierwszy_raz[1])
print("5.2", dostawy, wieczory_drewno, wieczory_gaz)

masa = 300
while sezon(masa)[4] > 0:
    masa += 1
print("5.4", masa)
```

**Odpowiedź:** 5.1: 2015-09-28, wieczorem; 5.2: 18 dostaw, 167 wieczorów drewnem, 32 wieczory gazem; 5.4: 468 kg

## 5.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
from datetime import date, timedelta

# dane do wykresu liniowego: data, masa drewna po wieczornym ogrzewaniu
dzien = date(2015, 9, 15)
drewno = 550

with open("wykres_5_3.txt", "w") as wynik:
    while dzien <= date(2016, 3, 31):
        if dzien.weekday() == 4 and drewno < 100:
            drewno += 300
        if dzien.weekday() >= 5 and drewno >= 26:
            drewno -= 26
        if drewno >= 26:
            drewno -= 26
        wynik.write(f"{dzien};{drewno}\n")
        dzien += timedelta(days=1)
```

**Odpowiedź:** wykres liniowy (oś X — data, oś Y — masa drewna wieczorem) tworzymy z pliku `wykres_5_3.txt`

## 6.1

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
osoby = {}
with open("osoby.txt") as file:
    next(file)
    for line in file:
        id_osoby, imie, nazwisko = line.strip().split("\t")
        osoby[id_osoby] = (nazwisko, imie)

rezerwacje = {}
with open("rezerwacje.txt") as file:
    next(file)
    for line in file:
        id_rezerwacji, id_osoby, id_wycieczki, dorosli, dzieci = line.strip().split("\t")
        rezerwacje[id_osoby] = rezerwacje.get(id_osoby, 0) + 1

lista = [osoby[id_osoby] for id_osoby in rezerwacje if rezerwacje[id_osoby] > 3]
for nazwisko, imie in sorted(lista):
    print(imie, nazwisko)
```

**Odpowiedź:** Sylwia Adamska, Marcin Ciesielski, Pawel Dziminski, Klaudia Kapuscinska, Ewelina Lagun, Michal Majewski, Katarzyna Michalak, Kamila Olobry, Piotr Otorowski, Danuta Pawezowska, Tomasz Stefanczyk, Pawel Straciuk, Monika Wer

## 6.2

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
osoby = {}
with open("osoby.txt") as file:
    next(file)
    for line in file:
        id_osoby, imie, nazwisko = line.strip().split("\t")
        osoby[id_osoby] = imie + " " + nazwisko

cena = {}
with open("wycieczki.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split("\t")
        cena[dane[0]] = int(dane[6])

zaplacone = {}
with open("rezerwacje.txt") as file:
    next(file)
    for line in file:
        id_rezerwacji, id_osoby, id_wycieczki, dorosli, dzieci = line.strip().split("\t")
        koszt = cena[id_wycieczki] * (int(dorosli) + 0.5 * int(dzieci))
        zaplacone[id_osoby] = zaplacone.get(id_osoby, 0) + koszt

najwiecej = max(zaplacone, key=zaplacone.get)
print(osoby[najwiecej], zaplacone[najwiecej])
```

**Odpowiedź:** Marcin Ciesielski, 34 017,50 zł

## 6.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
miesiac_wyjazdu = {}
with open("wycieczki.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split("\t")
        miesiac_wyjazdu[dane[0]] = int(dane[4][5:7])

nazwy = {6: "czerwiec", 7: "lipiec", 8: "sierpien", 9: "wrzesien"}
liczba = {}
with open("rezerwacje.txt") as file:
    next(file)
    for line in file:
        id_rezerwacji, id_osoby, id_wycieczki, dorosli, dzieci = line.strip().split("\t")
        miesiac = miesiac_wyjazdu[id_wycieczki]
        liczba[miesiac] = liczba.get(miesiac, 0) + 1

for miesiac in sorted(liczba):
    print(nazwy[miesiac], liczba[miesiac])
```

**Odpowiedź:** czerwiec 76, lipiec 505, sierpień 291, wrzesień 28

## 6.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
zestawienie = {}
lotniska = set()
with open("wycieczki.txt") as file:
    next(file)
    for line in file:
        id_wycieczki, kraj, miejsce, wylot, data_od, data_do, cena = line.strip().split("\t")
        lotniska.add(wylot)
        zestawienie[(kraj, wylot)] = zestawienie.get((kraj, wylot), 0) + 1

lotniska = sorted(lotniska)
kraje = sorted(set(kraj for kraj, wylot in zestawienie))
print("kraj", *lotniska)
for kraj in kraje:
    print(kraj, *[zestawienie.get((kraj, wylot), 0) for wylot in lotniska])
```

**Odpowiedź:** (Gdansk, Katowice, Krakow, Lodz, Poznan, Warszawa, Wroclaw) Bulgaria 26 19 17 22 24 20 25; Egipt 20 49 14 3 21 26 22; Grecja 27 26 25 33 17 29 19; Hiszpania 19 31 12 19 17 25 26; Maroko 21 22 26 26 23 21 28; Tunezja 23 26 13 32 20 25 25; Turcja 17 23 22 30 23 24 18
