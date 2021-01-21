<h1 align="center"> 🔥 <a href="https://discord.com/users/596478466849767475/">Wernex#9840</a> 🔥 </h1>

## MATURA 2021
<p><b>Projekt powstał w celu zgromadzenia pomocnych zagadnień na mature rozszerzoną z informatyki. </b></p>
<p><b>Bardzo proszę o nadsyłanie szybszych, łatwiejszych, innych rozwiązań, znalezionych błedów czy sugestii na discordzie lub w dziale <i>issues<i></b></p>

## Przydatne linki
   - <a href="https://pl.spoj.com/">POLSKI SPOJ</a> - pełno problemów algorytmicznych do rozwiązania
   - <a href="https://discord.gg/3hyj3kXQkt">DISCORD MATURALNY</a>
   - <a href="http://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Informatory/2015/aneks/Aneks_2021_informatyka_EM_niewidomi.pdf">Wymagania maturalne</a>
   - <a href="https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Materialy/Zbiory_zadan/Matura_Zbi%C3%B3r_zada%C5%84_Informatyka.pdf">Arkusz</a> -- <a href="https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Materialy/Zbiory_zadan/inf-pr-dane.zip">dane</a> -- <a href="https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Materialy/Zbiory_zadan/inf-pr-rozwiazania.zip">rozwiązania</a> - Zadania do ćwiczeń od CKE
   - <a href="https://cke.gov.pl/egzamin-maturalny/egzamin-w-nowej-formule/materialy-dodatkowe/probny-egzamin/informatyka-poziom-rozszerzony/">Próbne egzaminy</a>
   - <a href="https://arkusze.pl/informatyka-matura-poziom-rozszerzony/">Wszystkie arkusze</a>
   - <a href="https://docs.python.org/3/">Dokumentacja pythona</a>
   - <a href="https://www.w3schools.com/python/default.asp">Zagadnienia z pythona w przystępnej formie</a>
   - <a href="https://www.korepetycjezinformatyki.pl/arkusz-kalkulacyjny/">EXCEL</a> - wprowadzenie i troszke teorii
   - <a href="https://www.korepetycjezinformatyki.pl/arkusz-kalkulacyjny/">Python</a> - wprowadzenie i troszke teorii
   - <a href="https://calculatic.pl/poradnik/podstawowe-funkcje-excela/">EXCEL</a> - podstawowe funkcje
   
<a name="main"/>

