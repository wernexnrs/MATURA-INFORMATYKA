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

```python
# zip, enumerate, any i all w praktyce
a = [1, 4, 9, 16, 25]
print([y - x for x, y in zip(a, a[1:])])  # różnice sąsiednich elementów
#Output: [3, 5, 7, 9]
imiona = ["Ola", "Jan", "Ewa"]
punkty = [17, 25, 21]
for imie, pkt in zip(imiona, punkty):     # dwie listy równolegle
    print(imie, pkt, end="; ")
print()
#Output: Ola 17; Jan 25; Ewa 21;
nr, wartosc = max(enumerate(punkty, start=1), key=lambda p: p[1])
print(nr, wartosc)                        # numer (od 1) i wartość największego elementu
#Output: 2 25
print(all(x < y for x, y in zip(a, a[1:])), any(x % 5 == 0 for x in a))
#Output: True True
n = 91
print(any(n % d == 0 for d in range(2, n)))  # czy n ma dzielnik (czyli nie jest pierwsza)
#Output: True
```

## Wycinki (slicing) i odwracanie [⬆️](#)

   * __x[i]__ -> Element o indeksie `i` (liczonym od 0). Ujemne indeksy liczą od końca: `x[-1]` to ostatni element, `x[-2]` przedostatni
   * __x[start:stop]__ -> Wycinek od `start` do `stop` __bez__ `stop`. Pominięty `start` oznacza początek, pominięty `stop` - koniec. Wycinek poza zakresem nie zgłasza błędu (daje krótszy lub pusty wynik)
   * __x[start:stop:krok]__ -> Co `krok`-ty element; przy ujemnym kroku idziemy od końca
   * __x[::-1]__ -> Odwrócony napis, lista lub krotka (nowy obiekt, oryginał bez zmian)
   * __x[:]__ -> Płytka kopia listy
   * Wycinki działają dla napisów, list, krotek i `range`. Do wycinka listy można przypisać: `lista[1:3] = [0]`

```python
# wycinki
s = "informatyka"
print(s[0], s[-1], s[2:6], s[:4], s[-4:])
#Output: i a form info tyka
print(s[::2], s[1::2], s[::-1])
#Output: ifraya nomtk akytamrofni
liczby = [10, 20, 30, 40, 50]
print(liczby[1:3], liczby[::-1], liczby[-2:], liczby[10:])
#Output: [20, 30] [50, 40, 30, 20, 10] [40, 50] []
slowo = "kajak"
print(slowo == slowo[::-1])               # palindrom
#Output: True
print(int(str(1230)[::-1]), bin(6)[2:][::-1])  # odwrócona liczba, bity od najmłodszego
#Output: 321 011
s = "abcdef"
polowa = len(s) // 2
print(s[:polowa], s[polowa:])             # połowy napisu
#Output: abc def
liczby[1:3] = [0]
print(liczby)
#Output: [10, 0, 40, 50]
```

## Wyrażenia listowe (comprehension) [⬆️](#)

   * __[wyrażenie for x in iterable]__ -> Lista wyników wyrażenia dla każdego elementu
   * __[wyrażenie for x in iterable if warunek]__ -> Tylko elementy spełniające warunek (filtr)
   * __[a if warunek else b for x in iterable]__ -> Wybór wartości dla każdego elementu (tu `if ... else` stoi __przed__ `for`)
   * __{klucz: wartość for x in iterable}__ -> Słownik (dict comprehension)
   * __{wyrażenie for x in iterable}__ -> Zbiór (set comprehension), bez powtórzeń
   * __(wyrażenie for x in iterable)__ -> Wyrażenie generatorowe: nie tworzy listy w pamięci. W wywołaniu funkcji nawias można pominąć: `sum(x * x for x in liczby)`
   * Kilka `for` po kolei działa jak pętle zagnieżdżone (pierwszy `for` jest zewnętrzny)

