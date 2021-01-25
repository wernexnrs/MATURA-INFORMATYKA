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
  * __random__
  * __statistics__
  * __re__
  

## collections

<a name="counter"/>

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

## math

<a name="funkcje"/>

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
- __log2(x)__  -> Zwraca logarytm o podstawie 2 argumentu x.
- __pow(x, y)__ -> Zwraca wartość x**y.
- __sqrt(x)__ -> Zwraca pierwiastek kwadratowy argumentu x.
- __dist()__ -> Zwraca dystans między dwoma punktami
- __factorial()__  -> zwraca silnie
- __fsum()__  -> zwraca sume elementów obiektu
- __gcd()__  -> zwraca największy wspólny dzielnik
- __e__  -> zwraca wartość liczby Eulera (2.7182...)
- __pi__  -> zwraca wartość PI (3.1415...)



