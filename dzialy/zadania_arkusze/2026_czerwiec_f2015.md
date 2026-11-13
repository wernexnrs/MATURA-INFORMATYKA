<h1 align="center">Matura 2026 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-stara-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

```py
def szyfr(T, k):
    n = len(T)
    S = [""] * (n + 1)              # indeksy 1..n
    a = n // k
    c = n - a
    for i in range(1, n + 1):
        if i % k == 0:
            b = i // k
            S[n - a + b] = T[i - 1]
        else:
            S[c] = T[i - 1]
            c = c - 1
    return "".join(S[1:])


# 1.1
for tekst, k in [("korporacja", 6), ("tropikalny", 5), ("defragmentacja", 3)]:
    print(tekst, k, szyfr(tekst, k))

# 1.2 i 1.3 - szyfrogramy słowa "serwer" (n = 6) dla różnych kluczy
for k in range(1, 9):
    print(k, szyfr("serwer", k))
```

**Odpowiedź:** 1.1: korporacja (k = 6) → ajcaoprokr; tropikalny (k = 5) → nlakportiy; defragmentacja (k = 3) → ajatemaredfgnc. 1.2: k = 1. 1.3: k = n + 1 (lub dowolne k > n).

## 2.1 i 2.2

```py
# 2.2
def najwieksze_k(T):
    n = len(T)
    k = n - 1
    while k > 0:
        jest = True
        for i in range(k):                  # porównujemy T[1..k] z T[n-k+1..n]
            if T[i] != T[n - k + i]:
                jest = False
        if jest:
            return k
        k -= 1
    return 0


# 2.1
for T in [[1, 2, 3, 4], [1, 3, 4, 1, 1, 3, 4, 1], [3, 5, 3, 5, 3, 5, 3, 5, 3, 5]]:
    print(T, najwieksze_k(T))
```

**Odpowiedź:** 2.1: 0, 4, 8. 2.2: funkcja `najwieksze_k`.

## 4.1, 4.2, 4.3 i 4.4

```py
with open("dane.txt") as file:
    napis = file.read().strip()

pary = [napis[i:i + 2] for i in range(0, len(napis), 2)]      # kolejne np-pary
wynik = open("wyniki4.txt", "w")


def pierwsza(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def suma_kodow(tekst):
    return sum(ord(c) for c in tekst)


# 4.1
ile = 0
for i in range(1, len(pary)):
    if pary[i] == pary[i - 1]:
        ile += 1
print("4.1", ile, file=wynik)

# 4.2
wypisane = []
for para in pary:
    if pierwsza(suma_kodow(para)) and para not in wypisane:
        wypisane.append(para)
print("4.2", *wypisane, file=wynik)

# 4.3 - sprawdzamy wszystkie fragmenty pary[p..q]
najlepszy = ""
for p in range(len(pary)):
    suma = 0
    for q in range(p, len(pary)):
        suma += suma_kodow(pary[q])
        if pierwsza(suma) and 2 * (q - p + 1) > len(najlepszy):
            najlepszy = "".join(pary[p:q + 1])
print("4.3", najlepszy, suma_kodow(najlepszy), file=wynik)

# 4.4
licznik = {}
for para in pary:
    licznik[para] = licznik.get(para, 0) + 1
kolejnosc = sorted(licznik, key=lambda para: licznik[para])
print("4.4", "".join(kolejnosc), licznik[kolejnosc[-1]], licznik[kolejnosc[0]], file=wynik)

wynik.close()
```

**Odpowiedź:** 4.1: 17. 4.2: IN IL NY UR. 4.3: fragment INRZWZASEKYPYPYIEKDLEKODASINWNWNUP… (272 np-pary, kończy się …JNRAINYIRAWZODNY), suma kodów 42923. 4.4: BYLTOZIELONYUPRAWNYIURODZAJNYPASWZDLUZRZEKINIL, najwięcej wystąpień 23, najmniej 1.
