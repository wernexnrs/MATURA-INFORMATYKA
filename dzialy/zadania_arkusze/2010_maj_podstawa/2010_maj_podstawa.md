<h1 align="center">2010 Maj — poziom podstawowy</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2010-maj-matura-podstawowa.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2010-maj-matura-podstawowa-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2010-maj-matura-podstawowa-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2010-maj-matura-podstawowa-odpowiedzi.pdf)

## 1a

```py
def szyfruj(s, k):
    w = ""
    i = 0
    while i < k:
        j = i
        while j < len(s):
            w = w + s[j]
            j = j + k
        i = i + 1
    return w


print(szyfruj("ARKA", 2), szyfruj("MOTOR", 2))
```
**Odpowiedź:** AKRA, MTROO (kluczem jest k)

## 1c

```py
def szyfruj_pary(s):
    w = ""
    i = 0
    while i + 1 < len(s):
        w = w + s[i + 1] + s[i]
        i = i + 2
    if i < len(s):  # nieparzysta długość - ostatni znak bez zmian
        w = w + s[i]
    return w


print(szyfruj_pary("MOTOR"), szyfruj_pary("MATURA"))
```
**Odpowiedź:** OMOTR, AMUTAR

## 2a i 2b

```py
def czynniki_pierwsze(n):
    czynniki = []
    dzielnik = 2
    while n > 1:
        while n % dzielnik == 0:
            czynniki.append(dzielnik)
            n = n // dzielnik
        dzielnik = dzielnik + 1
    return czynniki


for n in [63, 184, 277]:
    print(n, czynniki_pierwsze(n))
```
**Odpowiedź:** 63 = 3·3·7; 184 = 2·2·2·23; 277 = 277

## 4

```py
with open("dane.txt") as file:
    with open("zadanie4.txt", "w") as wynik:
        for line in file:
            slowo = line.strip()
            if slowo == slowo[::-1]:
                print(slowo)
                wynik.write(slowo + "\n")
```
**Odpowiedź:** CBJBC, AABBHHIHHBBAA, CCJGJCC, FDDFFFDDF, BCACHCACB, DFDCCDFD, DFFFD, AABBAA, … (42 palindromy)

## 5a i 5b

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
def koszt_a(x):  # koszt w groszach
    if x <= 500:
        return x * 85 * 12
    return x * 75 * 12


def koszt_b(x):
    if x <= 300:
        return x * 90 * 12
    if x <= 600:
        return 300 * 90 * 12 + (x - 300) * 75 * 12
    return x * 65 * 12


# a) przedziały, w których A jest tańszy
przedzialy = []
for x in range(10, 1001, 10):
    if koszt_a(x) < koszt_b(x):
        if przedzialy and przedzialy[-1][1] == x - 10:
            przedzialy[-1][1] = x
        else:
            przedzialy.append([x, x])
print("a)", przedzialy)

# b) ten sam koszt
for x in range(10, 1001, 10):
    if koszt_a(x) == koszt_b(x):
        print("b)", x)
```
**Odpowiedź:** a) <10, 440> i <510, 600>; b) 450 sztuk

## 5c i 5d

*Zadanie na Excel — rozwiązanie w Pythonie.*

```py
def koszt_a(x):  # koszt w groszach
    if x <= 500:
        return x * 85 * 12
    return x * 75 * 12


def koszt_b(x):
    if x <= 300:
        return x * 90 * 12
    if x <= 600:
        return 300 * 90 * 12 + (x - 300) * 75 * 12
    return x * 65 * 12


najwiecej_c = 0
najwiecej_d = 0
for x in range(10, 1001, 10):
    if koszt_a(x) < koszt_b(500):
        najwiecej_c = x
    if koszt_b(x) < koszt_a(600):
        najwiecej_d = x

print("c)", najwiecej_c)
print("d)", najwiecej_d)
```
**Odpowiedź:** c) 550 sztuk; d) 690 sztuk

## 6a

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
najwyzszy = {"s": (0, ""), "c": (0, "")}

with open("noworodki.txt", encoding="cp1250") as file:
    for line in file:
        id_dziecka, plec, imie, data, waga, wzrost, id_matki = line.split()
        if int(wzrost) > najwyzszy[plec][0]:
            najwyzszy[plec] = (int(wzrost), imie)

print("chłopiec:", najwyzszy["s"][1], najwyzszy["s"][0])
print("dziewczynka:", najwyzszy["c"][1], najwyzszy["c"][0])
```
**Odpowiedź:** chłopiec: Oskar 62, dziewczynka: Maja 61

## 6b

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
urodzenia = {}

with open("noworodki.txt", encoding="cp1250") as file:
    for line in file:
        id_dziecka, plec, imie, data, waga, wzrost, id_matki = line.split()
        urodzenia[data] = urodzenia.get(data, 0) + 1

najwiecej = max(urodzenia, key=urodzenia.get)
print(najwiecej, urodzenia[najwiecej])
```
**Odpowiedź:** 1999-11-20, 23 dzieci

## 6c

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
mamy = {}

with open("mamy.txt", encoding="cp1250") as file:
    for line in file:
        id_matki, imie, wiek = line.split()
        mamy[id_matki] = (imie, int(wiek))

imiona = set()
with open("noworodki.txt", encoding="cp1250") as file:
    for line in file:
        id_dziecka, plec, imie, data, waga, wzrost, id_matki = line.split()
        if int(waga) > 4000 and mamy[id_matki][1] < 25:
            imiona.add(mamy[id_matki][0])

print(sorted(imiona))
```
**Odpowiedź:** Barbara, Eliza, Janina, Maria, Marzena, Paulina

## 6d

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
mamy = {}

with open("mamy.txt", encoding="cp1250") as file:
    for line in file:
        id_matki, imie, wiek = line.split()
        mamy[id_matki] = imie

with open("noworodki.txt", encoding="cp1250") as file:
    for line in file:
        id_dziecka, plec, imie, data, waga, wzrost, id_matki = line.split()
        if plec == "c" and imie == mamy[id_matki]:
            print(imie, data)
```
**Odpowiedź:** Anna 1999-11-21, Wiktoria 1999-11-20

## 6e

*Zadanie na Access — rozwiązanie w Pythonie.*

```py
porody = {}

with open("noworodki.txt", encoding="cp1250") as file:
    for line in file:
        id_dziecka, plec, imie, data, waga, wzrost, id_matki = line.split()
        porody[(data, id_matki)] = porody.get((data, id_matki), 0) + 1

daty = set()
for data, id_matki in porody:
    if porody[(data, id_matki)] == 2:
        daty.add(data)

for data in sorted(daty):
    print(data)
```
**Odpowiedź:** 1999-11-19, 1999-11-21, 1999-11-22, 1999-11-23, 1999-12-09, 1999-12-12
