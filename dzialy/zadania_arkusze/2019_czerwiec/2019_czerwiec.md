<h1 align="center">Matura 2019 — czerwiec (termin dodatkowy), poziom rozszerzony</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md) --- [PLIKI](https://github.com/wernexnrs/MATURA-INFORMATYKA/tree/master/dzialy/zadania_arkusze/2019_czerwiec)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2019-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2019-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2019-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2019-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1

```py
# Liczba wywołań Rek zależy tylko od tego, w którą połowę przedziału p..k pójdzie rekurencja.
# Sprawdzamy obie możliwości w każdym kroku i wybieramy najmniejszą / największą liczbę wywołań.
def wywolania(p, k, wybierz):
    if p < k:
        s = (p + k) // 2
        return 1 + wybierz(wywolania(p, s, wybierz), wywolania(s + 1, k, wybierz))
    return 1


print("najmniejsza:", wywolania(6, 14, min))
print("największa:", wywolania(6, 14, max))
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


print("wynik:", Rek(37, 1, 11))
```

**Odpowiedź:** Rek(37,7,11), Rek(37,10,11), Rek(37,11,11) (1.3: złożoność logarytmiczna)

## 2.1 i 2.2

```py
def deszyfruj(k, S):
    n = len(S)
    kolumny = n // k
    # tabela k wierszy na kolumny - szyfrogram to kolejne wiersze tabeli
    tabela = [S[w * kolumny:(w + 1) * kolumny] for w in range(k)]
    T = ""
    for kol in range(kolumny):
        if kol % 2 == 0:  # kolumny nieparzyste (numerując od 1) czytamy z góry na dół
            for w in range(k):
                T += tabela[w][kol]
        else:  # kolumny parzyste - z dołu do góry
            for w in range(k - 1, -1, -1):
                T += tabela[w][kol]
    return T


print(deszyfruj(3, "MA_FOYKARZNRTITU_IMA_"))
print(deszyfruj(10, "NKI_ATE_USGACYOKZZ_YYSJTCWEKI_SAEMTRLE_P"))
```

**Odpowiedź:** NAUCZYCIELEM_WSZYSTKIEGO_JEST_PRAKTYKA

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


with open("liczby.txt") as file:
    for line in file:
        liczba = int(line)
        if 100 <= liczba <= 5000 and czy_pierwsza(liczba):
            print(liczba)
```

**Odpowiedź:** 563, 2087, 163, 2423, 3581, 911, 997, 113, 1049, 1511, 2467, 283, 3559, 521, 4201, 877, 1301, 2749, 4919, 1213, 2039, 4111, 3331, 401, 2221

## 4.2

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


with open("pierwsze.txt") as file:
    for line in file:
        liczba = line.strip()
        if czy_pierwsza(int(liczba[::-1])):
            print(liczba)
```

**Odpowiedź:** 51 liczb: 31, 37, 101, 1009, 1021, 113, 1499, 1213, 1217, 1229, 1231, 1237, 1487, 1223, 7027, … , 112111

## 4.3

```py
def waga(liczba):
    while liczba >= 10:
        suma = 0
        for cyfra in str(liczba):
            suma += int(cyfra)
        liczba = suma
    return liczba


ile = 0

with open("pierwsze.txt") as file:
    for line in file:
        if waga(int(line)) == 1:
            ile += 1

print(ile)
```

**Odpowiedź:** 27

## 5.1

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
import math
from datetime import date, timedelta

with open("pogoda.txt") as file:
    file.readline()  # nagłówek
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

## 5.2

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

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

## 5.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

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

**Odpowiedź:** kwiecień 0 l – 0 zł, maj 13172 l – 14 m3 – 164,36 zł, czerwiec 89444 l – 90 m3 – 1056,60 zł, lipiec 217938 l – 218 m3 – 2559,32 zł, sierpień 310099 l – 311 m3 – 3651,14 zł, wrzesień 112774 l – 113 m3 – 1326,62 zł

## 5.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
chlodne = cieple_bez_deszczu = cieple_z_deszczem = 0

with open("pogoda.txt") as file:
    file.readline()
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