```python
# wyrażenia listowe
liczby = [3, 8, 5, 12, 7, 10]
print([x * x for x in liczby])
#Output: [9, 64, 25, 144, 49, 100]
print([x for x in liczby if x % 2 == 0])
#Output: [8, 12, 10]
print(["P" if x % 2 == 0 else "N" for x in liczby])
#Output: ['N', 'P', 'N', 'P', 'N', 'P']
print([int(c) for c in "2024"], sum(int(c) for c in "2024"))  # cyfry i suma cyfr
#Output: [2, 0, 2, 4] 8
print(sum(1 for x in liczby if x > 6))    # ile liczb spełnia warunek
#Output: 4
slowa = ["kot", "pies", "kot", "mysz"]
print({s: len(s) for s in slowa})
#Output: {'kot': 3, 'pies': 4, 'mysz': 4}
print(sorted({s[0] for s in slowa}))
#Output: ['k', 'm', 'p']
print({v: k for k, v in {"a": 1, "b": 2}.items()})  # odwrócenie słownika
#Output: {1: 'a', 2: 'b'}
tab = [[0] * 4 for _ in range(3)]         # tablica 3 x 4 - każdy wiersz to osobna lista
print(tab)
#Output: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
macierz = [[1, 2, 3], [4, 5, 6]]
print([x for wiersz in macierz for x in wiersz])  # spłaszczenie listy list
#Output: [1, 2, 3, 4, 5, 6]
print([(i, j) for i in range(2) for j in range(3) if i != j])
#Output: [(0, 1), (0, 2), (1, 0), (1, 2)]
```

## Sortowanie [⬆️](#)

   * __sorted(x, key=funkcja)__ -> Sortuje według wyniku funkcji `key` wywołanej dla każdego elementu (same elementy się nie zmieniają). Najczęściej `key=lambda e: ...`. Lista ma też metodę `.sort(key=..., reverse=...)`, która sortuje w miejscu
   * __reverse=True__ -> Kolejność malejąca (dotyczy całego klucza)
   * __Kilka kryteriów__ -> Klucz zwraca krotkę, a krotki porównywane są element po elemencie: `key=lambda e: (kryterium1, kryterium2)`
   * __Różne kierunki__ -> Dla liczb wystarczy minus: `key=lambda e: (-e[1], e[0])` (malejąco po liczbie, przy remisie rosnąco po nazwie). Gdy kryterium nie da się zanegować (napis), można sortować dwa razy: sortowanie jest __stabilne__, więc najpierw sortujemy po kryterium drugorzędnym, a potem po głównym
   * Napisy porównywane są znak po znaku według kodów: wielkie litery są przed małymi, a `"10" < "9"`. Liczby wczytane z pliku zamień na `int` przed sortowaniem
   * __min() / max()__ też przyjmują `key=`, np. najdłuższe słowo: `max(slowa, key=len)`

```python
# sortowanie z kluczem: (imię, ocena, wiek)
uczniowie = [("Ola", 5, 17), ("Jan", 3, 18), ("Ewa", 5, 16), ("Adam", 4, 18)]
print(sorted(uczniowie, key=lambda u: u[1]))
#Output: [('Jan', 3, 18), ('Adam', 4, 18), ('Ola', 5, 17), ('Ewa', 5, 16)]
# malejąco po ocenie, przy remisie alfabetycznie po imieniu
print(sorted(uczniowie, key=lambda u: (-u[1], u[0])))
#Output: [('Ewa', 5, 16), ('Ola', 5, 17), ('Adam', 4, 18), ('Jan', 3, 18)]
# malejąco po wieku, przy remisie malejąco po imieniu
print(sorted(uczniowie, key=lambda u: (u[2], u[0]), reverse=True))
#Output: [('Jan', 3, 18), ('Adam', 4, 18), ('Ola', 5, 17), ('Ewa', 5, 16)]
# rosnąco po ocenie, przy remisie malejąco po imieniu - dwa sortowania
wynik = sorted(uczniowie, key=lambda u: u[0], reverse=True)
wynik.sort(key=lambda u: u[1])
print([u[0] for u in wynik])
#Output: ['Jan', 'Adam', 'Ola', 'Ewa']
```

