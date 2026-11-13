<h1 align="center">Matura 2026 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2023)</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

```py
def szyfr(tekst, k):
    # tablice T i S indeksowane od 1, jak w treści (pozycja 0 nieużywana)
    n = len(tekst)
    T = [""] + list(tekst)
    S = [""] * (n + 1)
    a = n // k
    c = n - a
    for i in range(1, n + 1):
        if i % k == 0:
            b = i // k
            S[n - a + b] = T[i]
        else:
            S[c] = T[i]
            c = c - 1
    return "".join(S[1:])


# 1.1
print(szyfr("defragmentacja", 3))
print(szyfr("tropikalny", 5))

# 1.2 - dla k = 1 każdy znak trafia na swoje miejsce
print(szyfr("serwer", 1))

# 1.3 - dla k > n (np. k = n + 1) warunek i mod k = 0 nigdy nie zachodzi,
# więc znaki są wpisywane od końca
print(szyfr("serwer", len("serwer") + 1))
```

**Odpowiedź:** 1.1: defragmentacja, k = 3 → ajatemaredfgnc; tropikalny, k = 5 → nlakportiy. 1.2: k = 1. 1.3: k = n + 1 (dowolne k > n).

## 2.1 i 2.2

```py
def najwieksze_k(T):
    # T indeksowana od 0; sprawdzamy kolejne k od n - 1 w dół
    n = len(T)
    k = n - 1
    while k > 0:
        jest = True
        for i in range(k):
            if T[i] != T[n - k + i]:
                jest = False
        if jest:
            return k
        k = k - 1
    return 0


print(najwieksze_k([1, 2, 1, 1, 2, 1, 1]))  # przykład z treści: 4
print(najwieksze_k([1, 2, 3, 4]))
print(najwieksze_k([3, 5, 3, 5, 3, 5, 3, 5, 3, 5]))
```

**Odpowiedź:** 2.1: [1,2,3,4] → 0, [3,5,3,5,3,5,3,5,3,5] → 8. 2.2: funkcja `najwieksze_k` powyżej.

> W zasadach oceniania w pierwszym wierszu tabeli do 2.1 wpisano tablicę [1,2,3,2,4] zamiast [1,2,3,4] z arkusza — wynik (0) jest dla obu taki sam.

## 3.1

```py
with open("dane.txt") as file:
    napis = file.readline().strip()

pary = [napis[i:i + 2] for i in range(0, len(napis), 2)]
licznik = 0
for i in range(len(pary) - 1):
    if pary[i] == pary[i + 1]:
        licznik += 1

print(licznik)
```

**Odpowiedź:** 17

## 3.2

```py
def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    d = 2
    while d * d <= liczba:
        if liczba % d == 0:
            return False
        d += 1
    return True


with open("dane.txt") as file:
    napis = file.readline().strip()

najdluzszy = ""
for poczatek in range(0, len(napis), 2):  # fragment zaczyna się od początku np-pary
    suma = 0
    for koniec in range(poczatek, len(napis), 2):
        suma += ord(napis[koniec]) + ord(napis[koniec + 1])
        if czy_pierwsza(suma) and koniec + 2 - poczatek > len(najdluzszy):
            najdluzszy = napis[poczatek:koniec + 2]

print(najdluzszy)
```

**Odpowiedź:** INRZWZASEKYPYPYIEKDLEKODASINWNWNUPJNINEKYPDLUZASJNINYPUPWZRZ… (napis długości 544, zgodny z kluczem w całości)

## 3.3

```py
with open("dane.txt") as file:
    napis = file.readline().strip()

ile = {}
for i in range(0, len(napis), 2):
    para = napis[i:i + 2]
    ile[para] = ile.get(para, 0) + 1

pary = sorted(ile, key=lambda para: ile[para])
print("".join(pary))
```

**Odpowiedź:** BYLTOZIELONYUPRAWNYIURODZAJNYPASWZDLUZRZEKINIL

## 4.1, 4.2 i 4.3

```py
miasta = []  # (x, y, wielkosc); miasto nr i ma indeks i - 1
with open("mapa.txt") as file:
    for linia in file:
        x, y, wielkosc = map(int, linia.split())
        miasta.append((x, y, wielkosc))
n = len(miasta)

# 4.1
numer = 0
for i in range(n):
    if miasta[i][2] > miasta[numer][2]:
        numer = i
print("4.1", numer + 1, miasta[numer][2])

# 4.2
najmniejsza = 10 ** 9
pary = []
for i in range(n):
    for j in range(i + 1, n):
        d = abs(miasta[i][0] - miasta[j][0]) + abs(miasta[i][1] - miasta[j][1])
        if d < najmniejsza:
            najmniejsza = d
            pary = [(i + 1, j + 1)]
        elif d == najmniejsza:
            pary.append((i + 1, j + 1))
print("4.2", najmniejsza)
for a, b in pary:
    print(a, b)

# 4.3 - kwadrat (0,0)-(bok,bok), liczymy tylko miasta leżące wewnątrz
najwiekszy_bok = 0
for bok in range(1, 501):
    ludnosc = 0
    for x, y, wielkosc in miasta:
        if 0 < x < bok and 0 < y < bok:
            ludnosc += wielkosc
    if ludnosc / (bok * bok) > 2:
        najwiekszy_bok = bok
        najwieksza_ludnosc = ludnosc
print("4.3", najwiekszy_bok, najwieksza_ludnosc)
```

**Odpowiedź:** 4.1: 254 2483; 4.2: odległość 2, pary: 30 170, 120 176, 422 637, 426 599, 737 778; 4.3: 114 26078.

## 5

```py
def na_system(liczba, podstawa):
    cyfry = ""
    while liczba > 0:
        cyfry = str(liczba % podstawa) + cyfry
        liczba //= podstawa
    return cyfry


# 1251(6) + x(6) = 500(10) = y(3) - 110102(3)
x = 500 - int("1251", 6)
y = 500 + int("110102", 3)
print(na_system(x, 6), na_system(y, 3))
```

**Odpowiedź:** (1251)₆ + (501)₆ = (500)₁₀ = (1010221)₃ − (110102)₃
