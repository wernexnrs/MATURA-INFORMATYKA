<h1 align="center"> Metody </h1>
<p align="center">Nie jest to wyczerpanie tematu - tylko metody najbardziej przydatne na maturze.</p>

### STRING [⬆️](#)
<p>Napisy są niemodyfikowalne: wszystkie metody napisów zwracają nową wartość i nie zmieniają oryginalnego ciągu znaków. Wynik trzeba zapisać, np. <code>s = s.upper()</code>.</p>

<h5> Wielkość liter </h5>

  * __.lower()__ -> zamienia wszystkie litery na małe
  * __.upper()__ -> zamienia wszystkie litery na wielkie
  * __.capitalize()__ -> zamienia pierwszy znak na wielką literę, a pozostałe na małe
  * __.title()__ -> zamienia pierwszą literę każdego słowa na wielką, a pozostałe na małe
  * __.swapcase()__ -> zamienia małe litery na wielkie, a wielkie na małe

<h5> Szukanie i liczenie </h5>

  * __.count(sub, start=0, end=len(s))__ -> zwraca liczbę wystąpień podciągu `sub` (wystąpienia nie mogą na siebie nachodzić: `"aaaa".count("aa") == 2`). Opcjonalnie tylko w zakresie `s[start:end]`
  * __.find(sub, start=0, end=len(s))__ -> zwraca indeks początku pierwszego wystąpienia `sub`, a -1, jeżeli go nie ma
  * __.rfind(sub, start=0, end=len(s))__ -> jak `.find()`, ale zwraca indeks __ostatniego__ wystąpienia
  * __.index(sub, start=0, end=len(s))__ -> to samo co `.find()`, tylko gdy `sub` nie występuje, zgłasza błąd `ValueError` (analogicznie `.rindex()`)
  * __.startswith(prefix, start=0, end=len(s))__ -> `True`, jeżeli napis zaczyna się od `prefix` (można podać krotkę kilku możliwości)
  * __.endswith(suffix, start=0, end=len(s))__ -> `True`, jeżeli napis kończy się na `suffix` (można podać krotkę kilku możliwości)
  * Samo sprawdzenie, czy podciąg występuje: `"ab" in s`

<h5> Sprawdzanie zawartości </h5>

Dla pustego napisu wszystkie poniższe metody zwracają `False`. Żadna z nich nie uzna za liczbę napisu `"-5"` ani `"3.14"`.

  * __.isalpha()__ -> `True`, jeżeli same litery (także polskie, np. `"żółw"`)
  * __.isdigit()__ -> `True`, jeżeli same cyfry (także np. indeks górny `"²"`)
  * __.isdecimal()__ -> `True`, jeżeli same cyfry dziesiętne (`"0"`-`"9"`) - najbezpieczniejszy test przed `int()`
  * __.isnumeric()__ -> `True`, jeżeli same znaki liczbowe Unicode: cyfry, ale też np. `"½"`, `"Ⅻ"` (najszersza z trzech metod)
  * __.isalnum()__ -> `True`, jeżeli same litery i cyfry
  * __.isspace()__ -> `True`, jeżeli same białe znaki (spacja, tabulator, znak nowej linii...)
  * __.islower()__ -> `True`, jeżeli wszystkie litery są małe (i jest co najmniej jedna litera)
  * __.isupper()__ -> `True`, jeżeli wszystkie litery są wielkie (i jest co najmniej jedna litera)
  * __.istitle()__ -> `True`, jeżeli każde słowo zaczyna się wielką literą, a dalej ma małe