```python
# sortowanie napisów i słowników
slowa = ["Kot", "ala", "pies", "Be", "zebra"]
print(sorted(slowa))                      # wielkie litery przed małymi
#Output: ['Be', 'Kot', 'ala', 'pies', 'zebra']
print(sorted(slowa, key=str.lower))
#Output: ['ala', 'Be', 'Kot', 'pies', 'zebra']
print(sorted(slowa, key=lambda s: (len(s), s.lower())))
#Output: ['Be', 'ala', 'Kot', 'pies', 'zebra']
print(sorted(["10", "9", "100"]), sorted(["10", "9", "100"], key=int))
#Output: ['10', '100', '9'] ['9', '10', '100']
punkty = {"B": 7, "A": 7, "C": 9}
print(sorted(punkty.items(), key=lambda p: (-p[1], p[0])))
#Output: [('C', 9), ('A', 7), ('B', 7)]
print(sorted(punkty, key=punkty.get, reverse=True)[0])  # klucz z największą wartością
#Output: C
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

## Formatowanie tekstu (f-stringi) [⬆️](#)

   * __f"{wyrażenie}"__ -> Wstawia wartość wyrażenia do napisu. Po dwukropku można podać specyfikację formatu: `f"{x:specyfikacja}"` (to samo robi `format(x, "specyfikacja")`)
   * __:.2f__ -> Liczba z dokładnie 2 miejscami po przecinku (zaokrąglona), np. `f"{3.14159:.2f}" == "3.14"`. Separatorem dziesiętnym jest kropka; gdy potrzebny jest przecinek: `.replace(".", ",")`
   * __:5__, __:>5__, __:<5__, __:^5__ -> Pole o szerokości 5 znaków: wyrównanie domyślne (liczby do prawej, napisy do lewej), do prawej, do lewej, do środka. Przed znakiem wyrównania można podać znak wypełnienia, np. `:*^9`
   * __:05d__ -> Liczba całkowita dopełniona zerami z lewej do 5 znaków
   * __:b__, __:o__, __:x__, __:X__ -> Zapis dwójkowy, ósemkowy, szesnastkowy (małe / wielkie litery), bez przedrostka. Z `#` przedrostek jest dodawany: `f"{255:#x}" == "0xff"`
   * __:08b__ -> Zapis dwójkowy dopełniony zerami do 8 cyfr (np. pełny bajt)
   * __:,__ -> Separator tysięcy, __:.1%__ -> procent (mnoży przez 100 i dodaje `%`), __:+d__ -> liczba zawsze ze znakiem
   * __{x=}__ -> Wypisuje nazwę i wartość, np. `f"{x=}"` daje `x=5` - wygodne przy szukaniu błędów
   * Szerokość i dokładność mogą pochodzić ze zmiennej: `f"{x:>{n}}"`, `f"{x:0{n}b}"`, `f"{x:.{k}f}"`

```python
# f-stringi
x = 2 / 3
print(f"{x}|{x:.2f}|{x:.4f}|{10:.2f}")
#Output: 0.6666666666666666|0.67|0.6667|10.00
print(f"{3.5:.2f}".replace(".", ","))
#Output: 3,50
n = 42
print(f"[{n:5}] [{n:>5}] [{n:<5}] [{n:^5}] [{n:*^9}] [{n:05d}]")
#Output: [   42] [   42] [42   ] [ 42  ] [***42****] [00042]
print(f"[{'ab':5}] [{'ab':>5}]")
#Output: [ab   ] [   ab]
print(f"{10:b} {10:08b} {255:x} {255:X} {255:#x} {8:o}")
#Output: 1010 00001010 ff FF 0xff 10
dl = 6
print(f"{5:0{dl}b}", f"{'a':>{dl}}|", f"{x:.{dl}f}")
#Output: 000101      a| 0.666667
print(f"{1234567:,} {0.256:.1%} {7:+d} {-7:+d}")
#Output: 1,234,567 25.6% +7 -7
print(f"{n=}, {n * 2 = }")
#Output: n=42, n * 2 = 84
# tabelka wyników wyrównana w kolumnach
for imie, pkt in [("Ola", 17.5), ("Jan", 9.25)]:
    print(f"{imie:<6}{pkt:>8.2f}")
#Output: Ola      17.50
#Output: Jan       9.25
```

## Wejście i wyjście, pliki [⬆️](#)

   * __input(tekst)__ -> Wyświetla `tekst` i wczytuje linię z klawiatury. Zawsze zwraca __napis__, więc liczbę trzeba zamienić: `n = int(input())`
   * __print(*obiekty, sep=" ", end="\n", file=None)__ -> Wyświetla wartości oddzielone `sep` i zakończone `end`. Z argumentem `file=` zapisuje do pliku
   * __open(plik, tryb="r", encoding=None)__ -> Otwiera plik. Tryby: `"r"` - odczyt, `"w"` - zapis (nadpisuje plik), `"a"` - dopisywanie na końcu. Najlepiej używać z `with`, wtedy plik zamknie się sam
   * __with open(...) as f:__ -> Po wyjściu z bloku `with` plik jest zamykany automatycznie (także przy błędzie). Plik z danymi musi leżeć w tym samym folderze, z którego uruchamiasz program, albo trzeba podać pełną ścieżkę
   * __for linia in f:__ -> Czyta plik linia po linii. Każda linia (oprócz może ostatniej) kończy się znakiem `"\n"` - usuwa go `.strip()`, a `.split()` od razu dzieli linię na słowa bez białych znaków
   * Metody obiektu pliku (`.read()`, `.readline()`, `.readlines()`, `.write()`) są opisane w dziale [Metody](metody.md)
   * __Odpowiedzi do CKE__ -> Wyniki zapisuje się w pliku tekstowym o nazwie podanej w treści (np. `wyniki.txt`, `wyniki4.txt`), a każdą odpowiedź poprzedza się numerem zadania. Najprościej `print("4.1.", wynik, file=f)`; `f.write()` przyjmuje tylko napis i sam nie dodaje `"\n"`
   * Tryb `"w"` czyści plik przy otwarciu - jeśli kilka zadań zapisuje do jednego pliku, otwórz go raz albo dopisuj w trybie `"a"`
   * Polskie znaki: przy zapisie i odczycie podawaj `encoding="utf-8"`. Pliki CKE zwykle zawierają tylko znaki ASCII, ale starsze bywają w kodowaniu `cp1250`

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
```

```python
# typowe wczytywanie danych z pliku maturalnego
# (najpierw tworzymy przykładowy plik dane.txt - na maturze dostajesz go od CKE)
with open("dane.txt", "w") as f:
    f.write("12 7\n3 15\n8 8\n")

