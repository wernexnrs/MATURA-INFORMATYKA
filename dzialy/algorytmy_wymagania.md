<a name="main"/>

<h1 align="center"> Algorytmy wymienione w wymaganiach </h1>

1. __algorytmy na liczbach całkowitych:__ 
   - [x] [reprezentacja liczb w dowolnym systemie pozycyjnym, w tym w dwójkowym i szesnastkowym,](#konwersja)  
   - [x] [sprawdzanie, czy liczba jest liczbą pierwszą,](#is_prime) 
   - [x] [sprawdzanie, czy liczba jest liczbą doskonała,](#is_perfect)
   - [x] [rozkładanie liczby na czynniki pierwsze,](#prime_factors) 
   - [x] [iteracyjna i rekurencyjna realizacja algorytmu Euklidesa + NWW,](#nwd) 
   - [x] [iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego,](#fib) 
   - [x] [wydawanie reszty metodą zachłanną,](#zachlanna)    
2. __algorytmy wyszukiwania i porządkowania (sortowania):__ 
   - [x] [bąbelkowy, ](#bob) 
   - [x] [przez wybór, ](#wybor) 
   - [x] [przez wstawianie liniowe, ](#lin) 
   - [x] [przez scalanie,](#scalanie) 
   - [x] [szybki,](#fast)
   - [x] [kubełkowy,](#box)  
3. __algorytmy numeryczne__
   - [ ] [szybkie podnoszenie do potęgi,](#fast_power) do przekminienia
   - [x] [wyznaczanie miejsc zerowych funkcji metodą połowienia,](#bisekcja)  
4. __algorytmy na tekstach__
   - [x] [sprawdzanie, czy dany ciąg znaków tworzy palindrom,](#palindrom) 
   - [x] [sprawdzanie, czy dany ciąg znaków tworzy anagram,](#anagram) 
   - [x] [porządkowanie alfabetyczne,](#alfa) do przekminienia
      * Większości obiektów
      * Słowników    
   - [x] [wyszukiwanie wzorca w tekście,](#pattern)   
5. __algorytmy kompresji i szyfrowania__
   * kody znaków o zmiennej długości,
      * [ ] [Kompresja danych](#len) #nie potrafie
      * [ ] [alfabet Morse’a](#morse) #nie wiem        
   - [x] [szyfr Cezara,](#cezar)
   - [x] [szyfr przestawieniowy,](#przes)

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

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(n, b): #to_base(number,base)
    return BS[n] if n < b else to_base(n // b, b) + BS[n % b]
```

```python
#recursive version DEC --> ANY

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(n, b): #to_base(number,base)
    if n < b:
      return BS[n] 
    return to_base(n // b, b) + BS[n % b]
```

```python
#iterated version DEC --> ANY

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

## Iiteracyjna i rekurencyjna realizacja algorytmu Euklidesa + NWW [⬆️](#main)
```python
#recursive one-liner version

def nwd(a, b): return nwd(b, a % b) if b else a 
```

```python
#recursive version

def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a
```

```python
#iterated version

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a
```

```python
#Najmniejsza wspólna wielokrotność

def nww(a, b): return a * b // nwd(a, b)
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
   return f(n-1) + f(n-2)
```    

<a name="zachlanna"/>

## Wydawanie reszty metodą zachłanną [⬆️](#main)
```python
do_wydania = 6 
monety = [1,2,5]

def wydawanie(do_wydania,monety):
   count = 0
   historia = []

   while do_wydania > 0:
       nominal = 0
       for i in range(len(monety)):
           if monety[i] <= do_wydania and monety[i] > nominal:
               nominal = monety[i]
       do_wydania -= nominal

       historia.append(nominal)
       count+=1

   return f'Reszte wydasz w {count} monetach, te monety to {historia}'
```

<a name="bob"/>

## Sortowanie bąbelkowe [⬆️](#main)
```python
#In place

def bubble_sort(arr): 
    for i in range(len(arr)): 
        for j in range(len(arr)-i-1): 
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

def insertion_sort(A): 
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

def merge_sort(tab):
    if len(tab) > 1:
        mid = len(tab)//2
        L = tab[:mid]
        R = tab[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            tab[k] = R[j]
            j += 1
            k += 1
```

<a name="fast"/>

## Sortowanie szybkie [⬆️](#main)
```python

def partition(arr, low, high):
    
    i = (low-1)        
    pivot = arr[high]     
  
    for j in range(low, high): 
        if arr[j] <= pivot: 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1)

def quickSort(arr, low, high):
    
    if len(arr) == 1: 
        return arr
    
    if low < high: 
        pi = partition(arr, low, high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
  
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr, 0, n-1)

print(arr)

```

<a name="box"/>

## Sortowanie kubełkowe [⬆️](#main)
```python
# Python3 program to sort an array  
# using bucket sort  
def insertionSort(b): 
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1
        while j >= 0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up      
    return b      
              
def bucketSort(x): 
    arr = [] 
    slot_num = 10 # 10 means 10 slots, each 
                  # slot's size is 0.1 
    for i in range(slot_num): 
        arr.append([]) 
          
    # Put array elements in different buckets  
    for j in x: 
        index_b = int(slot_num * j)  
        arr[index_b].append(j) 
      
    # Sort individual buckets  
    for i in range(slot_num): 
        arr[i] = insertionSort(arr[i]) 
          
    # concatenate the result 
    k = 0
    for i in range(slot_num): 
        for j in range(len(arr[i])): 
            x[k] = arr[i][j] 
            k += 1
    return x 
  
# Driver Code 
x = [0.897, 0.565, 0.656, 
     0.1234, 0.665, 0.3434]  
print("Sorted Array is") 
print(bucketSort(x)) 
  
# This code is contributed by 
# Oneil Hsiao 
```

<a name="fast_power"/>

## Szybkie podnoszenie do potęgi [⬆️](#main)

to musze przemyśleć 

```python
#Iterated version

```

```python
#Recursive version
```

<a name="bisekcja"/>

## Wyznaczanie miejsc zerowych funkcji metodą połowienia - bisekcja [⬆️](#main)
```python
def f(x):
    return -4 * x + 2

#bisection(od,do)
def bisection(a,b,precyzja = 0.0001): 
    if f(a) * f(b) >= 0: 
        return None
    c = a 
    while b-a >= precyzja: 
        c = (a + b) / 2
        if f(c) == 0.0: 
            break
        if f(c) * f(a) < 0: 
            b = c 
        else: 
            a = c      
    return c
```

<a name="palindrom"/>

## Sprawdzanie, czy dany ciąg znaków tworzy palindrom [⬆️](#main)
```python
def is_palindrom(string):
    lista = list(string)
    if lista == lista[::-1]:
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

### Większości obiektów
```python
def sort(lista):
    return sorted(lista)
```

### Słowników
```python
#Po wartościach

def sort_dict_by_value(x):
    return {k: v for k, v in sorted(x.items(), key = lambda item: item[1])}
```

```python
#Po kluczach

from collections import OrderedDict

def sort_dict_by_key(x):
   return OrderedDict(sorted(x.items())) # to jest bez sensu powyzej pythona 3.7 sa inne metody ide spac zmienei jutro
```

<a name="pattern"/>

## Wyszukiwanie wzorca w tekście [⬆️](#main)
```python
def is_pattern(pattern,word):
    return pattern in word
```

<a name="len"/>

## Kompresja danych [⬆️](#main)

### Prefix free
Kod jest nazywany "prefix (free) code", jeżeli w systemie nie ma kodu słowa, który byłby prefixem innego kodu słowa.

Załóżmy, że mamy plik z 100,000 znakami, jedyne znaki jakie występują w pliku to: a,b,c,d,e,f i chcemy zmniejszysz rozmiar tego pliku kompresją, gdzie każdy kod znaku ma różną długość.

| | a | b | c | d | e | f |
| --- | --- | --- | --- | --- | --- | --- |
| Częstość | 45 | 13 | 12 | 16 | 9 | 5 |
| Fixed-length code | 0 | 101 | 100 | 111 | 1101 | 1100 |

Plik taki zajmnie (45 * 1 + 13 * 3 + 12 * 3 + 16 * 3 + 9 * 4 + 5 * 4) * 1000 = 224,000 bity

```python
text = "01101100"

cipher = {'0': 'a','101': 'b','100': 'c', '111': 'd', '1101': 'e', '1100': 'f'}

Odkoduj napis w zmiennej text zakładając, że jest to prefix (free) code. Powodzenia.
```

<a name="morse"/>

## Alfabet Morse’a [⬆️](#main)
```python
Nie wiem
```

<a name="cezar"/>

## Szyfr Cezara [⬆️](#main)
```python
def koduj(wiadomosc,klucz):
    wynik = ""
    wiadomosc = wiadomosc.upper().replace(" ", "")
    for i in wiadomosc:
        wynik += chr((ord(i) + klucz - 65) % 26 + 65)
    return wynik

def dekoduj(wiadomosc,klucz):
    klucz *= -1
    return koduj(wiadomosc,klucz)
```

<a name="przes"/>

## Szyfr przestawieniowy [⬆️](#main)
```python
tekst = "LA AAMK CORUAKB RUAKI P EIKS AIBSEKA" #jump =  1 to decrypt
tekst = list(tekst)
jump = 1

def przes(lista):
    for i in range(0,len(tekst)-2,2):
        tekst[i],tekst[i+jump] = tekst[i+jump],tekst[i]
    tekst = "".join(tekst)
    return tekst
print(tekst)
```
