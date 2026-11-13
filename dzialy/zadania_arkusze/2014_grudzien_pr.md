<h1 align="center">Matura próbna 2014 — grudzień (formuła od 2015)</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ I](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/egzamin_probny_2015/informatyka_pr/Czesc_1/A1Informatyka_PR_cz%C4%99%C5%9B%C4%87_I.pdf) --- [ARKUSZ II](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/egzamin_probny_2015/informatyka_pr/Czesc_2/A1Informatyka_PR_cz%C4%99%C5%9B%C4%87_II.pdf) --- [DANE](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/egzamin_probny_2015/informatyka_pr/Czesc_2/Dane_Pr/DANE_PR.zip) --- [ODPOWIEDZI I](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/egzamin_probny_2015/informatyka_pr/A1A2A3A4A7Informatyka_PR_cz%C4%99%C5%9B%C4%87_I_model_odpowiedzi.pdf) --- [ODPOWIEDZI II](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/egzamin_probny_2015/informatyka_pr/A1A2A3A4A7Informatyka_PR_czesc_II_model_odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

```py
def cyfry(k):
    # 1.2 - cyfry od najmniej znaczacej, n - liczba cyfr
    tab_cyfr = []
    while True:
        tab_cyfr.append(k % 10)
        k = k // 10
        if k == 0:
            break
    return len(tab_cyfr), tab_cyfr


def czy_armstronga(k):
    # 1.3 - odejmujemy od k kolejne cyfry podniesione do potegi n
    n, tab_cyfr = cyfry(k)
    for j in range(n):
        k = k - tab_cyfr[j] ** n
    return k == 0


print(cyfry(54321))
for k in [6, 407, 2278]:
    print(k, "P" if czy_armstronga(k) else "F")
```

**Odpowiedź:** 1.1: 6 — P, 407 — P, 2278 — F; dla k = 54321: n = 5, tab_cyfr = [1, 2, 3, 4, 5]

## 3.1 i 3.3

```py
def dekoduj(v, t, bity):
    # v - bajty tekstu skompresowanego, t - slownik {kod: znak}
    # bity czytamy od najstarszego bitu kazdego bajtu
    ciag_bitow = ""
    for bajt in v:
        ciag_bitow += bin(bajt)[2:].zfill(8)
    s = ""
    for i in range(0, len(ciag_bitow) - bity + 1, bity):
        kod = int(ciag_bitow[i:i + bity], 2)
        if kod in t:            # kod 0 to bity wolne na koncu
            s += t[kod]
    return s


print(bin(110)[2:].zfill(8), bin(64)[2:].zfill(8))
print(dekoduj([110, 64], {1: "K", 2: "A", 3: "J"}, 2))
print(dekoduj([41, 196], {1: "H", 2: "A", 3: "N", 4: "I"}, 3))
```

**Odpowiedź:** 3.1: 01101110 01000000 — KAJAK

## 3.2

```py
def rozne_znaki(s):
    R = []
    for znak in s:
        if znak not in R:
            R.append(znak)
    return len(R)


print(rozne_znaki("AAAABBBCCCBBBAAACC"), rozne_znaki("HANIA"))
```

**Odpowiedź:** dla "HANIA" r = 4

## 4.1 i 4.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
import math

# 4.1 - x = r*sin(2*pi*t/T), y = r*cos(2*pi*t/T)
r, T, dt, t_pocz = 5, 12.5, 0.05, 3
krok = 0
while True:
    t = t_pocz + krok * dt
    x = r * math.sin(2 * math.pi * t / T)
    y = r * math.cos(2 * math.pi * t / T)
    if y > x:
        print("4.1", round(t - t_pocz, 2), "(czas od poczatku ruchu:", round(t, 2), ")")
        break
    krok += 1

# 4.3 - spirala r = v*t, T = 10, dt = 0,5, pierwsze 10 sekund
T, dt, v = 10, 0.5, 1
punkty = []
for i in range(21):
    t = i * dt
    punkty.append((v * t * math.sin(2 * math.pi * t / T), v * t * math.cos(2 * math.pi * t / T)))

dlugosc = 0
for i in range(1, len(punkty)):
    dlugosc += math.dist(punkty[i - 1], punkty[i])
print("4.3", f"{dlugosc:.4f}")
```

**Odpowiedź:** 4.1: 4,85 s (czyli 7,85 s od początku ruchu); 4.3: 33,6520

## 4.2

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
import math

# punkty spirali do wykresu punktowego (x, y) w arkuszu
with open("spirala_4_2.txt", "w") as wynik:
    wynik.write("t;x;y\n")
    for i in range(21):
        t = i * 0.5
        x = t * math.sin(2 * math.pi * t / 10)
        y = t * math.cos(2 * math.pi * t / 10)
        wynik.write(f"{t};{x:.4f};{y:.4f}\n")
```

**Odpowiedź:** wykres punktowy z liniami (spirala) tworzymy z pliku `spirala_4_2.txt`

## 5.1, 5.2 i 5.3

```py
wyniki = []
with open("dziennik.txt") as file:
    for line in file:
        if line.strip():
            wyniki.append(int(line))

# 5.1 i 5.3 - pozytywne serie: (dlugosc, poprawa)
serie = []
poczatek = 0
for i in range(1, len(wyniki) + 1):
    if i == len(wyniki) or wyniki[i] <= wyniki[i - 1]:
        serie.append((i - poczatek, wyniki[i - 1] - wyniki[poczatek]))
        poczatek = i

print("5.1", sum(1 for dlugosc, poprawa in serie if dlugosc > 3))

najdluzszy = max(wyniki)
najkrotszy = min(wyniki)
print("5.2", najdluzszy, wyniki.index(najdluzszy) + 1, najkrotszy, wyniki.index(najkrotszy) + 1)

print("5.3", *max(serie))
```

**Odpowiedź:** 5.1: 11; 5.2: najdłuższy 601 (176. wynik), najkrótszy 401 (17. wynik); 5.3: 6 dni, poprawa o 158 cm
