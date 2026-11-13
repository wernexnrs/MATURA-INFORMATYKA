<h1 align="center">  Najważniejsze funkcje wbudowane </h1>

Funkcje wbudowane są dostępne zawsze, bez żadnego `import`. Pełna lista: `help("builtins")` albo [dokumentacja Pythona](https://docs.python.org/3/library/functions.html).

## Konwersje typów [⬆️](#)

   * __int(x)__ -> Zamienia liczbę lub napis na liczbę całkowitą. Z liczby zmiennoprzecinkowej obcina część ułamkową (w stronę zera), np. `int(-3.7) == -3`. Białe znaki na początku i końcu napisu są ignorowane, więc `int("42\n") == 42`
   * __int(napis, base)__ -> Zamienia napis zapisany w systemie o podstawie `base` (2-36) na liczbę dziesiętną, np. `int("1011", 2) == 11`, `int("ff", 16) == 255`
   * __float(x)__ -> Zamienia liczbę lub napis na liczbę zmiennoprzecinkową
   * __str(x)__ -> Zamienia obiekt na napis (string)
   * __bool(x)__ -> Zwraca `True` albo `False`. Fałszem są: `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`, `None`; wszystko inne jest prawdą (także napis `"0"`)
   * __list(iterable)__ -> Tworzy listę z dowolnego obiektu iterowalnego, np. `list("abc") == ['a', 'b', 'c']`
   * __tuple(iterable)__ -> Tworzy krotkę
   * __set(iterable)__ -> Tworzy zbiór (usuwa powtórzenia, nie zachowuje kolejności)
   * __frozenset(iterable)__ -> Tworzy zbiór niemodyfikowalny (może być kluczem słownika albo elementem innego zbioru)
   * __dict()__ -> Tworzy słownik, np. `dict(a=1, b=2)` albo `dict(zip(klucze, wartosci))`
   * __complex(re, im)__ -> Tworzy liczbę zespoloną, np. `complex(1, 2) == (1+2j)`

```python
# konwersje typów
print(int("1011", 2), int("ff", 16), int("17", 8))
#Output: 11 255 15
print(int(3.99), int(-3.99), int(" 42\n"))
#Output: 3 -3 42
print(float("2.5") * 2)
#Output: 5.0
print(str(12) + str(34))
#Output: 1234
print(bool(0), bool(""), bool("0"), bool([0]))
#Output: False False True True
print(list("abc"), set([3, 1, 3, 2]))
#Output: ['a', 'b', 'c'] {1, 2, 3}
print(dict(zip(["a", "b"], [1, 2])))
#Output: {'a': 1, 'b': 2}
```

## Liczby i systemy liczbowe [⬆️](#)

   * __abs(x)__ -> Zwraca wartość bezwzględną liczby
   * __round(x)__ -> Zaokrągla do liczby całkowitej (zwraca `int`). Uwaga: Python stosuje __zaokrąglanie bankierskie__ - gdy liczba jest dokładnie w połowie, wybiera liczbę parzystą: `round(2.5) == 2`, `round(3.5) == 4`
   * __round(x, n)__ -> Zaokrągla do `n` miejsc po przecinku (zwraca `float`). Ze względu na zapis binarny liczb wynik bywa zaskakujący: `round(2.675, 2) == 2.67`
   * __divmod(a, b)__ -> Zwraca krotkę `(a // b, a % b)`, czyli iloraz całkowity i resztę z dzielenia
   * __pow(x, y)__ -> Zwraca `x ** y`
   * __pow(x, y, m)__ -> Zwraca `(x ** y) % m`, ale liczy to dużo szybciej (szybkie potęgowanie modularne)
   * __bin(x)__ -> Zwraca zapis binarny liczby całkowitej jako napis z przedrostkiem `0b`
   * __oct(x)__ -> Zwraca zapis ósemkowy (oktalny) liczby całkowitej jako napis z przedrostkiem `0o`
   * __hex(x)__ -> Zwraca zapis szesnastkowy (heksadecymalny) liczby całkowitej jako napis z przedrostkiem `0x`
   * __format(x, "b")__ -> Zapis binarny bez przedrostka (`"o"` - ósemkowy, `"x"` - szesnastkowy). `format(5, "08b")` uzupełnia zerami do 8 znaków

```python
# liczby
print(abs(-7), abs(-2.5))
#Output: 7 2.5
print(round(2.5), round(3.5), round(-2.5), round(2.6))
#Output: 2 4 -2 3
print(round(3.14159, 2))
#Output: 3.14
print(divmod(17, 5), divmod(-7, 2))
#Output: (3, 2) (-4, 1)
print(pow(2, 10), pow(2, 10, 1000))
#Output: 1024 24
print(bin(10), oct(8), hex(255))
#Output: 0b1010 0o10 0xff
print(bin(10)[2:], format(10, "b"), format(5, "08b"))
#Output: 1010 1010 00000101
```

## Kolekcje [⬆️](#)

   * __len(x)__ -> Zwraca liczbę elementów (długość napisu, listy, słownika, zbioru...)
   * __min(iterable, key=None)__ -> Zwraca najmniejszy element. Można też podać kilka argumentów: `min(3, 1, 2)`. Parametr `key` to funkcja, według której wyniku porównujemy elementy
   * __max(iterable, key=None)__ -> Zwraca największy element; działa jak `min()`. Przy remisie zwraca pierwszy napotkany element
   * __sum(iterable, start=0)__ -> Zwraca sumę elementów (do wyniku dodaje `start`)
   * __sorted(iterable, key=None, reverse=False)__ -> Zwraca __nową__ posortowaną listę utworzoną z dowolnego obiektu iterowalnego (listy, napisu, zbioru, kluczy słownika...). Oryginał się nie zmienia. Sortowanie jest stabilne (elementy równe zachowują kolejność)
   * __reversed(sekwencja)__ -> Zwraca __iterator__ przechodzący po elementach od końca (nie listę!). Listę dostaniemy przez `list(reversed(x))`, a odwrócony napis przez `"".join(reversed(s))` lub `s[::-1]`
   * __any(iterable)__ -> Zwraca `True`, jeżeli choć jeden element jest prawdą (dla pustego obiektu `False`)
   * __all(iterable)__ -> Zwraca `True`, jeżeli każdy element jest prawdą (dla pustego obiektu `True`)

```python
# kolekcje
liczby = [5, 3, 8, 1]
slowa = ["kot", "zebra", "pies", "mysz"]
print(len(liczby), min(liczby), max(liczby), sum(liczby))
#Output: 4 1 8 17
print(max(slowa, key=len), min(slowa, key=len))
#Output: zebra kot
print(sorted(liczby), sorted(liczby, reverse=True), liczby)
#Output: [1, 3, 5, 8] [8, 5, 3, 1] [5, 3, 8, 1]
print(sorted(slowa, key=lambda s: (len(s), s)))
#Output: ['kot', 'mysz', 'pies', 'zebra']
print(sorted("python"))
#Output: ['h', 'n', 'o', 'p', 't', 'y']
print(reversed(liczby))
#Output: <list_reverseiterator object at 0x...>
print(list(reversed(liczby)), "".join(reversed("abc")))
#Output: [1, 8, 3, 5] cba
print(any(x > 7 for x in liczby), all(x > 0 for x in liczby))
#Output: True True
```

## Iteracja [⬆️](#)

   * __range(stop)__, __range(start, stop, step)__ -> Zwraca ciąg liczb całkowitych od `start` (domyślnie 0) do `stop` __bez__ `stop`, co `step` (domyślnie 1, może być ujemny)
   * __enumerate(iterable, start=0)__ -> Zwraca iterator par `(numer, element)`, numerowanych od `start`
   * __zip(*iterables)__ -> Łączy kilka obiektów w pary (krotki) element po elemencie; kończy na najkrótszym obiekcie. `zip(*macierz)` transponuje macierz
   * __map(funkcja, iterable)__ -> Zwraca iterator, który wywołuje funkcję na każdym elemencie, np. `list(map(int, "1 2 3".split()))`
   * __filter(funkcja, iterable)__ -> Zwraca iterator z tymi elementami, dla których funkcja zwraca prawdę. `filter(None, x)` usuwa elementy będące fałszem
   * __iter(obiekt)__ -> Tworzy iterator z obiektu iterowalnego
   * __next(iterator, domyślna)__ -> Zwraca kolejny element iteratora; gdy elementów zabraknie, zwraca wartość domyślną albo zgłasza `StopIteration`

```python
# iteracja
print(list(range(5)), list(range(2, 10, 3)), list(range(5, 0, -1)))
#Output: [0, 1, 2, 3, 4] [2, 5, 8] [5, 4, 3, 2, 1]
for nr, litera in enumerate("abc", start=1):
    print(nr, litera, end="; ")
print()
#Output: 1 a; 2 b; 3 c;
print(list(zip([1, 2, 3], "ab")))
#Output: [(1, 'a'), (2, 'b')]
macierz = [[1, 2, 3], [4, 5, 6]]
print(list(zip(*macierz)))
#Output: [(1, 4), (2, 5), (3, 6)]
print(list(map(int, "10 20 30".split())))
#Output: [10, 20, 30]
print(list(filter(lambda x: x % 2 == 0, range(10))))
#Output: [0, 2, 4, 6, 8]
it = iter([1, 2])
print(next(it), next(it), next(it, "koniec"))
#Output: 1 2 koniec
```

## Tekst i znaki [⬆️](#)

   * __ord(znak)__ -> Zwraca kod znaku w standardzie Unicode (dla liter angielskich to samo co ASCII): `ord("A") == 65`, `ord("a") == 97`, `ord("0") == 48`
   * __chr(kod)__ -> Zwraca znak o podanym kodzie Unicode: `chr(97) == "a"`
   * __format(wartość, specyfikacja)__ -> Formatuje wartość według specyfikacji, np. `format(3.14159, ".2f") == "3.14"`. To samo robią f-stringi: `f"{x:.2f}"`
   * Metody napisów (`.split()`, `.strip()`, `.upper()`...) opisane są w dziale [Metody](metody.md)

```python
# znaki i formatowanie
print(ord("A"), ord("a"), chr(66), chr(ord("a") + 2))
#Output: 65 97 B c
# szyfr Cezara (przesunięcie o 3, małe litery)
tekst = "xyzabc"
szyfr = "".join(chr((ord(c) - ord("a") + 3) % 26 + ord("a")) for c in tekst)
print(szyfr)
#Output: abcdef
x = 2 / 3
print(format(x, ".3f"), f"{x:.2f}", f"{7:03d}", f"{'ab':>5}|")
#Output: 0.667 0.67 007    ab|
```

## Wejście i wyjście [⬆️](#)

   * __input(tekst)__ -> Wyświetla `tekst` i wczytuje linię z klawiatury. Zawsze zwraca __napis__, więc liczbę trzeba zamienić: `n = int(input())`
   * __print(*obiekty, sep=" ", end="\n", file=None)__ -> Wyświetla wartości oddzielone `sep` i zakończone `end`. Z argumentem `file=` zapisuje do pliku
   * __open(plik, tryb="r", encoding=None)__ -> Otwiera plik. Tryby: `"r"` - odczyt, `"w"` - zapis (nadpisuje plik), `"a"` - dopisywanie na końcu. Najlepiej używać z `with`, wtedy plik zamknie się sam

```python
# pliki
with open("wyniki.txt", "w", encoding="utf-8") as f:
    print("Zadanie 1:", 42, file=f)
    f.write("Zadanie 2: 7\n")

with open("wyniki.txt", encoding="utf-8") as f:
    for linia in f:
        print(linia.strip())
#Output: Zadanie 1: 42
#Output: Zadanie 2: 7

print(1, 2, 3, sep=";", end="!\n")
#Output: 1;2;3!

# typowe wczytywanie danych z pliku maturalnego:
# with open("liczby.txt") as f:
#     liczby = [int(linia) for linia in f]
```

## Inne [⬆️](#)

   * __type(x)__ -> Zwraca klasę (typ) obiektu, np. `type(5) == int`
   * __isinstance(x, typ)__ -> Zwraca `True`, jeżeli obiekt jest danego typu (lub jednego z typów w krotce). Uwaga: `isinstance(True, int)` też daje `True`
   * __id(x)__ -> Zwraca identyfikator obiektu - liczbę unikalną dla obiektu przez cały czas jego istnienia. Dwie zmienne wskazują na ten sam obiekt, gdy `id(a) == id(b)` (to samo sprawdza `a is b`)
   * __callable(x)__ -> Zwraca `True`, jeżeli obiekt można wywołać (np. funkcja, klasa)
   * __help(x)__ -> Wyświetla pomoc (dokumentację) dla obiektu, np. `help(str.split)`
   * __dir(x)__ -> Zwraca listę atrybutów i metod obiektu, np. `dir(str)`
   * __eval(napis)__ -> Oblicza wyrażenie Pythona zapisane w napisie i zwraca wynik. __Uwaga:__ wykonuje dowolny kod, więc nie używaj go na danych z zewnątrz; do zamiany tekstu na liczbę służą `int()` i `float()`

```python
# typy i obiekty
print(type(5), type(5.0), type("5"))
#Output: <class 'int'> <class 'float'> <class 'str'>
print(isinstance(5, int), isinstance(5, (int, float)), isinstance(True, int))
#Output: True True True
a = [1, 2]
b = a          # ta sama lista
c = a.copy()   # nowa lista
print(id(a) == id(b), a is b, a is c, a == c)
#Output: True True False True
print(callable(len), callable(5))
#Output: True False
print(eval("2 + 3 * 4"))
#Output: 14
```
