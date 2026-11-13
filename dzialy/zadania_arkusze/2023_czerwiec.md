<h1 align="center">Matura 2023 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2023)</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

> W archiwum z danymi pliki do tego arkusza są w folderze `DANE_M` (folder `DANE_E` dotyczy arkusza w formule 2015).

## 1.1, 1.2 i 1.3

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
        print(x, y, k, z, z + z)
        return z + z
    dodawania += 2
    print(x, y, k, z, x + z + z)
    return x + z + z


def iloczyn_iteracyjny(x, y):
    z = 0
    while y >= 1:
        if y % 2 == 1:
            z = z + x
        x = x + x
        y = y // 2
    return z


# 1.1 - wiersze tabeli (od najgłębszego wywołania): x, y, k, z, wynik
iloczyn(10, 45)

# 1.2
for x, y in [(9, 11), (8, 32), (2, 47), (112, 112)]:
    dodawania = 0
    iloczyn(x, y)
    print("dodawań:", dodawania)

# 1.3
print(iloczyn_iteracyjny(10, 45), iloczyn_iteracyjny(112, 112))
```

**Odpowiedź:** 1.1 (x, y, k, z, wynik): (10, 45, 22, 220, 450), (10, 22, 11, 110, 220), (10, 11, 5, 50, 110), (10, 5, 2, 20, 50), (10, 2, 1, 10, 20), (10, 1, –, –, 10). 1.2: 8, 32 → 5; 2, 47 → 9; 112, 112 → 8. 1.3: `z ← 0`, `dopóki y ≥ 1`, `y ← y div 2` (funkcja `iloczyn_iteracyjny`).

## 2.1, 2.2, 2.3 i 2.4

```py
porownania = 0


def czy_mniejszy(n, s, k1, k2):
    # s indeksowane od 0, k1 i k2 od 1 (jak w treści)
    global porownania
    i = k1
    j = k2
    while i <= n and j <= n:
        porownania += 1  # pierwsza instrukcja jeżeli
        if s[i - 1] == s[j - 1]:
            i += 1
            j += 1
        elif s[i - 1] < s[j - 1]:
            return True
        else:
            return False
    return j <= n


# 2.1 - sprawdzenie odpowiedzi: s = aaaaaaaaaa, k1 = 2, k2 = 5
for s, k1, k2 in [("aaaaaaaaaa", 2, 5), ("ababababb", 1, 3)]:
    porownania = 0
    czy_mniejszy(len(s), s, k1, k2)
    print("2.1", s, k1, k2, porownania)

# 2.2
with open("wyniki2_2.txt", "w") as wyniki:
    for nazwa in ["slowa1.txt", "slowa2.txt", "slowa3.txt"]:
        with open(nazwa) as file:
            n = int(file.readline())
            s = file.readline().strip()
            k1, k2 = map(int, file.readline().split())
        odp = "TAK" if czy_mniejszy(n, s, k1, k2) else "NIE"
        print(nazwa, odp)
        wyniki.write(nazwa + " " + odp + "\n")


# 2.3 - sortowanie bąbelkowe numerów sufiksów
def tablica_sufiksow(n, s):
    T = [i for i in range(1, n + 1)]
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if not czy_mniejszy(n, s, T[j], T[j + 1]):
                T[j], T[j + 1] = T[j + 1], T[j]
    return T


print("2.3", tablica_sufiksow(10, "mascarpone"), tablica_sufiksow(11, "kalafiorowa"))

# 2.4 - najmniejszy sufiks
with open("slowa4.txt") as file, open("wyniki2_4.txt", "w") as wyniki:
    for linia in file:
        n, s = linia.split()
        n = int(n)
        najmniejszy = n
        for k in range(1, n):
            if czy_mniejszy(n, s, k, najmniejszy):
                najmniejszy = k
        print(s[najmniejszy - 1:])
        wyniki.write(s[najmniejszy - 1:] + "\n")
```

**Odpowiedź:** 2.1: np. s = aaaaaaaaaa, k1 = 2, k2 = 5 (6 porównań). 2.2: slowa1.txt TAK, slowa2.txt NIE, slowa3.txt NIE. 2.3: funkcja `tablica_sufiksow` (sortowanie bąbelkowe z porównaniem `czy_mniejszy`). 2.4: ato, a, abracadabrad, abecadlo, aaababbbbcaababaz, a, aaababbbbcaababaaabcaabb…, aaababbbbcaababaz, aaababbbbcaababacaacac…, aaababbbbcacbabaaabcaabb….

> W kluczu CKE do 2.1 pierwszy przykład (s = ababababb, k1 = 1, k2 = 3) daje 7 porównań, a nie 6 (6 równych par i jedna różna: s[7] = a, s[9] = b) — widać to w wyniku programu. Drugi przykład z klucza (aaaaaaaaaa, 2, 5) jest poprawny.

## 3.1, 3.2, 3.3 i 3.4

```py
with open("anagram.txt") as file:
    liczby = [linia.strip() for linia in file if linia.strip()]

# 3.1
zrownowazone = 0
prawie = 0
for x in liczby:
    roznica = x.count("1") - x.count("0")
    if roznica == 0:
        zrownowazone += 1
    elif abs(roznica) == 1:
        prawie += 1
print("3.1", zrownowazone, prawie, sep="\n")


# 3.2 - liczba anagramów: pierwsza cyfra to 1, pozostałe n-1 cyfr ustawiamy dowolnie
def silnia(n):
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik


def anagramy(x):
    jedynki = x.count("1") - 1
    zera = x.count("0")
    return silnia(jedynki + zera) // (silnia(jedynki) * silnia(zera))


osmiocyfrowe = [x for x in liczby if len(x) == 8]
najwiecej = max(anagramy(x) for x in osmiocyfrowe)
print("3.2")
for x in osmiocyfrowe:
    if anagramy(x) == najwiecej:
        print(x)

# 3.3
najwieksza = 0
for i in range(len(liczby) - 1):
    najwieksza = max(najwieksza, abs(int(liczby[i], 2) - int(liczby[i + 1], 2)))
print("3.3", bin(najwieksza)[2:])

# 3.4
bez_zera = 0
najlepsza = None
najlepsza_suma = -1
for x in liczby:
    dziesietna = str(int(x, 2))
    if "0" not in dziesietna:
        bez_zera += 1
    suma = sum(int(c) for c in set(dziesietna))
    if suma > najlepsza_suma:
        najlepsza_suma = suma
        najlepsza = dziesietna
print("3.4", bez_zera, najlepsza, sep="\n")
```

**Odpowiedź:** 3.1: 118 zrównoważonych, 219 prawie zrównoważonych. 3.2: 10110101, 11010100, 10100101, 11001001, 10110100, 11001101, 11000110 (po 35 anagramów). 3.3: 10011000111001. 3.4: a) 728, b) 7896.

## 4

```py
def na_dziesietny(napis, podstawa):
    liczba = 0
    for c in napis:
        liczba = liczba * podstawa + int(c)
    return liczba


def z_dziesietnego(liczba, podstawa):
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % podstawa) + wynik
        liczba = liczba // podstawa
    return wynik


print(z_dziesietnego(na_dziesietny("101201", 3), 9))
print(z_dziesietnego(na_dziesietny("2487", 9), 3))
```

**Odpowiedź:** 101201₃ = 351₉, 2487₉ = 2112221₃.
