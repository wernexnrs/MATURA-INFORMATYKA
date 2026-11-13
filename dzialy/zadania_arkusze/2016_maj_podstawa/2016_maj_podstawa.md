<h1 align="center">2016 Maj — poziom podstawowy (stara matura)</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2016-maj-matura-stara-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2016-maj-matura-stara-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2016-maj-matura-stara-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2016-maj-matura-stara-podstawowa-odpowiedzi.pdf)

## 1.1

```py
def kompresuj(tekst):
    wynik = ""
    i = 0
    while i < len(tekst):
        j = i
        while j < len(tekst) and tekst[j] == tekst[i]:
            j += 1
        wynik += str(j - i) + tekst[i]
        i = j
    return wynik


skompresowany = kompresuj("***##!!*")
print(skompresowany, len("***##!!*"), len(skompresowany))
```
**Odpowiedź:** 3\*2#2!1\*, rozmiar przed kompresją 8, po kompresji 8; 1.2: co najmniej 3 kolejne znaki; 1.3: bezstratna

## 1.4

```py
def rozmiar_po_kompresji(n, T):
    r = 1  # liczba grup takich samych znaków
    for i in range(1, n):
        if T[i] != T[i - 1]:
            r += 1
    return 2 * r


tekst = "FFFYYYYYYYYYFFFHAAAAA"
print(rozmiar_po_kompresji(len(tekst), tekst))
```
**Odpowiedź:** dla przykładu z treści – 10

## 2.1 i 2.3

```py
def suma_cyfr(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s


def wspolczynnik(n):
    return (n - suma_cyfr(n)) // 9


for n in [11, 42, 375, 913]:
    print(n, "=", suma_cyfr(n), "+", wspolczynnik(n), "* 9", "  k =", wspolczynnik(n))
```
**Odpowiedź:** 42 → k = 4; 375 → k = 40; 913 → k = 100 (2.2 – funkcja `suma_cyfr`)

## 4.1

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
count = 0

with open("demografia.txt") as file:
    next(file)  # pomijamy nagłówek
    for line in file:
        dane = line.strip().split("\t")
        saldo = float(dane[5].replace(",", "."))
        if dane[1] == "mazowieckie" and saldo < 0:
            count += 1

print(count)
```
**Odpowiedź:** 24

## 4.2

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
powiaty = []

with open("demografia.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split("\t")
        urodzenia = float(dane[3].replace(",", "."))
        zgony = float(dane[4].replace(",", "."))
        powiaty.append((round(urodzenia - zgony, 1), dane[0]))

powiaty.sort(reverse=True)
for przyrost, powiat in sorted(powiaty[:10], key=lambda x: x[1]):
    print(powiat, przyrost)
```
**Odpowiedź:** bytowski 5,7; gdanski 6,0; kartuski 8,7; koscierski 7,2; limanowski 6,4; m Zory 5,7; nowosadecki 6,1; poznanski 6,0; pszczynski 5,5; wejherowski 7,2

## 4.3

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
ludnosc = {}

