<h1 align="center">2018 Czerwiec</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2018-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2018-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2018-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2018-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

```py
def F(T, x):
    # wyszukiwanie binarne; T indeksowana od 1 jak w treści (T[0] nieużywane)
    n = len(T) - 1
    p, k = 1, n
    zmiany_p = zmiany_k = 0
    wartosci_s = []
    sprawdzenia = 0  # ile razy warunek p <= k był spełniony
    while p <= k:
        sprawdzenia += 1
        s = (p + k) // 2
        wartosci_s.append(s)
        if T[s] == x:
            return True, zmiany_p, zmiany_k, wartosci_s, sprawdzenia
        if T[s] < x:
            p = s + 1
            zmiany_p += 1
        else:
            k = s - 1
            zmiany_k += 1
    return False, zmiany_p, zmiany_k, wartosci_s, sprawdzenia


T = [None, 3, 5, 7, 8, 9, 13, 33, 37, 40, 43]

# 1.1 A, B, C
wynik, zp, zk, s, ile = F(T, 7)
print("x = 7:", wynik, "p:", zp, "k:", zk, "s:", s)
wynik, zp, zk, s, ile = F(T, 43)
print("x = 43:", "p:", zp, "k:", zk)

# 1.2 - n = 100, x większe od wszystkich elementów
T100 = [None] + list(range(1, 101))
print(F(T100, 1000)[4])

# 1.3
T_nieuporzadkowana = [None, 3, 5, 7, 8, 90, 13, 33, 37, 40, 43]
print(F(T_nieuporzadkowana, 43)[0])
```
**Odpowiedź:** 1.1: A. prawda; B. x = 7: p - 1, k - 1; x = 43: p - 3, k - 0; C. 5, 2, 3. 1.2: 7 razy. 1.3: fałsz.

## 2.1 i 2.3

```py
def fib_iteracyjnie(n):
    # 2.1 - bez tablic, tylko dwie ostatnie wartości
    f1 = f2 = 1
    for i in range(3, n + 1):
        f1, f2 = f2, f1 + f2
    return f2


def fib_szybko(n):
    # 2.3 - F(2k) = F(k+1)^2 - F(k-1)^2, F(2k-1) = F(k)^2 + F(k-1)^2
    if n == 1 or n == 2:
        return 1
    if n % 2 == 0:
        k = n // 2
        return fib_szybko(k + 1) ** 2 - fib_szybko(k - 1) ** 2
    k = (n + 1) // 2
    return fib_szybko(k) ** 2 + fib_szybko(k - 1) ** 2


print(fib_iteracyjnie(45), fib_szybko(45))
for n in range(1, 30):
    assert fib_iteracyjnie(n) == fib_szybko(n)
```
**Odpowiedź:** F45 = 1134903170 (obie funkcje)

## 4.1

```py
licznik = 0

with open("dane1.txt") as dane1, open("dane2.txt") as dane2:
    for wiersz1, wiersz2 in zip(dane1, dane2):
        a = list(map(int, wiersz1.split()))
        b = list(map(int, wiersz2.split()))
        if a[-1] == b[-1]:
            licznik += 1

print(licznik)
```
**Odpowiedź:** 32

## 4.2

```py
def parzystych(ciag):
    ile = 0
    for liczba in ciag:
        if liczba % 2 == 0:
            ile += 1
    return ile


licznik = 0

with open("dane1.txt") as dane1, open("dane2.txt") as dane2:
    for wiersz1, wiersz2 in zip(dane1, dane2):
        a = list(map(int, wiersz1.split()))
        b = list(map(int, wiersz2.split()))
        # 10 liczb, z czego 5 parzystych => 5 nieparzystych
        if parzystych(a) == 5 and parzystych(b) == 5:
            licznik += 1

print(licznik)
```
**Odpowiedź:** 50

## 4.3

```py
wiersze = []

with open("dane1.txt") as dane1, open("dane2.txt") as dane2:
    nr = 1
    for wiersz1, wiersz2 in zip(dane1, dane2):
        a = set(map(int, wiersz1.split()))
        b = set(map(int, wiersz2.split()))
        # porównujemy zbiory (a nie listy utworzone ze zbiorów - ich kolejność nie jest gwarantowana)
        if a == b:
            wiersze.append(nr)
        nr += 1

print(len(wiersze))
print(*wiersze, sep=", ")
```
**Odpowiedź:** 1 para ciągów, wiersz 999

## 4.4

```py
def scal(a, b):
    wynik = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            wynik.append(a[i])
            i += 1
        else:
            wynik.append(b[j])
            j += 1
    # jeden z ciągów się wyczerpał - przepisujemy resztę drugiego
    wynik += a[i:]
    wynik += b[j:]
    return wynik


with open("dane1.txt") as dane1, open("dane2.txt") as dane2, open("wynik4_4.txt", "w") as plik:
    for wiersz1, wiersz2 in zip(dane1, dane2):
        a = list(map(int, wiersz1.split()))
        b = list(map(int, wiersz2.split()))
        plik.write(" ".join(map(str, scal(a, b))) + "\n")
```
**Odpowiedź:** plik wynik4_4.txt (pierwsze wiersze: 1 5 6 6 8 13 13 14 15 15 24 24 33 33 34 35 36 41 44 45, 4 8 8 14 16 17 19 22 28 28 33 38 42 43 45 45 46 46 49 49, …)

