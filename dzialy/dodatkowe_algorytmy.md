<h1 align="center">  Dodatkowe algorytmy </h1>

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
