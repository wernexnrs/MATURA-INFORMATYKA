# 🔥 Wernex#9840 🔥 

## MATURA 2021
Projekt powstał w celu zgromadzenia pomocnych zagadnień na mature rozszerzoną z informatyki. 

## Technologie
Projekt tworzony przy użyciu:
* Python 3.9.1

<a name="main"/>

# TOC
1. [Algorytmy wymienione w wymaganiach](#a1)
2. [Dodatkowe algorytmy](#a2)
3. [Tricki](#a3)

<a name="a1"/>

# Algorytmy wymienione w wymaganiach 

1. algorytmy na liczbach całkowitych, np.:
   * [x] [reprezentacja liczb w dowolnym systemie pozycyjnym, w tym w dwójkowym i szesnastkowym,](#konwersja)  
   * [x] [sprawdzanie, czy liczba jest liczbą pierwszą,](#is_prime) 
   * [x] [sprawdzanie, czy liczba jest liczbą doskonała,](#is_perfect)
   * [x] [rozkładanie liczby na czynniki pierwsze,](#prime_factors) 
   * [x] [iteracyjna i rekurencyjna realizacja algorytmu Euklidesa, + NWW](#nwd) 
   * [x] [iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego,](#fib) 
   * [x] [wydawanie reszty metodą zachłanną,](#zachlanna) 
2. algorytmy wyszukiwania i porządkowania (sortowania), np.:
   * algorytmy sortowania ciągu liczb: 
      * [x] [bąbelkowy, ](#bob) 
      * [x] [przez wybór, ](#wybor) 
      * [x] [przez wstawianie liniowe, ](#lin) 
      * [x] [przez scalanie, ](#scalanie) 
      * [ ] szybki, 
      * [ ] kubełkowy,
3. algorytmy numeryczne, np.:
   * [x] [szybkie podnoszenie do potęgi,](#fast_prime) 
   * [x] [wyznaczanie miejsc zerowych funkcji metodą połowienia,](#bisekcja) 
4. algorytmy na tekstach, np.:
   * [x] [sprawdzanie, czy dany ciąg znaków tworzy palindrom,](#palindrom) 
   * [x] [sprawdzanie, czy dany ciąg znaków tworzy anagram,](#anagram) 
   * [x] [porządkowanie alfabetyczne,](#alfa) 
   * [x] [wyszukiwanie wzorca w tekście,](#pattern) 
5. algorytmy kompresji i szyfrowania, np.:
   * [ ] kody znaków o zmiennej długości, np. alfabet Morse’a,
   * [ ] szyfr Cezara,
   * [ ] szyfr przestawieniowy,
   
<a name="konwersja"/>

## Reprezentacja liczb w dowolnym systemie pozycyjnym, w tym w dwójkowym i szesnastkowym [⬆️](#main)

```python
#int("number_string",base) ANY --> DEC

dec_numbers = [15,12,2,4,7,8]

dec_TO_bin = [bin(i)[2:] for i in dec_numbers]
dec_TO_oct = [oct(i)[2:] for i in dec_numbers]
dec_TO_hex = [hex(i)[2:] for i in dec_numbers]

bin_TO_dec = [int(i,2) for i in dec_TO_bin]
oct_TO_dec = [int(i,8) for i in dec_TO_oct]
hex_TO_dec = [int(i,16) for i in dec_TO_hex]
```

```python
#recursive one-liner version DEC --> ANY

BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(n, b): #to_base(number,base)
    return BS[n] if n < b else to_base(n // b, b) + BS[n % b]
```

```python
#iterated version DEC --> ANY

BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(n, b):
    res = ""
    while n:
        res+=BS[n%b]
        n //= b
    return res[::-1]
```

<a name="is_prime"/>

## Sprawdzanie, czy liczba jest liczbą pierwszą [⬆️](#main)
```python
def is_prime(x):
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                return False
        return True
    return False
```

<a name="is_perfect"/>

## Sprawdzanie, czy liczba jest liczbą doskonała [⬆️](#main)
```python
def is_perfect(n):
    s = 1
    for i in range(2,n):
        if n % i == 0:
            s += i
    if n == s and n != 1:
        return True
    return False
```

<a name="prime_factors"/>

## Rozkładanie liczby na czynniki pierwsze [⬆️](#main)
```python
def prime_factors(n):
    factors = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            factors.append(k)
        k += 1
    return factors 
```

<a name="nwd"/>

## Iiteracyjna i rekurencyjna realizacja algorytmu Euklidesa [⬆️](#main)
```python
#recursive one-liner version
def nwd(a, b): return nwd(b, a%b) if b else a 

#recursive version
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a
```

```python
#iterated version
def nwd2(a, b):
    while b:
        a, b = b, a%b
    return a
```

```python
#Najmniejsza wspólna wielokrotność
def nww(a, b): return a*b//nwd(a, b)
```

<a name="fib"/>

## Iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego [⬆️](#main)
```python
#Iterated version

def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
```

```python
#Recursive version

def f(n):
   if n <= 1:
       return n
   return(f(n-1) + f(n-2))
```    

<a name="zachlanna"/>

## Wydawanie reszty metodą zachłanną [⬆️](#main)
```python
do_wydania = 6 #zł

monety = [1,2,5]
count = 0
historia = []

wybrana_moneta = int(input())

while (wybrana_moneta > 0):
    nominal = 0
    for i in range(len(monety)):
        if monety[i] <= wybrana_moneta and monety[i] > nominal:
            nominal = monety[i]
    wybrana_moneta = wybrana_moneta - nominal

    historia.append(nominal)
    count+=1

print(f'Reszte wydasz w {count} monetach, te monety to {historia}')
```

<a name="bob"/>

## Sortowanie bąbelkowe [⬆️](#main)
```python
#In place

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

<a name="wybor"/>

## Sortowanie przez wybór [⬆️](#main)
```python
#In place

def selection_sort(tab):
    for i in range(len(tab)):
        mini = i 
        for j in range(i+1, len(tab)): 
            if tab[mini] > tab[j]: 
                mini = j         
        tab[i], tab[mini] = tab[mini], tab[i]
```

<a name="lin"/>

## Sortowanie przez wstawianie liniowe [⬆️](#main)
```python
#In place

def insertionSort(A): 
    for i in range(1, len(A)):
        liczba = A[i]

        while i > 0 and A[i - 1] > liczba:
            A[i] = A[i -1]
            i -=1
        A[i] = liczba
```

<a name="scalanie"/>

## Sortowanie przez scalanie [⬆️](#main)
```python
#In place

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
```

<a name="fast_power"/>

## Szybkie podnoszenie do potęgi [⬆️](#main)
```python
#fast_power(number,power)

def fast_power(x,n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return x * x**(n-1)
    else:
        a = x**(n/2)
    return a**2
```

```python
def fast_power2(x,n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return x * (x**((n-1)/2))**2
    return (x**(n/2))**2
```

<a name="bisekcja"/>

## Wyznaczanie miejsc zerowych funkcji metodą połowienia - bisekcja [⬆️](#main)
```python
def f(x):
    return -4*x +2

#bisection(od,do)
def bisection(a,b,precyzja = 0.0001): 
    if f(a)*f(b) >= 0: 
        return None
    c = a 
    while (b-a) >= precyzja: 
        c = (a+b)/2
        if (f(c) == 0.0): 
            break
        if (f(c)*f(a) < 0): 
            b = c 
        else: 
            a = c      
    return c
      
print("{:.3f}".format( bisection(-100, 100) ))
```

<a name="palindrom"/>

## Sprawdzanie, czy dany ciąg znaków tworzy palindrom [⬆️](#main)
```python
def is_palindrom(string):
    lista = list(string)
    lista2 = lista[::-1]
    if lista == lista2:
        return True
    return False
```

<a name="anagram"/>

## Sprawdzanie, czy dany ciąg znaków tworzy anagram [⬆️](#main)
```python
def is_anagram(string,string2):
    if sorted(string) == sorted(string2):
        return True
    return False
```

<a name="alfa"/>

## Porządkowanie alfabetyczne [⬆️](#main)
```python
def sort(lista):
    return sorted(lista)
```

<a name="pattern"/>

## Wyszukiwanie wzorca w tekście [⬆️](#main)
```python
def is_pattern(pattern,word):
    return pattern in word
```

<a name="a2"/>

# Dodatkowe algorytmy

   * [x] [Czy liczba jest parzysta](#even)
   * [x] [Czy liczba jest podzielna przez n bez reszty](#n)
   * [x] [Czy liczba jest wielokrotnością n](#multiple)
   * [x] [Silnia (n)](#factorial)

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
