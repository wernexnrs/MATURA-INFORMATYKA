<a name="main"/>

<h1 align="center"> Metody </h1>
 
### STRING [⬆️](#main)  
<p>Wszystkie metody na napisach zwracają wartości. Nie zmieniają oryginalnego ciągu znaków.</p>

  * __.capitalize()__ -> zmienia pierwszy znak na duży
  * __.lower()__ -> zmienia ciąg na małe litery
  * __.upper()__ -> zmienia ciąg na wielkie litery
  * __.center()__ -> wyśrodkowany string
  * __.count()__ -> zwraca długość ciągu znaków
  * __.endswith()__ -> True jeżeli kończy sie podanym argumentem
  * __.find()__ -> zwraca index pierwszego znaku szukanego ciągu
  * __.index()__ -> zwraca index pierwszego napotkanego znaku szukanego ciągu
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
  * __.strip()__ -> usuwa białe znaki z początku i końca lub znaki podane jako argument
  * __.splitlines()__ -> zwraca liste ciągu znaków odzielonych końcem lini
  * __.split()__ -> zwraca liste ciągu znaków odzielonych argumentem
  * __.replace()__ -> zamienia argument1 na argument2
  * __.join()__ -> łączy ciągi znaków 
 
### LISTY [⬆️](#main)
  * __.append()__ -> Dodaje element na koniec listy
  * __.clear()__ -> Czyści liste
  * __.copy()__ -> Zwraca płytką kopię listy
  * __.count()__ -> Zwraca liczbę wystąpień argumentu
  * __.extend()__ -> Rozszerza listę
  * __.index()__ -> Zwraca index pierwszego napotkanego argumentu
  * __.insert()__ -> Wstawia element na dany index
  * __.pop()__ -> Usuwa element na danym indexie
  * __.remove()__ -> Usuwa element o danej wartości
  * __.reverse()__ -> Odwraca listę
  * __.sort()__ -> Sortuje listę

### SŁOWNIKI [⬆️](#main)
  * __.clear()__ -> Czyści słownik
  * __.copy()__ -> Plytka kopia
  * __.get()__ -> Zwraca wartość danego klucza
  * __.items()__ -> Zwraca listę krotek kluczy i wartości
  * __.keys()__ -> Zwraca listę kluczy
  * __.pop()__ -> Usuwa element z danym kluczem jako argumentem
  * __.popitem()__ -> Usuwa ostatni wstawiony do słownika element
  * __.update()__ -> Updates the dictionary with the specified key-value pairs
  * __.values()__ -> Zwraca listę wartości

### ZBIORY [⬆️](#main)
  * __.add()__ -> Adds an element to the set
  * __.clear()__ -> Removes all the elements from the set
  * __.copy()__ -> Returns a copy of the set
  * __.difference()__ -> Returns a set containing the difference between two or more sets
  * __.difference_update()__ -> Removes the items in this set that are also included in another, specified set
  * __.discard()__ -> Remove the specified item
  * __.intersection()__ -> Returns a set, that is the intersection of two other sets
  * __.intersection_update()__ -> Removes the items in this set that are not present in other, specified set(s)
  * __.isdisjoint()__ -> Returns whether two sets have a intersection or not
  * __.issubset()__ -> Returns whether another set contains this set or not
  * __.issuperset()__ -> Returns whether this set contains another set or not
  * __.pop()__ -> Removes an element from the set
  * __.remove()__ -> Removes the specified element
  * __.symmetric_difference()__ -> Returns a set with the symmetric differences of two sets
  * __.symmetric_difference_update()__ -> inserts the symmetric differences from this set and another
  * __.union()__ -> Return a set containing the union of sets
  * __.update()__ -> Update the set with the union of this set and others

### KROTKI [⬆️](#main)
  * __.count()__ ->	Returns the number of times a specified value occurs in a tuple
  * __.index()__ ->	Searches the tuple for a specified value and returns the position of where it was found