# TOC
1. [Algorytmy wymienione w wymaganiach](https://github.com/wernexnrs123/MATURA-INFORMATYKA/blob/master/dzialy/algorytmy_wymagania.md)
2. [Zadania z arkuszy](#a2)
3. [Dodatkowe algorytmy](#a3)
4. [Funkcje wbudowane](#a4)
5. [Metody](#a5)

<a name="a2"/>

# Zadania z arkuszy

1. 2015 maj
   - [x] [4.1](#bin1)
   - [x] [4.2](#bin2)
   - [x] [4.3](#bin3)
2. 2018 czerwiec
   - [x] [4.1](#e1)
   - [x] [4.2](#e2)
   - [x] [4.3](#e3)
 
 # 2015 maj
 
<a name="bin1"/>
W pliku liczby.txt znajduje się 1000 liczb naturalnych zapisanych binarnie. Każda liczba zapisana jest w osobnym wierszu.


 ## Podaj, ile liczb z pliku liczby.txt ma w swoim zapisie binarnym więcej zer niż jedynek.
 ```python
zera = jedynki = wynik = 0

with open("Dane_PR/liczby.txt") as file:
    for line in file:
        for char in line:
            if char == "0": zera+=1
            elif char == "1": jedynki+=1
        if zera>jedynki:
            wynik+=1
        zera = 0
        jedynki = 0
        
print(wynik)
 ```
 
 <a name="bin2"/>
 
 ## Podaj, ile liczb w pliku liczby.txt jest podzielnych przez 2 oraz ile liczb jest podzielnych przez 8. 
 ```python
przezdwa = przezosiem = 0

with open("Dane_PR/liczby.txt") as file:
    for line in file:
        line = int(line,2)

        if line%2 == 0:
            przezdwa += 1
        if line%8 == 0:
            przezosiem += 1
            
print(przezdwa,"|",przezosiem)
 ```

 <a name="bin3"/>
 
 ## Znajdź najmniejszą i największą liczbę w pliku liczby.txt. Jako odpowiedź podaj numery wierszy, w których się one znajdują. 
 ```python
lista = []

with open("Dane_PR/liczby.txt") as file:
    for line in file:
        lista.append(int(line,2))
        
print(lista.index(max(lista))+1,"|",lista.index(min(lista))+1)
 ```

 # 2018 czerwiec
Pliki dane1.txt i dane2.txt zawierają po 1000 wierszy. W każdym wierszu tych plików zapisany jest uporządkowany niemalejąco ciąg dziesięciu liczb całkowitych o wartościach z przedziału 〈0,100〉 , oddzielonych spacjami. 

<a name="e1"/>

 ## Porównaj ciągi zapisane w odpowiadających sobie wierszach w plikach dane1.txt i dane2.txt. Podaj, w ilu wierszach zapisane są ciągi, których ostania liczba jest taka sama. 
 ```python
count = 0
with open("NM_DANE_PR/dane1.txt") as dane1,open("NM_DANE_PR/dane2.txt") as dane2:
    for (a,b) in zip(dane1,dane2):
        a,b = a.strip(),b.strip()
        if a[-3:] == b[-3:]:
            count +=1
print(count)
 ```
 
 <a name="e2"/>

 ## Podaj, ile jest par ciągów (w odpowiadających sobie wierszach plików dane1.txt i dane2.txt) takich, że w jednym i drugim ciągu jest 5 liczb parzystych i 5 liczb nieparzystych. 
 ```python
count = parzyste = parzyste2 =0

with open("NM_DANE_PR/dane1.txt") as dane1,open("NM_DANE_PR/dane2.txt") as dane2:
    for (a,b) in zip(dane1,dane2):
        a,b = a.strip().split(),b.strip().split()
        for i,j in zip(a,b):
            i,j = int(i),int(j)
            if i % 2 == 0:
                parzyste+=1
            if j % 2 == 0:
                parzyste2+=1
        if parzyste == 5 and parzyste2 == 5:
            count+=1
        parzyste = parzyste2 = 0
print(count)

 ```
 
 <a name="e3"/>

 ## Policz, ile jest par ciągów (w odpowiadających sobie wierszach plików dane1.txt i dane2.txt), które utworzone są z takich samych liczb. Liczba powtórzeń takich samych liczb w ciągach może być różna. Wypisz numery wierszy, w których takie pary ciągów się znajdują. 
 ```python
index = 1
with open("NM_DANE_PR/dane1.txt") as dane1,open("NM_DANE_PR/dane2.txt") as dane2:
    for (a,b) in zip(dane1,dane2):
        a = list(set(a.strip().split()))
        b = list(set(b.strip().split()))

        if a == b:
            print(index)
        index += 1
 ```
 
# Dodatkowe algorytmy
  - [x] [Czy liczba jest parzysta](#even)
  - [x] [Czy liczba jest podzielna przez n bez reszty](#n)
  - [x] [Czy liczba jest wielokrotnością n](#multiple)
  - [x] [Silnia (n)](#factorial)
  - [x] [Pierwiastek kwadratowy](#sqrt)
  - [x] [Pierwiastek n-tego stopnia](#sqrt2)  
  - [x] [Suma liczb od a do b](#suma)
  - [x] [Iloczyn liczb od a do b](#iloczyn)  
  - [x] [Krotność](#kro)  
  - [x] [Moda](#moda)  
  - [x] [Mediana](#med) 
  - [x] [Średnia arytmetyczna](#ary) 
  - [x] [Średnia ważona](#waz) 
  - [x] [Średnia geometryczna](#geo)
  - [x] [Wariancja i odchylenie standardowe](#odchylenie) 
<a name="even"/>

## Czy liczba jest parzysta [⬆️](#main)
```python
def is_even(x):
   if x%2 == 0:
      return True
   return False
```

<a name="n"/>

## Czy liczba jest podzielna przez n bez reszty [⬆️](#main)
```python
def divisible(x,n):
   if x%n == 0:
      return True
   return False
```

<a name="multiple"/>

## Czy liczba jest wielokrotnością n [⬆️](#main)
```python
numbers = []

def x_range(n):
    for i in range(n):
        numbers.append(i)
    return numbers

def is_multiple(x,n):
   if x in x_range(n):
      return True
   return False

print(is_multiple(3,333))
```

<a name="factorial"/>

## Silnia (n) [⬆️](#main)
```python
from math import factorial

print(factorial(5))
```

```python
#Iterated version

def fact(n):
   factorial = 1
   if int(n) >= 1:
      for i in range (1,int(n)+1):
         factorial = factorial * i
   return factorial
```

```python
#Recursive version

def fact(n):
   if n == 1:
      return n
   elif n < 1:
      return None
   else:
      return n*fact(n-1)
```

<a name="sqrt"/>

## Pierwiastek kwadratowy [⬆️](#main)

```python
from math import sqrt

print(sqrt(4)) #2
```

<a name="sqrt2"/>

## Pierwiastek n-tego stopnia [⬆️](#main)

```python
#sqrt2(number,stopien)

def sqrt2(x,p):
    return x**(1/p)
```

<a name="suma"/>

## Suma liczb od a do b [⬆️](#main)

```python
def suma(a,b):
    return sum(range(a,b+1))

def suma2(a,b):
    wynik = 0
    for i in range(a,b+1): 
        wynik += i
    return wynik
```

<a name="iloczyn"/>

## Iloczyn liczb od a do b [⬆️](#main)

```python
def iloczyn(a,b):
    wynik = 1
    for i in range(a,b+1): 
        wynik *= i
    return wynik
```

<a name="kro"/>

## Krotność np. znaków w ciągu [⬆️](#main)

```python
from collections import Counter

lista_slow=['nie','zdam','matury']

lista_slow = ",".join(lista_slow)

print(Counter(lista_slow))

```

<a name="moda"/>

## Moda/dominanta [⬆️](#main)

```python
from collections import Counter

lista=[1,2,3,4,5,6,7,8,9,2,2,4,4,4,4]

def moda(lista):
    return Counter(lista).most_common(1)[0][0]
 ```
 
<a name="med"/>

## Mediana [⬆️](#main)

```python
def mediana(lista):
    if len(lista) % 2 == 0:
        mediana = lista[int(len(lista)/2)] + lista[int(len(lista)/2-1)]
        mediana /= 2
    else:
        mediana = lista[int(len(lista)/2)]
    return mediana
 ```

<a name="ary"/>

## Średnia arytmetyczna [⬆️](#main)

```python
def srednia(x):
    return sum(x)/len(x)
 ```
 
 ### Ze wzoru:
![equation](https://latex.codecogs.com/svg.latex?\bar{x}%20=%20\frac{x_{n}%20+%20x_{n}%20+{...}%20+%20x_{n}%20}{n})
 
<a name="waz"/>

## Średnia ważona [⬆️](#main)

```python
def srednia(lista,wagi):
    wynik = sum((i*j for i,j in zip(lista,wagi)))/sum(wagi)
    return wynik
 ```
 
### Ze wzoru:
![equation](https://latex.codecogs.com/svg.latex?\bar{x}_{w}%20=%20\frac{x_{1}%20*%20w_{1}%20+%20x_{2}%20*%20w_{2}%20+%20{...}%20+%20x_{n}%20*%20w_{n}}{w_{1}%20+%20w_{2}%20+%20{...}%20+%20w_{n}})
 
 <a name="geo"/>

## Średnia geometryczna [⬆️](#main)

```python
def srednia(lista):
    wynik = 1
    for i in lista:
        wynik *= i
    wynik = wynik**(1/len(lista))
    return wynik
 ```
 
<a name="odchylenie"/>

## Wariancja i odchylenie standardowe [⬆️](#main)

```python
def odchylenie(lista):
    return sum(i**2 for i in lista)/len(lista) - (sum(lista)/len(lista))**2
```
 
 Odchylenie standardowe jest pierwiastkiem kadratowym z wariancji
 
### Ze wzoru:
![equation](https://quicklatex.com/cache3/6b/ql_dbc23eb476667943870c8c8fe0e3af6b_l3.png)
 
<a name="a4"/>

# Metody

<a name="string"/>

## STRING
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
  
 <a name="listy"/>
 
## LISTY
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

<a name="slowniki"/>

## SŁOWNIKI
  * __.clear()__ -> Czyści słownik
  * __.copy()__ -> Plytka kopia
  * __.get()__ -> Zwraca wartość danego klucza
  * __.items()__ -> Zwraca listę krotek kluczy i wartości
  * __.keys()__ -> Zwraca listę kluczy
  * __.pop()__ -> Usuwa element z danym kluczem jako argumentem
  * __.popitem()__ -> Usuwa ostatni wstawiony do słownika element
  * __.update()__ -> Updates the dictionary with the specified key-value pairs
  * __.values()__ -> Zwraca listę wartości

<a name="coll"/>

## class.Collections.Counter()
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

   * __.elements()__ -> Zwracan iteracje kluczy: 'klucz'*vaule
   * __.most_common()__ -> zwraca liste krotek malejąca według wartości kluczy
   * __.subtract()__ -> zwraca counter jako wynik odejmowania z zachowaniem ujemnych wartości
   
<a name="a5"/>
  
# Funkcje wbudowane
   * __abs()__ -> 
   * __delattr()__ -> 
   * __hash()__ -> 
   * __memoryview()__ -> 
   * __set()__ -> 
   * __all()__ -> 
   * __dict()__ -> 
   * __help()__ -> 
   * __min()__ -> 
   * __setattr()__ -> 
   * __any()__ -> 
   * __dir()__ -> 
   * __hex()__ -> 
   * __next()__ -> 
   * __slice()__ -> 
   * __ascii()__ -> 
   * __divmod()__ -> 
   * __id()__ -> 
   * __object()__ -> 
   * __sorted()__ -> 
   * __bin()__ -> 
   * __enumerate()__ -> 
   * __input()__ -> 
   * __oct()__ -> 
   * __staticmethod()__ -> 
   * __bool()__ -> 
   * __eval()__ -> 
   * __int()__ -> 
   * __open()__ -> 
   * __str()__ -> 
   * __breakpoint()__ -> 
   * __exec()__ -> 
   * __isinstance()__ -> 
   * __ord()__ -> 
   * __sum()__ -> 
   * __bytearray()__ -> 
   * __filter()__ -> 
   * __issubclass()__ -> 
   * __pow()__ -> 
   * __super()__ -> 
   * __bytes()__ -> 
   * __float()__ -> 
   * __iter()__ -> 
   * __print()__ -> 
   * __tuple()__ -> 
   * __callable()__ -> 
   * __format()__ -> 
   * __len()__ -> 
   * __property()__ -> 
   * __type()__ -> 
   * __chr()__ -> 
   * __frozenset()__ -> 
   * __list()__ -> 
   * __range()__ -> 
   * __vars()__ -> 
   * __classmethod()__ -> 
   * __getattr()__ -> 
   * __locals()__ -> 
   * __repr()__ -> 
   * __zip()__ -> 
   * __compile()__ -> 
   * __globals()__ -> 
   * __map()__ -> 
   * __reversed()__ -> 
   * __import__()__ -> 
   * __complex()__ ->
   * __hasattr()__ -> 
   * __max()__ -> 
   * __round()__ -> 

