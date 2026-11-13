<h1 align="center">Matura 2025 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2023)</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

```py
def skroc(x):
    return x // 10


def dopisz(x):
    return x * 10


def ostatnia(x):
    return x % 10


wywolania = 0
dodawania = 0


def f(a, b):
    global wywolania, dodawania
    wywolania += 1
    if b == 0:
        return 0
    k = ostatnia(b)
    w = f(a, skroc(b))
    w = dopisz(w)
    while k > 0:
        w = w + a
        dodawania += 1
        k = k - 1
    return w


# 1.1
for a, b in [(42, 2), (4, 125), (103, 104)]:
    print(a, b, f(a, b))

# 1.2
wywolania = 0
f(987654321, 123456789)
print("1.2", wywolania)

# 1.3
for a, b in [(2024, 1000), (2024, 1234)]:
    dodawania = 0
    f(a, b)
    print("1.3", a, b, dodawania)
```

**Odpowiedź:** 1.1: f(42, 2) = 84, f(4, 125) = 500, f(103, 104) = 10712 (funkcja liczy a · b). 1.2: 10. 1.3: a) 1, b) 10.

## 2.1

```py
def polowy(k):
    dlugosc = 0
    x = k
    while x > 0:
        x = x // 10
        dlugosc = dlugosc + 1
    potega = 1
    for i in range(dlugosc // 2):
        potega = potega * 10
    a = k // potega
    b = k % potega
    return a, b


print(polowy(123456))
print(polowy(120056))
```

**Odpowiedź:** funkcja `polowy` (dla 123456 → a = 123, b = 456; dla 120056 → a = 120, b = 56).

## 2.2

```py
from math import gcd


def polowy(k):
    dlugosc = 0
    x = k
    while x > 0:
        x = x // 10
        dlugosc = dlugosc + 1
    potega = 10 ** (dlugosc // 2)
    return k // potega, k % potega


ile = 0
with open("liczby1.txt") as file:
    for wiersz in file:
        a, b = polowy(int(wiersz))
        if gcd(a, b) == 1:
            ile += 1
print(ile)
```

**Odpowiedź:** 296.

## 2.3

```py
def stopien_kaprekara(n):
    kwadrat = str(n * n)
    stopien = 0
    for i in range(1, len(kwadrat)):
        a = int(kwadrat[:i])
        b = int(kwadrat[i:])
        if a + b <= n:
            stopien += 1
    return stopien


najlepszy_stopien = -1
najlepsza_liczba = 0
with open("liczby2.txt") as file:
    for wiersz in file:
        n = int(wiersz)
        s = stopien_kaprekara(n)
        if s > najlepszy_stopien:
            najlepszy_stopien = s
            najlepsza_liczba = n
print(najlepszy_stopien)
print(najlepsza_liczba)
```

**Odpowiedź:** stopień 4, liczba 7746.

## 3.1, 3.2, 3.3 i 3.4

```py
with open("dane.txt") as file:
    napis = file.read().strip()

# wydzielenie liczb - maksymalnych ciągów cyfr
liczby = []
biezaca = ""
for znak in napis:
    if znak.isdigit():
        biezaca += znak
    else:
        if biezaca != "":
            liczby.append(biezaca)
        biezaca = ""
if biezaca != "":
    liczby.append(biezaca)

# 3.1
print("3.1", sum(1 for liczba in liczby if liczba.startswith("50")))

# 3.2
ile = [0] * 10
for znak in napis:
    if znak.isdigit():
        ile[int(znak)] += 1
najczestsza = ile.index(max(ile))
print("3.2", najczestsza, ile[najczestsza])

# 3.3
telefony = [liczba for liczba in liczby if len(liczba) == 9]
print("3.3")
for telefon in telefony:
    if telefon[0] == "5":
        print(telefon)

# 3.4
najmniej = min(len(set(telefon)) for telefon in telefony)
print("3.4")
for telefon in telefony:
    if len(set(telefon)) == najmniej:
        print(telefon)
```

**Odpowiedź:** 3.1: 4. 3.2: cyfra 1, 342 wystąpienia. 3.3: 588095244, 593151643, 583327270, 565269349, 583672019, 506585224, 574489008, 587103844, 510672749, 529135372, 515437684, 589477488. 3.4: 033035335, 050525250 (po 3 różne cyfry).
