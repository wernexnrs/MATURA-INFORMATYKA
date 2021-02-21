<h1 align="center">  Dodatkowe algorytmy </h1>

1. __algorytmy na liczbach całkowitych:__ 

    - [x] [Czy liczba jest parzysta](#even)
    - [x] [Czy liczba jest podzielna przez n bez reszty](#n)
    - [x] [Czy liczba jest wielokrotnością n](#multiple)   

2. __algorytmy wyszukiwania i porządkowania (sortowania):__ 

    - [x] [Krotność](#kro)  

3. __algorytmy numeryczne__

    - [x] [Silnia (n)](#factorial)
    - [x] [Pierwiastek kwadratowy](#sqrt)
    - [x] [Pierwiastek n-tego stopnia](#sqrt2)  
    - [x] [Suma liczb od a do b](#suma)
    - [x] [Iloczyn liczb od a do b](#iloczyn)  
    - [x] [Moda](#moda)  
    - [x] [Mediana](#med) 
    - [x] [Średnia arytmetyczna](#ary) 
    - [x] [Średnia ważona](#waz) 
    - [x] [Średnia geometryczna](#geo)
    - [x] [Wariancja i odchylenie standardowe](#odchylenie) 
    - [x] [Potęgowanie](#power) 

4. __algorytmy na tekstach__

    .......
    
5. __algorytmy kompresji i szyfrowania__

   .......
   
   - kody znaków o zmiennej długości,

      .......

  
<a name="even"/>

## Czy liczba jest parzysta [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python
def is_even(x):
   if x % 2 == 0:
      return True
   return False
```

</details>
    
<a name="n"/>

## Czy liczba jest podzielna przez n bez reszty [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python
def divisible(x,n):
   if x % n == 0:
      return True
   return False
```

</details>

<a name="multiple"/>

## Czy liczba jest wielokrotnością n [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python

def is_multiple2(x,n):
    if n % x == 0:
        return True
    return False
    
print(is_multiple(3,333))
```

</details>

<a name="factorial"/>

## Silnia (n) [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python
from math import factorial

print(factorial(5))
```

```python
#Iterated version

def fact(n):
   factorial = 1
   if n >= 1:
      for i in range (1, n + 1):
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
   return n*fact(n-1)
```

</details>

<a name="sqrt"/>

## Pierwiastek kwadratowy [⬆️](#main)

<details>
  <summary>Rozwiń</summary>

```python
from math import sqrt

print(sqrt(4))
```

```python
#sqrt1(number,stopien)

def sqrt1(x):
    return x ** (1/2)
```

</details>

<a name="sqrt2"/>

## Pierwiastek n-tego stopnia [⬆️](#main)

<details>
  <summary>Rozwiń</summary>

```python
#sqrt1(number,stopien)

def sqrt1(x,p):
    return x ** (1/p)
```

<a name="suma"/>

</details>

## Suma liczb od a do b [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python
def suma(a,b):
    return sum(range(a, b + 1))
```

```python
def suma(a,b):
    wynik = 0
    for i in range(a, b +1 ): 
        wynik += i
    return wynik
```

</details>

<a name="iloczyn"/>

## Iloczyn liczb od a do b [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python
def iloczyn(a,b):
    wynik = 1
    for i in range(a, b + 1): 
        wynik *= i
    return wynik
```

</details>

<a name="kro"/>

## Krotność np. znaków w ciągu [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python
from collections import Counter

lista_slow = ['nie','zdam','matury']

lista_slow = ",".join(lista_slow)

print(Counter(lista_slow))

```

```python
def freq(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(freq('slowo'))
```

</details>

<a name="moda"/>

## Moda/dominanta [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python
from collections import Counter

lista=[1,2,3,4,5]

def moda(lista):
    if all(i == 1 for i in Counter(lista).values()):
        return lista
    return Counter(lista).most_common(1)[0][0]
 ```
 
```python
 def moda(lista):
    return max(set(lista), key=lista.count)
 ``` 
 
</details>

<a name="med"/>

## Mediana [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python
def mediana(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j + 1], lista[j] = lista[j], lista[j + 1]

    if len(lista) % 2 == 0:
        mediana = lista[int(len(lista) / 2)] + lista[int(len(lista) / 2 - 1)]
        mediana /= 2
    else:
        mediana = lista[int(len(lista) / 2)]
    return mediana
 ```
 
 ### Ze wzoru:
![equation](https://raw.githubusercontent.com/wernexnrs123/MATURA-INFORMATYKA/master/dzialy/images/mediana.png)

</details>

<a name="ary"/>

## Średnia arytmetyczna [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python
def srednia(x):
    return sum(x)/len(x)
 ```
 
 ### Ze wzoru:
![equation](https://raw.githubusercontent.com/wernexnrs123/MATURA-INFORMATYKA/master/dzialy/images/srednia.png)

</details>

<a name="waz"/>

## Średnia ważona [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python
def srednia(lista, wagi):
    wynik = sum((i * j for i, j in zip(lista, wagi))) / sum(wagi)
    return wynik

 ```
 
### Ze wzoru:
![equation](https://raw.githubusercontent.com/wernexnrs123/MATURA-INFORMATYKA/master/dzialy/images/srednia_wazona.png)

</details>

 <a name="geo"/>

## Średnia geometryczna [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python
def srednia(lista):
    wynik = 1
    for i in lista:
        wynik *= i
    wynik = wynik ** (1/len(lista))
    return wynik
 ```
 
 ### Ze wzoru:
![equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/d97e78adc3acddf0b54ed5624ab2ceff2057bf40)

</details>

<a name="odchylenie"/>

## Wariancja i odchylenie standardowe [⬆️](#main)

<details>
  <summary>Rozwiń</summary>
    
```python
def odchylenie(lista):
    return sum(i ** 2 for i in lista) / len(lista) - (sum(lista) / len(lista)) ** 2

```
 
### Ze wzoru:
![equation](https://raw.githubusercontent.com/wernexnrs123/MATURA-INFORMATYKA/master/dzialy/images/wariancja.png)
 
</details>
