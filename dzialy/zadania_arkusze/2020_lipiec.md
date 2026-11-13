<h1 align="center">Matura 2020 — lipiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2020-lipiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2020-lipiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2020-lipiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2020-lipiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

```py
n = 10
P = [0] * (n + 1)  # indeksy 1..n, jak w treści
S = [0] * (n + 1)

for i in range(1, n + 1):
    P[i] = 1
    S[i] = 0

# sito Eratostenesa: P[j] = 1 dla liczb pierwszych (oraz dla 1, której pętla nie rusza)
for j in range(2, n + 1):
    if P[j] == 1:
        i = j * j
        while i <= n:
            P[i] = 0
            i = i + j
    # S[j] - ile liczb pierwszych jest w przedziale [2, j]
    S[j] = S[j - 1] + P[j]

print(P[1:])
print(S[1:])

# 1.3 - S[b] - S[a - 1] = suma P[a..b], a > 1, więc to liczba liczb pierwszych w [a, b]
a, b = 3, 10
print(S[b] - S[a - 1])
```
**Odpowiedź:** 1.1: P = 1, 1, 1, 0, 1, 0, 1, 0, 0, 0; 1.2: S = 0, 1, 2, 2, 3, 3, 4, 4, 4, 4; 1.3: B (liczba liczb pierwszych w przedziale [a, b])

## 2.1 i 2.2

```py
def rozklad(p, q):
    # rozkład p/q (p < q) na sumę ułamków egipskich - zwraca mianowniki
    mianowniki = []
    while p > 0:
        m = (q + p - 1) // p  # sufit z q/p - najmniejsze m, dla którego 1/m <= p/q
        mianowniki.append(m)
        # p/q - 1/m = (p*m - q) / (q*m)
        p, q = p * m - q, q * m
    return mianowniki


print(rozklad(8, 15))
print(rozklad(5, 6))
print(rozklad(4, 5))
```
**Odpowiedź:** 2.1: 8/15 = 1/2 + 1/30; 5/6 = 1/2 + 1/3. 2.2: algorytm powyżej (dla 4/5: 2, 4, 20)

## 4.1, 4.2 i 4.3

```py
identyfikatory = []
with open("identyfikator.txt") as file:
    for line in file:
        identyfikatory.append(line.strip())


def suma_cyfr(liczba):
    suma = 0
    for c in liczba:
        suma += int(c)
    return suma


# 4.1
najwieksza = max(suma_cyfr(x[3:]) for x in identyfikatory)
with open("wyniki4_1.txt", "w") as wynik:
    for x in identyfikatory:
        if suma_cyfr(x[3:]) == najwieksza:
            print(x, file=wynik)

# 4.2
with open("wyniki4_2.txt", "w") as wynik:
    for x in identyfikatory:
        seria, numer = x[:3], x[3:]
        if seria == seria[::-1] or numer == numer[::-1]:
            print(x, file=wynik)

# 4.3
wagi = [7, 3, 1, 7, 3, 1, 7, 3]


def czy_poprawny(x):
    # litery A..Z -> 10..35, cyfra kontrolna x[3] pomijana
    wartosci = []
    for c in x[:3]:
        wartosci.append(ord(c) - ord("A") + 10)
    for c in x[4:]:
        wartosci.append(int(c))
    suma = 0
    for i in range(len(wagi)):
        suma += wagi[i] * wartosci[i]
    return suma % 10 == int(x[3])


with open("wyniki4_3.txt", "w") as wynik:
    for x in identyfikatory:
        if not czy_poprawny(x):
            print(x, file=wynik)
```
**Odpowiedź:** 4.1: GYJ959787, JOK786969 (suma cyfr 45). 4.2: MBF340043, JKJ452719, GFG148345, AXA231829, KIK866983, LOL695279. 4.3: LIK235378, MBF340043, HFG378931, KIJ511146, NUK840936, OKH427482, RTS278686
