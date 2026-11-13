<h1 align="center">Matura 2025 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-stara-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.2

```py
def rozklad(n):
    czynniki = []
    d = 2
    while n > 1:
        if n % d == 0:
            czynniki.append(d)
            n //= d
        else:
            d += 1
    return czynniki


# 1.1
for n in [14, 27, 33]:
    czynniki = rozklad(n)
    dwie_rozne = len(czynniki) == 2 and czynniki[0] != czynniki[1]
    print(n, czynniki, "TAK" if dwie_rozne else "NIE")

# 1.2
n = 40
P = [0] * (n + 1)                   # P[2..n] - najmniejszy czynnik pierwszy liczby i
for i in range(2, n + 1):
    d = 2
    while i % d != 0:
        d += 1
    P[i] = d

for i in range(2, n + 1):           # algorytm Rozklad
    if P[i] == i:
        P[i] = 1
    else:
        j1 = P[i]
        j2 = i // j1
        if j1 != j2 and P[j2] == 1:     # P[j2] jest już przetworzone, bo j2 < i
            P[i] = 2
        else:
            P[i] = 3

print(P[2:])
```

**Odpowiedź:** 1.1: 14 = 2 · 7 – TAK; 27 = 3 · 3 · 3 – NIE; 33 = 3 · 11 – TAK. 1.2: luki: `P[i] = 1`; `P[j2] = 1`; `P[i] = 2`; `P[i] = 3`.

## 2.1, 2.2 i 2.3

```py
wywolania = 0
dodawania = 0


def f(a, b):
    global wywolania, dodawania
    wywolania += 1
    if b == 0:
        return 0
    k = b % 10                  # ostatnia(b)
    w = f(a, b // 10)           # skróć(b)
    w = w * 10                  # dopisz(w)
    while k > 0:
        w = w + a
        dodawania += 1
        k -= 1
    return w


# 2.1 (funkcja oblicza a * b)
for a, b in [(42, 2), (4, 125), (103, 104)]:
    print(a, b, f(a, b))

# 2.2
wywolania = 0
f(987654321, 123456789)
print(wywolania)

# 2.3
for a, b in [(2024, 1000), (2024, 1234)]:
    dodawania = 0
    f(a, b)
    print(a, b, dodawania)
```

**Odpowiedź:** 2.1: 84, 500, 10712. 2.2: 10. 2.3: a) 1, b) 10.

## 4.1, 4.2, 4.3 i 4.4

```py
with open("dane.txt") as file:
    napis = file.read().strip()

# wydzielenie ukrytych liczb (maksymalnych ciągów cyfr)
liczby = []
biezaca = ""
for znak in napis + " ":
    if znak.isdigit():
        biezaca += znak
    else:
        if biezaca != "":
            liczby.append(biezaca)
        biezaca = ""

# 4.1
ile = 0
for liczba in liczby:
    if liczba[:2] == "50":
        ile += 1
with open("wyniki4_1.txt", "w") as wynik:
    print(ile, file=wynik)

# 4.2
wystapienia = [0] * 10
for znak in napis:
    if znak.isdigit():
        wystapienia[int(znak)] += 1
najwiecej = max(wystapienia)
with open("wyniki4_2.txt", "w") as wynik:
    print(wystapienia.index(najwiecej), najwiecej, file=wynik)

# 4.3
telefony = [liczba for liczba in liczby if len(liczba) == 9]
with open("wyniki4_3.txt", "w") as wynik:
    for telefon in telefony:
        if telefon[0] == "5":
            print(telefon, file=wynik)

# 4.4
najmniej = min(len(set(telefon)) for telefon in telefony)
with open("wyniki4_4.txt", "w") as wynik:
    for telefon in telefony:
        if len(set(telefon)) == najmniej:
            print(telefon, file=wynik)
```

**Odpowiedź:** 4.1: 4. 4.2: cyfra 1, 342 razy. 4.3: 588095244, 593151643, 583327270, 565269349, 583672019, 506585224, 574489008, 587103844, 510672749, 529135372, 515437684, 589477488. 4.4: 033035335, 050525250.
