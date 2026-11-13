<h1 align="center">Matura 2009 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2009-maj-matura-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2009-maj-matura-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2009-maj-matura-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2009-maj-matura-podstawowa-odpowiedzi.pdf)

## 1a i 1b

```py
def algorytm(ciag):
    ile_razy = 0  # ile razy wykonano krok 3.
    aktualna = ciag[0]
    i = 1
    while i < len(ciag):
        nastepna = ciag[i]
        ile_razy += 1
        i += 1
        if nastepna > aktualna:
            aktualna = nastepna
        else:
            return "NIE", ile_razy
    return "TAK", ile_razy


A = [60.51, 61.34, 61.85, 61.97, 62.79, 63.00, 63.81, 63.88]
B = [60.41, 60.44, 60.85, 62.71, 61.79, 60.00]
C = [61.45, 60.89, 60.20, 60.01, 59.22, 58.99, 58.75]

for ciag in [A, B, C]:
    print(*algorytm(ciag))
```
**Odpowiedź:** a) TAK, gdy ciąg jest rosnący, w przeciwnym przypadku NIE; b) A: 7, B: 4, C: 1

## 1c

```py
def najwiekszy(ciag):
    maks = ciag[0]
    for liczba in ciag[1:]:
        if liczba > maks:
            maks = liczba
    return maks


print(najwiekszy([60.41, 60.44, 60.85, 62.71, 61.79, 60.00]))
```
**Odpowiedź:** algorytm wyznaczania maksimum (dla zawodnika B: 62.71)

## 2a i 2b

```py
def dwojkowy_na_dziesietny(s):
    calkowita, ulamkowa = s.split(",")
    w = 0
    for cyfra in calkowita:
        w = w * 2 + int(cyfra)
    w = w + int(ulamkowa[0]) * 0.5 + int(ulamkowa[1]) * 0.25
    return w


def dziesietny_na_dwojkowy(x):
    calkowita = int(x)
    ulamkowa = x - calkowita
    napis = bin(calkowita)[2:] + ","
    for _ in range(2):
        ulamkowa *= 2
        napis += str(int(ulamkowa))
        ulamkowa -= int(ulamkowa)
    return napis


print("kakao", dwojkowy_na_dziesietny("111,11"))
print("herbata czarna", dwojkowy_na_dziesietny("100,01"))
print("herbata owocowa", dziesietny_na_dwojkowy(4.50))
print("capuccino", dwojkowy_na_dziesietny("101,00"))
print("kawa espresso", dziesietny_na_dwojkowy(6.00))
```
**Odpowiedź:** herbata czarna 4,25; herbata owocowa 100,10; capuccino 5,00; kawa espresso 110,00

## 4a i 4b

```py
srednie = []

with open("temp.txt") as file:
    for line in file:
        dane = line.strip().replace(",", ".").split()
        rok = int(dane[0])
        temperatury = list(map(float, dane[1:]))
        srednie.append((sum(temperatury) / 12, rok))

najnizsza = min(srednie)
najwyzsza = max(srednie)
print("a)", round(najnizsza[0], 2), najnizsza[1])
print("b)", round(najwyzsza[0], 2), najwyzsza[1])
```
**Odpowiedź:** a) 4,74 — rok 1829; b) 9,82 — rok 1989

## 4c

```py
miesiace = [[] for _ in range(12)]

with open("temp.txt") as file:
    for line in file:
        dane = line.strip().replace(",", ".").split()
        for i in range(12):
            miesiace[i].append(float(dane[i + 1]))

for i in range(12):
    print(i + 1, min(miesiace[i]), max(miesiace[i]))
```
**Odpowiedź:** (miesiąc, min, max) 1: -13,5 3,5; 2: -13,7 5,1; 3: -6,9 7,4; 4: 2,4 13,2; 5: 7,9 18,2; 6: 13,0 22,4; 7: 14,6 23,5; 8: 14,0 23,8; 9: 9,1 16,8; 10: 1,8 12,6; 11: -3,4 7,6; 12: -14,8 3,9 (wykres punktowy wykonuje się w arkuszu kalkulacyjnym)

## 4d

```py
lata = []
sierpien = []

with open("temp.txt") as file:
    for line in file:
        dane = line.strip().replace(",", ".").split()
        lata.append(int(dane[0]))
        sierpien.append(float(dane[8]))

dlugosc = 1
najdluzszy = 1
koniec = 0

for i in range(1, len(sierpien)):
    if sierpien[i] < sierpien[i - 1]:
        dlugosc += 1
    else:
        dlugosc = 1
    if dlugosc > najdluzszy:
        najdluzszy = dlugosc
        koniec = i

print(lata[koniec - najdluzszy + 1], lata[koniec], najdluzszy)
```
**Odpowiedź:** od 1982 do 1987, długość 6

## 5

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


with open("liczby.txt") as file:
    with open("zad_5.txt", "w") as wynik:
        for line in file:
            liczba = int(line.strip())
            pierwiastek = int(liczba ** 0.5)
            while pierwiastek * pierwiastek > liczba:
                pierwiastek -= 1
            while (pierwiastek + 1) * (pierwiastek + 1) <= liczba:
                pierwiastek += 1
            if pierwiastek * pierwiastek == liczba and czy_pierwsza(pierwiastek):
                print(liczba)
                wynik.write(str(liczba) + "\n")
```
**Odpowiedź:** 5041, 1369, 32041, 844561, 4, 96721, 9, 942841, 49, 1849, 528529, 121, 961, 169