pary = []
with open("dane.txt") as f:
    for linia in f:
        a, b = map(int, linia.split())
        pary.append((a, b))
print(pary)
#Output: [(12, 7), (3, 15), (8, 8)]

with open("dane.txt") as f:
    linie = [linia.strip() for linia in f]    # lista napisów bez "\n"
print(linie)
#Output: ['12 7', '3 15', '8 8']

with open("dane.txt") as f:
    wiersze = f.readlines()                   # lista linii razem z "\n"
print(wiersze)
#Output: ['12 7\n', '3 15\n', '8 8\n']

with open("dane.txt") as f:
    liczby = list(map(int, f.read().split()))  # wszystkie liczby z pliku naraz
print(liczby, sum(liczby))
#Output: [12, 7, 3, 15, 8, 8] 53

with open("dane.txt") as f:
    for nr, linia in enumerate(f, start=1):   # numer wiersza liczony od 1
        a, b = map(int, linia.split())
        if a == b:
            print("równe liczby w wierszu", nr)
#Output: równe liczby w wierszu 3
```

```python
# plik z separatorem (średnik) i wierszem nagłówkowym
with open("uczniowie.txt", "w", encoding="utf-8") as f:
    f.write("imie;klasa;punkty\nOla;3a;87\nJan;3b;64\n")

with open("uczniowie.txt", encoding="utf-8") as f:
    naglowek = f.readline()                   # pomijamy pierwszy wiersz
    for linia in f:
        imie, klasa, punkty = linia.strip().split(";")
        print(imie, klasa, int(punkty) + 10)
#Output: Ola 3a 97
#Output: Jan 3b 74
```

```python
# zapis odpowiedzi do pliku wyników, każda poprzedzona numerem zadania
odp_1 = 53
odp_2 = [12, 15]
with open("wyniki4.txt", "w") as f:
    print("4.1.", odp_1, file=f)
    print("4.2.", *odp_2, file=f)
    f.write(f"4.3. {2 / 3:.2f}\n")

with open("wyniki4.txt") as f:
    print(f.read(), end="")
#Output: 4.1. 53
#Output: 4.2. 12 15
#Output: 4.3. 0.67
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