<h5> Dzielenie, łączenie, zamiana </h5>

  * __.split(sep=None, maxsplit=-1)__ -> zwraca listę fragmentów napisu oddzielonych separatorem `sep`. Bez argumentu dzieli po dowolnych białych znakach i pomija puste fragmenty. `maxsplit` ogranicza liczbę podziałów (-1 = bez limitu)
  * __.rsplit(sep=None, maxsplit=-1)__ -> jak `.split()`, ale przy `maxsplit` dzieli od końca
  * __.splitlines(keepends=False)__ -> zwraca listę linii napisu (podział na końcach linii); `keepends=True` zostawia znaki końca linii
  * __.partition(sep)__ -> zwraca krotkę `(przed, sep, po)` podzieloną na pierwszym wystąpieniu `sep`
  * __"sep".join(iterable)__ -> łączy napisy z obiektu iterowalnego, wstawiając między nie `sep`, np. `".".join(["a", "b"]) == "a.b"`. Elementy muszą być napisami
  * __.replace(old, new, count=-1)__ -> zamienia wystąpienia `old` na `new`; `count` ogranicza liczbę zamian (domyślnie wszystkie)
  * __.strip(chars=None)__ -> usuwa z początku i końca białe znaki lub znaki podane w argumencie (`chars` to zbiór znaków, a nie podciąg)
  * __.lstrip(chars=None)__ / __.rstrip(chars=None)__ -> jak `.strip()`, ale tylko z lewej / z prawej strony
  * __.translate(str.maketrans(skąd, dokąd))__ -> zamienia znaki według tabeli: i-ty znak `skąd` na i-ty znak `dokąd` (np. szyfry podstawieniowe). Trzeci argument `maketrans` to znaki do usunięcia

<h5> Wyrównywanie </h5>

  * __.center(width, fillchar=" ")__ -> zwraca napis wyśrodkowany w polu o szerokości `width`, dopełniony znakiem `fillchar`
  * __.ljust(width, fillchar=" ")__ -> wyrównuje do lewej (dopełnia z prawej)
  * __.rjust(width, fillchar=" ")__ -> wyrównuje do prawej (dopełnia z lewej), np. `"101".rjust(8, "0") == "00000101"`
  * __.zfill(width)__ -> dopełnia zerami z lewej do szerokości `width` (uwzględnia znak minus)

Wycinki i odwracanie napisów (`s[2:5]`, `s[::-1]`) oraz formatowanie f-stringami (`f"{x:.2f}"`, `f"{n:08b}"`) opisane są w dziale [Funkcje wbudowane](funkcje_wbudowane.md).

```python
# metody napisów
s = "  Ala ma kota  "
print(s.strip().upper(), s.strip().lower(), "aLA mA".capitalize())
#Output: ALA MA KOTA ala ma kota Ala ma
print("abrakadabra".count("a"), "abrakadabra".find("ra"), "abrakadabra".rfind("ra"), "abc".find("x"))
#Output: 5 2 9 -1
print("plik.txt".endswith((".txt", ".csv")), "0101".startswith("01"))
#Output: True True
print("123".isdecimal(), "-5".isdecimal(), "żółw".isalpha(), "abc1".isalnum(), "".isalpha())
#Output: True False True True False
print("1 2  3".split(), "1;2;;3".split(";"), "a b c d".split(" ", 2))
#Output: ['1', '2', '3'] ['1', '2', '', '3'] ['a', 'b', 'c d']
print("klucz=wartość".partition("="))
#Output: ('klucz', '=', 'wartość')
print("-".join(["2024", "05", "08"]), " ".join(map(str, [1, 2, 3])))
#Output: 2024-05-08 1 2 3
print("banan".replace("a", "o"), "banan".replace("a", "o", 1))
#Output: bonon bonan
print("abc cab".translate(str.maketrans("abc", "xyz")), "a-b-c".translate(str.maketrans("", "", "-")))
#Output: xyz zxy abc
print("xxhixx".strip("x"), "[" + "ok".center(6, "*") + "]")
#Output: hi [**ok**]
print("7".zfill(3), "101".rjust(8, "0"), "ab".ljust(4, ".") + "|")
#Output: 007 00000101 ab..|
```

