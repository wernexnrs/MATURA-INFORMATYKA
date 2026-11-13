<h1 align="center">Matura próbna 2022 — grudzień (formuła 2023)</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2022-grudzien-probna-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2022-grudzien-probna-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2022-grudzien-probna-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

```py
with open("mecz.txt") as file:
    mecz = file.readline().strip()

# 1.1
zmiany = 0
for i in range(1, len(mecz)):
    if mecz[i] != mecz[i - 1]:
        zmiany += 1
print("1.1", zmiany)

# 1.2
punkty_a = 0
punkty_b = 0
for znak in mecz:
    if znak == "A":
        punkty_a += 1
    else:
        punkty_b += 1
    if (punkty_a >= 1000 or punkty_b >= 1000) and abs(punkty_a - punkty_b) >= 3:
        break
if punkty_a > punkty_b:
    print("1.2", "A", str(punkty_a) + ":" + str(punkty_b))
else:
    print("1.2", "B", str(punkty_a) + ":" + str(punkty_b))

# 1.3 - dzielimy mecz na maksymalne bloki jednakowych znaków
dobre_passy = 0
najdluzsza = 0
druzyna = ""
dlugosc = 1
for i in range(1, len(mecz) + 1):
    if i < len(mecz) and mecz[i] == mecz[i - 1]:
        dlugosc += 1
    else:
        # koniec bloku mecz[i - dlugosc .. i - 1]
        if dlugosc >= 10:
            dobre_passy += 1
            if dlugosc > najdluzsza:
                najdluzsza = dlugosc
                druzyna = mecz[i - 1]
        dlugosc = 1
print("1.3", dobre_passy, druzyna, najdluzsza)
```

**Odpowiedź:** 1.1: 5030; 1.2: B 1001:1004; 1.3: 6 B 15

## 2.1, 2.2, 2.3 i 2.4

```py
strzalki = []


def rysuj(x, N):
    if 2 * x <= N:
        strzalki.append((x, 2 * x))
        rysuj(2 * x, N)
    if 2 * x + 1 <= N:
        strzalki.append((x, 2 * x + 1))
        rysuj(2 * x + 1, N)


# 2.1 - lista strzałek dla N = 10 (punkt x łączy się z 2x i 2x+1 - drzewo binarne)
rysuj(1, 10)
print("2.1", strzalki)

# 2.2 - każdy punkt poza 1 ma dokładnie jedną strzałkę wchodzącą (od x // 2)
strzalki = []
rysuj(1, 20)
print("2.2", len(strzalki), "ogólnie N - 1")

# 2.3 - idąc od N do 1 przechodzimy do N // 2
N = 2047
kroki = 0
while N > 1:
    N //= 2
    kroki += 1
print("2.3", kroki)


# 2.4 - z x da się dojść do y, gdy dzieląc y przez 2 (całkowicie) dojdziemy do x
def osiagalny(x, y):
    while y > x:
        y //= 2
    return x == y


print("2.4")
with open("pary.txt") as file:
    for line in file:
        x, y = map(int, line.split())
        if osiagalny(x, y):
            print(x, y)
```

**Odpowiedź:** 2.1: strzałki 1→2, 1→3, 2→4, 2→5, 3→6, 3→7, 4→8, 4→9, 5→10; 2.2: a) 19, b) N − 1; 2.3: 10; 2.4: 47 3044, 7650 61204, 1 245, 7 63669, 9125 18250, 5 43246

## 3.1, 3.2, 3.3 i 3.4

```py
# 3.1 - sito Eratostenesa (luki: N (wystarczy pierwiastek z N), PRAWDA, i * i, FAŁSZ, j + i)
def sito(N):
    SITO = [True] * (N + 1)
    SITO[0] = False
    SITO[1] = False
    i = 2
    while i * i <= N:
        if SITO[i]:
            j = i * i
            while j <= N:
                SITO[j] = False
                j = j + i
        i += 1
    return SITO


liczby = []
with open("liczby.txt") as file:
    for line in file:
        liczby.append(int(line))

SITO = sito(1000000)

# 3.2
ile = 0
for x in liczby:
    if SITO[x - 1]:
        ile += 1
print("3.2", ile)

# 3.3 - rozkład x = p + (x - p), p <= x - p
najwiecej, liczba_max = -1, 0
najmniej, liczba_min = 10 ** 9, 0
for x in liczby:
    rozklady = 0
    for p in range(2, x // 2 + 1):
        if SITO[p] and SITO[x - p]:
            rozklady += 1
    if rozklady > najwiecej:
        najwiecej, liczba_max = rozklady, x
    if rozklady < najmniej:
        najmniej, liczba_min = rozklady, x
print("3.3", liczba_max, najwiecej, liczba_min, najmniej)

# 3.4
cyfry = "0123456789ABCDEF"
ile_cyfr = [0] * 16
for x in liczby:
    while x > 0:
        ile_cyfr[x % 16] += 1
        x //= 16
print("3.4")
for i in range(16):
    print(cyfry[i] + ":" + str(ile_cyfr[i]))
```

**Odpowiedź:** 3.1: luki kolejno: N (wystarczy √N), PRAWDA, i * i, FAŁSZ, j + i; 3.2: 21; 3.3: 910620 9932 18676 195; 3.4: 0:32, 1:26, 2:37, 3:31, 4:43, 5:25, 6:28, 7:23, 8:38, 9:28, A:45, B:33, C:29, D:23, E:44, F:10
