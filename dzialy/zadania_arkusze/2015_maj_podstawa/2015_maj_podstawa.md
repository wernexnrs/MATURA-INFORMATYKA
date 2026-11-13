<h1 align="center">Matura 2015 — maj, poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2015-maj-matura-stara-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2015-maj-matura-stara-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2015-maj-matura-stara-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2015-maj-matura-stara-podstawowa-odpowiedzi.pdf)

## 1.1

```py
def na_szostkowy(x):
    wynik = ""
    while x > 0:
        wynik = str(x % 6) + wynik
        x = x // 6
    return wynik


print(na_szostkowy(int("1000", 6) // int("10", 6)))  # 10 * ? = 1000
print(na_szostkowy(int("425", 6) - int("41", 6)))  # 425 - ? = 41
print(na_szostkowy(int("154", 6) // int("55", 6)))  # 154 / ? = 55
```
**Odpowiedź:** 10 * 100 = 1000, 425 − 344 = 41, 154 / 2 = 55

## 1.2

```py
def wartosc(d, C):  # C[0] - cyfra najmniej znacząca
    w = 0
    for i in range(d - 1, -1, -1):
        w = w * 6 + C[i]
    return w


print(wartosc(4, [0, 0, 0, 1]))
```
**Odpowiedź:** dla d = 4 i C = [0, 0, 0, 1] → 216

## 2.1

```py
def zlicz(n, k, A):
    T = [0] * (k + 1)  # T[0] nieużywane
    for i in range(n):
        pozycja = A[i]
        T[pozycja] = T[pozycja] + 1
    return T[1:]


print(zlicz(6, 6, [3, 5, 6, 2, 1, 4]))
print(zlicz(7, 4, [2, 3, 4, 2, 3, 1, 2]))
print(zlicz(7, 3, [3, 2, 3, 2, 3, 2, 3]))
print(zlicz(5, 8, [3, 3, 1, 5, 8]))
```
**Odpowiedź:** T[i] to liczba wystąpień liczby i w tablicy A; [1, 1, 1, 1, 1, 1], [1, 3, 2, 1], [0, 3, 4], [1, 0, 2, 0, 1, 0, 0, 1]

## 2.2

```py
def najczestszy(n, k, A):
    T = [0] * (k + 1)
    for i in range(n):
        T[A[i]] += 1
    y = 1
    for i in range(2, k + 1):
        if T[i] > T[y]:
            y = i
    return y


print(najczestszy(5, 3, [1, 2, 3, 2, 2]))
print(najczestszy(8, 3, [1, 2, 3, 3, 2, 3, 3, 3]))
```
**Odpowiedź:** 2 oraz 3 (dla przykładów z treści)

## 4.1

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
marki = ["Dama", "Granta", "Dorkas", "Lodera"]
start = [237, 198, 207, 312]
wzrost = [1020, 1027, 1030, 1020]  # w promilach: +2%, +2,7%, +3%, +2%
spadek = [990, 988, 981, 975]  # -1%, -1,2%, -1,9%, -2,5%


