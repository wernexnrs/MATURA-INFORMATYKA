<h1 align="center">Matura próbna 2021 — marzec</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

Test diagnostyczny CKE – marzec 2021.

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2021-marzec-probna-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2021-marzec-probna-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2021-marzec-probna-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2021-marzec-probna-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.2

```py
def runda(k, x, y):
    # drużyny spotkają się w rundzie r, gdy ich numery różnią się tylko na r ostatnich bitach,
    # więc dzielimy oba numery przez 2 (usuwamy ostatni bit), aż staną się równe
    r = 0
    while x != y:
        r += 1
        x //= 2
        y //= 2
    return r


for k, x, y in [(3, 2, 6), (4, 0, 3), (4, 3, 7), (5, 16, 30)]:
    print(k, x, y, runda(k, x, y))
```

**Odpowiedź:** 1.1: (3, 2, 6) → 3, (4, 0, 3) → 2, (4, 3, 7) → 3, (5, 16, 30) → 4; 1.2: algorytm w kodzie

## 2.1 i 2.2

```py
def Algo(n):
    ile_s = 0  # liczba wykonań instrukcji s <- (p + k) div 2
    if n <= 2:
        return 1, ile_s
    p = 1
    k = n
    while k - p > 1:
        s = (p + k) // 2
        ile_s += 1
        if s * s <= n:
            p = s
        else:
            k = s
    return p, ile_s


# 2.1
for n in [5, 35, 1025]:
    print(n, Algo(n)[0])
# 2.2
for n in [5, 2, 63, 1024]:
    print(n, Algo(n)[1])
```

**Odpowiedź:** 2.1: Algo(5) = 2, Algo(35) = 5, Algo(1025) = 32; 2.2: 5 → 2, 2 → 0, 63 → 6, 1024 → 10

## 4.1

```py
miasta = {}  # kod kraju -> liczba miast

with open("galerie.txt") as file:
    for line in file:
        kod_kraju = line.split()[0]
        miasta[kod_kraju] = miasta.get(kod_kraju, 0) + 1

with open("wynik4_1.txt", "w") as wynik:
    for kod_kraju, ile in miasta.items():
        print(kod_kraju, ile)
        wynik.write(f"{kod_kraju} {ile}\n")
```

**Odpowiedź:** GB 5, D 15, E 6, I 6, F 2, RO 1, A 1, H 1, BG 1, CZ 1, B 1, S 1, HR 1, NL 2, LV 1, GR 1, LT 1, FIN 1, DK 1, IRL 1

## 4.2

```py
galerie = []  # (miasto, powierzchnia, liczba lokali)

with open("galerie.txt") as file:
    for line in file:
        dane = line.split()
        miasto = dane[1]
        liczby = [int(x) for x in dane[2:]]
        powierzchnia = 0
        lokale = 0
        for i in range(0, len(liczby), 2):
            if liczby[i] != 0:  # zera uzupełniają wiersz do 70 par
                powierzchnia += liczby[i] * liczby[i + 1]
                lokale += 1
        galerie.append((miasto, powierzchnia, lokale))

# a)
with open("wynik4_2a.txt", "w") as wynik:
    for miasto, powierzchnia, lokale in galerie:
        print(miasto, powierzchnia, lokale)
        wynik.write(f"{miasto} {powierzchnia} {lokale}\n")

# b)
najwieksza = max(galerie, key=lambda g: g[1])
najmniejsza = min(galerie, key=lambda g: g[1])
with open("wynik4_2b.txt", "w") as wynik:
    for miasto, powierzchnia, lokale in [najwieksza, najmniejsza]:
        print(miasto, powierzchnia)
        wynik.write(f"{miasto} {powierzchnia}\n")
```

**Odpowiedź:** a) Londyn 3628 58, Berlin 3777 59, Madryt 2217 34, Rzym 3678 51, … , Duisburg 3948 61; b) Essen 4760, Wilno 1620

## 4.3

