<h1 align="center">Matura 2010 — maj, poziom podstawowy</h1>
 
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
