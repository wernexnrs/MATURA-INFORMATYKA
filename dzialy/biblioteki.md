## Wszystkie opisane tu zagadnienia nie są wyczerpaniem tematu. Są to jedynie rzeczy, które moga się przydać.

# Przydatne moduły
  * __collections__ - słowniki
    * [Counter()](#counter)
      * .elements()
      * .most_common()
      * .subtract()
    * [OrderedDict()](#order)
  * __math__ - matematyka
    * [funkcje](#funkcje)
  * __statistics__ - statystyka
    * [funkcje](#statfunc)
  * __re__ - RegEX
    * [funkcje](#refunc)
    * [Metacharacters](#meta)
    * [Specjalne sekwencje](#special)
    * [Zbiory](#sets)
    * [Białe znaki](#biale)
  * __fractions__ - ułamki
    * [Fraction](#ulamki)
  * __itertools__
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
  * __operator__
  * __functools__
  * __enum__

## collections
### Counter() [⬆️](#)
<a name="counter"></a>
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

### OrderedDict() [⬆️](#)
Właściwości:
<a name="order"></a>
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

## math
<a name="funkcje"></a>

### Funkcje [⬆️](#)

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


## statistics
<a name="statfunc"></a>

### Funkcje [⬆️](#)

- __mean()__ -> Średnia arytmetyczna
- __median()__ -> Mediana
- __median_high()__ -> w zbiorze parzystym zwraca większa wartość środkową
- __median_low()__ -> w zbiorze parzystym zwraca mniejsza wartość środkową
- __mode()__ -> moda/dominanta
- __pstdev()__ -> Calculates the standard deviation from an entire population
- __stdev()__ -> Calculates the standard deviation from a sample of data
- __pvariance()__ -> Calculates the variance of an entire population
- __variance()__ -> Calculates the variance from a sample of data

## re
<a name="refunc"></a>

RegEx w pythonie.

### Funkcje [⬆️](#)

- __findall()__ -> Returns a list containing all matches
- __search()__ -> Returns a Match object if there is a match anywhere in the string
- __split()__ -> Returns a list where the string has been split at each match
- __sub()__ -> Replaces one or many matches with a string

### Metacharacters [⬆️](#)
<a name="meta"></a>

| znak | opis | przykład
| :--: | :--: | :--:
| [] |	Zbiór znaków | "[a-m]"
| \ |	Sygnał specjalnej sekwencji |	"\d"
| . |	każdy znak oprócz końca linii	| "he..o"
| ^	| Zaczyna się od	| "^hello"
| $	| Kończy się na	| "world$"
| *	| Zero or more occurrences |	"aix*"
| +	| One or more occurrences	| "aix+"
| {} |	Wystąpnienia danego znaku	| "al{2}"
| "|"	| to albo to	| "falls|stays"

### Specjalne sekwencje
<a name="special"></a>

| znak |	opis | przykład
| :--: | :--: | :--:
| \A	| Zwraca dopasowanie, jeżeli ciąg jest na początku stringa	| "\AThe"
| \b	| Zwraca dopasowanie, jeżeli ciąg jest na początku lub na końcu stringa (r - raw string) | r"\bain" r"ain\b"
| \B	| Zwraca dopasowanie, jeżeli ciąg jest w stringu lecz nie na końcu ani początku. (r - raw string) |	r"\Bain" r"ain\B"
| \d	| Zwraca dopasowanie liczb w ciągu	| "\d"
| \D	| Zwraca dopasowanie, gdzie nie ma liczb |	"\D"
| \s	| Zwraca dopasowanie białych znaków | "\s"
| \S	| Zwraca dopasowanie, gdzie nie ma białych znaków	| "\S"
| \w	| Zwraca dopasowanie, gdzie ciąg znaków zawiera litery alfabetu angielskiegu, liczby i podłogę	| "\w"
| \W	| Zwraca	dopasowanie gdzie nie ma tego co up | "\W"
| \Z	| Zwraca dopasowanie, jeżeli ciąg jest na końcu stringa	| "Spain\Z"

### Zbiory
<a name="sets"></a>

| zbiór |	opis
| :--: | :--:
| [arn]	| Zwraca dopasowanie gdzie jakis z elementów znajduje się w stringu
| [a-n]	| Zwraca dopasowanie wszystkiego co ma małe litery od a do n
| [^arn]	| Wszystko bez wymienionych
| [0123]	| Zwraca dopasowanie wymienionych liczb
| [0-9]	| Zwraca dopasowanie liczb od 0 do 9
| [0-5][0-9]	| zwraca wszystko od 00 do 59
| [a-zA-Z]	| Zwraca wszsytko co w alfabecie czy duże czy małe
| [+]	| Zwraca szukane znaki tutaj +

### Białe znaki
<a name="biale"></a>
| znak |	opis
| :--: | :--:
| \'	| Pojedyńczy cytat
| \\	| Backslash
| \n	| enter
| \r	| Carriage Return
| \t	| tabulator
| \b	| Backspace
| \f	| Form Feed
| \ooo	| liczba ósemkowa
| \xhh	| liczba szesnastkowa

## fractions [⬆️](#)
<a name="ulamki"></a>

class fractions.Fraction(numerator=0, denominator=1)

```python
from fractions import Fraction
Fraction(16, -10)
#Fraction(-8, 5)
>>> Fraction(123)
#Fraction(123, 1)
>>> Fraction()
#Fraction(0, 1)
>>> Fraction('3/7')
#Fraction(3, 7)
>>> Fraction(' -3/7 ')
#Fraction(-3, 7)
```

## itertools [⬆️](#)
<a name="count"></a>

### count()
```python
data = [100,200,300,400]

data2 = list(zip(itertools.count(start = 0, step = 1), data))

#Output:  [(0, 100), (1, 200), (2, 300), (3,400)]
```

### zip_longest()
<a name="zip_longest"></a>

zip -> iteruje tyle razy ile wynosi długość krótszego obiektu

zip_longest -> iteruje tyle razy ile wynosi długość dłuższego obiektu

```python
#normal zip

data = [100,200,300,400]

data2 = list(zip(range(10), data))

#Output:  [(0, 100), (1, 200), (2, 300), (3,400)]
```

```python
#itertools zip

data = [100,200,300,400]

data2 = list(itertools.zip_longest(range(10), data))

#Output:  [(0, 100), (1, 200), (2, 300), (3, 400), (4, None), (5, None), (6, None), (7, None), (8, None), (9, None)]
```

### cycle()
<a name="cycle"></a>

```python
data = itertools.cycle([0,1])

for _ in range(6):
    print(next(data))

#Output:  0 1 0 1 0 1
```

### repeat()
<a name="repeat"></a>

```python
data = itertools.repeat(2, times=3)

for _ in range(6):
    print(next(data))

#Output:  2 2 2 StopIteration

print(list(map(pow, range(5), itertools.repeat(2)))

# Output: [0, 1, 4, 9, 16]
```

### starmap()
<a name="starmap"></a>

```python

print(list(itertools.starmap(pow, [(0,2), (1,2), (2,2)] )))

# Output: [0, 1, 4]
```

### combinations()
<a name="combinations"></a>

Wszystkie możliwe sposoby na zgrupowanie pewnej ilości znaków, gdzie kolejność nie ma znaczenia.

```python
chars = ['a', 'b', 'c', 'd']

result = itertools.combinations(chars, 2)

for i in result:
    print(i)
'''
('a', 'b') nie ma powtórzeń np ('b', 'a') bo to to samo
('a', 'c')
('a', 'd')
('b', 'c')
('b', 'd')
('c', 'd')
'''
```

### permutations()
<a name="permutations"></a>

Wszystkie możliwe sposoby na zgrupowanie pewnej ilości znaków, gdzie kolejność MA znaczenie.

```python
chars = ['a', 'b', 'c', 'd']

result = itertools.permutations(chars, 2)

for i in result:
    print(i)
'''
('a', 'b')
('a', 'c')
('a', 'd')
('b', 'a')
('b', 'c')
('b', 'd')
('c', 'a')
('c', 'b')
('c', 'd')
('d', 'a')
('d', 'b')
('d', 'c')
'''
```

### product()
<a name="product"></a>

Wszystkie możliwe sposoby na zgrupowanie pewnej ilości liczb, gdzie kolejność MA znaczenie wraz z powtórzeniami tych znaków.

```python
numbers = [0, 1, 2, 3]

result = itertools.product(numbers, repeat=2)

for i in result:
    print(i)
'''
(0, 0)
(0, 1)
(1, 0)
(1, 1)
'''
```

### chain()
<a name="chain"></a>

Iteracja po kilku obiektach na raz

```python
numbers = [0, 1, 2, 3]
chars = ['a', 'b', 'c', 'd']
es = ['first', 'second', 'third', 'fourth']

result = itertools.chain(numbers, chars, es)

for i in result:
    print(i)
'''
0
1
2
3
a
b
c
d
first
second
third
fourth
'''
```

### islice()
<a name="islice"></a>

Slice obiektu bez wykorzystywania kopii jak np podczas krojenia list.

```python
# islice(object,start,stop,step)
result = itertools.islice(range(10), 1, 5, 2)

for i in result:
    print(i)
'''
1
3
'''
```

### accumulate()
<a name="accumulate"></a>

Operacje podczas iteracji

```python
import itertools, operator

numbers = [1, 5, 4, 3]

print(list(itertools.accumulate(numbers))) # [1, 6, 10, 13], dodawanie
print( list(itertools.accumulate(numbers, operator.mul))) # [1, 5, 20, 60], mnożenie
```

### groupby()
<a name="groupby"></a>

Grupowanie obiektów.

Obiekt musi być posortowany po grupowanej wartości inaczej dane te zostaną pominiete.

```python
itertools.groupby(object,key) # moze kiedys
```
