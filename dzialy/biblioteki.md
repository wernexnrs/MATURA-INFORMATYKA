# Wszystkie opisane tu zagadnienia nie są wyczerpaniem tematu. Są to jedynie rzeczy, które moga się przydać.

# Przydatne moduły

  * __collections__
    * [Counter()](#counter)
      * .elements()
      * .most_common()
      * .subtract()
    * [OrderedDict()](#order)
  * __math__
    * [funkcje](#funkcje)
  * __statistics__
    * [funkcje](#statfunc)
  * __re__
    * [funkcje](#refunc)
    * [Metacharacters](#meta)
    * [Specjalne sekwencje](#special)
    * [Zbiory](#sets)
    * [Białe znaki](#biale)
  
<a name="counter"/>

## collections

### Counter() [⬆️](#main)
```python
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # dodawanie 
#Output: Counter({'a': 4, 'b': 3})
c - d                       # odejmowanie, zachowanie tylko dodatnich liczb
#Output:Counter({'a': 2})
c & d                       # min każdego klucza 
#Output:Counter({'a': 1, 'b': 1})
c | d                       # max każdego klucza
#Output:Counter({'a': 3, 'b': 2})
```
<h5> Metody </h5>

   * __.elements()__ -> zwraca iteracje kluczy: 'klucz'*vaule
   * __.most_common()__ -> zwraca liste krotek malejąca według wartości kluczy
   * __.subtract()__ -> zwraca counter jako wynik odejmowania z zachowaniem ujemnych wartości

<a name="order"/>

### OrderedDict() [⬆️](#main)

Właściwości:
 - Gdy porównamy 2 słowniki klasy dict, które zawierają te same elementy, niezależnie od ich kolejności dostaniemy True. Słowniki klasy OrderedDict do zwrócenia prawdy muszą mieć tą samą kolejność elementów.
 
Zwraca podsłownik, którym można zarządzać np.:
```python
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v
'''
Regular dictionary:
a A
c C
b B
e E
d D

OrderedDict:
a A
b B
c C
d D
e E
'''
```

<a name="funkcje"/>

## math

### Funkcje [⬆️](#main)

- __cos(x)__ -> Zwraca cosinus argumentu x.
- __sin(x)__ ->  Zwraca sinus argumentu x.
- __tan(x)__ -> Zwraca tangens argumentu x.
- __radians(x)__ -> Przekształca kąt x ze stopni na radiany.
- __degrees(x)__ -> Przekształca kąt x z radianów na stopnie.
- __exp(x)__ -> Zwraca wartość e**x.
- __fabs(x)__ -> Zwraca moduł (wartość bezwzględną) argumentu x.
- __floor(x)__ -> Zwraca quotpodłogę (największą liczbę całkowitą nie większą od) argumentu x w postaci liczby zmiennoprzecinkowej.
- __ceil(x)__ -> Zwraca najmniejszą liczbę całkowitą nie mniejszą od argumentu x w postaci liczby zmiennoprzecinkowej.
- __hypot(x, y)__ -> Zwraca wartość sqrt(x*x + y*y). Jest to długość przeciwprostokątnej w trójkącie prostokątnym o przyprostokątnych, których długości są równe x oraz y, lub odległość punktu (x, y) od środka układu współrzędnych.
- __log(x,y)__ -> Zwraca logarytm o podstawie y argumentu x.
- __log10(x)__ -> Zwraca logarytm o podstawie 10 argumentu x.
- __log2(x)__ -> Zwraca logarytm o podstawie 2 argumentu x.
- __pow(x, y)__ -> Zwraca wartość x**y.
- __sqrt(x)__ -> Zwraca pierwiastek kwadratowy argumentu x.
- __dist()__ -> Zwraca dystans między dwoma punktami
- __factorial()__  -> zwraca silnie
- __fsum()__ -> zwraca sume elementów obiektu
- __prod()__ -> zwraca iloczyn elementów obiektu
- __gcd()__ -> zwraca największy wspólny dzielnik
- __e__ -> zwraca wartość liczby Eulera (2.7182...)
- __pi__ -> zwraca wartość PI (3.1415...)


<a name="statfunc"/>

## statistics

### Funkcje [⬆️](#main)

- __mean()__ -> Średnia arytmetyczna
- __median()__ -> Mediana
- __median_high()__ -> w zbiorze parzystym zwraca większa wartość środkową
- __median_low()__ -> w zbiorze parzystym zwraca mniejsza wartość środkową
- __mode()__ -> moda/dominanta
- __pstdev()__ -> Calculates the standard deviation from an entire population
- __stdev()__ -> Calculates the standard deviation from a sample of data
- __pvariance()__ -> Calculates the variance of an entire population
- __variance()__ -> Calculates the variance from a sample of data

<a name="refunc"/>

## re

RegEx w pythonie.

### Funkcje [⬆️](#main)

- __findall() -> Returns a list containing all matches
- __search() -> Returns a Match object if there is a match anywhere in the string
- __split() -> Returns a list where the string has been split at each match
- __sub() -> Replaces one or many matches with a string

<a name="meta"/>

### Metacharacters [⬆️](#main)

| znak | opis | przykład |
| :--: | :--: | :--: |
| [] |	Zbiór znaków | "[a-m]"	|
| \ |	Sygnał specjalnej sekwencji |	"\d"	 |
| . |	każdy znak oprócz końca linii	| "he..o"	|
| ^	| Zaczyna się od	| "^hello"	|
| $	| Kończy się na	| "world$"	|
| *	| Zero or more occurrences |	"aix*"|	
| +	| One or more occurrences	| "aix+"	|
| {} |	Wystąpnienia danego znaku	| "al{2}"	|
| "|"	| to albo to	| "falls|stays"|

<a name="special"/>

### Specjalne sekwencje

| znak |	opis | przykład |
| :--: | :--: | :--: |
| \A	| Zwraca dopasowanie, jeżeli ciąg jest na początku stringa	| "\AThe"	|
| \b	| Zwraca dopasowanie, jeżeli ciąg jest na początku lub na końcu stringa (r - raw string) | r"\bain" r"ain\b"	|
| \B	| Zwraca dopasowanie, jeżeli ciąg jest w stringu lecz nie na końcu ani początku. (r - raw string) |	r"\Bain" r"ain\B"	|
| \d	| Zwraca dopasowanie liczb w ciągu	| "\d"	|
| \D	| Zwraca dopasowanie, gdzie nie ma liczb |	"\D"	|
| \s	| Zwraca dopasowanie białych znaków | "\s"	|
| \S	| Zwraca dopasowanie, gdzie nie ma białych znaków	| "\S"	|
| \w	| Zwraca dopasowanie, gdzie ciąg znaków zawiera litery alfabetu angielskiegu, liczby i podłogę	| "\w"	|
| \W	| Zwraca	dopasowanie gdzie nie ma tego co up | "\W"	|
| \Z	| Zwraca dopasowanie, jeżeli ciąg jest na końcu stringa	| "Spain\Z" |

<a name="sets"/>

### Zbiory

| zbiór |	opis | 
| :--: | :--: |
| [arn]	| Zwraca dopasowanie gdzie jakis z elementów znajduje się w stringu	|
| [a-n]	| Zwraca dopasowanie wszystkiego co ma małe litery od a do n	|
| [^arn]	| Wszystko bez wymienionych |
| [0123]	| Zwraca dopasowanie wymienionych liczb	|
| [0-9]	| Zwraca dopasowanie liczb od 0 do 9	|
| [0-5][0-9]	| zwraca wszystko od 00 do 59	|
| [a-zA-Z]	| Zwraca wszsytko co w alfabecie czy duże czy małe	|
| [+]	| Zwraca szukane znaki tutaj + |

<a name="biale"/>

### Białe znaki
| znak |	opis | 
| :--: | :--: |
| \'	| Pojedyńczy cytat	|
| \\	| Backslash	|
| \n	| enter	|
| \r	| Carriage Return	|
| \t	| tabulator	|
| \b	| Backspace	|
| \f	| Form Feed	|
| \ooo	| liczba ósemkowa	|
| \xhh	| liczba szesnastkowa |
