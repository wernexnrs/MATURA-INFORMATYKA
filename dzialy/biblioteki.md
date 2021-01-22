# Przydatne biblioteki

  * __Collections__
    * [Counter()](counter)
      * .elements()
      * .most_common()
      * .subtract()
    * [OrderedDict()](order)
  * __Math__
  

## Collections

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

   * __.elements()__ -> Zwracan iteracje kluczy: 'klucz'*vaule
   * __.most_common()__ -> zwraca liste krotek malejąca według wartości kluczy
   * __.subtract()__ -> zwraca counter jako wynik odejmowania z zachowaniem ujemnych wartości

<a name="order"/>

### OrderedDict()
Zwraca podsłownik, którym można zarządzać
