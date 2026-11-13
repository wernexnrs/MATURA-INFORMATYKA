# Przydatne moduły

Wszystkie opisane tu zagadnienia nie są wyczerpaniem tematu. Są to jedynie rzeczy, które mogą się przydać. Moduły należą do biblioteki standardowej Pythona (nie trzeba nic instalować), ale każdy trzeba najpierw zaimportować, np. `import math` albo `from math import sqrt`.

  * __collections__ - specjalne kontenery (słowniki, kolejki)
    * [Counter()](#counter)
      * .elements()
      * .most_common()
      * .subtract()
    * [defaultdict()](#defaultdict)
    * [OrderedDict()](#order)
    * [deque()](#deque)
  * __math__ - matematyka
    * [funkcje](#funkcje)
  * __statistics__ - statystyka
    * [funkcje](#statfunc)
  * __re__ - wyrażenia regularne (RegEx)
    * [funkcje](#refunc)
    * [Metaznaki](#meta)
    * [Specjalne sekwencje](#special)
    * [Zbiory](#sets)
    * [Znaki specjalne w napisach](#biale)
  * __fractions__ - ułamki
    * [Fraction](#ulamki)
  * __itertools__ - iteratory, kombinatoryka
    * [count](#count)
    * [zip_longest](#zip_longest)
    * [cycle](#cycle)
    * [repeat](#repeat)
    * [starmap](#starmap)
    * [combinations](#combinations)
    * [permutations](#permutations)
    * [product](#product)
    * [chain](#chain)
    * [islice](#islice)
    * [accumulate](#accumulate)
    * [groupby](#groupby)
    * [pairwise](#pairwise)
  * __operator__ - operatory jako funkcje
    * [itemgetter i funkcje operatorów](#itemgetter)
  * __functools__ - narzędzia dla funkcji
    * [reduce](#reduce)
    * [lru_cache / cache](#cache)
    * [cmp_to_key](#cmp_to_key)
  * __bisect__ - wyszukiwanie binarne w posortowanej liście
    * [bisect_left / bisect_right / insort](#bisect)
  * __heapq__ - kopiec (kolejka priorytetowa)
    * [heappush / heappop / nlargest](#heapq)
  * __datetime__ - daty i czas
    * [date / datetime / timedelta](#datetime)
    * [calendar](#calendar)
  * __sys__ - ustawienia interpretera
    * [setrecursionlimit](#sys)
  * __enum__ - typy wyliczeniowe
    * [Enum](#enum-klasa)

## collections
### Counter() [⬆️](#)
<a name="counter"></a>

Słownik do zliczania: kluczami są elementy, a wartościami liczba ich wystąpień. Dla brakującego klucza zwraca 0 (bez błędu).

```python
# zliczanie elementów
from collections import Counter

c = Counter("abracadabra")
print(c)
#Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(c["a"], c["z"])
#Output: 5 0
print(c.most_common(2))
#Output: [('a', 5), ('b', 2)]
print(Counter([3, 1, 3, 3, 2]).most_common(1)[0][0])  # najczęstszy element
#Output: 3
```

```python
# typowe zastosowania Counter
from collections import Counter

print(Counter("kajak") == Counter("jakak"))     # czy słowa są anagramami
#Output: True
c = Counter("mississippi")
print(sorted(c.items()))
#Output: [('i', 4), ('m', 1), ('p', 2), ('s', 4)]
print(sum(1 for v in c.values() if v > 1))     # ile różnych liter się powtarza
#Output: 3
najczestsza, ile = Counter([4, 1, 4, 2, 1, 4]).most_common(1)[0]
print(najczestsza, ile)
#Output: 4 3
```

```python
# działania na licznikach
from collections import Counter

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print(c + d)                # dodawanie
#Output: Counter({'a': 4, 'b': 3})
print(c - d)                # odejmowanie, zostają tylko dodatnie liczności
#Output: Counter({'a': 2})
print(c & d)                # minimum dla każdego klucza
#Output: Counter({'a': 1, 'b': 1})
print(c | d)                # maksimum dla każdego klucza
#Output: Counter({'a': 3, 'b': 2})
print(list(c.elements()))
#Output: ['a', 'a', 'a', 'b']
c.subtract(d)               # zmienia c w miejscu, zostawia zera i liczby ujemne
print(c)
#Output: Counter({'a': 2, 'b': -1})
```
<h5> Metody </h5>

   * __.elements()__ -> zwraca iterator po elementach, w którym każdy element powtarza się tyle razy, ile wynosi jego liczność (elementy z licznością 0 lub ujemną są pomijane)
   * __.most_common(n)__ -> zwraca listę `n` par `(element, liczność)` posortowaną malejąco według liczności; bez argumentu - wszystkie pary
   * __.subtract(inny)__ -> odejmuje liczności __w miejscu__ (zwraca `None`), zachowując zera i wartości ujemne
   * __.update(iterable)__ -> dodaje liczności w miejscu, np. `c.update("aab")`

### defaultdict() [⬆️](#)
<a name="defaultdict"></a>

Słownik, który dla brakującego klucza sam tworzy wartość domyślną (zamiast zgłaszać `KeyError`). W nawiasie podajemy funkcję tworzącą tę wartość: `int` (0), `list` (pusta lista), `set` (pusty zbiór).

```python
from collections import defaultdict

licznik = defaultdict(int)
for znak in "kajak":
    licznik[znak] += 1
print(dict(licznik))
#Output: {'k': 2, 'a': 2, 'j': 1}

grupy = defaultdict(list)
for slowo in ["kot", "pies", "koza", "papuga"]:
    grupy[slowo[0]].append(slowo)
print(dict(grupy))
#Output: {'k': ['kot', 'koza'], 'p': ['pies', 'papuga']}
```

### OrderedDict() [⬆️](#)
<a name="order"></a>

Słownik pamiętający kolejność dodawania elementów. Od Pythona 3.7 zwykły `dict` też ją pamięta, więc `OrderedDict` przydaje się głównie dzięki dodatkowym metodom i innemu porównywaniu:
 - Gdy porównamy 2 słowniki klasy `dict`, które zawierają te same elementy, niezależnie od ich kolejności dostaniemy `True`. Słowniki klasy `OrderedDict` są równe tylko wtedy, gdy mają też tę samą kolejność elementów.
 - __.move_to_end(klucz, last=True)__ przenosi element na koniec (lub na początek, gdy `last=False`).
 - __.popitem(last=True)__ usuwa ostatni element (lub pierwszy, gdy `last=False`).

```python
from collections import OrderedDict

d = OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
print(list(d.items()))
#Output: [('a', 'A'), ('b', 'B'), ('c', 'C')]

d.move_to_end('a')
print(list(d))
#Output: ['b', 'c', 'a']
print(d.popitem(last=False))
#Output: ('b', 'B')

print({1: 1, 2: 2} == {2: 2, 1: 1})
#Output: True
print(OrderedDict([(1, 1), (2, 2)]) == OrderedDict([(2, 2), (1, 1)]))
#Output: False
```

### deque() [⬆️](#)
<a name="deque"></a>

Kolejka dwustronna: szybkie dodawanie i usuwanie elementów z obu końców (`list.pop(0)` jest wolne dla długich list). Przydaje się np. w przeszukiwaniu wszerz (BFS).

```python
from collections import deque

q = deque([1, 2, 3])
q.append(4)          # na koniec
q.appendleft(0)      # na początek
print(q)
#Output: deque([0, 1, 2, 3, 4])
print(q.popleft(), q.pop())
#Output: 0 4
q.rotate(1)          # przesunięcie cykliczne w prawo
print(q)
#Output: deque([3, 1, 2])
```

   * __append(x)__ / __appendleft(x)__ -> dodaje element na koniec / na początek
   * __pop()__ / __popleft()__ -> usuwa i zwraca element z końca / z początku (kolejka FIFO: `append` + `popleft`)
   * __rotate(n)__ -> przesuwa elementy cyklicznie o `n` w prawo (ujemne `n` - w lewo)
   * __deque(maxlen=k)__ -> kolejka o ograniczonej długości: po dodaniu elementu ponad limit najstarszy z drugiego końca jest usuwany

```python
# BFS: najkrótsza droga w labiryncie ("#" - ściana), ruchy góra / dół / lewo / prawo
from collections import deque

plansza = ["..#.",
           ".##.",
           "...."]
n, m = len(plansza), len(plansza[0])
odl = [[-1] * m for _ in range(n)]
odl[0][0] = 0
kolejka = deque([(0, 0)])
while kolejka:
    w, k = kolejka.popleft()
    for dw, dk in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nw, nk = w + dw, k + dk
        if 0 <= nw < n and 0 <= nk < m and plansza[nw][nk] == "." and odl[nw][nk] == -1:
            odl[nw][nk] = odl[w][k] + 1
            kolejka.append((nw, nk))
print(odl[0][3])
#Output: 7
```

```python
# deque z maxlen - pamięta tylko k ostatnich elementów (okno przesuwne)
from collections import deque

ostatnie = deque(maxlen=3)
for x in [5, 1, 4, 2, 8]:
    ostatnie.append(x)
    print(list(ostatnie), sum(ostatnie))
#Output: [5] 5
#Output: [5, 1] 6
#Output: [5, 1, 4] 10
#Output: [1, 4, 2] 7
#Output: [4, 2, 8] 14
```

## math
<a name="funkcje"></a>

### Funkcje [⬆️](#)

Funkcje trygonometryczne przyjmują kąt w __radianach__.

- __cos(x)__ -> Zwraca cosinus argumentu x.
- __sin(x)__ -> Zwraca sinus argumentu x.
- __tan(x)__ -> Zwraca tangens argumentu x.
- __radians(x)__ -> Przekształca kąt x ze stopni na radiany.
- __degrees(x)__ -> Przekształca kąt x z radianów na stopnie.
- __exp(x)__ -> Zwraca wartość e**x.
- __fabs(x)__ -> Zwraca moduł (wartość bezwzględną) argumentu x, zawsze jako liczbę zmiennoprzecinkową.
- __floor(x)__ -> Zwraca podłogę argumentu x, czyli największą liczbę całkowitą nie większą od x (jako `int`), np. `floor(-2.5) == -3`.
- __ceil(x)__ -> Zwraca sufit argumentu x, czyli najmniejszą liczbę całkowitą nie mniejszą od x (jako `int`).
- __trunc(x)__ -> Obcina część ułamkową (zaokrągla w stronę zera), jak `int(x)`.
- __hypot(x, y)__ -> Zwraca wartość sqrt(x*x + y*y). Jest to długość przeciwprostokątnej w trójkącie prostokątnym o przyprostokątnych, których długości są równe x oraz y, lub odległość punktu (x, y) od środka układu współrzędnych.
- __log(x, base)__ -> Zwraca logarytm z x o podstawie `base`; bez drugiego argumentu - logarytm naturalny (o podstawie e).
- __log10(x)__ -> Zwraca logarytm z x o podstawie 10.
- __log2(x)__ -> Zwraca logarytm z x o podstawie 2.
- __pow(x, y)__ -> Zwraca wartość x**y (zawsze jako `float`).
- __sqrt(x)__ -> Zwraca pierwiastek kwadratowy z x (jako `float`).
- __isqrt(n)__ -> Zwraca całkowitą część pierwiastka z liczby całkowitej n (dokładnie, bez błędów zaokrągleń) - przydatne przy sprawdzaniu, czy liczba jest pierwsza.
- __dist(p, q)__ -> Zwraca odległość (euklidesową) między punktami p i q podanymi jako krotki/listy współrzędnych.
- __factorial(n)__ -> Zwraca silnię n!.
- __comb(n, k)__ -> Zwraca liczbę kombinacji (symbol Newtona).
- __perm(n, k)__ -> Zwraca liczbę wariacji bez powtórzeń (k-elementowych ustawień z n elementów).
- __fsum(iterable)__ -> Zwraca dokładną sumę liczb zmiennoprzecinkowych (bez błędów zaokrągleń, które pojawiają się przy dodawaniu w pętli).
- __prod(iterable)__ -> Zwraca iloczyn elementów.
- __gcd(a, b)__ -> Zwraca największy wspólny dzielnik (NWD).
- __lcm(a, b)__ -> Zwraca najmniejszą wspólną wielokrotność (NWW), od Pythona 3.9. We wcześniejszych wersjach: `a * b // gcd(a, b)`.
- __e__ -> Stała: liczba Eulera (2.7182...).
- __pi__ -> Stała: liczba pi (3.1415...).
- __inf__ -> Stała: nieskończoność (przydatna jako początkowe minimum).

```python
import math

print(math.floor(2.7), math.ceil(2.1), math.floor(-2.5), math.trunc(-2.5))
#Output: 2 3 -3 -2
print(math.sqrt(16), math.isqrt(17), math.pow(2, 3))
#Output: 4.0 4 8.0
print(math.gcd(12, 18), math.lcm(4, 6), 12 * 18 // math.gcd(12, 18))
#Output: 6 12 36
print(math.factorial(5), math.comb(5, 2), math.perm(5, 2), math.prod([2, 3, 4]))
#Output: 120 10 20 24
print(math.log(8, 2), math.log10(1000), math.log2(1024))
#Output: 3.0 3.0 10.0
print(math.hypot(3, 4), math.dist((1, 1), (4, 5)))
#Output: 5.0 5.0
print(round(math.sin(math.radians(30)), 2), round(math.degrees(math.pi), 1))
#Output: 0.5 180.0
suma = 0
for x in [0.1] * 10:
    suma += x
print(suma, math.fsum([0.1] * 10))
#Output: 0.9999999999999999 1.0
```

```python
# typowe zastosowania na maturze
import math

def czy_pierwsza(n):
    if n < 2:
        return False
    for d in range(2, math.isqrt(n) + 1):   # wystarczy sprawdzić dzielniki do pierwiastka
        if n % d == 0:
            return False
    return True

print([n for n in range(30) if czy_pierwsza(n)])
#Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
n = (10**15 + 1) ** 2 - 1
print(math.isqrt(n), int(math.sqrt(n)))       # isqrt jest dokładne, sqrt liczy na float
#Output: 1000000000000000 1000000000000001
print(math.isqrt(49) ** 2 == 49, math.isqrt(50) ** 2 == 50)  # czy liczba jest kwadratem
#Output: True False
print(math.gcd(12, 18, 24), math.lcm(4, 6, 10))  # wiele argumentów (Python 3.9+)
#Output: 6 60
a, b = 12, 18
g = math.gcd(a, b)
print(f"{a // g}/{b // g}")                   # skracanie ułamka 12/18
#Output: 2/3
print([math.comb(4, k) for k in range(5)])    # wiersz trójkąta Pascala
#Output: [1, 4, 6, 4, 1]
print(math.perm(5), math.perm(5, 3), math.comb(49, 6))
#Output: 120 60 13983816
```

## statistics
<a name="statfunc"></a>

### Funkcje [⬆️](#)

- __mean()__ -> Średnia arytmetyczna
- __median()__ -> Mediana (dla parzystej liczby elementów: średnia dwóch środkowych)
- __median_low()__ -> Dla parzystej liczby elementów zwraca mniejszą z dwóch wartości środkowych
- __median_high()__ -> Dla parzystej liczby elementów zwraca większą z dwóch wartości środkowych
- __mode()__ -> Moda (dominanta) - najczęstsza wartość; gdy jest kilka, zwraca pierwszą napotkaną
- __multimode()__ -> Lista wszystkich najczęstszych wartości
- __pstdev()__ -> Odchylenie standardowe całej populacji (dzielenie przez n)
- __stdev()__ -> Odchylenie standardowe z próby (dzielenie przez n - 1)
- __pvariance()__ -> Wariancja całej populacji (dzielenie przez n)
- __variance()__ -> Wariancja z próby (dzielenie przez n - 1)

```python
import statistics

dane = [2, 4, 4, 4, 5, 5, 7, 9]
print(statistics.mean(dane), statistics.median(dane))
#Output: 5 4.5
print(statistics.median_low(dane), statistics.median_high(dane))
#Output: 4 5
print(statistics.mode(dane), statistics.multimode([1, 1, 2, 2, 3]))
#Output: 4 [1, 2]
print(statistics.pstdev(dane), statistics.pvariance(dane))
#Output: 2.0 4
print(round(statistics.stdev(dane), 4), round(statistics.variance(dane), 4))
#Output: 2.1381 4.5714
```

## re
<a name="refunc"></a>

Wyrażenia regularne (RegEx) w Pythonie. Wzorce warto zapisywać jako surowe napisy `r"..."` - wtedy `\` nie jest traktowany jako znak specjalny Pythona (np. `"\b"` to znak backspace, a `r"\b"` to granica słowa).

### Funkcje [⬆️](#)

- __findall(wzorzec, tekst)__ -> Zwraca listę wszystkich dopasowań (gdy wzorzec ma grupy w nawiasach - listę grup)
- __search(wzorzec, tekst)__ -> Zwraca obiekt `Match` dla pierwszego dopasowania w dowolnym miejscu tekstu albo `None`
- __match(wzorzec, tekst)__ -> Jak `search()`, ale dopasowanie musi zaczynać się na początku tekstu
- __fullmatch(wzorzec, tekst)__ -> Dopasowanie musi obejmować cały tekst (np. sprawdzanie poprawności formatu)
- __split(wzorzec, tekst)__ -> Zwraca listę fragmentów tekstu podzielonego w miejscach dopasowań
- __sub(wzorzec, zamiana, tekst)__ -> Zamienia wszystkie dopasowania na podany napis
- Obiekt `Match`: `.group()` - dopasowany tekst, `.group(1)` - pierwsza grupa, `.start()` / `.end()` - pozycje

```python
import re

tekst = "Ala ma 2 koty i 13 rybek, tel. 123-456-789"
print(re.findall(r"\d+", tekst))
#Output: ['2', '13', '123', '456', '789']
m = re.search(r"\d{3}-\d{3}-\d{3}", tekst)
print(m.group(), m.start())
#Output: 123-456-789 31
print(re.match(r"\d+", tekst), re.match(r"[A-Z]\w+", tekst).group())
#Output: None Ala
print(re.fullmatch(r"[01]+", "10110") is not None, re.fullmatch(r"[01]+", "1012") is not None)
#Output: True False
print(re.sub(r"\d", "#", "a1b22"), re.split(r"[,;]\s*", "a, b;c"))
#Output: a#b## ['a', 'b', 'c']
print(re.findall(r"(\w+)@(\w+)\.pl", "jan@wp.pl, ola@onet.pl"))
#Output: [('jan', 'wp'), ('ola', 'onet')]
print(re.findall(r"\bk\w*", "kot i kajak oraz smok"))
#Output: ['kot', 'kajak']
```

### Metaznaki [⬆️](#)
<a name="meta"></a>

| znak | opis | przykład
| :--: | :--: | :--:
| `[]` | Zbiór znaków | `"[a-m]"`
| `\` | Początek specjalnej sekwencji (lub zwykły znak specjalny, np. `\.` to kropka) | `"\d"`
| `.` | Dowolny znak oprócz znaku nowej linii | `"he..o"`
| `^` | Początek tekstu | `"^hello"`
| `$` | Koniec tekstu | `"world$"`
| `*` | Zero lub więcej powtórzeń | `"aix*"`
| `+` | Jedno lub więcej powtórzeń | `"aix+"`
| `?` | Zero lub jedno powtórzenie | `"aix?"`
| `{}` | Dokładna liczba powtórzeń lub zakres `{min,max}` | `"al{2}"`, `"\d{2,4}"`
| &#124; | Alternatywa: to albo to | "falls&#124;stays"
| `()` | Grupa (fragment, który można potem odczytać) | `"(\d+)-(\d+)"`

### Specjalne sekwencje
<a name="special"></a>

| znak | opis | przykład
| :--: | :--: | :--:
| `\A` | Dopasowanie tylko na początku tekstu | `"\AThe"`
| `\b` | Granica słowa: dopasowanie na początku lub na końcu słowa (używaj `r"..."`) | `r"\bain"` `r"ain\b"`
| `\B` | Dopasowanie wewnątrz słowa, ale nie na jego początku lub końcu (używaj `r"..."`) | `r"\Bain"` `r"ain\B"`
| `\d` | Cyfra | `"\d"`
| `\D` | Znak, który nie jest cyfrą | `"\D"`
| `\s` | Biały znak (spacja, tabulator, nowa linia...) | `"\s"`
| `\S` | Znak, który nie jest białym znakiem | `"\S"`
| `\w` | Znak „słowa”: litera (także polska), cyfra lub podkreślnik `_` | `"\w"`
| `\W` | Znak, który nie pasuje do `\w` | `"\W"`
| `\Z` | Dopasowanie tylko na końcu tekstu | `"Spain\Z"`

### Zbiory
<a name="sets"></a>

| zbiór | opis
| :--: | :--:
| `[arn]` | Jeden ze znaków: `a`, `r` lub `n`
| `[a-n]` | Dowolna mała litera od `a` do `n`
| `[^arn]` | Dowolny znak oprócz wymienionych
| `[0123]` | Jedna z wymienionych cyfr
| `[0-9]` | Dowolna cyfra od 0 do 9
| `[0-5][0-9]` | Liczba dwucyfrowa od 00 do 59
| `[a-zA-Z]` | Dowolna litera alfabetu angielskiego, mała lub wielka
| `[+]` | Wewnątrz zbioru znaki specjalne tracą znaczenie - tu dopasowuje zwykły znak `+`

### Znaki specjalne w napisach
<a name="biale"></a>

Sekwencje zaczynające się od `\` w zwykłych napisach Pythona (w napisach surowych `r"..."` nie są zamieniane).

| znak | opis
| :--: | :--:
| `\'` | Apostrof
| `\"` | Cudzysłów
| `\\` | Ukośnik wsteczny (backslash)
| `\n` | Nowa linia (enter)
| `\r` | Powrót karetki (carriage return)
| `\t` | Tabulator
| `\b` | Backspace
| `\f` | Nowa strona (form feed)
| `\ooo` | Znak o kodzie zapisanym ósemkowo, np. `\101` to `A`
| `\xhh` | Znak o kodzie zapisanym szesnastkowo, np. `\x41` to `A`

## fractions [⬆️](#)
<a name="ulamki"></a>

`fractions.Fraction(numerator=0, denominator=1)` - ułamek zwykły liczony dokładnie (bez błędów zaokrągleń). Ułamek jest automatycznie skracany, a znak minus trafia do licznika.

```python
from fractions import Fraction

print(Fraction(16, -10), Fraction(123), Fraction())
#Output: -8/5 123 0
print(Fraction('3/7'), Fraction(' -3/7 '), Fraction('0.25'))
#Output: 3/7 -3/7 1/4
print(repr(Fraction(6, 4)))
#Output: Fraction(3, 2)
u = Fraction(1, 3) + Fraction(1, 6)
print(u, u.numerator, u.denominator, float(u))
#Output: 1/2 1 2 0.5
print(Fraction(0.1) == Fraction(1, 10), Fraction(0.1).limit_denominator(100))
#Output: False 1/10
```

## itertools [⬆️](#)

Funkcje z `itertools` zwracają iteratory - żeby zobaczyć wszystkie elementy naraz, trzeba je zamienić na listę (`list(...)`) albo przejść pętlą `for`.

### count()
<a name="count"></a>

Nieskończony licznik: `count(start=0, step=1)`.

```python
import itertools

data = [100, 200, 300, 400]
data2 = list(zip(itertools.count(start=0, step=1), data))
print(data2)
#Output: [(0, 100), (1, 200), (2, 300), (3, 400)]
```

### zip_longest()
<a name="zip_longest"></a>

zip -> iteruje tyle razy, ile wynosi długość najkrótszego obiektu

zip_longest -> iteruje tyle razy, ile wynosi długość najdłuższego obiektu; brakujące miejsca wypełnia `fillvalue` (domyślnie `None`)

```python
# zwykły zip
data = [100, 200, 300, 400]
data2 = list(zip(range(10), data))
print(data2)
#Output: [(0, 100), (1, 200), (2, 300), (3, 400)]
```

```python
# itertools.zip_longest
import itertools

data = [100, 200, 300, 400]
data2 = list(itertools.zip_longest(range(6), data))
print(data2)
#Output: [(0, 100), (1, 200), (2, 300), (3, 400), (4, None), (5, None)]
print(list(itertools.zip_longest("abc", "x", fillvalue="-")))
#Output: [('a', 'x'), ('b', '-'), ('c', '-')]
```

### cycle()
<a name="cycle"></a>

Powtarza elementy obiektu w nieskończoność.

```python
import itertools

data = itertools.cycle([0, 1])
for _ in range(6):
    print(next(data), end=" ")
print()
#Output: 0 1 0 1 0 1
```

### repeat()
<a name="repeat"></a>

Powtarza jedną wartość `times` razy (bez `times` - w nieskończoność).

```python
import itertools

data = itertools.repeat(2, times=3)
print(list(data))
#Output: [2, 2, 2]
# kolejne next(data) zgłosiłoby StopIteration

print(list(map(pow, range(5), itertools.repeat(2))))
#Output: [0, 1, 4, 9, 16]
```

### starmap()
<a name="starmap"></a>

Jak `map()`, ale każdy element (krotka) jest rozpakowywany na argumenty funkcji.

```python
import itertools

print(list(itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])))
#Output: [0, 1, 4]
```

### combinations()
<a name="combinations"></a>

Wszystkie możliwe sposoby wybrania pewnej liczby elementów, gdzie kolejność nie ma znaczenia (kombinacje). Nie ma np. `('b', 'a')`, bo to to samo co `('a', 'b')`. Wersja z powtórzeniami elementów: `combinations_with_replacement()`.

```python
import itertools

chars = ['a', 'b', 'c', 'd']
result = itertools.combinations(chars, 2)
print(list(result))
#Output: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
print(len(list(itertools.combinations(range(10), 3))))
#Output: 120
liczby = [3, 7, 5, 5, 2, 8]
print(sum(1 for x, y in itertools.combinations(liczby, 2) if x + y == 10))  # ile par daje sumę 10
#Output: 3
```

### permutations()
<a name="permutations"></a>

Wszystkie możliwe ustawienia pewnej liczby elementów, gdzie kolejność MA znaczenie. Bez drugiego argumentu - permutacje wszystkich elementów.

```python
import itertools

chars = ['a', 'b', 'c', 'd']
result = itertools.permutations(chars, 2)
print(list(result))
#Output: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('b', 'd'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c')]
print(["".join(p) for p in itertools.permutations("abc")])
#Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```

### product()
<a name="product"></a>

Iloczyn kartezjański: wszystkie możliwe ciągi elementów, gdzie kolejność MA znaczenie, a elementy mogą się powtarzać (`repeat` - długość ciągu).

```python
import itertools

numbers = [0, 1]
result = itertools.product(numbers, repeat=2)
print(list(result))
#Output: [(0, 0), (0, 1), (1, 0), (1, 1)]
print(list(itertools.product("ab", [1, 2])))
#Output: [('a', 1), ('a', 2), ('b', 1), ('b', 2)]
print(len(list(itertools.product(range(10), repeat=3))))  # wszystkie 3-cyfrowe kody
#Output: 1000
```

### chain()
<a name="chain"></a>

Iteracja po kilku obiektach naraz, jeden po drugim. `chain.from_iterable()` spłaszcza listę list.

```python
import itertools

numbers = [0, 1, 2, 3]
chars = ['a', 'b', 'c', 'd']
es = ['first', 'second']

print(list(itertools.chain(numbers, chars, es)))
#Output: [0, 1, 2, 3, 'a', 'b', 'c', 'd', 'first', 'second']
print(list(itertools.chain.from_iterable([[1, 2], [3], [4, 5]])))
#Output: [1, 2, 3, 4, 5]
```

### islice()
<a name="islice"></a>

Wycinek (slice) dowolnego iteratora, także nieskończonego, bez tworzenia kopii jak przy wycinaniu list. Nie obsługuje ujemnych indeksów.

```python
import itertools

# islice(obiekt, start, stop, step)
result = itertools.islice(range(10), 1, 5, 2)
print(list(result))
#Output: [1, 3]
print(list(itertools.islice(itertools.count(10), 3)))
#Output: [10, 11, 12]
```

### accumulate()
<a name="accumulate"></a>

Wyniki pośrednie kolejnych operacji (domyślnie sumy prefiksowe).

```python
import itertools, operator

numbers = [1, 5, 4, 3]

print(list(itertools.accumulate(numbers)))                # dodawanie
#Output: [1, 6, 10, 13]
print(list(itertools.accumulate(numbers, operator.mul)))  # mnożenie
#Output: [1, 5, 20, 60]
print(list(itertools.accumulate(numbers, max)))           # bieżące maksimum
#Output: [1, 5, 5, 5]
```

```python
# sumy prefiksowe: suma fragmentu a[i..j] w czasie O(1)
from itertools import accumulate

a = [2, 7, 1, 8, 2, 8]
pref = list(accumulate(a, initial=0))  # initial - wartość na początku (Python 3.8+)
print(pref)
#Output: [0, 2, 9, 10, 18, 20, 28]
i, j = 1, 3
print(pref[j + 1] - pref[i], sum(a[i:j + 1]))
#Output: 16 16
```

### groupby()
<a name="groupby"></a>

Grupowanie __kolejnych__ elementów o tym samym kluczu: `groupby(obiekt, key=None)`. Zwraca pary `(klucz, grupa)`. Jeżeli elementy o tym samym kluczu nie stoją obok siebie, utworzą kilka osobnych grup - żeby zgrupować wszystkie, trzeba najpierw posortować dane po tym samym kluczu.

```python
import itertools

# długości serii takich samych znaków
print([(k, len(list(g))) for k, g in itertools.groupby("aaabbcaa")])
#Output: [('a', 3), ('b', 2), ('c', 1), ('a', 2)]

slowa = ["kot", "pies", "koza", "pyton", "mysz"]
slowa.sort(key=lambda s: s[0])
for litera, grupa in itertools.groupby(slowa, key=lambda s: s[0]):
    print(litera, list(grupa))
#Output: k ['kot', 'koza']
#Output: m ['mysz']
#Output: p ['pies', 'pyton']
```

### pairwise()
<a name="pairwise"></a>

Kolejne pary sąsiednich elementów: `(a0, a1), (a1, a2), ...` (od Pythona 3.10). Działa jak `zip(a, a[1:])`, ale dla dowolnego obiektu iterowalnego, także pliku.

```python
from itertools import pairwise

print(list(pairwise([1, 4, 9, 16])))
#Output: [(1, 4), (4, 9), (9, 16)]
print(list(pairwise("abc")))
#Output: [('a', 'b'), ('b', 'c')]
a = [3, 5, 8, 6, 7, 9, 10, 2]
print(all(x < y for x, y in pairwise(a)))  # czy ciąg jest rosnący
#Output: False
najdl = dl = 1                             # najdłuższy spójny fragment rosnący
for x, y in pairwise(a):
    dl = dl + 1 if y > x else 1
    najdl = max(najdl, dl)
print(najdl)
#Output: 4
```

## operator [⬆️](#)
<a name="itemgetter"></a>

Operatory Pythona w postaci funkcji - przydatne jako argument `key=` przy sortowaniu oraz w `map()`, `reduce()`, `accumulate()`.

- __itemgetter(i)__ -> Tworzy funkcję zwracającą `x[i]`. `itemgetter(1, 0)` zwraca krotkę `(x[1], x[0])` - sortowanie po kilku kluczach.
- __attrgetter("nazwa")__ -> Tworzy funkcję zwracającą atrybut obiektu `x.nazwa`.
- __add, sub, mul, truediv, floordiv, mod, pow__ -> Odpowiedniki `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- __eq, ne, lt, le, gt, ge__ -> Odpowiedniki `==`, `!=`, `<`, `<=`, `>`, `>=`.

```python
from operator import itemgetter, mul

uczniowie = [("Ola", 5), ("Jan", 3), ("Ewa", 5), ("Adam", 4)]
print(sorted(uczniowie, key=itemgetter(1)))
#Output: [('Jan', 3), ('Adam', 4), ('Ola', 5), ('Ewa', 5)]
print(sorted(uczniowie, key=itemgetter(1, 0)))
#Output: [('Jan', 3), ('Adam', 4), ('Ewa', 5), ('Ola', 5)]
print(max(uczniowie, key=itemgetter(1)))
#Output: ('Ola', 5)

oceny = {"Ola": 5, "Jan": 3, "Adam": 4}
print(sorted(oceny.items(), key=itemgetter(1), reverse=True))
#Output: [('Ola', 5), ('Adam', 4), ('Jan', 3)]
print(list(map(mul, [1, 2, 3], [4, 5, 6])))
#Output: [4, 10, 18]
```

## functools [⬆️](#)

### reduce()
<a name="reduce"></a>

`reduce(funkcja, iterable, początek)` - „zwija” obiekt do jednej wartości, wykonując funkcję na wyniku i kolejnym elemencie: `f(f(f(a, b), c), d)`.

```python
from functools import reduce
import operator
import math

print(reduce(operator.mul, [1, 2, 3, 4, 5]))       # iloczyn
#Output: 120
print(reduce(lambda a, b: a * 10 + b, [1, 2, 3]))  # cyfry -> liczba
#Output: 123
print(reduce(math.gcd, [12, 18, 24]))              # NWD wielu liczb
#Output: 6
print(reduce(operator.add, [], 0))                 # wartość początkowa dla pustej listy
#Output: 0
```

### lru_cache / cache
<a name="cache"></a>

Dekorator zapamiętujący wyniki funkcji (memoizacja). Gdy funkcja zostanie wywołana ponownie z tymi samymi argumentami, wynik jest brany z pamięci, a nie liczony od nowa. Dzięki temu rekurencja (np. ciąg Fibonacciego) działa błyskawicznie zamiast w czasie wykładniczym. `@cache` (od Pythona 3.9) to to samo co `@lru_cache(maxsize=None)`. Argumenty funkcji muszą być niemodyfikowalne (liczby, napisy, krotki - nie listy).

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10), fib(100))
#Output: 55 354224848179261915075
```

```python
# @cache: liczba dróg w siatce (ruchy tylko w prawo i w dół)
from functools import cache

@cache
def drogi(w, k):
    if w == 0 or k == 0:
        return 1
    return drogi(w - 1, k) + drogi(w, k - 1)

print(drogi(2, 2), drogi(16, 16))
#Output: 6 601080390
```

Przy bardzo głębokiej rekurencji (np. `fib(5000)` od razu) Python zgłosi `RecursionError` - wtedy pomaga `sys.setrecursionlimit(10000)` albo wersja iteracyjna.

### cmp_to_key()
<a name="cmp_to_key"></a>

Pozwala sortować według własnej funkcji porównującej `porownaj(a, b)`, która zwraca liczbę ujemną (a przed b), 0 (równe) lub dodatnią (b przed a).

```python
from functools import cmp_to_key

def porownaj(a, b):
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0

# największa liczba ułożona z podanych liczb
liczby = [3, 30, 34, 5, 9]
print("".join(sorted(map(str, liczby), key=cmp_to_key(porownaj))))
#Output: 9534330
```

## bisect [⬆️](#)
<a name="bisect"></a>

Wyszukiwanie binarne w __posortowanej__ liście - O(log n) zamiast O(n) przy przeglądaniu po kolei.

- __bisect_left(a, x)__ -> Indeks pierwszego elementu `>= x` (miejsce wstawienia `x` przed równymi). Tyle elementów listy jest mniejszych od `x`.
- __bisect_right(a, x)__ (to samo co __bisect(a, x)__) -> Indeks pierwszego elementu `> x`. Tyle elementów jest `<= x`.
- __insort(a, x)__ -> Wstawia `x` tak, żeby lista pozostała posortowana (szukanie jest szybkie, ale samo wstawienie to O(n)).
- Od Pythona 3.10 funkcje przyjmują `key=`, jak `sorted()`.

```python
from bisect import bisect_left, bisect_right, insort

a = [1, 3, 3, 3, 7, 9]
print(bisect_left(a, 3), bisect_right(a, 3), bisect_left(a, 4))
#Output: 1 4 4
print(bisect_right(a, 3) - bisect_left(a, 3))  # ile razy występuje 3
#Output: 3
print(bisect_right(a, 7) - bisect_left(a, 2))  # ile elementów z przedziału [2, 7]
#Output: 4
i = bisect_left(a, 7)
print(i < len(a) and a[i] == 7)                # czy 7 jest w liście
#Output: True
insort(a, 5)
print(a)
#Output: [1, 3, 3, 3, 5, 7, 9]
progi = [30, 50, 75, 90]                       # numer przedziału, do którego należy wynik
oceny = "FDCBA"
print([oceny[bisect_right(progi, p)] for p in [12, 30, 74, 90, 100]])
#Output: ['F', 'D', 'C', 'A', 'A']
```

## heapq [⬆️](#)
<a name="heapq"></a>

Kopiec (kolejka priorytetowa) na zwykłej liście: `kopiec[0]` to zawsze __najmniejszy__ element, a dodanie i zdjęcie elementu kosztuje O(log n). Python ma tylko kopiec minimalny - kopiec maksymalny uzyskamy, wstawiając liczby ze znakiem minus.

- __heappush(kopiec, x)__ -> Dodaje element.
- __heappop(kopiec)__ -> Usuwa i zwraca najmniejszy element.
- __heapify(lista)__ -> Zamienia listę w kopiec w miejscu (O(n)).
- __nlargest(k, iterable, key=None)__ / __nsmallest(k, iterable, key=None)__ -> Lista `k` największych / najmniejszych elementów.
- Elementami mogą być krotki `(priorytet, dane)` - porównywane są najpierw po priorytecie.

```python
import heapq

kopiec = []
for x in [5, 1, 8, 3, 2]:
    heapq.heappush(kopiec, x)
print(kopiec[0], [heapq.heappop(kopiec) for _ in range(3)])
#Output: 1 [1, 2, 3]
a = [9, 4, 7, 1]
heapq.heapify(a)
print(heapq.heappop(a), a[0])
#Output: 1 4
print(heapq.nlargest(3, [5, 1, 8, 3, 9, 2]), heapq.nsmallest(2, [5, 1, 8, 3, 9, 2]))
#Output: [9, 8, 5] [1, 2]
print(heapq.nlargest(2, ["kot", "hipopotam", "pies"], key=len))
#Output: ['hipopotam', 'pies']
maks = []                                      # kopiec maksymalny - liczby z minusem
for x in [5, 1, 8]:
    heapq.heappush(maks, -x)
print(-heapq.heappop(maks))
#Output: 8
zadania = [(3, "pranie"), (1, "matura"), (2, "zakupy")]
heapq.heapify(zadania)
while zadania:
    priorytet, nazwa = heapq.heappop(zadania)
    print(priorytet, nazwa)
#Output: 1 matura
#Output: 2 zakupy
#Output: 3 pranie
```

## datetime [⬆️](#)
<a name="datetime"></a>

Daty w zadaniach maturalnych: ile dni minęło między pomiarami, jaki to dzień tygodnia, dane z kolejnych dni.

- __date(rok, miesiąc, dzień)__ -> Data.
- __date.fromisoformat("2024-05-08")__ -> Data z napisu w formacie `RRRR-MM-DD` (taki format ma wiele plików CKE).
- __datetime.strptime(napis, format)__ -> Data i czas z napisu w dowolnym formacie, np. `"%d.%m.%Y"` (`%d` dzień, `%m` miesiąc, `%Y` rok, `%H:%M` godzina); `.date()` zostawia samą datę.
- __d2 - d1__ -> Różnica dat (`timedelta`); liczba dni to `(d2 - d1).days`.
- __d + timedelta(days=n)__ -> Data przesunięta o `n` dni (są też `weeks=`, `hours=`, `minutes=`).
- __.weekday()__ -> Dzień tygodnia: 0 = poniedziałek, ..., 6 = niedziela. __.isoweekday()__ -> 1 = poniedziałek, ..., 7 = niedziela.
- __.year__, __.month__, __.day__ -> Części daty.
- __.strftime(format)__ -> Data jako napis, np. `d.strftime("%d.%m.%Y")`. Nazwy dni i miesięcy (`%A`, `%B`) zależą od ustawień systemu, więc polskie nazwy lepiej trzymać we własnej liście.
- Daty można porównywać (`<`, `==`), sortować i używać jako kluczy słownika. Napisy `RRRR-MM-DD` sortują się poprawnie nawet jako zwykły tekst.

```python
from datetime import date, datetime, timedelta

d1 = date(2024, 2, 27)
d2 = date.fromisoformat("2024-03-02")
print(d2 - d1, (d2 - d1).days)                 # 2024 jest rokiem przestępnym
#Output: 4 days, 0:00:00 4
print(d1 + timedelta(days=3), d1 - timedelta(weeks=1))
#Output: 2024-03-01 2024-02-20
dni = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
print(d2.weekday(), d2.isoweekday(), dni[d2.weekday()])
#Output: 5 6 sobota
print(d2.year, d2.month, d2.day, d2.strftime("%d.%m.%Y"))
#Output: 2024 3 2 02.03.2024
d3 = datetime.strptime("08.05.2023", "%d.%m.%Y").date()
print(d3, d3 > d2, min(d1, d2, d3))
#Output: 2023-05-08 False 2023-05-08
maj = [date(2023, 5, 1) + timedelta(days=i) for i in range(31)]
print(sum(1 for d in maj if d.weekday() == 6))  # ile niedziel było w maju 2023
#Output: 4
t1 = datetime(2024, 5, 8, 9, 0)
t2 = datetime(2024, 5, 8, 12, 30)
print(t2 - t1, (t2 - t1).total_seconds() / 60)  # różnica w minutach
#Output: 3:30:00 210.0
```

```python
# odstępy (w dniach) między kolejnymi datami z pliku
from datetime import date

with open("pomiary.txt", "w") as f:
    f.write("2023-12-30\n2024-01-02\n2024-01-03\n2024-03-01\n")

with open("pomiary.txt") as f:
    daty = [date.fromisoformat(linia.strip()) for linia in f]
print([(b - a).days for a, b in zip(daty, daty[1:])])
#Output: [3, 1, 58]
```

### calendar
<a name="calendar"></a>

- __calendar.isleap(rok)__ -> `True`, jeżeli rok jest przestępny (podzielny przez 4 i niepodzielny przez 100 albo podzielny przez 400).
- __calendar.monthrange(rok, miesiąc)__ -> Krotka (dzień tygodnia 1. dnia miesiąca, liczba dni w miesiącu); dni tygodnia numerowane jak w `weekday()` (od Pythona 3.12 jako stałe `calendar.MONDAY`... - `int()` zamienia je na liczbę).
- __calendar.leapdays(r1, r2)__ -> Liczba lat przestępnych w przedziale `[r1, r2)`.

```python
import calendar

print(calendar.isleap(2024), calendar.isleap(1900), calendar.isleap(2000))
#Output: True False True
pierwszy, ile_dni = calendar.monthrange(2024, 2)   # luty 2024 zaczął się w czwartek (3)
print(int(pierwszy), ile_dni, calendar.monthrange(2023, 2)[1])
#Output: 3 29 28
print(calendar.leapdays(2000, 2025))
#Output: 7
rok = 2100
print(rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0))  # to samo bez modułu
#Output: False
```

## sys [⬆️](#)
<a name="sys"></a>

- __sys.setrecursionlimit(n)__ -> Podnosi limit głębokości rekurencji (domyślnie ok. 1000 wywołań, potem `RecursionError`). Przy bardzo głębokiej rekurencji program może mimo to przepełnić stos - wtedy lepiej przepisać algorytm na pętlę.
- __sys.getrecursionlimit()__ -> Zwraca aktualny limit.

```python
import sys

sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())
#Output: 10000

def dlugosc(lista, i=0):        # rekurencyjne liczenie długości listy
    if i == len(lista):
        return 0
    return 1 + dlugosc(lista, i + 1)

print(dlugosc([0] * 5000))      # przy domyślnym limicie: RecursionError
#Output: 5000
```

## enum [⬆️](#)
<a name="enum-klasa"></a>

Typ wyliczeniowy: zbiór nazwanych stałych. Zamiast „magicznych” liczb (np. 1, 2, 3) używamy czytelnych nazw. Na maturze rzadko potrzebny.

```python
from enum import Enum

class Kolor(Enum):
    CZERWONY = 1
    ZIELONY = 2
    NIEBIESKI = 3

print(Kolor.ZIELONY, Kolor.ZIELONY.name, Kolor.ZIELONY.value)
#Output: Kolor.ZIELONY ZIELONY 2
print(Kolor(3), Kolor["CZERWONY"])
#Output: Kolor.NIEBIESKI Kolor.CZERWONY
print([k.name for k in Kolor])
#Output: ['CZERWONY', 'ZIELONY', 'NIEBIESKI']
print(Kolor.CZERWONY == Kolor.CZERWONY, Kolor.CZERWONY == 1)
#Output: True False
```
