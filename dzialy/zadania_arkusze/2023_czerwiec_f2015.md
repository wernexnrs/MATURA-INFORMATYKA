<h1 align="center">Matura 2023 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-stara-rozszerzona-odpowiedzi.pdf)

> Pliki do zadania 4 są w archiwum w folderze `DANE/DANE_E`.

## 1.1 i 1.2

```py
def suma_cyfr(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


# 1.2 - tylko operacje na liczbach całkowitych
def dobre_przyjaciolki(a, b):
    ostatnia_a = a % 10
    ostatnia_b = b % 10
    suma_a = 0
    while a > 0:
        if a < 10:
            pierwsza_a = a
        suma_a += a % 10
        a //= 10
    suma_b = 0
    while b > 0:
        if b < 10:
            pierwsza_b = b
        suma_b += b % 10
        b //= 10
    if suma_a != suma_b:
        return False
    return pierwsza_a == ostatnia_b or pierwsza_b == ostatnia_a


# 1.1
for a, b in [(131, 50), (416, 84), (32, 221)]:
    print(a, b, suma_cyfr(a), suma_cyfr(b), suma_cyfr(a) == suma_cyfr(b), dobre_przyjaciolki(a, b))
```

**Odpowiedź:** 1.1: 131 i 50: 5, 5, PRAWDA, FAŁSZ; 416 i 84: 11, 12, FAŁSZ, FAŁSZ; 32 i 221: 5, 5, PRAWDA, PRAWDA. 1.2: funkcja `dobre_przyjaciolki`.

## 2.1, 2.2 i 2.3

```py
dodawania = 0


def iloczyn(x, y):
    global dodawania
    if y == 1:
        return x
    k = y // 2
    z = iloczyn(x, k)
    if y % 2 == 0:
        dodawania += 1
        wynik = z + z
    else:
        dodawania += 2
        wynik = x + z + z
    print(x, y, k, z, wynik)        # 2.1 - wiersz tabeli (wypisywane od najgłębszego wywołania)
    return wynik


# 2.3 - wersja iteracyjna
def iloczyn_iter(x, y):
    z = 0
    while y >= 1:
        if y % 2 == 1:
            z = z + x
        x = x + x
        y = y // 2
    return z


# 2.1
iloczyn(10, 45)

# 2.2
for x, y in [(9, 11), (8, 32), (2, 47), (112, 112)]:
    dodawania = 0
    iloczyn(x, y)
    print("liczba dodawań:", x, y, dodawania)

# 2.3 - sprawdzenie
print(all(iloczyn_iter(x, y) == x * y for x in range(1, 50) for y in range(1, 50)))
```

**Odpowiedź:** 2.1: (x, y, k, z, wynik): (10, 45, 22, 220, 450), (10, 22, 11, 110, 220), (10, 11, 5, 50, 110), (10, 5, 2, 20, 50), (10, 2, 1, 10, 20), (10, 1, –, –, 10). 2.2: 5, 5, 9, 8. 2.3: `z ← 0`, `dopóki y ≥ 1` (tzn. y > 0), `y ← y div 2`.

## 4.1, 4.2, 4.3 i 4.4

```py
with open("anagram.txt") as file:
    liczby = [linia.strip() for linia in file if linia.strip()]

wynik = open("wyniki4.txt", "w")

# 4.1
zrownowazone = 0
prawie = 0
for liczba in liczby:
    roznica = abs(liczba.count("1") - liczba.count("0"))
    if roznica == 0:
        zrownowazone += 1
    elif roznica == 1:
        prawie += 1
print("4.1", zrownowazone, prawie, file=wynik)


# 4.2 - pierwsza cyfra musi być 1, pozostałe jedynki rozmieszczamy na 7 miejscach: C(7, jedynki - 1)
def silnia(n):
    s = 1
    for i in range(2, n + 1):
        s *= i
    return s


def anagramy(liczba):
    reszta = len(liczba) - 1
    jedynki = liczba.count("1") - 1
    return silnia(reszta) // (silnia(jedynki) * silnia(reszta - jedynki))


osmiocyfrowe = [liczba for liczba in liczby if len(liczba) == 8]
najwiecej = max(anagramy(liczba) for liczba in osmiocyfrowe)
print("4.2", file=wynik)
for liczba in osmiocyfrowe:
    if anagramy(liczba) == najwiecej:
        print(liczba, file=wynik)

# 4.3
dziesietne = [int(liczba, 2) for liczba in liczby]
najwieksza = 0
for i in range(1, len(dziesietne)):
    najwieksza = max(najwieksza, abs(dziesietne[i] - dziesietne[i - 1]))
print("4.3", bin(najwieksza)[2:], file=wynik)

# 4.4
bez_zera = 0
najlepsza = dziesietne[0]
for x in dziesietne:
    if "0" not in str(x):
        bez_zera += 1
    if sum(int(c) for c in set(str(x))) > sum(int(c) for c in set(str(najlepsza))):
        najlepsza = x
print("4.4", bez_zera, najlepsza, file=wynik)

wynik.close()
```

**Odpowiedź:** 4.1: 118 zrównoważonych, 219 prawie zrównoważonych. 4.2: 10110101, 11010100, 10100101, 11001001, 10110100, 11001101, 11000110. 4.3: 10011000111001. 4.4: a) 728, b) 7896.