## 5.1

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
suma = 0
ile = 0

with open("pomiary.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        godzina = dane[1]
        if "05:00" <= godzina <= "12:00":  # format GG:MM - można porównywać jak napisy
            suma += float(dane[2 + 4].replace(",", "."))  # czujnik5
            ile += 1

print(f"{suma / ile:.2f}")
```
**Odpowiedź:** 12,50

## 5.2

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
wystapienia = [{} for _ in range(10)]  # dla każdego czujnika: kelwiny -> liczba wystąpień

with open("pomiary.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        for c in range(10):
            # temperatura w setnych częściach stopnia, żeby uniknąć błędów float
            setne = int(dane[2 + c].replace(",", "").replace("-", ""))
            if dane[2 + c].startswith("-"):
                setne = -setne
            kelwiny = (27315 + setne) // 100  # zaokrąglenie w dół
            wystapienia[c][kelwiny] = wystapienia[c].get(kelwiny, 0) + 1

for c in range(10):
    najczesciej = max(wystapienia[c].values())
    wartosci = [k for k in wystapienia[c] if wystapienia[c][k] == najczesciej]
    print(f"czujnik{c + 1}", *sorted(wartosci))
```
**Odpowiedź:** 287, 288 (lub 286), 283, 284, 284, 287 (lub 296), 286, 288, 285, 286

## 5.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
suma = {}
ile = {}

with open("pomiary.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        miesiac = int(dane[0][5:7])
        suma[miesiac] = suma.get(miesiac, 0) + float(dane[11].replace(",", "."))  # czujnik10
        ile[miesiac] = ile.get(miesiac, 0) + 1

for miesiac in sorted(suma):
    print(miesiac, f"{suma[miesiac] / ile[miesiac]:.2f}")
```
**Odpowiedź:** sty 0,91; lut 0,16; mar 2,30; kwi 12,84; maj 13,56; cze 14,54; lip 22,22; sie 22,23; wrz 16,03; paź 15,03; lis 15,54; gru 0,65 (+ wykres słupkowy)

## 5.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
przedzial1 = 0  # (-10, 15]
przedzial2 = 0  # (15, 20]

with open("pomiary.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        for t in dane[2:]:
            t = float(t.replace(",", "."))
            if -10 < t <= 15:
                przedzial1 += 1
            elif 15 < t <= 20:
                przedzial2 += 1

if przedzial1 > przedzial2:
    print("(-10, 15]", przedzial1)
else:
    print("(15, 20]", przedzial2)
```
**Odpowiedź:** (-10, 15], 1150 pomiarów

## 5.5

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
def na_setne(tekst):
    # "-4,98" -> -498 (liczymy w setnych częściach stopnia)
    setne = int(tekst.replace(",", "").replace("-", ""))
    if tekst.startswith("-"):
        return -setne
    return setne


def napis(setne):
    znak = "-" if setne < 0 else ""
    setne = abs(setne)
    return f"{znak}{setne // 100},{setne % 100:02d}"


czujniki = [1, 2, 8, 9]
pierwsze = {}  # data 2017 -> (godzina, wartości wg wniosków I i II, wartości wg wniosków I, II i III)

with open("pomiary.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split(";")
        data = "2017" + dane[0][4:]
        miesiac = int(data[5:7])
        dzien = int(data[8:10])

        wynik_ab = []
        wynik_abc = []
        for c in czujniki:
            t = na_setne(dane[1 + c])
            if 5 <= dzien <= 10 and c in [1, 2, 9]:      # wniosek I
                t -= 120
            if miesiac in [7, 8] and c == 8:              # wniosek II (w dół do 2 miejsc)
                t = t * 107 // 100
            wynik_ab.append(t)
            if miesiac == 5:                              # wniosek III
                t += 90
            wynik_abc.append(t)

        if data not in pierwsze:  # pierwszy pomiar danego dnia (dane są uporządkowane)
            pierwsze[data] = (dane[1], wynik_ab, wynik_abc)

for data in ["2017-05-05", "2017-07-07"]:
    godzina, ab, abc = pierwsze[data]
    print(data, godzina, "czujniki 1, 2, 8, 9")
    print("  wnioski I i II:     ", *[napis(t) for t in ab])
    print("  wnioski I, II i III:", *[napis(t) for t in abc])
```
**Odpowiedź:** 2017-05-05 07:05: I i II - czujnik1 9,46, czujnik2 9,39, czujnik8 14,52, czujnik9 10,45; I, II i III - 10,36, 10,29, 15,42, 11,35. 2017-07-07 00:04: 23,42, 19,39, 26,67, 20,70 (w obu wariantach)

## 6.1

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
from datetime import date

ceny = {}
with open("ceny_za_dobe.txt") as file:
    next(file)
    for line in file:
        klasa, cena = line.strip().split(";")
        ceny[klasa] = int(cena)

samochody = {}  # nr ewidencyjny -> (klasa, nr rejestracyjny)
with open("samochody.txt") as file:
    next(file)
    for line in file:
        nr_ew, nr_firmowy, miejscowosc, nr_rej = line.strip().split(";")
        samochody[nr_ew] = (nr_firmowy[0], nr_rej)

klienci = {}  # nr klienta -> (imię, nazwisko)
with open("klienci.txt") as file:
    next(file)
    for line in file:
        nr_klienta, imie, nazwisko = line.strip().split(";")
        klienci[nr_klienta] = (imie, nazwisko)


def na_date(tekst):
    r, m, d = map(int, tekst.split("-"))
    return date(r, m, d)


zestawienie = []
with open("wypozyczenia.txt") as file:
    next(file)
    for line in file:
        nr_ew, nr_klienta, wypozyczenie, zwrot = line.strip().split(";")
        imie, nazwisko = klienci[nr_klienta]
        klasa, nr_rej = samochody[nr_ew]
        doby = (na_date(zwrot) - na_date(wypozyczenie)).days
        zestawienie.append((nazwisko, imie, nr_rej, doby, doby * ceny[klasa]))

zestawienie.sort()
print(*zestawienie[0])
print(*zestawienie[-1])
```
**Odpowiedź:** pierwszy: Aabacka Nela WI1150 2 160,00 zł; ostatni: Zgbacka Aaricia WI1126 11 880,00 zł

## 6.2

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
klasa = {}  # nr ewidencyjny -> klasa samochodu
with open("samochody.txt") as file:
    next(file)
    for line in file:
        nr_ew, nr_firmowy, miejscowosc, nr_rej = line.strip().split(";")
        klasa[nr_ew] = nr_firmowy[0]

wypozyczenia = {}
with open("wypozyczenia.txt") as file:
    next(file)
    for line in file:
        nr_ew, nr_klienta, wypozyczenie, zwrot = line.strip().split(";")
        k = klasa[nr_ew]
        wypozyczenia[k] = wypozyczenia.get(k, 0) + 1

for k in sorted(wypozyczenia):
    print(k, wypozyczenia[k])
```
**Odpowiedź:** B 100, C 48, D 53

## 6.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
klienci = {}
with open("klienci.txt") as file:
    next(file)
    for line in file:
        nr_klienta, imie, nazwisko = line.strip().split(";")
        klienci[nr_klienta] = (imie, nazwisko)

ile = {}
with open("wypozyczenia.txt") as file:
    next(file)
    for line in file:
        nr_ew, nr_klienta, wypozyczenie, zwrot = line.strip().split(";")
        ile[nr_klienta] = ile.get(nr_klienta, 0) + 1

najwiecej = max(ile.values())
for nr_klienta in ile:
    if ile[nr_klienta] == najwiecej:
        print(*klienci[nr_klienta], najwiecej)
```
**Odpowiedź:** Ramzes Hcbacki, 5 wypożyczeń

## 6.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
wypozyczane = set()
with open("wypozyczenia.txt") as file:
    next(file)
    for line in file:
        nr_ew, nr_klienta, wypozyczenie, zwrot = line.strip().split(";")
        wypozyczane.add(nr_ew)

zestawienie = {}  # (miejscowość, klasa) -> liczba niewypożyczanych samochodów
with open("samochody.txt") as file:
    next(file)
    for line in file:
        nr_ew, nr_firmowy, miejscowosc, nr_rej = line.strip().split(";")
        if nr_ew not in wypozyczane:
            klucz = (miejscowosc, nr_firmowy[0])
            zestawienie[klucz] = zestawienie.get(klucz, 0) + 1

for miejscowosc, klasa in sorted(zestawienie):
    print(miejscowosc, klasa, zestawienie[(miejscowosc, klasa)])
print("razem:", sum(zestawienie.values()))
```
**Odpowiedź:** (B, C, D) Aniolkowo 12 8 7, Manipulatowo 31 14 11, Nieszczerzyn 17 9 4 (tyle podaje klucz CKE), program wypisuje też Piarowa 16 18 8, Wielka Wola 25 11 7

## 6.5

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
wypozyczajacy = set()
with open("wypozyczenia.txt") as file:
    next(file)
    for line in file:
        nr_ew, nr_klienta, wypozyczenie, zwrot = line.strip().split(";")
        wypozyczajacy.add(nr_klienta)

licznik = 0
with open("klienci.txt") as file:
    next(file)
    for line in file:
        nr_klienta, imie, nazwisko = line.strip().split(";")
        if nr_klienta not in wypozyczajacy:
            licznik += 1

print(licznik)
```
**Odpowiedź:** 72