### LISTY [⬆️](#)
<p>Metody list zmieniają listę <b>w miejscu</b> i większość z nich zwraca <code>None</code> - nie pisz <code>lista = lista.sort()</code>.</p>

  * __.append(x)__ -> dodaje element `x` na koniec listy
  * __.extend(iterable)__ -> dodaje na koniec wszystkie elementy z obiektu iterowalnego (rozszerza listę)
  * __.insert(i, x)__ -> wstawia element `x` przed indeksem `i`
  * __.remove(x)__ -> usuwa pierwszy element o wartości `x`; zgłasza `ValueError`, jeżeli go nie ma
  * __.pop(i=-1)__ -> usuwa element o indeksie `i` (domyślnie ostatni) i go zwraca
  * __.clear()__ -> usuwa wszystkie elementy
  * __.index(x, start=0, end=len(lista))__ -> zwraca indeks pierwszego wystąpienia `x`; zgłasza `ValueError`, jeżeli go nie ma
  * __.count(x)__ -> zwraca liczbę wystąpień `x`
  * __.sort(key=None, reverse=False)__ -> sortuje listę w miejscu (zwraca `None`). `key` - funkcja, według której wyniku sortujemy; `reverse=True` - malejąco
  * __.reverse()__ -> odwraca kolejność elementów w miejscu (zwraca `None`)
  * __.copy()__ -> zwraca płytką kopię listy (to samo co `lista[:]`)

<h5> .sort() czy sorted()? </h5>

  * __lista.sort()__ -> zmienia oryginalną listę, działa tylko dla list
  * __sorted(obiekt)__ -> zwraca __nową__ listę, oryginał zostaje bez zmian; działa dla dowolnego obiektu iterowalnego (napisu, krotki, zbioru, słownika)

```python
# metody list
lista = [3, 1, 2]
lista.append(5)
lista.extend([7, 1])
lista.insert(0, 9)
print(lista)
#Output: [9, 3, 1, 2, 5, 7, 1]
print(lista.pop(), lista.pop(0), lista)
#Output: 1 9 [3, 1, 2, 5, 7]
lista.remove(1)
print(lista, lista.index(5), lista.count(3))
#Output: [3, 2, 5, 7] 2 1
wynik = lista.sort()
print(wynik, lista)
#Output: None [2, 3, 5, 7]
lista.sort(reverse=True)
print(lista)
#Output: [7, 5, 3, 2]
lista.reverse()
print(lista)
#Output: [2, 3, 5, 7]
slowa = ["kot", "Ala", "pies", "be"]
slowa.sort(key=len)
print(slowa, sorted(slowa, key=str.lower))
#Output: ['be', 'kot', 'Ala', 'pies'] ['Ala', 'be', 'kot', 'pies']
# pułapka: płytka kopia listy dwuwymiarowej
a = [[0, 0], [0, 0]]
b = a.copy()
b[0][0] = 1
print(a)
#Output: [[1, 0], [0, 0]]
# poprawnie: kopia każdego wiersza (albo copy.deepcopy)
a = [[0, 0], [0, 0]]
c = [wiersz[:] for wiersz in a]
c[0][0] = 1
print(a, c)
#Output: [[0, 0], [0, 0]] [[1, 0], [0, 0]]
# sortowanie listy krotek: malejąco po punktach, przy remisie rosnąco po imieniu
wyniki = [("Ola", 87), ("Jan", 92), ("Ewa", 87)]
wyniki.sort(key=lambda w: (-w[1], w[0]))
print(wyniki)
#Output: [('Jan', 92), ('Ewa', 87), ('Ola', 87)]
```