with open("demografia.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split("\t")
        ludnosc[dane[1]] = ludnosc.get(dane[1], 0) + int(dane[2])

wojewodztwa = sorted(ludnosc, key=ludnosc.get, reverse=True)
for wojewodztwo in wojewodztwa[:4]:
    print(wojewodztwo, ludnosc[wojewodztwo])
```
**Odpowiedź:** mazowieckie 5222167, slaskie 4640725, wielkopolskie 3408281, malopolskie 3298270

## 4.4

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
urodzenia = []

with open("demografia.txt") as file:
    next(file)
    for line in file:
        dane = line.strip().split("\t")
        if dane[1] == "opolskie":
            # współczynnik w dziesiątych częściach (np. 10,4 -> 104), żeby liczyć na liczbach całkowitych
            wsp = round(float(dane[3].replace(",", ".")) * 10)
            urodzenia.append((dane[0], int(dane[2]) * wsp // 10000))

for powiat, liczba in sorted(urodzenia):
    print(powiat, liczba)
```
**Odpowiedź:** brzeski 995, glubczycki 459, kedzierzynsko-kozielski 812, kluczborski 591, krapkowicki 561, m Opole 1182, namyslowski 473, nyski 1337, oleski 584, opolski 1093, prudnicki 528, strzelecki 657 (wykres kolumnowy wykonuje się w arkuszu kalkulacyjnym)

## 5.1

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
klienci = {}
notebooki_hw = set()

with open("klienci.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_klienta, imie, nazwisko = line.strip().split("\t")
        klienci[id_klienta] = (nazwisko, imie)

with open("produkty.txt") as file:
    next(file)
    for line in file:
        id_produktu, nazwa, grupa, producent, cena = line.strip().split("\t")
        if grupa == "Notebooki" and producent == "HW":
            notebooki_hw.add(id_produktu)

wynik = set()
with open("zamowienia.txt") as file:
    next(file)
    for line in file:
        id_zamowienia, data, id_produktu, id_klienta, liczba_sztuk = line.strip().split("\t")
        if id_produktu in notebooki_hw:
            wynik.add(klienci[id_klienta])

for nazwisko, imie in sorted(wynik):
    print(imie, nazwisko)
```
**Odpowiedź:** Albert Banach, Felicja Bogdanska, Beata Brun, Tytus Chmiel, Piotr Gniewny, Edyta Kaczor, Anna Knap, Michal Sawicki, Jerzy Szybki, Feliks Wysoki

## 5.2

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
produkty = {}
szukany = ""

with open("klienci.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_klienta, imie, nazwisko = line.strip().split("\t")
        if imie == "Anna" and nazwisko == "Kotnicka":
            szukany = id_klienta

with open("produkty.txt") as file:
    next(file)
    for line in file:
        id_produktu, nazwa, grupa, producent, cena = line.strip().split("\t")
        produkty[id_produktu] = (nazwa, grupa, producent)

with open("zamowienia.txt") as file:
    next(file)
    for line in file:
        id_zamowienia, data, id_produktu, id_klienta, liczba_sztuk = line.strip().split("\t")
        if id_klienta == szukany:
            print(*produkty[id_produktu])
```
**Odpowiedź:** A8-143 Notebooki TSB; IXP3 Aparaty cyfrowe SPE; TM4233 Notebooki Beca; SATP100-260 Notebooki TSB

## 5.3

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
klienci = {}
zamowienia = {}

with open("klienci.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_klienta, imie, nazwisko = line.strip().split("\t")
        klienci[id_klienta] = nazwisko + " " + imie

with open("zamowienia.txt") as file:
    next(file)
    for line in file:
        id_zamowienia, data, id_produktu, id_klienta, liczba_sztuk = line.strip().split("\t")
        zamowienia[id_klienta] = zamowienia.get(id_klienta, 0) + 1

najwiecej = max(zamowienia, key=zamowienia.get)
print(klienci[najwiecej], zamowienia[najwiecej])
```
**Odpowiedź:** Stuhr Maksymilian 7

## 5.4

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
klienci = {}
ceny = {}
wydatki = {}

with open("klienci.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_klienta, imie, nazwisko = line.strip().split("\t")
        klienci[id_klienta] = imie + " " + nazwisko

with open("produkty.txt") as file:
    next(file)
    for line in file:
        id_produktu, nazwa, grupa, producent, cena = line.strip().split("\t")
        ceny[id_produktu] = float(cena.replace(",", "."))

with open("zamowienia.txt") as file:
    next(file)
    for line in file:
        id_zamowienia, data, id_produktu, id_klienta, liczba_sztuk = line.strip().split("\t")
        kwota = ceny[id_produktu] * int(liczba_sztuk)
        wydatki[id_klienta] = wydatki.get(id_klienta, 0) + kwota

najwiecej = sorted(wydatki, key=wydatki.get, reverse=True)
for id_klienta in najwiecej[:3]:
    print(klienci[id_klienta], round(wydatki[id_klienta], 2))
```
**Odpowiedź:** Krystian Garnek 41471,02 zł; Albin Szary 32311,58 zł; Małgorzata Sobieska 31725,98 zł

## 5.5

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
notebooki = set()

with open("produkty.txt") as file:
    next(file)
    for line in file:
        id_produktu, nazwa, grupa, producent, cena = line.strip().split("\t")
        if grupa == "Notebooki":
            notebooki.add(id_produktu)

sztuki = 0
with open("zamowienia.txt") as file:
    next(file)
    for line in file:
        id_zamowienia, data, id_produktu, id_klienta, liczba_sztuk = line.strip().split("\t")
        if data[:7] == "2013-03" and id_produktu in notebooki:
            sztuki += int(liczba_sztuk)

print(sztuki)
```
**Odpowiedź:** 39

## 6.1

W arkuszu plik nazywa się `dane_6.txt`, w paczce z danymi CKE – `dane4.txt`.

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


count = 0

with open("dane4.txt") as file:
    for line in file:
        if czy_pierwsza(int(line)):
            count += 1

print(count)
```
**Odpowiedź:** 236

## 6.2

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


pierwsze = []

with open("dane4.txt") as file:
    for line in file:
        liczba = int(line)
        if czy_pierwsza(liczba):
            pierwsze.append(liczba)

print("max =", max(pierwsze), "min =", min(pierwsze))
```
**Odpowiedź:** max = 29881, min = 73

## 6.3

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


liczby = []

with open("dane4.txt") as file:
    for line in file:
        liczby.append(int(line))

pary = []
for i in range(1, len(liczby)):
    a = liczby[i - 1]
    b = liczby[i]
    if abs(a - b) == 2 and czy_pierwsza(a) and czy_pierwsza(b):
        pary.append((a, b))

print(len(pary))
for a, b in pary:
    print(a, b)
```
**Odpowiedź:** 4 pary: 1999 1997, 1721 1723, 1481 1483, 809 811