def produkcja(m):  # lista produkcji w kolejnych kwartałach 2005-2012
    kwartaly = [start[m]]
    for _ in range(19):  # do końca 2009 roku
        kwartaly.append(kwartaly[-1] * wzrost[m] // 1000)
    for _ in range(4):  # 2010 - bez zmian
        kwartaly.append(kwartaly[-1])
    for _ in range(8):  # 2011 i 2012 - spadek
        kwartaly.append(kwartaly[-1] * spadek[m] // 1000)
    return kwartaly


for m in range(4):
    print(marki[m], produkcja(m)[27])  # IV kwartał 2011 to kwartał nr 28
```
**Odpowiedź:** Dama 317, Granta 300, Dorkas 322, Lodera 398

## 4.2

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
marki = ["Dama", "Granta", "Dorkas", "Lodera"]
start = [237, 198, 207, 312]
wzrost = [1020, 1027, 1030, 1020]
spadek = [990, 988, 981, 975]

najwczesniej = None
for m in range(4):
    kwartaly = [start[m]]
    for _ in range(19):
        kwartaly.append(kwartaly[-1] * wzrost[m] // 1000)
    for _ in range(4):
        kwartaly.append(kwartaly[-1])
    while kwartaly[-1] >= start[m]:  # spadek trwa aż do zejścia poniżej produkcji z I kw. 2005
        kwartaly.append(kwartaly[-1] * spadek[m] // 1000)
    numer = len(kwartaly) - 1  # numer kwartału liczony od 0 (I kw. 2005)
    if najwczesniej is None or numer < najwczesniej[0]:
        najwczesniej = (numer, marki[m], kwartaly[-1])

numer, marka, liczba = najwczesniej
print(marka, liczba, "kwartał:", numer % 4 + 1, "rok:", 2005 + numer // 4)
```
**Odpowiedź:** Lodera, 305 sztuk, II kwartał 2014 roku

## 4.3 i 4.4

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
marki = ["Dama", "Granta", "Dorkas", "Lodera"]
start = [237, 198, 207, 312]
wzrost = [1020, 1027, 1030, 1020]
spadek = [990, 988, 981, 975]

razem_do_2010 = 0
for m in range(4):
    kwartaly = [start[m]]
    for _ in range(19):
        kwartaly.append(kwartaly[-1] * wzrost[m] // 1000)
    for _ in range(4):
        kwartaly.append(kwartaly[-1])
    for _ in range(8):
        kwartaly.append(kwartaly[-1] * spadek[m] // 1000)

    ponad_300 = 0
    for x in kwartaly:
        if x > 300:
            ponad_300 += 1
    print("4.3", marki[m], ponad_300)

    razem_do_2010 += sum(kwartaly[:24])  # 24 kwartały: 2005-2010

print("4.4", razem_do_2010)
```
**Odpowiedź:** 4.3: Dama 18, Granta 9, Dorkas 17, Lodera 32; 4.4: 29368 (wykres 4.5 wykonuje się w arkuszu kalkulacyjnym)

## 5.1

```py
dlugosci = [0] * 13

with open("slowa.txt") as file:
    for line in file:
        slowo = line.strip()
        dlugosci[len(slowo)] += 1

for n in range(1, 13):
    print(n, dlugosci[n])
```
**Odpowiedź:** 1 84, 2 65, 3 92, 4 75, 5 104, 6 75, 7 95, 8 71, 9 81, 10 62, 11 102, 12 94

## 5.2

```py
slowa = []

with open("slowa.txt") as file:
    for line in file:
        slowa.append(line.strip())

with open("nowe.txt") as file:
    for line in file:
        slowo = line.strip()
        print(slowo, slowa.count(slowo), slowa.count(slowo[::-1]))
```
**Odpowiedź:** hxqsf 4 5, erraegrdsj 0 0, cpcxpzj 3 1, arphlqleftqm 10 1, wdt 0 4, … , rceij 5 0

## 6.1

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
osoby = {}

with open("osoby.txt", encoding="cp1250") as file:
    next(file)  # pomijamy nagłówek
    for line in file:
        id_osoby, imie, nazwisko = line.strip().split(";")
        osoby[id_osoby] = imie + " " + nazwisko

with open("konta.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_konta, id_osoby, bank, nr_konta, srodki = line.strip().split(";")
        if nr_konta[:2] == "49":
            print(osoby[id_osoby])
```
**Odpowiedź:** Rodryk Sakson

## 6.2

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
osoby = {}
srodki_osoby = {}

with open("osoby.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_osoby, imie, nazwisko = line.strip().split(";")
        osoby[id_osoby] = imie + " " + nazwisko

with open("konta.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_konta, id_osoby, bank, nr_konta, srodki = line.strip().split(";")
        srodki_osoby[id_osoby] = srodki_osoby.get(id_osoby, 0) + float(srodki.replace(",", "."))

najbogatszy = max(srodki_osoby, key=srodki_osoby.get)
print(osoby[najbogatszy], round(srodki_osoby[najbogatszy], 2))
```
**Odpowiedź:** Kazimierz Baran, 42366,12 zł

## 6.3

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
osoby = {}
liczba_kont = {}

with open("osoby.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_osoby, imie, nazwisko = line.strip().split(";")
        osoby[id_osoby] = imie + " " + nazwisko

with open("konta.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_konta, id_osoby, bank, nr_konta, srodki = line.strip().split(";")
        liczba_kont[id_osoby] = liczba_kont.get(id_osoby, 0) + 1

najwiecej = max(liczba_kont.values())
for id_osoby in liczba_kont:
    if liczba_kont[id_osoby] == najwiecej:
        print(osoby[id_osoby])
```
**Odpowiedź:** Grzegorz Potocki, Maria Zamojska, Ewa Klimaszewska, Krystyna Tobera

## 6.4

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
liczba_kont = {}
kwota = {}

with open("konta.txt", encoding="cp1250") as file:
    next(file)
    for line in file:
        id_konta, id_osoby, bank, nr_konta, srodki = line.strip().split(";")
        liczba_kont[bank] = liczba_kont.get(bank, 0) + 1
        kwota[bank] = kwota.get(bank, 0) + float(srodki.replace(",", "."))

najwiecej = max(liczba_kont, key=liczba_kont.get)
najmniej = min(liczba_kont, key=liczba_kont.get)
print("max:", najwiecej, liczba_kont[najwiecej], round(kwota[najwiecej], 2))
print("min:", najmniej, liczba_kont[najmniej], round(kwota[najmniej], 2))
```
**Odpowiedź:** max: BRE Bank SA, 103 konta, 530751,56 zł; min: Skok, 5 kont, 28202,60 zł