### SŁOWNIKI [⬆️](#)
<p>Odczyt <code>d[klucz]</code> zgłasza błąd <code>KeyError</code>, gdy klucza nie ma. Od Pythona 3.7 słownik pamięta kolejność dodawania elementów.</p>

  * __.get(key, default=None)__ -> zwraca wartość dla klucza `key`, a jeżeli klucza nie ma - `default` (bez błędu)
  * __.setdefault(key, default=None)__ -> zwraca wartość dla klucza; jeżeli klucza nie ma, najpierw wstawia go z wartością `default`
  * __.keys()__ -> zwraca widok kluczy (można po nim iterować, listę daje `list(d.keys())`)
  * __.values()__ -> zwraca widok wartości
  * __.items()__ -> zwraca widok par `(klucz, wartość)`, np. `for k, v in d.items():`
  * __.pop(key, default)__ -> usuwa element o danym kluczu i zwraca jego wartość; jeżeli klucza nie ma, zwraca `default`, a gdy go nie podano - zgłasza `KeyError`
  * __.popitem()__ -> usuwa i zwraca ostatnio wstawioną parę `(klucz, wartość)`
  * __.update(inny)__ -> dodaje pary z innego słownika (lub z listy par); istniejące klucze nadpisuje
  * __dict.fromkeys(klucze, value=None)__ -> tworzy nowy słownik z podanymi kluczami i jedną wartością dla wszystkich
  * __.copy()__ -> zwraca płytką kopię słownika
  * __.clear()__ -> usuwa wszystkie elementy
  * Sprawdzenie, czy klucz istnieje: `klucz in d`

```python
# metody słowników
d = {"a": 1, "b": 2}
print(d.get("a"), d.get("z"), d.get("z", 0))
#Output: 1 None 0
print(list(d.keys()), list(d.values()), list(d.items()))
#Output: ['a', 'b'] [1, 2] [('a', 1), ('b', 2)]
d.update({"b": 5, "c": 3})
print(d)
#Output: {'a': 1, 'b': 5, 'c': 3}
print(d.pop("a"), d.pop("x", -1), d)
#Output: 1 -1 {'b': 5, 'c': 3}
print(d.popitem(), d)
#Output: ('c', 3) {'b': 5}
grupy = {}
for slowo in ["kot", "koza", "pies"]:
    grupy.setdefault(slowo[0], []).append(slowo)
print(grupy)
#Output: {'k': ['kot', 'koza'], 'p': ['pies']}
# zliczanie wystąpień
licznik = {}
for znak in "abracadabra":
    licznik[znak] = licznik.get(znak, 0) + 1
print(licznik)
#Output: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
# sortowanie po wartościach (malejąco)
print(sorted(licznik.items(), key=lambda p: p[1], reverse=True)[:2])
#Output: [('a', 5), ('b', 2)]
print(max(licznik, key=licznik.get), dict.fromkeys("ab", 0))
#Output: a {'a': 0, 'b': 0}
```

### ZBIORY [⬆️](#)
<p>Zbiór przechowuje elementy bez powtórzeń i bez kolejności. Pusty zbiór to <code>set()</code> - zapis <code>{}</code> tworzy pusty słownik.</p>

  * __.add(x)__ -> dodaje element `x`
  * __.update(iterable)__ -> dodaje wszystkie elementy z obiektu iterowalnego
  * __.remove(x)__ -> usuwa element `x`; zgłasza `KeyError`, jeżeli go nie ma
  * __.discard(x)__ -> usuwa element `x`; nie zgłasza błędu, jeżeli go nie ma
  * __.pop()__ -> usuwa i zwraca dowolny element (nie wiadomo który)
  * __.clear()__ -> usuwa wszystkie elementy
  * __.copy()__ -> zwraca kopię zbioru
  * __x.union(y)__ lub `x | y` -> suma: wszystkie elementy z obu zbiorów (bez powtórzeń)
  * __x.intersection(y)__ lub `x & y` -> część wspólna: elementy, które są w obu zbiorach
  * __x.difference(y)__ lub `x - y` -> różnica: elementy z `x`, których nie ma w `y`
  * __x.symmetric_difference(y)__ lub `x ^ y` -> różnica symetryczna: elementy, które są dokładnie w jednym ze zbiorów (wszystko poza częścią wspólną)
  * __x.issubset(y)__ lub `x <= y` -> `True`, jeżeli wszystkie elementy `x` są w `y`
  * __x.issuperset(y)__ lub `x >= y` -> `True`, jeżeli `x` zawiera wszystkie elementy `y`
  * __x.isdisjoint(y)__ -> `True`, jeżeli zbiory nie mają wspólnych elementów