## Typowe pułapki [⬆️](#)

   * __`/` a `//`__ -> `/` zawsze daje `float` (`6 / 2 == 3.0`), a `//` to dzielenie całkowite zaokrąglone __w dół__, także dla liczb ujemnych (`-7 // 2 == -4`). Indeksy i liczby całkowite licz przez `//`
   * __`%` dla liczb ujemnych__ -> Wynik ma znak dzielnika: `-7 % 3 == 2` (inaczej niż w C++). `int(x / y)` obcina w stronę zera, więc dla ujemnych różni się od `x // y`
   * __float__ -> Liczby zmiennoprzecinkowe są przybliżone: `0.1 + 0.2 != 0.3`. Nie porównuj ich przez `==` - użyj `math.isclose(a, b)` albo `abs(a - b) < 1e-9`. Jeszcze lepiej licz na liczbach całkowitych (kwoty w groszach, kwadraty odległości zamiast pierwiastków, `math.isqrt()` zamiast `math.sqrt()`)
   * __Zaokrąglanie__ -> `round()` zaokrągla połówki do liczby parzystej (`round(0.5) == 0`, `round(2.5) == 2`), a `int()` obcina część ułamkową. Wynik z dokładnością do 2 miejsc najlepiej wypisać przez `f"{x:.2f}"`
   * __Mutowalny argument domyślny__ -> `def f(x, lista=[])` - ta sama lista jest używana przy każdym wywołaniu i „pamięta” poprzednie wywołania. Zamiast tego `lista=None`, a w funkcji `if lista is None: lista = []`
   * __Lista dwuwymiarowa__ -> `[[0] * m] * n` tworzy n odwołań do __tej samej__ listy. Twórz ją przez `[[0] * m for _ in range(n)]`. `tab.copy()` i `tab[:]` kopiują tylko zewnętrzną listę - kopia 2D to `[w[:] for w in tab]` albo `copy.deepcopy(tab)`
   * __Rekurencja__ -> Domyślny limit głębokości to ok. 1000 wywołań, potem `RecursionError`. Limit podnosi `sys.setrecursionlimit(10000)`; przy bardzo głębokiej rekurencji bezpieczniej przepisać algorytm na pętlę
   * __Zmiana listy w trakcie iteracji__ -> Usuwanie elementów w pętli `for x in lista` pomija elementy. Utwórz nową listę: `[x for x in lista if warunek]`
   * __Dane z pliku to napisy__ -> `"12" + "3" == "123"` i `"9" > "10"`. Zamień je na liczby (`int()`, `map(int, ...)`) przed liczeniem i porównywaniem

```python
# dzielenie
print(7 / 2, 6 / 2, 7 // 2, -7 // 2, 7 % 3, -7 % 3)
#Output: 3.5 3.0 3 -4 1 2
print(int(-7 / 2), -7 // 2)               # int() obcina w stronę zera, // zaokrągla w dół
#Output: -3 -4
```

```python
# liczby zmiennoprzecinkowe i zaokrąglanie
import math

print(0.1 + 0.2, 0.1 + 0.2 == 0.3)
#Output: 0.30000000000000004 False
print(math.isclose(0.1 + 0.2, 0.3), abs((0.1 + 0.2) - 0.3) < 1e-9)
#Output: True True
print(round(0.5), round(1.5), round(2.5), int(2.99))
#Output: 0 2 2 2
print(f"{2.675:.2f}", f"{1 / 3:.3f}")     # 2.675 jest zapisane jako 2.67499999...
#Output: 2.67 0.333
print(math.floor(2.5 + 0.5), math.floor(3.5 + 0.5))  # "szkolne" zaokrąglanie liczb dodatnich
#Output: 3 4
```

```python
# mutowalny argument domyślny
def dodaj_zle(x, lista=[]):
    lista.append(x)
    return lista

def dodaj_dobrze(x, lista=None):
    if lista is None:
        lista = []
    lista.append(x)
    return lista

print(dodaj_zle(1), dodaj_zle(2))
#Output: [1, 2] [1, 2]
print(dodaj_dobrze(1), dodaj_dobrze(2))
#Output: [1] [2]
```

```python
# lista dwuwymiarowa i kopiowanie
import copy

zla = [[0] * 3] * 2
zla[0][0] = 1
print(zla)
#Output: [[1, 0, 0], [1, 0, 0]]
dobra = [[0] * 3 for _ in range(2)]
dobra[0][0] = 1
print(dobra)
#Output: [[1, 0, 0], [0, 0, 0]]
kopia_plytka = dobra.copy()
kopia_wierszy = [w[:] for w in dobra]
kopia_gleboka = copy.deepcopy(dobra)
dobra[1][1] = 5
print(kopia_plytka[1][1], kopia_wierszy[1][1], kopia_gleboka[1][1])
#Output: 5 0 0
```

```python
# rekurencja i limit głębokości
import sys

def suma(n):
    if n == 0:
        return 0
    return n + suma(n - 1)

print(sys.getrecursionlimit())
#Output: 1000
try:
    suma(5000)
except RecursionError:
    print("RecursionError")
#Output: RecursionError
sys.setrecursionlimit(10000)
print(suma(5000))
#Output: 12502500
```

```python
# usuwanie elementów w trakcie iteracji i napisy zamiast liczb
liczby = [2, 4, 5, 6, 8]
for x in liczby:
    if x % 2 == 0:
        liczby.remove(x)
print(liczby)                             # źle - część parzystych została
#Output: [4, 5, 8]
liczby = [2, 4, 5, 6, 8]
liczby = [x for x in liczby if x % 2 != 0]
print(liczby)
#Output: [5]
print("12" + "3", "9" > "10", int("9") > int("10"))
#Output: 123 True False
```
