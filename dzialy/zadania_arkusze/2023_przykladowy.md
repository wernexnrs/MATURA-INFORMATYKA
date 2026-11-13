<h1 align="center">Przykładowy arkusz CKE — formuła 2023</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2023-przykladowy-arkusz-cke-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2023-przykladowy-arkusz-cke-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2023-przykladowy-arkusz-cke-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

```py
def wczytaj_plansze(nazwa):
    plansze = []
    with open(nazwa) as file:
        wiersze = [linia.strip() for linia in file]
    for i in range(0, len(wiersze), 9):
        if len(wiersze[i:i + 8]) == 8 and wiersze[i]:
            plansze.append(wiersze[i:i + 8])
    return plansze


plansze = wczytaj_plansze("szachy.txt")

# 1.1
ile_plansz = 0
max_pustych = 0
for p in plansze:
    puste = 0
    for k in range(8):
        if all(p[w][k] == "." for w in range(8)):
            puste += 1
    if puste > 0:
        ile_plansz += 1
        max_pustych = max(max_pustych, puste)
print("1.1", ile_plansz, max_pustych)

# 1.2
ile_rownowag = 0
min_bierek = 64
for p in plansze:
    biale = []
    czarne = []
    for wiersz in p:
        for znak in wiersz:
            if znak.isupper():
                biale.append(znak)
            elif znak.islower():
                czarne.append(znak.upper())
    if sorted(biale) == sorted(czarne):
        ile_rownowag += 1
        min_bierek = min(min_bierek, len(biale) + len(czarne))
print("1.2", ile_rownowag, min_bierek)


# 1.3
def szachuje(p, wieza, krol):
    # czy jakaś wieża (znak wieza) szachuje króla (znak krol)
    for w in range(8):
        for k in range(8):
            if p[w][k] != wieza:
                continue
            for dw, dk in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = w + dw, k + dk
                while 0 <= x < 8 and 0 <= y < 8 and p[x][y] == ".":
                    x, y = x + dw, y + dk
                if 0 <= x < 8 and 0 <= y < 8 and p[x][y] == krol:
                    return True
    return False


biala = 0
czarna = 0
for p in plansze:
    if szachuje(p, "W", "k"):
        biala += 1
    if szachuje(p, "w", "K"):
        czarna += 1
print("1.3", biala, czarna)
```

**Odpowiedź:** 1.1: `36 3`. 1.2: `22 28`. 1.3: `3 1`.

## 2.1, 2.2 i 2.3

```py
def gra(A, s):
    B = [False] * (s + 1)
    B[0] = True
    for a in A:  # Tura(k)
        for i in range(s, a - 1, -1):
            if B[i - a] and not B[i]:
                B[i] = True
    return B


# 2.1
for A, s in [([1, 2, 3], 5), ([1, 2, 5, 10], 14), ([13, 5, 5, 2, 7], 17), ([7, 6, 5, 4, 3, 2, 1], 25)]:
    print("2.1", A, s, "TAK" if gra(A, s)[s] else "NIE")

# 2.2
A = list(range(5, 101, 5))
print("2.2", sum(gra(A, 500)))

# 2.3 - sprawdzenie przykładowej odpowiedzi
A = [1, 2, 4, 8, 16, 32, 64, 128]
print("2.3", all(gra(A, s)[s] for s in range(1, 201)))
```

**Odpowiedź:** 2.1: TAK (dane), NIE, TAK, TAK. 2.2: 101 (pola B[0], B[5], …, B[500]). 2.3: np. A = [1, 2, 4, 8, 16, 32, 64, 128] (każde s od 1 do 255 da się zapisać jako sumę różnych potęg dwójki).

## 3.1, 3.2, 3.3, 3.4 i 3.5

```py
def potega_mod(a, x, M):
    # szybkie potęgowanie modularne - O(log x) mnożeń
    wynik = 1
    a = a % M
    while x > 0:
        if x % 2 == 1:
            wynik = wynik * a % M
        a = a * a % M
        x = x // 2
    return wynik


def czy_pierwsza(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def nwd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 3.1
print("3.1", potega_mod(3, 3, 11), potega_mod(9, 2, 80))
for M, a, b in [(31, 5, 25), (59, 2, 5)]:
    x = 0
    while potega_mod(a, x, M) != b:
        x += 1
    print("3.1 x =", x)

trojki = []
with open("liczby.txt") as file:
    for linia in file:
        M, a, b = map(int, linia.split())
        trojki.append((M, a, b))

# 3.3
print("3.3", sum(1 for M, a, b in trojki if czy_pierwsza(M)))

# 3.4
print("3.4", sum(1 for M, a, b in trojki if nwd(M, a) == 1))

# 3.5
ile = 0
for M, a, b in trojki:
    potega = 1 % M  # a^0 mod M
    for x in range(M):
        if potega == b:
            ile += 1
            break
        potega = potega * a % M
print("3.5", ile)
```

**Odpowiedź:** 3.1: b = 5 (M = 11), x = 2 (M = 31), x = 6 (M = 59), b = 1 (M = 80). 3.2: funkcja `potega_mod` (szybkie potęgowanie, O(log x)). 3.3: 343. 3.4: 712. 3.5: 764.
