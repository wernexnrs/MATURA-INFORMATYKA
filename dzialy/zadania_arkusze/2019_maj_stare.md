<h1 align="center">Matura 2019 — maj, poziom rozszerzony (stara formuła)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2019-maj-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2019-maj-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2019-maj-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2019-maj-matura-stara-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.3

```py
def oblicz_C(A):
    n = len(A)
    C = [0] * n
    for i in range(n):
        C[i] = 1
        for j in range(i):
            if A[j] < A[i] and C[j] + 1 > C[i]:
                C[i] = C[j] + 1
    return C


# 1.1
for A in [[4, 2, 3, 1, 5], [3, 3, 3, 3], [1, 2, 3, 4], [1, 3, 2, 5],
          [3, 5, 1, 4, 6, 7, 2, 10, 9, 11], [3, 1, 4, 2, 6, 5, 7]]:
    print(A, oblicz_C(A))

# 1.3 - C[i] to długość najdłuższego rosnącego podciągu kończącego się na A[i],
# więc potrzebny jest rosnący podciąg długości 6, ale nie 7
A = [1, 2, 3, 4, 5, 6, 1, 1]
print(A, oblicz_C(A), max(oblicz_C(A)))
```

**Odpowiedź:** 1.1: [1,2,3,4] → [1,2,3,4], [1,3,2,5] → [1,2,2,3], [3,5,1,4,6,7,2,10,9,11] → [1,2,1,2,3,4,2,5,5,6], [3,1,4,2,6,5,7] → [1,1,2,2,3,3,4]. 1.3: np. [1,2,3,4,5,6,1,1] (rosnący podciąg długości 6, brak rosnącego podciągu długości 7).

> W kluczu w wierszu trzecim tablicy A wpisano omyłkowo [6,5,1,4,6,7,2,10,9,11] zamiast [3,5,1,4,6,7,2,10,9,11] z arkusza; podana tablica C ([1,2,1,2,3,4,2,5,5,6]) odpowiada tablicy z arkusza.

## 2.1, 2.2 i 2.3

```py
def pot(a, k):
    # a^k mod k - po każdym mnożeniu bierzemy resztę, żeby liczby nie rosły
    p = 1
    for i in range(k):
        p = p * a % k
    return p


def testF(k):
    for a in range(2, k):
        if pot(a, k) != a:
            return 0
    return 1


def czy_pierwsza(k):
    if k < 2:
        return 0
    d = 2
    while d * d <= k:
        if k % d == 0:
            return 0
        d += 1
    return 1


def czyLC(k):
    # liczba Carmichaela = złożona, ale przechodzi test Fermata
    if testF(k) == 1 and czy_pierwsza(k) == 0:
        return 1
    return 0


print(pot(3, 7), testF(7), testF(9))
print([k for k in range(3, 3000) if czyLC(k) == 1])
```

**Odpowiedź:** funkcje `pot`, `testF` i `czyLC`; sprawdzenie: pot(3, 7) = 3, testF(7) = 1, testF(9) = 0, liczby Carmichaela < 3000: 561, 1105, 1729, 2465, 2821.

## 4.1, 4.2 i 4.3

```py
mapy = []
with open("dzialki.txt") as file:
    wiersze = [line.strip() for line in file if line.strip() != ""]
for m in range(len(wiersze) // 30):
    mapy.append(wiersze[30 * m: 30 * m + 30])

# 4.1
ile = 0
for mapa in mapy:
    trawa = 0
    for wiersz in mapa:
        trawa += wiersz.count("*")
    if trawa >= 0.7 * 30 * 30:
        ile += 1
print("4.1", ile)


# 4.2 - obrót o 180 stopni: odwracamy kolejność wierszy i każdy wiersz
def obrot(mapa):
    return [wiersz[::-1] for wiersz in mapa[::-1]]


print("4.2", end=" ")
for i in range(len(mapy)):
    for j in range(i + 1, len(mapy)):
        if obrot(mapy[i]) == mapy[j]:
            print(i + 1, j + 1, end=" ")
print()


# 4.3
def najwiekszy_plac(mapa):
    bok = 0
    # kwadrat o boku bok + 1 mieści się, gdy w wierszach i kolumnach 0..bok nie ma X
    while bok < 30:
        dobry = True
        for i in range(bok + 1):
            for j in range(bok + 1):
                if mapa[i][j] == "X":
                    dobry = False
        if not dobry:
            break
        bok += 1
    return bok


boki = [najwiekszy_plac(mapa) for mapa in mapy]
najwiekszy = max(boki)
print("4.3", najwiekszy, end=" ")
for i in range(len(mapy)):
    if boki[i] == najwiekszy:
        print(i + 1, end=" ")
print()
```

**Odpowiedź:** 4.1: 5; 4.2: działki 14 i 39; 4.3: bok 12, działki 28, 32, 45