```python
# metody zbiorów
x = {1, 2, 3, 4}
y = {3, 4, 5}
print(sorted(x.union(y)), sorted(x | y))
#Output: [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
print(sorted(x.intersection(y)), sorted(x.difference(y)), sorted(x.symmetric_difference(y)))
#Output: [3, 4] [1, 2] [1, 2, 5]
print({3, 4}.issubset(x), x.issuperset({1, 2}), x.isdisjoint({7, 8}))
#Output: True True True
x.add(10)
x.discard(99)
x.remove(1)
print(sorted(x), len(set("abracadabra")))
#Output: [2, 3, 4, 10] 5
```

### KROTKI [⬆️](#)
<p>Krotki są niemodyfikowalne - mają tylko dwie metody.</p>

  * __.count(x)__ -> zwraca liczbę wystąpień wartości `x`
  * __.index(x)__ -> zwraca indeks pierwszego wystąpienia `x`; zgłasza `ValueError`, jeżeli go nie ma

```python
# metody krotek
t = (1, 2, 2, 3)
print(t.count(2), t.index(3))
#Output: 2 3
```

### PLIKI [⬆️](#)
Obiekt pliku zwraca funkcja `open()` (opisana w dziale [Funkcje wbudowane](funkcje_wbudowane.md)). Najwygodniej używać jej z `with` - plik zamknie się sam. Plik czytany jest od miejsca, w którym skończył poprzedni odczyt: po `.read()` kolejny odczyt zwraca pusty napis.

  * __.read()__ -> zwraca całą (pozostałą) zawartość pliku jako jeden napis
  * __.readline()__ -> zwraca kolejną linię razem ze znakiem `"\n"`; na końcu pliku zwraca pusty napis `""`. Przydaje się do pominięcia wiersza nagłówkowego
  * __.readlines()__ -> zwraca listę wszystkich (pozostałych) linii, każda ze znakiem `"\n"` na końcu
  * __for linia in plik:__ -> czytanie linia po linii - najprostsze i oszczędza pamięć
  * __.write(napis)__ -> zapisuje napis (tylko typu `str`, liczby trzeba zamienić przez `str()` lub f-string) i __nie__ dodaje `"\n"`; zwraca liczbę zapisanych znaków
  * __.writelines(lista_napisów)__ -> zapisuje kolejne napisy z listy, także bez dodawania `"\n"`
  * __.close()__ -> zamyka plik (przy `with` niepotrzebne)
  * Tryby `open()`: `"r"` - odczyt (domyślny), `"w"` - zapis od nowa (czyści plik), `"a"` - dopisywanie na końcu

```python
# metody plików
with open("liczby.txt", "w") as f:
    f.write("10\n20\n")
    f.writelines(["30\n", "40\n"])

with open("liczby.txt") as f:
    print(repr(f.readline()), repr(f.readline()))
    print(f.readlines())
#Output: '10\n' '20\n'
#Output: ['30\n', '40\n']

with open("liczby.txt") as f:
    tekst = f.read()
    print(repr(tekst), repr(f.read()))
#Output: '10\n20\n30\n40\n' ''
print(tekst.split(), tekst.splitlines())
#Output: ['10', '20', '30', '40'] ['10', '20', '30', '40']

with open("liczby.txt", "a") as f:      # dopisywanie na końcu pliku
    print(50, file=f)
with open("liczby.txt") as f:
    print([int(linia) for linia in f])  # int() ignoruje "\n" na końcu linii
#Output: [10, 20, 30, 40, 50]
```
