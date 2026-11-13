<h1 align="center">Matura 2018 — maj, poziom rozszerzony (stara formuła)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2018-maj-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2018-maj-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2018-maj-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2018-maj-matura-stara-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.4

```py
def humor(n):
    # zwraca: liczbę wykonań pętli (*) dla k = n, tablicę T i wynik algorytmu
    T = [n]
    i = 0
    while True:
        k = T[i]
        suma = 0
        while k > 0:
            suma = suma + (k % 10) * (k % 10)
            k = k // 10
        if suma == 1:
            return T, "liczba wesoła"
        for j in range(i + 1):
            if T[j] == suma:
                return T, "liczba smutna"
        i = i + 1
        T.append(suma)


def ile_obrotow(k):
    # ile razy warunek k > 0 w wierszu (*) daje prawdę = liczba cyfr k
    ile = 0
    while k > 0:
        ile += 1
        k = k // 10
    return ile


# 1.1
print(ile_obrotow(15), ile_obrotow(5005))

# 1.2
print(humor(7))
print(humor(145))

# 1.4 - szukamy cyfr a, b, c, dla których liczba 94abc jest wesoła
for n in range(94000, 95000):
    T, wynik = humor(n)
    if wynik == "liczba wesoła":
        print(n, T)
        break

print(humor(94111))   # inny przykład: 81 + 16 + 1 + 1 + 1 = 100, a 1 + 0 + 0 = 1
```

**Odpowiedź:** 1.1: 15 → 2, 5005 → 4, x → liczba cyfr x, czyli ⌊log₁₀ x⌋ + 1. 1.2: n = 7: T = 7, 49, 97, 130, 10 – liczba wesoła; n = 145: T = 145, 42, 20, 4, 16, 37, 58, 89 – liczba smutna. 1.4: np. 94000 (T = [94000, 97, 130, 10]) albo 94111 (T = [94111, 100]).

> W kluczu przy 1.4 podano „94111, T=[100]” – według algorytmu T[0] = n, więc pełna zawartość tablicy to [94111, 100].

## 2.1 i 2.2

```py
def czy_automorficzna(n):
    potega = 10                 # najmniejsza potęga 10 większa od n, czyli 10^k
    while potega <= n:
        potega = potega * 10
    return n * n % potega == n


# 2.1
for n in [5, 6, 11, 25, 36, 76]:
    print(n, "TAK" if czy_automorficzna(n) else "NIE")

# 2.2
n = int(input())
if czy_automorficzna(n):
    print("Tak")
else:
    print("Nie")
```

**Odpowiedź:** 2.1: 6 – TAK, 11 – NIE, 25 – TAK, 36 – NIE, 76 – TAK. 2.2: funkcja `czy_automorficzna` (10^k liczymy jako najmniejszą potęgę 10 większą od n).

## 6.1, 6.2 i 6.3

```py
pary = []
with open("slowa.txt") as file:
    for line in file:
        pary.append(line.split())

# 6.1
ile = 0
for slowo1, slowo2 in pary:
    if slowo1[-1] == "A":
        ile += 1
    if slowo2[-1] == "A":
        ile += 1
print("6.1", ile)

# 6.2
ile = 0
for slowo1, slowo2 in pary:
    if slowo1 in slowo2:
        ile += 1
print("6.2", ile)

# 6.3
anagramy = []
for slowo1, slowo2 in pary:
    if sorted(slowo1) == sorted(slowo2):
        anagramy.append((slowo1, slowo2))
print("6.3", len(anagramy))
for slowo1, slowo2 in anagramy:
    print(slowo1, slowo2)
```

**Odpowiedź:** 6.1: 71; 6.2: 234; 6.3: 38 par (AYE YEA, BRD RDB, BWRHQ BWRHQ, DANHC DANHC, DCCD CDDC, …)
