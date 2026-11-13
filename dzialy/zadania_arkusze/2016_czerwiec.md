<h1 align="center">Matura 2016 — czerwiec (termin dodatkowy), poziom rozszerzony</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2016-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2016-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2016-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2016-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

```py
wywolania = []


def F(n):
    wywolania.append(f"F({n})")
    if n == 1 or n == 2:
        s = n
    else:
        s = n * F(n - 2)
    s = s * (n + 1)
    return s


# 1.1
for n in range(1, 7):
    print(n, F(n))

# 1.2
wywolania = []
F(11)
print(", ".join(wywolania))

# 1.3 - porównanie z (n+1)!
silnia = 1
for n in range(1, 11):
    silnia *= n + 1
    print(n, F(n), silnia)
```
**Odpowiedź:** 1.1: F(1..6) = 2, 6, 24, 120, 720, 5040; 1.2: F(11), F(9), F(7), F(5), F(3), F(1); 1.3: (n+1)!

## 2.1, 2.2 i 2.3

```py
def mniejsza(a, b):
    # czy a << b na planecie X
    if a % 2 == 0 and b % 2 == 1:
        return True
    if a % 2 == 1 and b % 2 == 0:
        return False
    if a % 2 == 0:  # obie parzyste - zwykły porządek
        return a < b
    return a > b    # obie nieparzyste - odwrotny porządek


def klucz(a):
    # klucz sortowania: najpierw parzyste rosnąco, potem nieparzyste malejąco
    if a % 2 == 0:
        return (0, a)
    return (1, -a)


def najwiekszy(A):
    # 2.3
    maks = A[0]
    for x in A[1:]:
        if mniejsza(maks, x):
            maks = x
    return maks


# 2.1
print(sorted([3, 6, 8, 11, 15, 20, 35, 70, 100, 1000], key=klucz))

# 2.2 - najmniejszym elementem ma być 10, np. dopisujemy 10 i 1
print(min([10, 1, 27, 16, 7, 32], key=klucz))

# 2.3
print(najwiekszy([3, 6, 8, 11, 15, 20, 35, 70, 100, 1000]))
print(najwiekszy([2, 4, 6, 8]))
```
**Odpowiedź:** 2.1: 6, 8, 20, 70, 100, 1000, 35, 15, 11, 3; 2.2: 10 i np. 1 (dowolna nieparzysta oprócz 7 i 27 albo parzysta większa od 10)

## 4.1

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
miesiace = [0] * 13

with open("ubezpieczenia.txt") as file:
    next(file)
    for line in file:
        nazwisko, imie, data, miejsce = line.strip().split(";")
        miesiace[int(data[5:7])] += 1

for miesiac in range(1, 13):
    print(miesiac, miesiace[miesiac])
```
**Odpowiedź:** 1: 26, 2: 22, 3: 30, 4: 27, 5: 25, 6: 31, 7: 33, 8: 19, 9: 29, 10: 32, 11: 28, 12: 29

## 4.2

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
kobiety = {}

with open("ubezpieczenia.txt") as file:
    next(file)
    for line in file:
        nazwisko, imie, data, miejsce = line.strip().split(";")
        if imie[-1] == "a":
            kobiety[miejsce] = kobiety.get(miejsce, 0) + 1

for miejsce in kobiety:
    print(miejsce, kobiety[miejsce])
```
**Odpowiedź:** wieś 24, małe miasto 20, średnie miasto 59, duże miasto 97

## 4.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
suma_kobiety = 0
suma_mezczyzni = 0

with open("ubezpieczenia.txt") as file:
    next(file)
    for line in file:
        nazwisko, imie, data, miejsce = line.strip().split(";")
        wiek = 2016 - int(data[:4])  # liczymy rocznikami

        # składka w tysięcznych częściach procenta (0,1% = 100, 0,15% = 150, 0,12% = 120),
        # żeby uniknąć błędów zaokrągleń float
        if wiek <= 30:
            procent = 100
        elif wiek <= 45:
            procent = 150
        else:
            procent = 120

        if imie[-1] == "a":
            kwota = 25000
        else:
            kwota = 30000

        skladka = kwota * procent / 100000
        if wiek > 60:
            skladka += 49

        if imie[-1] == "a":
            suma_kobiety += skladka
        else:
            suma_mezczyzni += skladka

print(f"{suma_kobiety:.2f}")
print(f"{suma_mezczyzni:.2f}")
```
**Odpowiedź:** kobiety 8961,50 zł, mężczyźni 6261,00 zł

## 4.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
przedzialy = {}  # początek przedziału (20, 30, ..., 70) -> liczba osób

with open("ubezpieczenia.txt") as file:
    next(file)
    for line in file:
        nazwisko, imie, data, miejsce = line.strip().split(";")
        wiek = 2016 - int(data[:4])
        poczatek = wiek // 10 * 10
        przedzialy[poczatek] = przedzialy.get(poczatek, 0) + 1

for poczatek in range(20, 80, 10):
    print(f"{poczatek}-{poczatek + 9}", przedzialy.get(poczatek, 0))
```
**Odpowiedź:** 20-29: 62, 30-39: 56, 40-49: 64, 50-59: 56, 60-69: 71, 70-79: 22 (+ wykres kolumnowy)

## 6.1

```py
licznik = 0

with open("liczby.txt") as file:
    for line in file:
        if line.strip()[-1] == "8":
            licznik += 1

print(licznik)
```
**Odpowiedź:** 103

## 6.2

```py
licznik = 0

with open("liczby.txt") as file:
    for line in file:
        kod = line.strip()
        if kod[-1] == "4" and "0" not in kod[:-1]:
            licznik += 1

print(licznik)
```
**Odpowiedź:** 29

## 6.3

```py
licznik = 0

with open("liczby.txt") as file:
    for line in file:
        kod = line.strip()
        # liczba dwójkowa jest parzysta, gdy jej ostatnia cyfra (przedostatni znak kodu) to 0
        if kod[-1] == "2" and kod[-2] == "0":
            licznik += 1

print(licznik)
```
**Odpowiedź:** 153

## 6.4

```py
suma = 0

with open("liczby.txt") as file:
    for line in file:
        kod = line.strip()
        if kod[-1] == "8":
            suma += int(kod[:-1], 8)

print(suma)
```
**Odpowiedź:** 887918739

## 6.5

```py
kod_min = kod_max = None
wartosc_min = wartosc_max = None

with open("liczby.txt") as file:
    for line in file:
        kod = line.strip()
        wartosc = int(kod[:-1], int(kod[-1]))
        if wartosc_min is None or wartosc < wartosc_min:
            wartosc_min = wartosc
            kod_min = kod
        if wartosc_max is None or wartosc > wartosc_max:
            wartosc_max = wartosc
            kod_max = kod

print(kod_max, wartosc_max)
print(kod_min, wartosc_min)
```
**Odpowiedź:** największa: 8066218209 (347931225), najmniejsza: 100002 (16)
