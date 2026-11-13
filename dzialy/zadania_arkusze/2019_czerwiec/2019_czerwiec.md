<h1 align="center">Matura 2019 — czerwiec (termin dodatkowy), poziom rozszerzony</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md) --- [PLIKI](https://github.com/wernexnrs/MATURA-INFORMATYKA/tree/master/dzialy/zadania_arkusze/2019_czerwiec)

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2019-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2019-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2019-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2019-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1

```py
# Liczba wywołań Rek zależy tylko od tego, w którą połowę przedziału p..k pójdzie rekurencja.
# Sprawdzamy obie możliwości w każdym kroku i wybieramy najmniejszą / największą liczbę wywołań.
def wywolania(p, k, wybierz):
    if p < k:
        s = (p + k) // 2
        return 1 + wybierz(wywolania(p, s, wybierz), wywolania(s + 1, k, wybierz))
    return 1


print("najmniejsza:", wywolania(6, 14, min))
print("największa:", wywolania(6, 14, max))
```

**Odpowiedź:** najmniejsza liczba wywołań 4, największa 5

## 1.2

```py
T = [1, 5, 8, 10, 12, 14, 19, 20, 23, 30, 38]


def Rek(x, p, k):
    print(f"Rek({x},{p},{k})")
    if p < k:
        s = (p + k) // 2
        if T[s - 1] >= x:  # tablica w treści jest numerowana od 1
            return Rek(x, p, s)
        else:
            return Rek(x, s + 1, k)
    else:
        if T[p - 1] == x:
            return p
        return -1


print("wynik:", Rek(37, 1, 11))
```

**Odpowiedź:** Rek(37,7,11), Rek(37,10,11), Rek(37,11,11) (1.3: złożoność logarytmiczna)

## 2.1 i 2.2

```py
def deszyfruj(k, S):
    n = len(S)
    kolumny = n // k
    # tabela k wierszy na kolumny - szyfrogram to kolejne wiersze tabeli
    tabela = [S[w * kolumny:(w + 1) * kolumny] for w in range(k)]
    T = ""
    for kol in range(kolumny):
        if kol % 2 == 0:  # kolumny nieparzyste (numerując od 1) czytamy z góry na dół
            for w in range(k):
                T += tabela[w][kol]
        else:  # kolumny parzyste - z dołu do góry
            for w in range(k - 1, -1, -1):
                T += tabela[w][kol]
    return T


print(deszyfruj(3, "MA_FOYKARZNRTITU_IMA_"))
print(deszyfruj(10, "NKI_ATE_USGACYOKZZ_YYSJTCWEKI_SAEMTRLE_P"))
```

**Odpowiedź:** NAUCZYCIELEM_WSZYSTKIEGO_JEST_PRAKTYKA

## 4.1

```py
def czy_pierwsza(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


with open("liczby.txt") as file:
    for line in file:
        liczba = int(line)
        if 100 <= liczba <= 5000 and czy_pierwsza(liczba):
            print(liczba)
```

**Odpowiedź:** 563, 2087, 163, 2423, 3581, 911, 997, 113, 1049, 1511, 2467, 283, 3559, 521, 4201, 877, 1301, 2749, 4919, 1213, 2039, 4111, 3331, 401, 2221

## 4.2

```py
def czy_pierwsza(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


with open("pierwsze.txt") as file:
    for line in file:
        liczba = line.strip()
        if czy_pierwsza(int(liczba[::-1])):
            print(liczba)
```

**Odpowiedź:** 51 liczb: 31, 37, 101, 1009, 1021, 113, 1499, 1213, 1217, 1229, 1231, 1237, 1487, 1223, 7027, … , 112111

## 4.3

```py
def waga(liczba):
    while liczba >= 10:
        suma = 0
        for cyfra in str(liczba):
            suma += int(cyfra)
        liczba = suma
    return liczba


ile = 0

with open("pierwsze.txt") as file:
    for line in file:
        if waga(int(line)) == 1:
            ile += 1

print(ile)
```

**Odpowiedź:** 27

## 5.1

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
import math
from datetime import date, timedelta

with open("pogoda.txt") as file:
    file.readline()  # nagłówek
    dane = []
    for line in file:
        temperatura, opady = line.split()
        dane.append((float(temperatura.replace(",", ".")), float(opady.replace(",", "."))))

POJEMNOSC = 25000
stan = POJEMNOSC  # 31 marca o 21:00 zbiornik był pełen
dzien = date(2015, 4, 1)
dolewki = []  # (data, ile litrów dolano)

for temperatura, opady in dane:
    if opady > 0:
        stan = min(POJEMNOSC, stan + math.ceil(700 * opady))
    else:
        stan -= math.ceil(0.0003 * temperatura ** 1.5 * stan)
    if temperatura > 15 and opady <= 0.6:
        potrzeba = 12000 if temperatura <= 30 else 24000
        if stan < potrzeba:
            dolewki.append((dzien, POJEMNOSC - stan))
            stan = POJEMNOSC
        stan -= potrzeba
    dzien += timedelta(days=1)

print(dolewki[0])
print("razem dolano:", sum(ile for d, ile in dolewki))
```

**Odpowiedź:** 6 maja 2015 r., 13172 litrów (łącznie dolano 743 427 litrów)

## 5.2

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
import math
from datetime import date, timedelta

with open("pogoda.txt") as file:
    file.readline()
    dane = []
    for line in file:
        temperatura, opady = line.split()
        dane.append((float(temperatura.replace(",", ".")), float(opady.replace(",", "."))))

POJEMNOSC = 25000
stan = POJEMNOSC
dzien = date(2015, 4, 1)

for temperatura, opady in dane:
    if opady > 0:
        stan = min(POJEMNOSC, stan + math.ceil(700 * opady))
    else:
        stan -= math.ceil(0.0003 * temperatura ** 1.5 * stan)
    if temperatura > 15 and opady <= 0.6:
        potrzeba = 12000 if temperatura <= 30 else 24000
        if stan < potrzeba:
            stan = POJEMNOSC
        stan -= potrzeba
    print(dzien, stan)  # stan o 21:00 - dane do wykresu liniowego
    dzien += timedelta(days=1)
```

**Odpowiedź:** wykres liniowy stanu zbiornika o 21:00 w kolejnych dniach (od 2015-04-01 do 2015-09-30)

## 5.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
import math
from datetime import date, timedelta

with open("pogoda.txt") as file:
    file.readline()
    dane = []
    for line in file:
        temperatura, opady = line.split()
        dane.append((float(temperatura.replace(",", ".")), float(opady.replace(",", "."))))

POJEMNOSC = 25000
stan = POJEMNOSC
dzien = date(2015, 4, 1)
dolano = {miesiac: 0 for miesiac in range(4, 10)}

for temperatura, opady in dane:
    if opady > 0:
        stan = min(POJEMNOSC, stan + math.ceil(700 * opady))
    else:
        stan -= math.ceil(0.0003 * temperatura ** 1.5 * stan)
    if temperatura > 15 and opady <= 0.6:
        potrzeba = 12000 if temperatura <= 30 else 24000
        if stan < potrzeba:
            dolano[dzien.month] += POJEMNOSC - stan
            stan = POJEMNOSC
        stan -= potrzeba
    dzien += timedelta(days=1)

for miesiac, litry in dolano.items():
    m3 = math.ceil(litry / 1000)
    print(miesiac, litry, m3, round(m3 * 11.74, 2))
```

**Odpowiedź:** kwiecień 0 l – 0 zł, maj 13172 l – 14 m3 – 164,36 zł, czerwiec 89444 l – 90 m3 – 1056,60 zł, lipiec 217938 l – 218 m3 – 2559,32 zł, sierpień 310099 l – 311 m3 – 3651,14 zł, wrzesień 112774 l – 113 m3 – 1326,62 zł

## 5.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
chlodne = cieple_bez_deszczu = cieple_z_deszczem = 0

with open("pogoda.txt") as file:
    file.readline()
    for line in file:
        temperatura, opady = line.split()
        temperatura = float(temperatura.replace(",", "."))
        opady = float(opady.replace(",", "."))
        if temperatura <= 15:
            chlodne += 1
        elif opady <= 0.6:
            cieple_bez_deszczu += 1
        else:
            cieple_z_deszczem += 1

print(chlodne, cieple_bez_deszczu, cieple_z_deszczem)
```

**Odpowiedź:** 88 dni (temperatura ≤ 15°C), 73 dni (temperatura > 15°C i opady ≤ 0,6), 22 dni (temperatura > 15°C i opady > 0,6)

## 6 [[ACCESS] POBIERZ](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze/2019_czerwiec/6.accdb?raw=true)

Uwaga: plik `oferty.txt` od CKE jest zapisany w kodowaniu UTF-16, dlatego otwieramy go z `encoding="utf-16"`.

## 6.1

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
def wczytaj(nazwa, kodowanie="utf-8"):
    with open(nazwa, encoding=kodowanie) as file:
        file.readline()  # nagłówek
        return [[pole.strip() for pole in line.split("\t")] for line in file if line.strip()]


agenci = wczytaj("agenci.txt")
oferty = wczytaj("oferty.txt", "utf-16")
zainteresowanie = wczytaj("zainteresowanie.txt")

ile_klientow = {}
for id_oferty, id_klienta in zainteresowanie:
    ile_klientow[id_oferty] = ile_klientow.get(id_oferty, 0) + 1

najlepsza = max(ile_klientow, key=ile_klientow.get)

for oferta in oferty:
    if oferta[0] == najlepsza:
        id_agenta = oferta[8]

for agent in agenci:
    if agent[0] == id_agenta:
        print(najlepsza, agent[1], agent[2])
```

**Odpowiedź:** AB553DN, Karol Zakowicz

#### Kwerenda o nazwie 6_1(wynik)
```sql
SELECT TOP 1 Agenci.Imie, Agenci.Nazwisko, Zainteresowanie.Id_oferty
FROM Agenci INNER JOIN (Oferty INNER JOIN Zainteresowanie ON Oferty.Id_oferty = Zainteresowanie.Id_oferty) ON Agenci.Id_agenta = Oferty.Id_agenta
GROUP BY Agenci.Imie, Agenci.Nazwisko, Zainteresowanie.Id_oferty, Oferty.Id_agenta
ORDER BY Count(Zainteresowanie.Id_klienta) DESC;
```

## 6.2

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
from decimal import Decimal, ROUND_HALF_UP


def wczytaj(nazwa, kodowanie="utf-8"):
    with open(nazwa, encoding=kodowanie) as file:
        file.readline()
        return [[pole.strip() for pole in line.split("\t")] for line in file if line.strip()]


oferty = wczytaj("oferty.txt", "utf-16")

suma = {}
ile = {}
for oferta in oferty:
    woj, cena = oferta[1], int(oferta[6])
    suma[woj] = suma.get(woj, 0) + cena
    ile[woj] = ile.get(woj, 0) + 1

for woj in sorted(suma):
    # Decimal - zaokrąglenie "szkolne" (0,005 w górę), tak jak w Accessie/Excelu
    srednia = Decimal(suma[woj]) / ile[woj]
    print(woj, srednia.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
```

**Odpowiedź:** dolnoslaskie 345000,00; kujawsko-pomorskie 299000,00; lodzkie 304100,00; lubelskie 260879,33; lubuskie 227283,33; malopolskie 650000,00; mazowieckie 267082,83; opolskie 400000,00; podkarpackie 301312,50; podlaskie 271206,95; pomorskie 414150,00; swietokrzyskie 319207,63; warminsko-mazurskie 132450,00; wielkopolskie 298600,00; zachodniopomorskie 269025,20

#### Kwerenda o nazwie 6_2(wynik)
```sql
SELECT Oferty.Woj, Avg(Oferty.Cena) AS ŚredniaOfCena
FROM Oferty
GROUP BY Oferty.Woj
ORDER BY Oferty.Woj;
```

## 6.3

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
def wczytaj(nazwa, kodowanie="utf-8"):
    with open(nazwa, encoding=kodowanie) as file:
        file.readline()
        return [[pole.strip() for pole in line.split("\t")] for line in file if line.strip()]


agenci = wczytaj("agenci.txt")
oferty = wczytaj("oferty.txt", "utf-16")

agent = {}
for id_agenta, imie, nazwisko in agenci:
    agent[id_agenta] = imie + " " + nazwisko

for id_oferty, woj, status, pow, pokoje, lazienki, cena, data, id_agenta in oferty:
    # przedostatni znak M - mieszkanie, ostatni T - z basenem
    if id_oferty.endswith("MT") and status == "A":
        print(agent[id_agenta], id_oferty, woj, pow, cena)
```

**Odpowiedź:** Piotr Kopacz AB543MT podlaskie 85 325000; Adam Nowak AB557MT lubelskie 83 349000; Karol Zakowicz AB644MT mazowieckie 76 174500; Milena Karwik AB691MT lubuskie 39 170000; Adam Nowak AB695MT podkarpackie 162 420800; Rozalia Siedlecka AB696MT wielkopolskie 42 160000; Karol Szwarc AB699MT lodzkie 68 190500; Krzysztof Nowak AB700MT mazowieckie 85 265000; Adam Nowak AB702MT mazowieckie 49 186000 (klucz CKE pomija ofertę AB700MT, choć w danych spełnia ona warunki zadania)

#### Kwerenda o nazwie 6_3(wynik)
```sql
SELECT Oferty.Id_oferty, Agenci.Imie, Agenci.Nazwisko, Oferty.Woj, Oferty.Pow, Oferty.Cena
FROM Agenci INNER JOIN Oferty ON Agenci.Id_agenta = Oferty.Id_agenta
WHERE (((Oferty.Id_oferty) Like "*MT") AND ((Oferty.Status) Like "A"));
```

## 6.4

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
def wczytaj(nazwa, kodowanie="utf-8"):
    with open(nazwa, encoding=kodowanie) as file:
        file.readline()
        return [[pole.strip() for pole in line.split("\t")] for line in file if line.strip()]


agenci = wczytaj("agenci.txt")
oferty = wczytaj("oferty.txt", "utf-16")

sprzedali_w_2017 = set()
for id_oferty, woj, status, pow, pokoje, lazienki, cena, data, id_agenta in oferty:
    if data.startswith("2017") and status == "S":
        sprzedali_w_2017.add(id_agenta)

for id_agenta, imie, nazwisko in agenci:
    if id_agenta not in sprzedali_w_2017:
        print(imie, nazwisko)
```

**Odpowiedź:** Jerzy Andrzejewski, Krzysztof Nowak, Milena Karwik

#### Kwerenda o nazwie 6_4(wynik)
```sql
SELECT Agenci.imie, Agenci.nazwisko
FROM Agenci
WHERE (((Agenci.Id_agenta) Not In (SELECT id_agenta FROM oferty WHERE status="S" AND data_zglosz LIKE "2017*")));
```

## 6.5

*Zadanie na Excel/Access — rozwiązanie w Pythonie.*

```py
def wczytaj(nazwa, kodowanie="utf-8"):
    with open(nazwa, encoding=kodowanie) as file:
        file.readline()
        return [[pole.strip() for pole in line.split("\t")] for line in file if line.strip()]


agenci = wczytaj("agenci.txt")
oferty = wczytaj("oferty.txt", "utf-16")

agent = {}
for id_agenta, imie, nazwisko in agenci:
    agent[id_agenta] = imie + " " + nazwisko

for id_oferty, woj, status, pow, pokoje, lazienki, cena, data, id_agenta in oferty:
    if status == "A" and int(pow) > 180 and int(lazienki) >= 2:
        print(id_oferty, pow, pokoje, lazienki, cena, agent[id_agenta])
```

**Odpowiedź:** 11 ofert: AB666DN 220 6 3 450000 Krzysztof Nowak; AB670DN 208 5 3 358400 Karol Zakowicz; AB672DT 212 6 2 575000 Sebastian Babij; AB680DT 220 6 2 520000 Adam Nowak; AB682DN 203 5 3 485000 Adam Nowak; … ; AB697DN 195 6 2 460000 Karol Szwarc

#### Kwerenda o nazwie 6_5(wynik)
```sql
SELECT Oferty.Id_oferty, Oferty.Pow, Oferty.L_pokoi, Oferty.L_laz, Oferty.Cena, Agenci.Imie, Agenci.Nazwisko, Oferty.Status
FROM Agenci INNER JOIN Oferty ON Agenci.Id_agenta = Oferty.Id_agenta
WHERE (((Oferty.Pow)>180) AND ((Oferty.L_laz)>1) AND ((Oferty.Status) Like "A"));
```
