<h1 align="center"> Metody </h1>
<h3 align="center">Nie jest to wyczerpanie tematu. </h3>

### STRING [⬆️](#)
<p>Wszystkie metody na napisach zwracają wartości. Nie zmieniają oryginalnego ciągu znaków.</p>

  * __.capitalize()__ -> zmienia pierwszy znak na duży
  * __.lower()__ -> zmienia ciąg na małe litery
  * __.upper()__ -> zmienia ciąg na wielkie litery
  * __.center(length, char = " ")__ -> wyśrodkowany string
  * __.count(value, start = 0, end = -1)__ -> zwraca ilość wystąpień danego znaku
  * __.endswith(value, start = 0, end = -1)__ -> True jeżeli kończy sie podaną wartością
  * __.find(value, start = 0, end = -1)__ -> zwraca index pierwszego znaku szukanego ciągu, -1 jeżeli nie ma
  * __.index()__ -> To samo co find tylko tutaj zwraca błąd, jeżeli znaku nie ma w stringu
  * __.isalpha()__ -> True jeżeli same litery
  * __.isdecimal()__ -> True jeżeli same liczby
  * __.islower()__ -> True jeżeli same małe znaki
  * __.isnumeric()__ -> True jeżeli same liczby ascii
  * __.isspace()__ -> True jeżeli same białe znaki
  * __.istitle()__ -> True jeżeli pierwsza litera każdego słowa jest wielka
  * __.isupper()__ -> True jeżeli same duze litery
  * __.islower()__ -> True jeżeli same małe litery
  * __.title()__ -> zmienia pierwszy znak każdego słowa na wielki
  * __.swapcase()__ -> zamienia małe na wielkie, wielkie na małe litery
  * __.strip(char)__ -> usuwa białe znaki z początku i końca lub znaki podane jako argument
  * __.splitlines(keeplinebreaks = False)__ -> zwraca liste ciągu znaków odzielonych końcem lini
  * __.split(separator, maxsplit = -1)__ -> zwraca liste ciągu znaków odzielonych argumentem
  * __.replace(x, y, count)__ -> zamienia x na y
  * __".".join(iterable)__ -> łączy ciągi znaków w tym wypadku kropką

### LISTY [⬆️](#)
  * __.append()__ -> Dodaje element na koniec listy
  * __.clear()__ -> Czyści liste
  * __.copy()__ -> Zwraca płytką kopię listy
  * __.count(value)__ -> Zwraca liczbę wystąpień argumentu
  * __.extend()__ -> Rozszerza listę
  * __.index()__ -> Zwraca index pierwszego napotkanego argumentu
  * __.insert(pos, elmnt)__ -> Wstawia element na dany index
  * __.pop(pos = -1)__ -> Usuwa element na danym indexie, zwraca go również
  * __.remove()__ -> Usuwa pierwszy element o danej wartości
  * __.reverse()__ -> Odwraca listę
  * __.sort(reverse = True | False, key = myFunc)__ -> Sortuje listę w miejscu

### SŁOWNIKI [⬆️](#)
  * __.clear()__ -> Czyści słownik
  * __.copy()__ -> Plytka kopia
  * __.get(keyname, value)__ -> Zwraca wartość danego klucza
  * __.fromkeys(x, y)__ -> Zwraca słownik klucza i wartości
  * __.items()__ -> Zwraca listę krotek kluczy i wartości
  * __.keys()__ -> Zwraca listę kluczy
  * __.pop(keyname, defaultvalue)__ -> Usuwa element z danym kluczem, jeżeli nie ma zwraca wartość argumentu "defaultvalue"
  * __.popitem()__ -> Usuwa ostatni wstawiony do słownika element
  * __.update()__ -> Updates the dictionary with the specified key-value pairs
  * __.values()__ -> Zwraca listę wartości

### ZBIORY [⬆️](#)
  * __.add()__ -> Dodaje element
  * __.clear()__ -> Usuwa wszystkie elementy
  * __.copy()__ -> Zwraca kopie
  * __x.difference(y)__ -> Zwraca zbiór elementów z x których nie ma w y
  * __.discard()__ -> Usuwa dany element, nie zwraca błędu jeżeli go nie ma
  * __x.intersection(y)__ -> Zwraca zbiór z wartościami które występują w obu zbiorach
  * __x.isdisjoint(y)__ -> Zwraca prawdę, jeżeli nie ma takiego elementu który jest w obu zbiorach
  * __x.issubset(y)__ -> Zwraca prawdę, jeżeli wszystkie elementy z x są w y
  * __.pop()__ -> Usuwa randomowy element ze zbioru, również go zwraca
  * __.remove()__ -> Usuwa dany element ze zbioru
  * __x.symmetric_difference(y)__ -> Zwraca elementy które nie są częscią wspólną zbiorów
  * __.union()__ -> Zwraca zbiór wszystkich elementów bez powtórzeń

### KROTKI [⬆️](#)
  * __.count(x)__ ->	Zwraca liczbę powtórzeń wartości
  * __.index(x)__ ->	Zwraca index wartości i błąd jeżeli wartości nie ma
