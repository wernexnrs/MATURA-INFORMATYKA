<center><h2> 🔥 **Wernex#9840** 🔥 </h2></center>

## MATURA 2021
Projekt powstał w celu zgromadzenia pomocnych zagadnień na mature rozszerzoną z informatyki. 

## Technologie
Projekt tworzony przy użyciu:
* Python 3.9.1

## Przydatne linki
<a href="http://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Informatory/2015/aneks/Aneks_informatyka_EM_standardowy.pdf">Pełne wymagania maturalne</a><br>
<a href="https://pl.spoj.com/">Polski SPOJ</a> - pełno problemów algorytmicznych do rozwiązania<br>
Zadania od CKE: <a href="https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Materialy/Zbiory_zadan/Matura_Zbi%C3%B3r_zada%C5%84_Informatyka.pdf">Informatyka</a> -- <a href="https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Materialy/Zbiory_zadan/inf-pr-dane.zip">dane</a> -- <a href="https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Materialy/Zbiory_zadan/inf-pr-rozwiazania.zip">rozwiązania</a>


<a name="main"/>

# TOC
1. [Algorytmy wymienione w wymaganiach](#a1)
2. [Dodatkowe algorytmy](#a2)
2. [Tricki](#a3)

<a name="a1"/>

# Algorytmy wymienione w wymaganiach 

1. algorytmy na liczbach całkowitych, np.:
    * [x] [reprezentacja liczb w dowolnym systemie pozycyjnym, w tym w dwójkowym i szesnastkowym,](#konwersja)  
    * [x] [sprawdzanie, czy liczba jest liczbą pierwszą,](#is_prime) 
    * [x] [sprawdzanie, czy liczba jest liczbą doskonała,](#is_perfect)
    * [x] [rozkładanie liczby na czynniki pierwsze,](#prime_factors) 
    * [x] [iteracyjna i rekurencyjna realizacja algorytmu Euklidesa,](#nwd) 
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
    * [ ] kody znaków o zmiennej długości, np. alfabet Morse’a,](#konwersja) 
    * [ ] szyfr Cezara,
    * [ ] szyfr przestawieniowy,
   
<a name="konwersja"/>

### reprezentacja liczb w dowolnym systemie pozycyjnym, w tym w dwójkowym i szesnastkowym[⬆️](#main)

```python
dec_numbers = [15,12,2,4,7,8]

dec_TO_bin = [bin(i)[2:] for i in dec_numbers]
dec_TO_oct = [oct(i)[2:] for i in dec_numbers]
dec_TO_hex = [hex(i)[2:] for i in dec_numbers]


bin_TO_dec = [int(i,2) for i in dec_TO_bin]
oct_TO_dec = [int(i,8) for i in dec_TO_oct]
hex_TO_dec = [int(i,16) for i in dec_TO_hex]

#to_base(number,base)
BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(n, b): 
    return BS[n] if n < b else to_base(n // b, b) + BS[n % b]

def to_base2(s, b):
    res = ""
    while s:
        res+=BS[s%b]
        s//= b
    return res[::-1] or "0"

print(to_base(12, 16))
print(to_base2(12, 16))
```
<a name="is_prime"/>

### sprawdzanie, czy liczba jest liczbą pierwszą[⬆️](#main)
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

### sprawdzanie, czy liczba jest liczbą doskonała[⬆️](#main)
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

### rozkładanie liczby na czynniki pierwsze[⬆️](#main)
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

### iteracyjna i rekurencyjna realizacja algorytmu Euklidesa[⬆️](#main)
```python
def nwd(a, b): return nwd(b, a%b) if b else a #recursive

#^the same
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

#iteration
def nwd2(a, b):
    while b:
        a, b = b, a%b
    return a

def nww(a, b): return a*b//nwd(a, b)
```
<a name="fib"/>

### iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego[⬆️](#main)
```python
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def recur_f(n):
   if n <= 1:
       return n
   return(recur_f(n-1) + recur_f(n-2))
    
for i in range(10): #first 10 numbers
    print(f(i))
    
for i in range(10): #first 10 numbers    
    print(recur_f(i))
```
<a name="zachlanna"/>

## wydawanie reszty metodą zachłanną[⬆️](#main)
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

## sortowanie bąbelkowe[⬆️](#main)
```python
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
  

arr = [64, 34, 25, 12, 22, 11, 90] 
  
print(bubbleSort(arr))
```
<a name="wybor"/>

## sortowanie przez wybór[⬆️](#main)
```python
def selection_sort(tab):
    for i in range(len(tab)):
        mini = i 
        for j in range(i+1, len(tab)): 
            if tab[mini] > tab[j]: 
                mini = j         
        tab[i], tab[mini] = tab[mini], tab[i]
    return tab

tab = [64, 34, 25, 12, 22, 11, 90] 
    
print(selection_sort(tab))
```
<a name="lin"/>

## sortowanie przez wstawianie liniowe[⬆️](#main)
```python
def insertionSort(A): 
    for i in range(1, len(A)):
        liczba = A[i]

        while i > 0 and A[i - 1] > liczba:
            A[i] = A[i -1]
            i -=1
        A[i] = liczba
    return A
  
arr = [12, 11, 13, 5, 6]

print(insertionSort(arr))
```

<a name="scalanie"/>

## sortowanie przez scalanie[⬆️](#main)
```python
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
    return arr

arr = [12, 11, 13, 5, 6, 7]

print(mergeSort(arr))
```
<a name="fast_power"/>

## szybkie podnoszenie do potęgi[⬆️](#main)
```python
def fast_power(x,n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return x * x**(n-1)
    else:
        a = x**(n/2)
    return a**2

#albo
def fast_power2(x,n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return x * (x**((n-1)/2))**2
    return (x**(n/2))**2


print(fast_power(3,6))
print(fast_power2(3,6))
```
<a name="bisekcja"/>

## wyznaczanie miejsc zerowych funkcji metodą połowienia - bisekcja[⬆️](#main)
```python
def f(x):
    return -4*x +2

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

## sprawdzanie, czy dany ciąg znaków tworzy palindrom[⬆️](#main)
```python
def if_palindrom(string):
    lista = list(string)
    lista2 = lista[::-1]
    if lista == lista2:
        return True
    return False

string = "ala"

print(if_palindrom(string))
```
<a name="anagram"/>

## sprawdzanie, czy dany ciąg znaków tworzy anagram[⬆️](#main)
```python
def if_anagram(string,string2):
    if sorted(string) == sorted(string2):
        return True
    return False

string = "anagram"
string2 = "nagaram"

print(if_anagram(string,string2))
```
<a name="alfa"/>

## porządkowanie alfabetyczne[⬆️](#main)
```python
def sort(lista):
    return sorted(lista)

lista = ["C","D","A","O"]

print(sort(lista))

#to jest python po co mam znac rozbudowana wersje..

#przez wstawianie
def sort_poco(lista):
    for i in range(len(lista)):
        mini = i 
        for j in range(i+1, len(lista)): 
            if lista[mini] > lista[j]: 
                mini = j         
        lista[i], lista[mini] = lista[mini], lista[i]
    return lista

print(sort_poco(lista))    
```
<a name="pattern"/>

## wyszukiwanie wzorca w tekście[⬆️](#main)
```python
def is_pattern(pattern,word):
    return pattern in word

pattern = "motyw"
word = "lokomotywa"

print(is_pattern(pattern,word))

#implementacje iteracyjną zrobię kiedy indziej 
```
