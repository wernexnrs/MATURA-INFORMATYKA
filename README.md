## MATURA
Projekt powstał w celu zgromadzenia pomocnych zagadnień na mature rozszerzoną z informatyki. 

## Technologie
Projekt tworzony przy użyciu:
* Python 3.9.1

## Wymagania
**opisuje podstawowe algorytmy i stosuje:**
1. algorytmy na liczbach całkowitych, np.:
    * [x] [reprezentacja liczb w dowolnym systemie pozycyjnym, w tym w dwójkowym i szesnastkowym,](#link1)
    * [x] sprawdzanie, czy liczba jest liczbą pierwszą, doskonałą,
    * [x] rozkładanie liczby na czynniki pierwsze,
    * [x] iteracyjna i rekurencyjna realizacja algorytmu Euklidesa,
    * [x] iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego,
    * [x] wydawanie reszty metodą zachłanną,
2. algorytmy wyszukiwania i porządkowania (sortowania), np.:
    * algorytmy sortowania ciągu liczb: 
      * [x] bąbelkowy, 
      * [x] przez wybór, 
      * [x] przez wstawianie liniowe, 
      * [x] przez scalanie, 
      * [ ] szybki, 
      * [ ] kubełkowy,
3. algorytmy numeryczne, np.:
    * [x] szybkie podnoszenie do potęgi,
    * [x] wyznaczanie miejsc zerowych funkcji metodą połowienia,
4. algorytmy na tekstach, np.:
    * [x] sprawdzanie, czy dany ciąg znaków tworzy palindrom, anagram,
    * [x] porządkowanie alfabetyczne,
    * [x] wyszukiwanie wzorca w tekście,
5.algorytmy kompresji i szyfrowania, np.:
    * [ ] kody znaków o zmiennej długości, np. alfabet Morse’a,
    * [ ] szyfr Cezara,
    * [ ] szyfr przestawieniowy,

### reprezentacja liczb w dowolnym systemie pozycyjnym, w tym w dwójkowym i szesnastkowym

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
### sprawdzanie, czy liczba jest liczbą pierwszą
```python
def is_prime(x):
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                return False
        return True
    return False
```
### sprawdzanie, czy liczba jest liczbą doskonała
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
### rozkładanie liczby na czynniki pierwsze
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
### iteracyjna i rekurencyjna realizacja algorytmu Euklidesa
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
### iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego
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
