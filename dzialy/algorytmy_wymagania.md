<a name="main"></a>
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
   - [x] [szybkie podnoszenie do potęgi,](#fast_power)
   - [x] [wyznaczanie miejsc zerowych funkcji metodą połowienia,](#bisekcja)

4. __algorytmy na tekstach__
   - [x] [sprawdzanie, czy dany ciąg znaków tworzy palindrom,](#palindrom)
   - [x] [sprawdzanie, czy dany ciąg znaków tworzy anagram,](#anagram)
   - [x] [porządkowanie alfabetyczne, (leksykograficzne)](#alfa)
   - [x] [wyszukiwanie wzorca w tekście,](#pattern)

5. __algorytmy kompresji i szyfrowania__
   - kody znaków o zmiennej długości,
	 * [x] [Kompresja danych](#len)
	 * [x] [Alfabet Morse’a](#morse)
   - szyfry przestawieniowe,
	* [x] [Transpozycyjny](#przes)
	* [ ] [Szyfr AtBash](#atbash)
	* [x] [Szyfr Cezara](#cezar)
### Rzeczy, które nie są zwinięte w jakis sposób potrzebują poprawy

<a name="konwersja"></a>
## Reprezentacja liczb w dowolnym systemie pozycyjnym, w tym w dwójkowym i szesnastkowym [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#int("number_string",base) ANY --> DEC

dec_numbers = [15, 12, 2, 4, 7, 8]

dec_TO_bin = [bin(i)[2:] for i in dec_numbers]
dec_TO_oct = [oct(i)[2:] for i in dec_numbers]
dec_TO_hex = [hex(i)[2:] for i in dec_numbers]

bin_TO_dec = [int(i, 2) for i in dec_TO_bin]
oct_TO_dec = [int(i, 8) for i in dec_TO_oct]
hex_TO_dec = [int(i, 16) for i in dec_TO_hex]
```

```python
#recursive one-liner version DEC --> ANY

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(n, b):  # to_base(number,base)
    return BS[n] if n < b else to_base(n // b, b) + BS[n % b]
```

```python
#recursive version DEC --> ANY

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(n, b):  # to_base(number,base)
    if n < b:
        return BS[n]
    return to_base(n // b, b) + BS[n % b]
```
<b>

```
BS -> "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(n, b):
	Jeżeli n < b:
		Zwróć BS[n]
	W innym wypadku:
		Zwróć to_base(n // b, b) + BS[n % b]
```
</b>

```python
#iterated version with slices DEC --> ANY

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(n, b):
    res = ""
    while n:
        res += BS[n % b]
        n //= b
    return res[::-1]
```
</details>

<a name="is_prime"></a>
## Sprawdzanie, czy liczba jest liczbą pierwszą [⬆️](#)
<details><summary>Rozwiń</summary>

```python
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    return False
```
<b>

```
A <- [1,2 … n]

Dla i = 1,2 … n
	Jeżeli i > 1
		Dla j = 2,3 ... i
			Jeżeli i mod j == 0
				Zwróć Fałsz
		Zwróć Prawde
	W innym wypadku
		Zwróć Fałsz
```
</b>
</details>

<a name="is_perfect"></a>
## Sprawdzanie, czy liczba jest liczbą doskonała [⬆️](#)
<details><summary>Rozwiń</summary>

```python
def is_perfect(n):
    s = 1
    for i in range(2, n):
        if n % i == 0:
            s += i
    if n == s and n != 1:
        return True
    return False
```
<b>

```
A = [1,2 … n]

Dla i = 1,2 … n
	s <- 1
	Dla  j = [2, 3, n]
		Jeżeli i mod j == 0
			s <- s + 1
	Jeżeli n == s oraz n != 1
		Zwróć Prawde
	Zwróć Fałsz
```
</b>
</details>

<a name="prime_factors"></a>
## Rozkładanie liczby na czynniki pierwsze [⬆️](#)
<details><summary>Rozwiń</summary>

```python
def prime_factors(n):
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            print(k)  # albo do tablicy sobie wrzucać
        k += 1
```
<b>

```
n = liczba całkowita
div - operator dzielenia całkowitego

k <- 2

Dopóki n != 1
	Dopóki n mod k == 0
		n <- n div k # dzielenie całkowite
		Wypisz k
	k <- k + 1
```
</b>
</details>

<a name="nwd"></a>
## Iiteracyjna i rekurencyjna realizacja algorytmu Euklidesa + NWW [⬆️](#)
<details><summary>Rozwiń</summary>

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
<b>

```
a - liczba całkowita
b - liczba całkowita

def nwd(a, b):
	Jeżeli b > 0:
		Zwróc nwd(b, a % b)
	W innym wypadku
		Zwróć a
```
</b>

```python
#iterated version

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a
```
<b>

```
a - liczba całkowita
b - liczba całkowita

def nwd(a, b):
	Dopóki b != 0
		t <- a
		a <- b
		b <- t mod b
	Zwróć a
```
</b>

```python
#Najmniejsza wspólna wielokrotność

def nww(a, b): return a * b // nwd(a, b)
```
<b>

```
a - liczba całkowita
b - liczba całkowita
div - dzielenie całkowite

def nww(a, b):
	Zwróć a * b div nwd(a,b)
```
</b>
</details>

<a name="fib"></a>
## Iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#Iterated version

def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
```
<b>

```
a <- 0
b <- 1
n - n'ty wyraz ciągu

Dla i = 1,2 ... n
	t <- a
	a <- b
	b <- t + b
```
</b>

```python
#Recursive version

def f(n):
    if n <= 1:
        return n
    return f(n - 1) + f(n - 2)
```
<b>

```
def f(n)
	Jeżeli n <= 1
		Zwróć n
	W innym wypadku
		Zwróć f(n-1) + f(n-2)
```
</b>
</details>

<a name="zachlanna"></a>
## Wydawanie reszty metodą zachłanną [⬆️](#)
<details><summary>Rozwiń</summary>

```python
do_wydania = 6
monety = [1, 2, 5]

def wydawanie(do_wydania, monety):
    count = 0
    historia = []

    while do_wydania > 0:
        nominal = 0
        for i in range(len(monety)):
            if do_wydania >= monety[i] > nominal:
                nominal = monety[i]
        do_wydania -= nominal

        historia.append(nominal)
        count += 1

    return f'Reszte wydasz w {count} monetach, te monety to {historia}'

print(wydawanie(do_wydania, monety))
```
<b>

```
do_wydania <- 6
monety <- [1, 2, 5]
count <- 0
historia <- []

Dopóki do_wydania > 0:
	nominal <- 0

	Dla i = 1,2,3, ... , rozmiar tablicy (bedzie podany, najczesciej n)
		Jeżeli do_wydania >= monety[i] > nominal:
			nominal <- monety[i]
			historia[i] <- nominal
		do_wydania <- do_wydania - nominal
		count <- count + 1
```
</b>
</details>

<a name="bob"></a>
## Sortowanie bąbelkowe [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#In place

def bubble_sort(tab):
    for i in range(len(tab)):
        for j in range(len(tab) - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j + 1], tab[j] = tab[j], tab[j + 1]
```
<b>

```
A = [1,2 … n]

Dla i = 1,2 … n
	Dla j = 1,2 ... n – i – 1
		Jeżeli A[j] > A[j + 1]
			t <- A[j + 1]
			A[j + 1] <- A[j]
			A[j] <- t
```
</b>
</details>

<a name="wybor"></a>
## Sortowanie przez wybór [⬆️](#)
<details><summary>Rozwiń</summary>

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
<b>

```
A <- [1,2 … n]
n <- ilość liczb

Dla i = 1,2 … n
	mini = i
	Dla j = i + 1, ... n
		Jeżeli A[mini] > A[j]
			mini <- j
	t <- A[i]
	A[i] <- A[mini]
	A[mini] <- t
```
</b>
</details>

<a name="lin"></a>
## Sortowanie przez wstawianie liniowe [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#In place

def insertion_sort(A):
    for i in range(1, len(A)):
        liczba = A[i]

        while i > 0 and A[i - 1] > liczba:
            A[i] = A[i - 1]
            i -= 1
        A[i] = liczba
```
<b>

```
n <- liczba całkowita
A <- [1,2 ... n]

Dla i = 1, 2, ... , n
	liczba <- A[i]

	Dopóki i > 0 oraz A[i - 1] > liczba
		A[i] <- A[i - 1]
		i <- i - 1
	A[i] <- liczba
```
</b>
</details>

<a name="scalanie"></a>
## Sortowanie przez scalanie [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#In place

def merge_sort(tab):
    if len(tab) < 2:
        return tab

    i = j = k = 0
    mid = len(tab) // 2
    L, R = tab[:mid], tab[mid:]
    merge_sort(L)
    merge_sort(R)

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
<b>

```
n <- długość tablicy
div <- dzielenie całkowite
len() <- długość obiektu

def merge_sort(tab):
	Jeżeli n < 2:
		Zwróć tab
	i <- 0
	j <- 0
	k <- 0

	L <- tab[:mid]
	R <- tab[mid:]
	merge_sort(L)
        merge_sort(R)

	Dla i = 1, 2, ..

	Dopóki i < len(L) oraz j < len(R)
		Jeżeli L[i] < R[i]
			i <- i + 1
		k <- k + 1

	Dopóki i < len(L)
        	tab[k] = L[i]
        	i <- i + 1
        	k <- k + 1

    	Dopóki j < len(R)
        	tab[k] = R[j]
        	j <- j + 1
        	k <- k + 1
```
</b>
</details>

<a name="fast"></a>
## Sortowanie szybkie [⬆️](#)
<details><summary>Rozwiń</summary>

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    less = []
    greater = []

    pivot = arr.pop(len(arr) // 2)
    for x in arr:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)


arr = [60, 20, 11, 122, 214, 345, 1324, 1, 2, 3, 6, 74, 3, 9]

print(quicksort(arr))

# This code is contributed by Pixel
```
<b>

```
n <- wielkosć tablicy

def qs(arr)
    Jeżeli n <= 1:
        Zwróc arr

    less <- []
    greater <- []
    pivot <- n div 2 # dzielenie całkowite

    Dla x = 1,2,3, ... , n
        Jeżeli x <= pivot
            less[x] <- arr[x]
        W innym wypadku
            greater[x] <- arr[x]
    Zwróć qs(less) + [pivot] + qs(greater)
```
</b>
</details>

<a name="box"></a>
## Sortowanie kubełkowe [⬆️](#)
<details open><summary>Rozwiń</summary>

```python
# Not in place

def bucketSort(arr):
    buckets, output = [[] for _ in range(len(arr))], []

    for i in range(len(arr)):
        buckets[int(len(arr) * arr[i])].append(arr[i])

    for i in range(len(buckets)):
        insertion_sort(buckets[i])

        while len(buckets[i]) > 0:
            output.append(buckets[i].pop(0))
    return output


def insertion_sort(arr):
    for i in range(1, len(arr)):
        liczba = arr[i]
        while i > 0 and arr[i - 1] > liczba:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = liczba
```
<b>

```
n <- dlugość tablicy

def BucketSort(arr):
	Dla
```
</b>
</details>

<a name="fast_power"></a>
## Szybkie podnoszenie do potęgi [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#Iterated version

def fast_power(base, power):
    result, m = 1, 1000000007
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % m
        power //= 2
        base = (base * base) % m
    return result
```
<b>

```
mod - reszta z dzielenia
div - dzielenie całkowite

def fast_power(base,power):
	result <- 1
	mod <- 1000000007
	Dopóki power > 0:
		Jeżeli power mod 2 == 1:
			result <- (result * base) mod m
		power <- power div 2
		base = (base * base) mod m
	Zwróć result
```

</details>
</b>

<a name="bisekcja"></a>
## Wyznaczanie miejsc zerowych funkcji metodą połowienia - bisekcja [⬆️](#)
<details><summary>Rozwiń</summary>

```python
def f(x):
    return -4 * x + 2


# bisection(od,do)
def bisection(a, b, precyzja=0.0001):
    if f(a) * f(b) >= 0:
        return None
    c = a
    while b - a >= precyzja:
        c = (a + b) / 2
        if f(c) == 0.0:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c
```
<b>

```
def f(x):
	Zwróć -4 * x + 2


def bisection(a, b, precyzja=0.0001):

	Jeżeli f(a) * f(b) >= 0:
		Zwróć None
	    c <- a
	    Dopóki b - a >= precyzja:
		c -< (a + b) / 2
		Jeżeli f(c) == 0.0:
		    break
		Jeżeli f(c) * f(a) < 0:
		    b <- c
		else:
		    a <- c
	    Zwróć c
```
</b>
</details>

<a name="palindrom"></a>
## Sprawdzanie, czy dany ciąg znaków tworzy palindrom [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#With list and slices

def is_palindrom(string):
    lista = list(string)
    if lista == lista[::-1]:
        return True
    return False
```

```python
#With 2 strings

def is_palindrom(string):
    wynik = ""
    for i in string[::-1]:
        wynik += i
    if wynik == string:
        return True
    return False
```

```python
# Recursive version

def isPalindrom(string):
    if len(string) == 1:
        return True
    if len(string) == 2:
        if string[0] == string[1]:
            return True
        return False
    return isPalindrom(string[1:-1]) if string[0] == string[-1] else False

# This code is contributed by Pixel
```

```python
#Iterated version

def is_palindrom(string, pal):
    if len(string) != len(pal):
        return None

    for i in range(len(string)):
        for j in range(len(pal) - 1, -1, -1):
            if string[i] == pal[i]:
                return True
            return False
```
<b>

```
n - długość tablicy

def is_palindrom(string, pal):
	Dla i = 1, 2, ... n
		Dla j = n, n-1, n-2 ... n-n
			Jeżeli string[i] == pal[i]
				Zwróć Prawdę
			W innym wypadku
				Zwróc Fałsz
```
</b>
</details>

<a name="anagram"></a>
## Sprawdzanie, czy dany ciąg znaków tworzy anagram [⬆️](#)
<details open><summary>Rozwiń</summary>

```python
#With sorting

def is_anagram(string,string2):
    if sorted(string) == sorted(string2):
        return True
    return False
```

```python
def sort_1(string):
    string = list(string)
    for i in range(len(string)):
        for j in range(len(string) - i - 1):
            if string[j] > string[j + 1]:
                string[j], string[j + 1] = string[j + 1], string[j]
    return "".join(string)


def is_anagram(string, pattern):
    if len(string) != len(pattern):
        return False

    string = sort_1(string)
    pattern = sort_1(pattern)
    for i in range(len(string)):
        if string[i] != pattern[i]:
            return False
        return True
```
<b>

```
Pseudocode
```
</b>

```python

def isIn(char, string):
    charInside = False
    for i in range(len(string)):
        if char == string[i]:
            charInside = True
    return True if charInside else False


def isAnagram(string, pattern):
    if len(string) != len(pattern):
        return False

    for i in range(len(string)):
        if not isIn(string[i], pattern):
            return False

    for i in range(len(pattern)):
        if not isIn(pattern[i], string):
            return False
    return True

# This code is contributed by Pixel
```
<b>

```
Pseudocode
```
</b>
</details>

<a name="alfa"></a>
## Porządkowanie alfabetyczne [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#Sortowanie liter bąbelkowo

slowo = "niezdammatury"


def bubble_sort(tab):
    tab = list(tab)
    for i in range(len(tab)):
        for j in range(len(tab) - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j + 1], tab[j] = tab[j], tab[j + 1]
    return "".join(tab)


print(bubble_sort(slowo))
```
</details>

<a name="pattern"></a>
## Wyszukiwanie wzorca w tekście [⬆️](#)
<details><summary>Rozwiń</summary>
	
```py
def is_pattern(tekst, pattern):
    for i in range(len(tekst)):
        j = 0
        while j < len(pattern) and tekst[i + j] == pattern[j]:
            j += 1
        if j > 0 and j == len(pattern):
            return True
    return False
```

<b>

```
pseudocode
```
</b>

</details>

<a name="len"></a>
## Kompresja danych [⬆️](#)

### Prefix free
<details open><summary>Rozwiń</summary>

Raczej nie obowiązuje na maturze, ale kto wie.

Kod jest nazywany "prefix (free) code", jeżeli w systemie nie ma kodu słowa, który byłby prefixem innego kodu słowa.

Załóżmy, że mamy plik z 100,000 znakami, jedyne znaki jakie występują w pliku to: a,b,c,d,e,f i chcemy zmniejszyć rozmiar tego pliku kompresją, gdzie każdy kod znaku ma różną długość.

|                   |   a   |   b   |   c   |   d   |   e   |   f   |
| ----------------: | :---: | :---: | :---: | :---: | :---: | :---: |
|          Częstość |  45   |  13   |  12   |  16   |   9   |   5   |
| Fixed-length code |   0   |  101  |  100  |  111  | 1101  | 1100  |

Plik taki zajmnie (45 * 1 + 13 * 3 + 12 * 3 + 16 * 3 + 9 * 4 + 5 * 4) * 1000 = 224,000 bity

```python
#Iterated version

text = "010111010011111001001100"

cipher = {'0': 'n', '101': 'i', '100': 'm', '111': 'z', '1101': 'e', '1100': 'd', '1001': 'a', '00': ' '}


def decrypt(cipher, text): #brak obsługi błedów, jeżeli zmienna text skonstruowana jest niepoprawnie.
    res = ""
    while text:
        for k in cipher:
            if text.startswith(k):
                res += cipher[k]
                text = text[len(k):]
    return res


to_code = "zdam"


def encrypt(cipher, text):
    res = ""
    for char in text:
        if char in cipher.values():
            for k, v in cipher.items():
                if v == char:
                    res += k
        else:
            res += "-"
    return res


print(decrypt(cipher, text))
print(encrypt(cipher, to_code))
```
</details>

<a name="morse"></a>
## Alfabet Morse’a [⬆️](#)
<details><summary>Rozwiń</summary>

```python
# define coding dict
morseEncode = {
    'a': '.-', 'b': '-...', 'c': '-.-.', ' ': '  ',
    'd': '-..', 'e': '.', 'f': '..-.', '': '',
    'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-',
    'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
}
# swap coding table for decoding dict
morseDecode = {val: key for key, val in morseEncode.items()}
morseDecode.update({'_': ' '})

# define coding function
def morseCode(string, decode=False):
    string = string.lower()
    output = ""
    if not decode:  # then encode
        for char in string:
            output += morseEncode.get(char, '')  # print '*' for unexpected characters
            if char != ' ': output += ' '
    else:
        string = string.replace('  ', ' _ ')
        for char in string.split(' '):
            output += morseDecode.get(char, '')  # print '*' for unexpected codes
    return output

# test
string = "Keep learning"
coded = morseCode(string)
print("Coded:", coded)
decoded = morseCode(coded, decode=True)
print("Decoded:", decoded)

# This code is contributed by Pixel
```
</details>

<a name="atbash"></a>
## Szyfr AtBash[⬆️](#)
<details open><summary>Rozwiń</summary>
	
```python
txt = "Nie zdam maturki elo"


def atbash(txt):
    txt = list(txt)
    for i in range(len(txt)):
        if "A" <= txt[i] <= "Z":  # wielkie litery
            txt[i] = chr(ord("Z") - (ord(txt[i]) - ord("A")))

        if "a" <= txt[i] <= "z":  # małe litery
            txt[i] = chr(ord("z") - (ord(txt[i]) - ord("a")))

        if txt[i] == " ":
            txt[i] = " "

    return "".join(txt)


print(atbash(txt))

```
</details>

<a name="przes"></a>
## Transpozycyjny szyfr przestawieniowy [⬆️](#)
<details><summary>Rozwiń</summary>

Szyfry przestawieniowe dokonują przestawienia znaków w tekście. Tekst zaszyfrowany jest permutacją tekstu jawnego, tzn. zawiera wszystkie znaki tekstu jawnego, jednak ustawione w innej kolejności. Operacja taka nosi nazwę transpozycji.

 
```python
tekst = "InEz Dma amTrUy ,b ojsett rdun aes"  # jump =  3 to decrypt


def przes(tekst, jump):
    tekst = list(tekst)
    for i in range(0, len(tekst)-1, jump):
        tekst[i], tekst[i + 1] = tekst[i + 1], tekst[i]
    return "".join(tekst)


print(przes(tekst, 3))
```
</details>

<a name="cezar"></a>
## Szyfr Cezara [⬆️](#)
<details><summary>Rozwiń</summary>

```python
def koduj(wiadomosc, klucz):
    wynik = ""
    wiadomosc = wiadomosc.upper().strip().replace(" ", "")
    for i in wiadomosc:
        wynik += chr((ord(i) + klucz - 65) % 26 + 65)
    return wynik


def dekoduj(wiadomosc, klucz):
    klucz *= -1
    return koduj(wiadomosc, klucz)
```
<b>

```
wiadomosc <- przechowuje ciąg wielkich liter alfabetu angielskiego, bez spacji i znaków specjalnych
ord() - pokazuje kod znaku w unicode
chr() - pokazuje znak kodu unicode
n <- długość ciągu znaków
klucz <- liczba całkowita z przedziału 1-26

koduj(wiadomosc, klucz):
	wynik = ""
	Dla i = 1, 2, 3 ... n
		wynik += chr((ord(i) + klucz - 65) % 26 + 65)
	Zwróć wynik
```
</b>
</details>