```py
rodzaje = []  # (miasto, liczba różnych rodzajów lokali)

with open("galerie.txt") as file:
    for line in file:
        dane = line.split()
        miasto = dane[1]
        liczby = [int(x) for x in dane[2:]]
        powierzchnie = set()
        for i in range(0, len(liczby), 2):
            if liczby[i] != 0:
                powierzchnie.add(liczby[i] * liczby[i + 1])
        rodzaje.append((miasto, len(powierzchnie)))

najwiecej = max(rodzaje, key=lambda r: r[1])
najmniej = min(rodzaje, key=lambda r: r[1])

with open("wynik4_3.txt", "w") as wynik:
    for miasto, ile in [najwiecej, najmniej]:
        print(miasto, ile)
        wynik.write(f"{miasto} {ile}\n")
```

**Odpowiedź:** Berlin 35, Kolonia 18

## 5.1

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
polaczenia = {}

with open("telefony.txt") as file:
    file.readline()  # nagłówek
    for line in file:
        numer = line.split()[0]
        polaczenia[numer] = polaczenia.get(numer, 0) + 1

for numer, ile in sorted(polaczenia.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(numer, ile)
```

**Odpowiedź:** 4546455 – 8, 3505978 – 7, 4657345 – 6

## 5.2

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
stacjonarne = {}
komorkowe = {}

with open("telefony.txt") as file:
    file.readline()
    for line in file:
        numer, data, poczatek, koniec = line.split()
        if data not in stacjonarne:
            stacjonarne[data] = 0
            komorkowe[data] = 0
        if len(numer) == 7:
            stacjonarne[data] += 1
        elif len(numer) == 8:
            komorkowe[data] += 1

for data in stacjonarne:  # dni są w pliku w kolejności chronologicznej
    print(data, komorkowe[data], stacjonarne[data])
# na podstawie zestawienia należy jeszcze wykonać wykres kolumnowy
```

**Odpowiedź:** 3-07-2017: komórkowe 27, stacjonarne 67; 4-07-2017: 23, 68; 5-07-2017: 24, 79; … ; 31-07-2017: 23, 82 (łącznie 512 i 1524) (+ wykres kolumnowy)

## 5.3

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
import math


def sekundy(czas):
    g, m, s = czas.split(":")
    return int(g) * 3600 + int(m) * 60 + int(s)


ile = 0
czas = 0

with open("telefony.txt") as file:
    file.readline()
    for line in file:
        numer, data, poczatek, koniec = line.split()
        if len(numer) == 7 and numer.startswith("12"):
            ile += 1
            czas += sekundy(koniec) - sekundy(poczatek)

print(ile, math.ceil(czas / 60))
```

**Odpowiedź:** 21 połączeń, 192 minuty

## 5.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

```py
import math


def sekundy(czas):
    g, m, s = czas.split(":")
    return int(g) * 3600 + int(m) * 60 + int(s)


ABONAMENT = 50
LIMIT = 800 * 60  # w sekundach

wykorzystane = 0      # sekundy rozmów krajowych wliczone w abonament
stacjonarne = 0       # sekundy rozmów ponad limit
komorkowe = 0
zagraniczne_zl = 0

with open("telefony.txt") as file:
    file.readline()
    for line in file:  # połączenia są zapisane chronologicznie
        numer, data, poczatek, koniec = line.split()
        czas = sekundy(koniec) - sekundy(poczatek)
        if len(numer) >= 10:
            zagraniczne_zl += math.ceil(czas / 60)  # 1 zł za każdą rozpoczętą minutę
            continue
        z_abonamentu = min(czas, LIMIT - wykorzystane)
        wykorzystane += z_abonamentu
        if len(numer) == 7:
            stacjonarne += czas - z_abonamentu
        else:
            komorkowe += czas - z_abonamentu

# każdy rozpoczęty pakiet 100 minut
stacjonarne_zl = math.ceil(stacjonarne / 6000) * 5
komorkowe_zl = math.ceil(komorkowe / 6000) * 6

print("abonament", ABONAMENT)
print("stacjonarne", stacjonarne_zl)
print("komórkowe", komorkowe_zl)
print("zagraniczne", zagraniczne_zl)
print("suma", ABONAMENT + stacjonarne_zl + komorkowe_zl + zagraniczne_zl)
```

**Odpowiedź:** abonament 50 zł, stacjonarne 610 zł, komórkowe 240 zł, zagraniczne 967 zł, razem 1867 zł
