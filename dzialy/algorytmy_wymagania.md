<a name="main"></a>
<h1 align="center"> Algorytmy wymienione w wymaganiach </h1>

1. __algorytmy na liczbach całkowitych:__
   - ![py] ![c++] ![java] [reprezentacja liczb w dowolnym systemie pozycyjnym, w tym w dwójkowym i szesnastkowym,](#konwersja)
   - ![py] ![c++] ![java] [sprawdzanie, czy liczba jest liczbą pierwszą,](#is_prime)
   - ![py] ![c++] ![java] [sito Eratostenesa,](#sito)
   - ![py] ![c++] ![java] [sprawdzanie, czy liczba jest liczbą doskonałą,](#is_perfect)
   - ![py] ![c++] ![java] [rozkładanie liczby na czynniki pierwsze,](#prime_factors)
   - ![py] ![c++] ![java] [iteracyjna i rekurencyjna realizacja algorytmu Euklidesa + NWW,](#nwd)
   - ![py] ![c++] ![java] [iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego,](#fib)
   - ![py] ![c++] ![java] [wydawanie reszty metodą zachłanną,](#zachlanna)

2. __algorytmy wyszukiwania i porządkowania (sortowania):__
   - ![py] ![c++] ![java] [wyszukiwanie liniowe,](#liniowe)
   - ![py] ![c++] ![java] [wyszukiwanie binarne (iteracyjne i rekurencyjne),](#binarne)
   - ![py] ![c++] ![java] [jednoczesne wyszukiwanie minimum i maksimum,](#minmax)
   - ![py] ![c++] ![java] [bąbelkowy, ](#bob)
   - ![py] ![c++] ![java] [przez wybór, ](#wybor)
   - ![py] ![c++] ![java] [przez wstawianie liniowe lub binarne, ](#lin)
   - ![py] ![c++] ![java] [przez scalanie,](#scalanie)
   - ![py] ![c++] ![java] [szybki,](#fast)
   - ![py] ![c++] ![java] [kubełkowy,](#box)

3. __algorytmy numeryczne__
   - ![py] ![c++] ![java] [szybkie podnoszenie do potęgi,](#fast_power)
   - ![py] ![c++] ![java] [wyznaczanie miejsc zerowych funkcji metodą połowienia,](#bisekcja)
   - ![py] ![c++] ![java] [obliczanie pierwiastka kwadratowego metodą Herona (Newtona),](#heron)
   - ![py] ![c++] ![java] [obliczanie wartości wielomianu za pomocą schematu Hornera,](#horner)
   - ![py] ![c++] ![java] [obliczanie pola obszarów zamkniętych (metoda prostokątów i trapezów),](#pole)

4. __algorytmy na tekstach__
   - ![py] ![c++] ![java] [sprawdzanie, czy dany ciąg znaków tworzy palindrom,](#palindrom)
   - ![py] ![c++] ![java] [sprawdzanie, czy dany ciąg znaków tworzy anagram,](#anagram)
   - ![py] ![c++] ![java] [porządkowanie alfabetyczne, (leksykograficzne)](#alfa)
   - ![py] ![c++] ![java] [wyszukiwanie wzorca w tekście,](#pattern)
   - ![py] ![c++] ![java] [obliczanie wartości wyrażenia w odwrotnej notacji polskiej (ONP),](#onp)

5. __algorytmy kompresji i szyfrowania__
   - kody znaków o zmiennej długości,
	 * ![py] ![c++] ![java] [Kompresja danych (kod prefiksowy)](#len)
	 * ![py] ![c++] ![java] [Kod Huffmana](#huffman)
	 * ![py] ![c++] ![java] [Alfabet Morse’a](#morse)
   - szyfry przestawieniowe,
	 * ![py] ![c++] ![java] [Transpozycyjny](#przes)
   - szyfry podstawieniowe,
	 * ![py] ![c++] ![java] [Szyfr AtBash](#atbash)
	 * ![py] ![c++] ![java] [Szyfr Cezara](#cezar)
	 * ![py] ![c++] ![java] [Szyfr Vigenère’a](#vigenere)
   - szyfr z kluczem jawnym,
	 * ![py] ![c++] ![java] [RSA + rozszerzony algorytm Euklidesa](#rsa)

6. __algorytmy geometryczne__
   - ![py] ![c++] ![java] [sprawdzanie warunku trójkąta,](#trojkat)
   - ![py] ![c++] ![java] [badanie położenia punktów względem prostej,](#punkt_prosta)
   - ![py] ![c++] ![java] [badanie przynależności punktu do odcinka,](#punkt_odcinek)
   - ![py] ![c++] ![java] [przecinanie się odcinków,](#odcinki)
   - ![py] ![c++] ![java] [przynależność punktu do obszaru (wielokąta),](#punkt_wielokat)
   - konstrukcje rekurencyjne,
	 * ![py] ![c++] ![java] [Krzywa Kocha](#koch)
	 * ![py] ![c++] ![java] [Drzewo Pitagorasa](#pitagoras)

<a name="konwersja"></a>
## Systemy liczbowe [⬆️](#)
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


def to_base(n, b):  # to_base(number,base), n >= 0, 2 <= b <= 36
    return BS[n] if n < b else to_base(n // b, b) + BS[n % b]
```

```python
#recursive version DEC --> ANY

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(n, b):  # to_base(number,base), n >= 0, 2 <= b <= 36
    if n < b:
        return BS[n]
    return to_base(n // b, b) + BS[n % b]
```
<b>

```
BS <- "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n - liczba dziesiętna (n >= 0)
b - podstawa systemu (2 <= b <= 36)
mod - reszta z dzielenia
div - dzielenie całkowite

def to_base(n, b):
	Jeżeli n < b:
		Zwróć BS[n]
	W innym wypadku:
		Zwróć to_base(n div b, b) + BS[n mod b]
```
</b>

```python
#iterated version with slices DEC --> ANY

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(n, b):  # to_base(number,base), n >= 0, 2 <= b <= 36
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res += BS[n % b]
        n //= b
    return res[::-1]  # cyfry powstają od końca, więc odwracamy napis
```
<b>

```
BS <- "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n - liczba dziesiętna (n >= 0)
b - podstawa systemu (2 <= b <= 36)
mod - reszta z dzielenia
div - dzielenie całkowite

def to_base(n, b):
	Jeżeli n == 0
		Zwróć "0"
	res <- ""
	Dopóki n > 0
		res <- BS[n mod b] + res
		n <- n div b
	Zwróć res
```
</b>

```python
#manual version ANY --> DEC (schemat Hornera)

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_dec(liczba, b):  # to_dec("number_string", base), np. to_dec("1F", 16) == 31
    wynik = 0
    for znak in liczba.upper():
        wynik = wynik * b + BS.index(znak)  # BS.index(znak) - wartość cyfry
    return wynik
```
<b>

```
liczba[1..n] - napis z cyframi liczby w systemie o podstawie b
wartosc(c) - wartość cyfry c (0..9, A = 10, B = 11, ...)

def to_dec(liczba, b):
	wynik <- 0
	Dla i = 1, 2, ... n
		wynik <- wynik * b + wartosc(liczba[i])
	Zwróć wynik
```
</b>

```cpp
// C++23
#include <cctype>
#include <print>
#include <string>
#include <vector>

const std::string BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

// DEC --> dowolny system, rekurencyjnie (n >= 0, 2 <= b <= 36)
std::string to_base_rek(long long n, int b) {
    if (n < b)
        return std::string(1, BS[n]);
    return to_base_rek(n / b, b) + BS[n % b];
}

// DEC --> dowolny system, iteracyjnie
std::string to_base(long long n, int b) {
    if (n == 0)
        return "0";
    std::string res = "";
    while (n > 0) {
        res = BS[n % b] + res;  // cyfry powstają od końca, więc dopisujemy je z przodu
        n /= b;
    }
    return res;
}

// dowolny system --> DEC (schemat Hornera), np. to_dec("1F", 16) == 31
long long to_dec(const std::string& liczba, int b) {
    long long wynik = 0;
    for (char znak : liczba) {
        char c = std::toupper(static_cast<unsigned char>(znak));
        int cyfra = static_cast<int>(BS.find(c));  // pozycja znaku w BS to wartość cyfry
        wynik = wynik * b + cyfra;
    }
    return wynik;
}

int main() {
    std::vector<long long> liczby = {15, 12, 2, 4, 7, 8, 0, 255};
    for (long long x : liczby)
        std::println("{} -> {} {} {} {}", x, to_base(x, 2), to_base(x, 8), to_base(x, 16), to_base_rek(x, 16));

    std::println("{} {} {} {}", to_dec("1F", 16), to_dec("ff", 16), to_dec("1011", 2), to_dec("Z", 36));
    std::println("{}", to_base(1000000, 36));

    // gotowe narzędzia: std::format zapisuje liczbę w systemie 2, 8 i 16,
    // a std::stoll czyta napis w dowolnym systemie (jak int("777", 8) w Pythonie)
    std::println("wbudowane: {:b} {:o} {:X}", 15, 15, 15);
    std::println("{}", std::stoll("777", nullptr, 8));
}
```

```java
// Java 25
public class SystemyLiczbowe {
    static final String BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // DEC --> dowolny system, rekurencyjnie (n >= 0, 2 <= b <= 36)
    static String toBaseRek(long n, int b) {
        if (n < b)
            return String.valueOf(BS.charAt((int) n));
        return toBaseRek(n / b, b) + BS.charAt((int) (n % b));
    }

    // DEC --> dowolny system, iteracyjnie
    static String toBase(long n, int b) {
        if (n == 0)
            return "0";
        var res = new StringBuilder();
        while (n > 0) {
            res.append(BS.charAt((int) (n % b)));
            n /= b;
        }
        return res.reverse().toString();  // cyfry powstają od końca, więc odwracamy napis
    }

    // dowolny system --> DEC (schemat Hornera), np. toDec("1F", 16) == 31
    static long toDec(String liczba, int b) {
        long wynik = 0;
        for (char znak : liczba.toUpperCase().toCharArray())
            wynik = wynik * b + BS.indexOf(znak);  // pozycja znaku w BS to wartość cyfry
        return wynik;
    }

    public static void main(String[] args) {
        long[] liczby = {15, 12, 2, 4, 7, 8, 0, 255};
        for (long x : liczby)
            System.out.println(x + " -> " + toBase(x, 2) + " " + toBase(x, 8) + " " + toBase(x, 16) + " " + toBaseRek(x, 16));

        System.out.println(toDec("1F", 16) + " " + toDec("ff", 16) + " " + toDec("1011", 2) + " " + toDec("Z", 36));
        System.out.println(toBase(1000000, 36));

        // gotowe metody: Integer.toString(liczba, podstawa) i Integer.parseInt(napis, podstawa)
        System.out.println("wbudowane: " + Integer.toBinaryString(15) + " " + Integer.toOctalString(15) + " "
                + Integer.toHexString(15).toUpperCase());
        System.out.println(Long.parseLong("777", 8));
    }
}
```
</details>

<a name="is_prime"></a>
## Liczba pierwsza [⬆️](#)
<details><summary>Rozwiń</summary>

```python
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
```
<b>

```
x - sprawdzana liczba całkowita
mod - reszta z dzielenia

def is_prime(x):
	Jeżeli x <= 1
		Zwróć Fałsz
	Dla i = 2, 3, ... część całkowita z pierwiastka z x
		Jeżeli x mod i == 0
			Zwróć Fałsz
	Zwróć Prawdę
```
</b>

```cpp
// C++23
#include <print>
#include <vector>

bool is_prime(long long x) {
    if (x <= 1)
        return false;
    for (long long i = 2; i * i <= x; i++)  // i * i <= x, czyli i <= pierwiastek z x
        if (x % i == 0)
            return false;
    return true;
}

int main() {
    std::vector<long long> liczby = {-7, 0, 1, 2, 3, 4, 9, 17, 25, 97, 1000000007};
    for (long long x : liczby)
        std::println("{} {}", x, is_prime(x));
}
```

```java
// Java 25
public class LiczbaPierwsza {
    static boolean isPrime(long x) {
        if (x <= 1)
            return false;
        for (long i = 2; i * i <= x; i++)  // i * i <= x, czyli i <= pierwiastek z x
            if (x % i == 0)
                return false;
        return true;
    }

    public static void main(String[] args) {
        long[] liczby = {-7, 0, 1, 2, 3, 4, 9, 17, 25, 97, 1000000007};
        for (long x : liczby)
            System.out.println(x + " " + isPrime(x));
    }
}
```
</details>

<a name="sito"></a>
## Sito Eratostenesa [⬆️](#)
<details><summary>Rozwiń</summary>

Wyznacza wszystkie liczby pierwsze z przedziału [2, n]. Zaczynamy od tablicy, w której każda liczba jest "kandydatem" na liczbę pierwszą, a następnie dla kolejnych liczb pierwszych i wykreślamy ich wielokrotności (zaczynając od i * i, bo mniejsze wielokrotności zostały już wykreślone).

```python
def sito(n):  # zwraca listę liczb pierwszych <= n
    if n < 2:
        return []
    pierwsza = [True] * (n + 1)
    pierwsza[0] = pierwsza[1] = False
    i = 2
    while i * i <= n:
        if pierwsza[i]:
            for j in range(i * i, n + 1, i):
                pierwsza[j] = False
        i += 1

    wynik = []
    for i in range(2, n + 1):
        if pierwsza[i]:
            wynik.append(i)
    return wynik


print(sito(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```
<b>

```
n - górna granica przedziału
pierwsza[2..n] - tablica wartości logicznych

def sito(n):
	Dla i = 2, 3, ... n
		pierwsza[i] <- Prawda
	i <- 2
	Dopóki i * i <= n
		Jeżeli pierwsza[i]
			j <- i * i
			Dopóki j <= n
				pierwsza[j] <- Fałsz
				j <- j + i
		i <- i + 1
	Zwróć wszystkie i, dla których pierwsza[i] == Prawda
```
</b>

```cpp
// C++23
#include <print>
#include <vector>

std::vector<int> sito(int n) {  // zwraca liczby pierwsze <= n
    if (n < 2)
        return {};
    std::vector<bool> pierwsza(n + 1, true);
    pierwsza[0] = false;
    pierwsza[1] = false;
    for (int i = 2; i * i <= n; i++)
        if (pierwsza[i])
            for (int j = i * i; j <= n; j += i)
                pierwsza[j] = false;

    std::vector<int> wynik;
    for (int i = 2; i <= n; i++)
        if (pierwsza[i])
            wynik.push_back(i);
    return wynik;
}

int main() {
    std::println("{}", sito(30));  // [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    std::println("{} {} {}", sito(0), sito(1), sito(2));
    std::println("{} {}", sito(100).size(), sito(1000000).size());  // 25 78498
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SitoEratostenesa {
    static List<Integer> sito(int n) {  // zwraca liczby pierwsze <= n
        var wynik = new ArrayList<Integer>();
        if (n < 2)
            return wynik;
        var pierwsza = new boolean[n + 1];
        Arrays.fill(pierwsza, true);
        pierwsza[0] = false;
        pierwsza[1] = false;
        for (int i = 2; i * i <= n; i++)
            if (pierwsza[i])
                for (int j = i * i; j <= n; j += i)
                    pierwsza[j] = false;

        for (int i = 2; i <= n; i++)
            if (pierwsza[i])
                wynik.add(i);
        return wynik;
    }

    public static void main(String[] args) {
        System.out.println(sito(30));  // [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        System.out.println(sito(0) + " " + sito(1) + " " + sito(2));
        System.out.println(sito(100).size() + " " + sito(1000000).size());  // 25 78498
    }
}
```
</details>

<a name="is_perfect"></a>
## Liczba doskonała [⬆️](#)
<details><summary>Rozwiń</summary>

Liczba doskonała to liczba naturalna równa sumie swoich dzielników mniejszych od niej samej, np. 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14.

```python
#O(n) version

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
n - sprawdzana liczba naturalna
mod - reszta z dzielenia

def is_perfect(n):
	s <- 1
	Dla i = 2, 3, ... n - 1
		Jeżeli n mod i == 0
			s <- s + i
	Jeżeli n == s oraz n != 1
		Zwróć Prawdę
	W innym wypadku
		Zwróć Fałsz
```
</b>

```python
#O(sqrt(n)) version - dzielniki występują w parach (i, n // i)

def is_perfect(n):
    if n < 2:
        return False
    s = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i != n // i:  # drugi dzielnik z pary (nie dodajemy dwa razy pierwiastka)
                s += n // i
        i += 1
    return s == n
```
<b>

```
n - sprawdzana liczba naturalna
mod - reszta z dzielenia
div - dzielenie całkowite

def is_perfect(n):
	Jeżeli n < 2
		Zwróć Fałsz
	s <- 1
	i <- 2
	Dopóki i * i <= n
		Jeżeli n mod i == 0
			s <- s + i
			Jeżeli i != n div i
				s <- s + n div i
		i <- i + 1
	Zwróć s == n
```
</b>

```cpp
// C++23
#include <print>
#include <vector>

// O(n) - sprawdzamy wszystkie liczby od 2 do n - 1
bool is_perfect_wolno(long long n) {
    long long s = 1;
    for (long long i = 2; i < n; i++)
        if (n % i == 0)
            s += i;
    return n == s && n != 1;
}

// O(sqrt(n)) - dzielniki występują w parach (i, n / i)
bool is_perfect(long long n) {
    if (n < 2)
        return false;
    long long s = 1;
    for (long long i = 2; i * i <= n; i++)
        if (n % i == 0) {
            s += i;
            if (i != n / i)  // drugi dzielnik z pary (nie dodajemy dwa razy pierwiastka)
                s += n / i;
        }
    return s == n;
}

int main() {
    std::vector<long long> wolno, szybko;
    for (long long n = 0; n <= 1000; n++)
        if (is_perfect_wolno(n))
            wolno.push_back(n);
    for (long long n = 0; n <= 10000; n++)
        if (is_perfect(n))
            szybko.push_back(n);
    std::println("{}", wolno);   // [6, 28, 496]
    std::println("{}", szybko);  // [6, 28, 496, 8128]
    std::println("{}", is_perfect(33550336));  // true
}
```

```java
// Java 25
import java.util.ArrayList;

public class LiczbaDoskonala {
    // O(n) - sprawdzamy wszystkie liczby od 2 do n - 1
    static boolean isPerfectWolno(long n) {
        long s = 1;
        for (long i = 2; i < n; i++)
            if (n % i == 0)
                s += i;
        return n == s && n != 1;
    }

    // O(sqrt(n)) - dzielniki występują w parach (i, n / i)
    static boolean isPerfect(long n) {
        if (n < 2)
            return false;
        long s = 1;
        for (long i = 2; i * i <= n; i++)
            if (n % i == 0) {
                s += i;
                if (i != n / i)  // drugi dzielnik z pary (nie dodajemy dwa razy pierwiastka)
                    s += n / i;
            }
        return s == n;
    }

    public static void main(String[] args) {
        var wolno = new ArrayList<Long>();
        var szybko = new ArrayList<Long>();
        for (long n = 0; n <= 1000; n++)
            if (isPerfectWolno(n))
                wolno.add(n);
        for (long n = 0; n <= 10000; n++)
            if (isPerfect(n))
                szybko.add(n);
        System.out.println(wolno);   // [6, 28, 496]
        System.out.println(szybko);  // [6, 28, 496, 8128]
        System.out.println(isPerfect(33550336));  // true
    }
}
```
</details>

<a name="prime_factors"></a>
## Rozkład na czynniki pierwsze [⬆️](#)
<details><summary>Rozwiń</summary>

```python
def prime_factors(n):  # dla n <= 1 zwraca pustą listę
    czynniki = []
    k = 2
    while n > 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)  # albo print(k)
        k += 1
    return czynniki


print(prime_factors(360))  # [2, 2, 2, 3, 3, 5]
```
<b>

```
n - liczba całkowita
div - dzielenie całkowite
mod - reszta z dzielenia

def prime_factors(n):
	czynniki <- []
	k <- 2
	Dopóki n > 1
		Dopóki n mod k == 0
			n <- n div k
			Dodaj k na koniec czynniki
		k <- k + 1
	Zwróć czynniki
```
</b>

```cpp
// C++23
#include <print>
#include <vector>

std::vector<long long> prime_factors(long long n) {  // dla n <= 1 zwraca pusty wektor
    std::vector<long long> czynniki;
    long long k = 2;
    while (n > 1) {
        while (n % k == 0) {
            n /= k;
            czynniki.push_back(k);
        }
        k++;
    }
    return czynniki;
}

int main() {
    std::println("{}", prime_factors(360));  // [2, 2, 2, 3, 3, 5]
    for (long long n : {1LL, 0LL, 97LL, 1024LL, 9699690LL, 600851475143LL})
        std::println("{} {}", n, prime_factors(n));
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;

public class RozkladNaCzynniki {
    static List<Long> primeFactors(long n) {  // dla n <= 1 zwraca pustą listę
        var czynniki = new ArrayList<Long>();
        long k = 2;
        while (n > 1) {
            while (n % k == 0) {
                n /= k;
                czynniki.add(k);
            }
            k++;
        }
        return czynniki;
    }

    public static void main(String[] args) {
        System.out.println(primeFactors(360));  // [2, 2, 2, 3, 3, 5]
        for (long n : new long[] {1, 0, 97, 1024, 9699690, 600851475143L})
            System.out.println(n + " " + primeFactors(n));
    }
}
```
</details>

<a name="nwd"></a>
## NWD i NWW (algorytm Euklidesa) [⬆️](#)
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
mod - reszta z dzielenia

def nwd(a, b):
	Jeżeli b > 0:
		Zwróć nwd(b, a mod b)
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
mod - reszta z dzielenia

def nwd(a, b):
	Dopóki b != 0
		t <- a
		a <- b
		b <- t mod b
	Zwróć a
```
</b>

```python
#Najmniejsza wspólna wielokrotność (korzysta z funkcji nwd powyżej)

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

```cpp
// C++23
#include <numeric>
#include <print>
#include <utility>
#include <vector>

// rekurencyjnie
long long nwd_rek(long long a, long long b) {
    if (b > 0)
        return nwd_rek(b, a % b);
    return a;
}

// iteracyjnie
long long nwd(long long a, long long b) {
    while (b != 0) {
        long long t = a;
        a = b;
        b = t % b;
    }
    return a;
}

// najmniejsza wspólna wielokrotność (najpierw dzielimy, żeby nie przekroczyć zakresu long long)
long long nww(long long a, long long b) {
    return a / nwd(a, b) * b;
}

int main() {
    std::vector<std::pair<long long, long long>> pary = {{48, 18}, {17, 5}, {0, 5}, {5, 0}, {270, 192}, {1071, 462}, {4, 6}};
    for (auto [a, b] : pary)
        std::println("{} {}: nwd {} {} nww {}", a, b, nwd(a, b), nwd_rek(a, b), nww(a, b));

    // gotowe funkcje z <numeric> (C++17)
    std::println("{} {}", std::gcd(48, 18), std::lcm(4, 6));
}
```

```java
// Java 25
public class NwdNww {
    // rekurencyjnie
    static long nwdRek(long a, long b) {
        if (b > 0)
            return nwdRek(b, a % b);
        return a;
    }

    // iteracyjnie
    static long nwd(long a, long b) {
        while (b != 0) {
            long t = a;
            a = b;
            b = t % b;
        }
        return a;
    }

    // najmniejsza wspólna wielokrotność (najpierw dzielimy, żeby nie przekroczyć zakresu long)
    static long nww(long a, long b) {
        return a / nwd(a, b) * b;
    }

    public static void main(String[] args) {
        long[][] pary = {{48, 18}, {17, 5}, {0, 5}, {5, 0}, {270, 192}, {1071, 462}, {4, 6}};
        for (long[] p : pary)
            System.out.println(p[0] + " " + p[1] + ": nwd " + nwd(p[0], p[1]) + " " + nwdRek(p[0], p[1]) + " nww " + nww(p[0], p[1]));

        // dla bardzo dużych liczb: java.math.BigInteger ma gotową metodę gcd
        System.out.println(java.math.BigInteger.valueOf(48).gcd(java.math.BigInteger.valueOf(18)) + " " + nww(4, 6));
    }
}
```
</details>

<a name="fib"></a>
## Liczby Fibonacciego [⬆️](#)
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
n - numer wyrazu ciągu (f(0) = 0, f(1) = 1)

def f(n):
	a <- 0
	b <- 1
	Dla i = 1, 2, ... n
		t <- a
		a <- b
		b <- t + b
	Zwróć a
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

```cpp
// C++23
#include <print>
#include <vector>

// iteracyjnie (long long mieści wyrazy do f(91))
long long f(int n) {
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        long long t = a;
        a = b;
        b = t + b;
    }
    return a;
}

// rekurencyjnie (bardzo wolno dla dużych n - te same wyrazy liczone są wiele razy)
long long f_rek(int n) {
    if (n <= 1)
        return n;
    return f_rek(n - 1) + f_rek(n - 2);
}

int main() {
    std::vector<long long> iter, rek;
    for (int n = 0; n <= 15; n++) {
        iter.push_back(f(n));
        rek.push_back(f_rek(n));
    }
    std::println("{}", iter);  // [0, 1, 1, 2, 3, 5, 8, 13, ...]
    std::println("{}", rek);
    std::println("{}", f(90));  // 2880067194370816120
}
```

```java
// Java 25
import java.util.ArrayList;

public class Fibonacci {
    // iteracyjnie (long mieści wyrazy do f(91))
    static long f(int n) {
        long a = 0, b = 1;
        for (int i = 0; i < n; i++) {
            long t = a;
            a = b;
            b = t + b;
        }
        return a;
    }

    // rekurencyjnie (bardzo wolno dla dużych n - te same wyrazy liczone są wiele razy)
    static long fRek(int n) {
        if (n <= 1)
            return n;
        return fRek(n - 1) + fRek(n - 2);
    }

    public static void main(String[] args) {
        var iter = new ArrayList<Long>();
        var rek = new ArrayList<Long>();
        for (int n = 0; n <= 15; n++) {
            iter.add(f(n));
            rek.add(fRek(n));
        }
        System.out.println(iter);  // [0, 1, 1, 2, 3, 5, 8, 13, ...]
        System.out.println(rek);
        System.out.println(f(90));  // 2880067194370816120
    }
}
```
</details>

<a name="zachlanna"></a>
## Wydawanie reszty (algorytm zachłanny) [⬆️](#)
<details><summary>Rozwiń</summary>

W każdym kroku wybieramy największą monetę, która nie jest większa od kwoty pozostałej do wydania. Dla nominałów takich jak w Polsce (1, 2, 5, 10, ...) daje to najmniejszą liczbę monet, ale dla dowolnych nominałów nie zawsze (np. kwota 6 i monety [1, 3, 4] -> 4 + 1 + 1 zamiast 3 + 3).

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
        if nominal == 0:  # żadna moneta nie mieści się w kwocie - reszty nie da się wydać
            return None
        do_wydania -= nominal

        historia.append(nominal)
        count += 1

    return count, historia


wynik = wydawanie(do_wydania, monety)
if wynik is None:
    print("Nie da się wydać reszty tymi monetami")
else:
    print(f'Resztę wydasz w {wynik[0]} monetach, te monety to {wynik[1]}')
```
<b>

```
do_wydania - kwota do wydania
monety[1..n] - dostępne nominały (każdy w dowolnej ilości)

def wydawanie(do_wydania, monety):
	count <- 0
	historia <- []
	Dopóki do_wydania > 0
		nominal <- 0
		Dla i = 1, 2, ... n
			Jeżeli do_wydania >= monety[i] oraz monety[i] > nominal
				nominal <- monety[i]
		Jeżeli nominal == 0
			Zwróć "nie da się wydać reszty"
		do_wydania <- do_wydania - nominal
		Dodaj nominal na koniec historia
		count <- count + 1
	Zwróć count, historia
```
</b>

```cpp
// C++23
#include <optional>
#include <print>
#include <vector>

// zwraca listę wydanych monet albo std::nullopt, gdy reszty nie da się wydać
std::optional<std::vector<int>> wydawanie(int do_wydania, const std::vector<int>& monety) {
    std::vector<int> historia;
    while (do_wydania > 0) {
        int nominal = 0;
        for (int moneta : monety)
            if (do_wydania >= moneta && moneta > nominal)
                nominal = moneta;
        if (nominal == 0)  // żadna moneta nie mieści się w kwocie - reszty nie da się wydać
            return std::nullopt;
        do_wydania -= nominal;
        historia.push_back(nominal);
    }
    return historia;  // liczba monet to historia.size()
}

void pokaz(int do_wydania, const std::vector<int>& monety) {
    auto wynik = wydawanie(do_wydania, monety);
    if (!wynik)
        std::println("Nie da się wydać reszty tymi monetami");
    else
        std::println("Resztę wydasz w {} monetach, te monety to {}", wynik->size(), *wynik);
}

int main() {
    pokaz(6, {1, 2, 5});  // 2 monety: [5, 1]
    pokaz(6, {1, 3, 4});  // 3 monety: [4, 1, 1], choć wystarczą 2 (3 + 3)
    pokaz(3, {2});
    pokaz(0, {1, 2, 5});
    pokaz(289, {1, 2, 5, 10, 20, 50, 100, 200});
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class WydawanieReszty {
    // zwraca listę wydanych monet albo Optional.empty(), gdy reszty nie da się wydać
    static Optional<List<Integer>> wydawanie(int doWydania, List<Integer> monety) {
        var historia = new ArrayList<Integer>();
        while (doWydania > 0) {
            int nominal = 0;
            for (int moneta : monety)
                if (doWydania >= moneta && moneta > nominal)
                    nominal = moneta;
            if (nominal == 0)  // żadna moneta nie mieści się w kwocie - reszty nie da się wydać
                return Optional.empty();
            doWydania -= nominal;
            historia.add(nominal);
        }
        return Optional.of(historia);  // liczba monet to historia.size()
    }

    static void pokaz(int doWydania, List<Integer> monety) {
        var wynik = wydawanie(doWydania, monety);
        if (wynik.isEmpty())
            System.out.println("Nie da się wydać reszty tymi monetami");
        else
            System.out.println("Resztę wydasz w " + wynik.get().size() + " monetach, te monety to " + wynik.get());
    }

    public static void main(String[] args) {
        pokaz(6, List.of(1, 2, 5));  // 2 monety: [5, 1]
        pokaz(6, List.of(1, 3, 4));  // 3 monety: [4, 1, 1], choć wystarczą 2 (3 + 3)
        pokaz(3, List.of(2));
        pokaz(0, List.of(1, 2, 5));
        pokaz(289, List.of(1, 2, 5, 10, 20, 50, 100, 200));
    }
}
```
</details>

<a name="liniowe"></a>
## Wyszukiwanie liniowe [⬆️](#)
<details><summary>Rozwiń</summary>

Sprawdzamy po kolei wszystkie elementy tablicy (tablica nie musi być posortowana). Złożoność O(n).

```python
def linear_search(tab, x):  # indeks pierwszego wystąpienia x albo -1
    for i in range(len(tab)):
        if tab[i] == x:
            return i
    return -1
```
<b>

```
tab[1..n] - przeszukiwana tablica
x - szukana wartość

def linear_search(tab, x):
	Dla i = 1, 2, ... n
		Jeżeli tab[i] == x
			Zwróć i
	Zwróć -1
```
</b>

```cpp
// C++23
#include <print>
#include <vector>

int linear_search(const std::vector<int>& tab, int x) {  // indeks pierwszego wystąpienia x albo -1
    for (int i = 0; i < std::ssize(tab); i++)
        if (tab[i] == x)
            return i;
    return -1;
}

int main() {
    std::vector<int> tab = {5, 3, 8, 3, 1};
    for (int x : {3, 1, 5, 7})
        std::println("{} {}", x, linear_search(tab, x));  // 3 -> 1, 1 -> 4, 5 -> 0, 7 -> -1
    std::println("{}", linear_search({}, 1));             // pusta tablica -> -1
}
```

```java
// Java 25
public class WyszukiwanieLiniowe {
    static int linearSearch(int[] tab, int x) {  // indeks pierwszego wystąpienia x albo -1
        for (int i = 0; i < tab.length; i++)
            if (tab[i] == x)
                return i;
        return -1;
    }

    public static void main(String[] args) {
        int[] tab = {5, 3, 8, 3, 1};
        for (int x : new int[] {3, 1, 5, 7})
            System.out.println(x + " " + linearSearch(tab, x));  // 3 -> 1, 1 -> 4, 5 -> 0, 7 -> -1
        System.out.println(linearSearch(new int[0], 1));        // pusta tablica -> -1
    }
}
```
</details>

<a name="binarne"></a>
## Wyszukiwanie binarne [⬆️](#)
<details><summary>Rozwiń</summary>

Działa tylko dla tablicy posortowanej rosnąco. W każdym kroku porównujemy szukaną wartość ze środkowym elementem i odrzucamy połowę przedziału. Złożoność O(log n).

```python
#Iterated version

def binary_search(tab, x):  # indeks elementu równego x albo -1
    lewy, prawy = 0, len(tab) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if tab[srodek] == x:
            return srodek
        elif tab[srodek] < x:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1
```
<b>

```
tab[1..n] - tablica posortowana rosnąco
x - szukana wartość
div - dzielenie całkowite

def binary_search(tab, x):
	lewy <- 1
	prawy <- n
	Dopóki lewy <= prawy
		srodek <- (lewy + prawy) div 2
		Jeżeli tab[srodek] == x
			Zwróć srodek
		Jeżeli tab[srodek] < x
			lewy <- srodek + 1
		W innym wypadku
			prawy <- srodek - 1
	Zwróć -1
```
</b>

```python
#Recursive version - wywołanie: binary_search_rek(tab, x, 0, len(tab) - 1)

def binary_search_rek(tab, x, lewy, prawy):
    if lewy > prawy:
        return -1
    srodek = (lewy + prawy) // 2
    if tab[srodek] == x:
        return srodek
    if tab[srodek] < x:
        return binary_search_rek(tab, x, srodek + 1, prawy)
    return binary_search_rek(tab, x, lewy, srodek - 1)
```
<b>

```
tab[1..n] - tablica posortowana rosnąco
div - dzielenie całkowite
wywołanie: binary_search_rek(tab, x, 1, n)

def binary_search_rek(tab, x, lewy, prawy):
	Jeżeli lewy > prawy
		Zwróć -1
	srodek <- (lewy + prawy) div 2
	Jeżeli tab[srodek] == x
		Zwróć srodek
	Jeżeli tab[srodek] < x
		Zwróć binary_search_rek(tab, x, srodek + 1, prawy)
	W innym wypadku
		Zwróć binary_search_rek(tab, x, lewy, srodek - 1)
```
</b>

```cpp
// C++23
#include <print>
#include <vector>

// iteracyjnie - zwraca indeks elementu równego x albo -1 (tab posortowana rosnąco)
int binary_search(const std::vector<int>& tab, int x) {
    int lewy = 0, prawy = std::ssize(tab) - 1;
    while (lewy <= prawy) {
        int srodek = (lewy + prawy) / 2;
        if (tab[srodek] == x)
            return srodek;
        else if (tab[srodek] < x)
            lewy = srodek + 1;
        else
            prawy = srodek - 1;
    }
    return -1;
}

// rekurencyjnie - wywołanie: binary_search_rek(tab, x, 0, tab.size() - 1)
int binary_search_rek(const std::vector<int>& tab, int x, int lewy, int prawy) {
    if (lewy > prawy)
        return -1;
    int srodek = (lewy + prawy) / 2;
    if (tab[srodek] == x)
        return srodek;
    if (tab[srodek] < x)
        return binary_search_rek(tab, x, srodek + 1, prawy);
    return binary_search_rek(tab, x, lewy, srodek - 1);
}

int main() {
    std::vector<int> tab = {1, 3, 5, 7, 9, 11};
    std::vector<int> iter, rek;
    for (int x = 0; x <= 12; x++) {
        iter.push_back(binary_search(tab, x));
        rek.push_back(binary_search_rek(tab, x, 0, std::ssize(tab) - 1));
    }
    std::println("{}", iter);  // [-1, 0, -1, 1, -1, 2, ...]
    std::println("{}", rek);
    std::println("{}", binary_search({}, 5));  // -1
}
```

```java
// Java 25
import java.util.ArrayList;

public class WyszukiwanieBinarne {
    // iteracyjnie - zwraca indeks elementu równego x albo -1 (tab posortowana rosnąco)
    static int binarySearch(int[] tab, int x) {
        int lewy = 0, prawy = tab.length - 1;
        while (lewy <= prawy) {
            int srodek = (lewy + prawy) / 2;
            if (tab[srodek] == x)
                return srodek;
            else if (tab[srodek] < x)
                lewy = srodek + 1;
            else
                prawy = srodek - 1;
        }
        return -1;
    }

    // rekurencyjnie - wywołanie: binarySearchRek(tab, x, 0, tab.length - 1)
    static int binarySearchRek(int[] tab, int x, int lewy, int prawy) {
        if (lewy > prawy)
            return -1;
        int srodek = (lewy + prawy) / 2;
        if (tab[srodek] == x)
            return srodek;
        if (tab[srodek] < x)
            return binarySearchRek(tab, x, srodek + 1, prawy);
        return binarySearchRek(tab, x, lewy, srodek - 1);
    }

    public static void main(String[] args) {
        int[] tab = {1, 3, 5, 7, 9, 11};
        var iter = new ArrayList<Integer>();
        var rek = new ArrayList<Integer>();
        for (int x = 0; x <= 12; x++) {
            iter.add(binarySearch(tab, x));
            rek.add(binarySearchRek(tab, x, 0, tab.length - 1));
        }
        System.out.println(iter);  // [-1, 0, -1, 1, -1, 2, ...]
        System.out.println(rek);
        System.out.println(binarySearch(new int[0], 5));  // -1
    }
}
```
</details>

<a name="minmax"></a>
## Minimum i maksimum jednocześnie [⬆️](#)
<details><summary>Rozwiń</summary>

Wersja naiwna porównuje każdy element osobno z minimum i z maksimum, czyli wykonuje ok. 2n porównań. Metoda "parami" bierze po dwa elementy, najpierw porównuje je ze sobą, a potem mniejszy z minimum, a większy z maksimum - 3 porównania na 2 elementy, czyli ok. 3n/2 porównań.

```python
#Wersja naiwna (ok. 2n porównań)

def min_max_naiwnie(tab):
    if len(tab) == 0:
        return None
    mini = maks = tab[0]
    for i in range(1, len(tab)):
        if tab[i] < mini:
            mini = tab[i]
        if tab[i] > maks:
            maks = tab[i]
    return mini, maks
```

```python
#Metoda "parami" (ok. 3n/2 porównań)

def min_max(tab):  # zwraca (minimum, maksimum) albo None dla pustej tablicy
    n = len(tab)
    if n == 0:
        return None
    if n % 2 == 1:  # nieparzysta liczba elementów - pierwszy element jest i min, i max
        mini = maks = tab[0]
        start = 1
    else:  # parzysta - pierwszą parę porównujemy ze sobą
        if tab[0] < tab[1]:
            mini, maks = tab[0], tab[1]
        else:
            mini, maks = tab[1], tab[0]
        start = 2

    for i in range(start, n - 1, 2):
        if tab[i] < tab[i + 1]:
            mniejszy, wiekszy = tab[i], tab[i + 1]
        else:
            mniejszy, wiekszy = tab[i + 1], tab[i]
        if mniejszy < mini:
            mini = mniejszy
        if wiekszy > maks:
            maks = wiekszy
    return mini, maks
```
<b>

```
tab[1..n] - tablica liczb (n >= 1)
mod - reszta z dzielenia

def min_max(tab):
	Jeżeli n mod 2 == 1
		mini <- tab[1]
		maks <- tab[1]
		i <- 2
	W innym wypadku
		Jeżeli tab[1] < tab[2]
			mini <- tab[1]
			maks <- tab[2]
		W innym wypadku
			mini <- tab[2]
			maks <- tab[1]
		i <- 3
	Dopóki i < n
		Jeżeli tab[i] < tab[i + 1]
			mniejszy <- tab[i]
			wiekszy <- tab[i + 1]
		W innym wypadku
			mniejszy <- tab[i + 1]
			wiekszy <- tab[i]
		Jeżeli mniejszy < mini
			mini <- mniejszy
		Jeżeli wiekszy > maks
			maks <- wiekszy
		i <- i + 2
	Zwróć mini, maks
```
</b>

```cpp
// C++23
#include <optional>
#include <print>
#include <utility>
#include <vector>

// wersja naiwna (ok. 2n porównań); dla pustej tablicy zwraca std::nullopt
std::optional<std::pair<int, int>> min_max_naiwnie(const std::vector<int>& tab) {
    if (tab.empty())
        return std::nullopt;
    int mini = tab[0], maks = tab[0];
    for (std::size_t i = 1; i < tab.size(); i++) {
        if (tab[i] < mini)
            mini = tab[i];
        if (tab[i] > maks)
            maks = tab[i];
    }
    return std::pair{mini, maks};
}

// metoda "parami" (ok. 3n/2 porównań)
std::optional<std::pair<int, int>> min_max(const std::vector<int>& tab) {
    int n = std::ssize(tab);
    if (n == 0)
        return std::nullopt;
    int mini, maks, start;
    if (n % 2 == 1) {  // nieparzysta liczba elementów - pierwszy element jest i min, i max
        mini = maks = tab[0];
        start = 1;
    } else {           // parzysta - pierwszą parę porównujemy ze sobą
        if (tab[0] < tab[1]) {
            mini = tab[0];
            maks = tab[1];
        } else {
            mini = tab[1];
            maks = tab[0];
        }
        start = 2;
    }
    for (int i = start; i < n - 1; i += 2) {
        int mniejszy = tab[i], wiekszy = tab[i + 1];
        if (mniejszy > wiekszy)
            std::swap(mniejszy, wiekszy);
        if (mniejszy < mini)
            mini = mniejszy;
        if (wiekszy > maks)
            maks = wiekszy;
    }
    return std::pair{mini, maks};
}

int main() {
    std::vector<std::vector<int>> testy = {{3, 1, 4, 1, 5, 9, 2, 6}, {7}, {2, 1}, {5, 5, 5}, {-3, 10, -20, 4, 0}, {}};
    for (const auto& tab : testy) {
        auto w1 = min_max_naiwnie(tab);
        auto w2 = min_max(tab);
        if (w2)
            std::println("{} {}", *w1, *w2);  // pary wypisują się jako (min, max)
        else
            std::println("brak");
    }
}
```

```java
// Java 25
import java.util.Optional;

public class MinMax {
    record Wynik(int mini, int maks) {
        @Override
        public String toString() {
            return "(" + mini + ", " + maks + ")";
        }
    }

    // wersja naiwna (ok. 2n porównań); dla pustej tablicy zwraca Optional.empty()
    static Optional<Wynik> minMaxNaiwnie(int[] tab) {
        if (tab.length == 0)
            return Optional.empty();
        int mini = tab[0], maks = tab[0];
        for (int i = 1; i < tab.length; i++) {
            if (tab[i] < mini)
                mini = tab[i];
            if (tab[i] > maks)
                maks = tab[i];
        }
        return Optional.of(new Wynik(mini, maks));
    }

    // metoda "parami" (ok. 3n/2 porównań)
    static Optional<Wynik> minMax(int[] tab) {
        int n = tab.length;
        if (n == 0)
            return Optional.empty();
        int mini, maks, start;
        if (n % 2 == 1) {  // nieparzysta liczba elementów - pierwszy element jest i min, i max
            mini = maks = tab[0];
            start = 1;
        } else {           // parzysta - pierwszą parę porównujemy ze sobą
            mini = Math.min(tab[0], tab[1]);
            maks = Math.max(tab[0], tab[1]);
            start = 2;
        }
        for (int i = start; i < n - 1; i += 2) {
            int mniejszy, wiekszy;
            if (tab[i] < tab[i + 1]) {
                mniejszy = tab[i];
                wiekszy = tab[i + 1];
            } else {
                mniejszy = tab[i + 1];
                wiekszy = tab[i];
            }
            if (mniejszy < mini)
                mini = mniejszy;
            if (wiekszy > maks)
                maks = wiekszy;
        }
        return Optional.of(new Wynik(mini, maks));
    }

    public static void main(String[] args) {
        int[][] testy = {{3, 1, 4, 1, 5, 9, 2, 6}, {7}, {2, 1}, {5, 5, 5}, {-3, 10, -20, 4, 0}, {}};
        for (int[] tab : testy) {
            var w1 = minMaxNaiwnie(tab);
            var w2 = minMax(tab);
            if (w2.isPresent())
                System.out.println(w1.get() + " " + w2.get());
            else
                System.out.println("brak");
        }
    }
}
```
</details>

<a name="bob"></a>
## Sortowanie bąbelkowe [⬆️](#)
<details><summary>Rozwiń</summary>

Sortuje rosnąco (zamiana, gdy tab[j] > tab[j + 1]).

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
A[1..n] - sortowana tablica

Dla i = 1, 2, ... n
	Dla j = 1, 2, ... n – i
		Jeżeli A[j] > A[j + 1]
			t <- A[j + 1]
			A[j + 1] <- A[j]
			A[j] <- t
```
</b>

```py
# Wersja zoptymalizowana - kończy pracę, gdy w całym przebiegu nie było żadnej zamiany
arr = [1,1,1,1,1,1,2]


def swap(arr,x,y): #to albo swap jak wyżej
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

def bubblesort(arr):

    for i in range(len(arr)):
        issorted = True
        for j in range(1,len(arr)-i):
            if arr[j] < arr[j-1]:
                swap(arr,j ,j-1)
                issorted = False
        if issorted:
            break

bubblesort(arr)
print(arr)
```
<b>

```
A[1..n] - sortowana tablica

Dla i = 1, 2, ... n
	posortowana <- Prawda
	Dla j = 2, 3, ... n – i + 1
		Jeżeli A[j] < A[j - 1]
			Zamień A[j] z A[j - 1]
			posortowana <- Fałsz
	Jeżeli posortowana
		Zakończ sortowanie
```
</b>

```cpp
// C++23
#include <print>
#include <utility>
#include <vector>

// w miejscu
void bubble_sort(std::vector<int>& tab) {
    int n = std::ssize(tab);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (tab[j] > tab[j + 1])
                std::swap(tab[j], tab[j + 1]);
}

// wersja zoptymalizowana - kończy pracę, gdy w całym przebiegu nie było żadnej zamiany
void bubble_sort_opt(std::vector<int>& arr) {
    int n = std::ssize(arr);
    for (int i = 0; i < n; i++) {
        bool issorted = true;
        for (int j = 1; j < n - i; j++)
            if (arr[j] < arr[j - 1]) {
                std::swap(arr[j], arr[j - 1]);
                issorted = false;
            }
        if (issorted)
            break;
    }
}

int main() {
    std::vector<std::vector<int>> testy = {{5, 1, 4, 2, 8, 0, -3}, {1, 1, 1, 1, 1, 1, 2}, {}, {42}, {3, 2, 1}};
    for (const auto& t : testy) {
        auto a = t, b = t;  // kopie, bo sortujemy w miejscu
        bubble_sort(a);
        bubble_sort_opt(b);
        std::println("{} {}", a, b);
    }
}
```

```java
// Java 25
import java.util.Arrays;

public class SortowanieBabelkowe {
    // w miejscu
    static void bubbleSort(int[] tab) {
        int n = tab.length;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n - i - 1; j++)
                if (tab[j] > tab[j + 1]) {
                    int t = tab[j];
                    tab[j] = tab[j + 1];
                    tab[j + 1] = t;
                }
    }

    // wersja zoptymalizowana - kończy pracę, gdy w całym przebiegu nie było żadnej zamiany
    static void bubbleSortOpt(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            boolean issorted = true;
            for (int j = 1; j < n - i; j++)
                if (arr[j] < arr[j - 1]) {
                    int t = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = t;
                    issorted = false;
                }
            if (issorted)
                break;
        }
    }

    public static void main(String[] args) {
        int[][] testy = {{5, 1, 4, 2, 8, 0, -3}, {1, 1, 1, 1, 1, 1, 2}, {}, {42}, {3, 2, 1}};
        for (int[] t : testy) {
            int[] a = t.clone(), b = t.clone();  // kopie, bo sortujemy w miejscu
            bubbleSort(a);
            bubbleSortOpt(b);
            System.out.println(Arrays.toString(a) + " " + Arrays.toString(b));
        }
    }
}
```
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
A[1..n] - sortowana tablica
n - ilość liczb

Dla i = 1, 2, ... n
	mini <- i
	Dla j = i + 1, ... n
		Jeżeli A[mini] > A[j]
			mini <- j
	t <- A[i]
	A[i] <- A[mini]
	A[mini] <- t
```
</b>

```cpp
// C++23
#include <print>
#include <utility>
#include <vector>

// w miejscu
void selection_sort(std::vector<int>& tab) {
    int n = std::ssize(tab);
    for (int i = 0; i < n; i++) {
        int mini = i;  // indeks najmniejszego elementu w tab[i..n-1]
        for (int j = i + 1; j < n; j++)
            if (tab[mini] > tab[j])
                mini = j;
        std::swap(tab[i], tab[mini]);
    }
}

int main() {
    std::vector<std::vector<int>> testy = {{64, 25, 12, 22, 11}, {5, 1, 4, 2, 8, 0, -3}, {}, {42}, {2, 2, 1, 1}};
    for (auto t : testy) {
        selection_sort(t);
        std::println("{}", t);
    }
}
```

```java
// Java 25
import java.util.Arrays;

public class SortowaniePrzezWybor {
    // w miejscu
    static void selectionSort(int[] tab) {
        for (int i = 0; i < tab.length; i++) {
            int mini = i;  // indeks najmniejszego elementu w tab[i..n-1]
            for (int j = i + 1; j < tab.length; j++)
                if (tab[mini] > tab[j])
                    mini = j;
            int t = tab[i];
            tab[i] = tab[mini];
            tab[mini] = t;
        }
    }

    public static void main(String[] args) {
        int[][] testy = {{64, 25, 12, 22, 11}, {5, 1, 4, 2, 8, 0, -3}, {}, {42}, {2, 2, 1, 1}};
        for (int[] t : testy) {
            selectionSort(t);
            System.out.println(Arrays.toString(t));
        }
    }
}
```
</details>

<a name="lin"></a>
## Sortowanie przez wstawianie [⬆️](#)
<details><summary>Rozwiń</summary>

### Wstawianie liniowe
Kolejny element wstawiamy do posortowanej już części tablicy, przesuwając większe elementy o jedno miejsce w prawo.

```python
#In place

def insertion_sort(A):
    for i in range(1, len(A)):
        liczba = A[i]
        j = i
        while j > 0 and A[j - 1] > liczba:
            A[j] = A[j - 1]
            j -= 1
        A[j] = liczba
```
<b>

```
n - długość tablicy
A[1..n] - sortowana tablica

Dla i = 2, 3, ... n
	liczba <- A[i]
	j <- i
	Dopóki j > 1 oraz A[j - 1] > liczba
		A[j] <- A[j - 1]
		j <- j - 1
	A[j] <- liczba
```
</b>

```cpp
// C++23
#include <print>
#include <vector>

// w miejscu
void insertion_sort(std::vector<int>& A) {
    for (int i = 1; i < std::ssize(A); i++) {
        int liczba = A[i];
        int j = i;
        while (j > 0 && A[j - 1] > liczba) {  // przesuwamy większe elementy w prawo
            A[j] = A[j - 1];
            j--;
        }
        A[j] = liczba;
    }
}

int main() {
    std::vector<std::vector<int>> testy = {{12, 11, 13, 5, 6}, {5, 1, 4, 2, 8, 0, -3}, {}, {42}, {3, 3, 2, 1}};
    for (auto t : testy) {
        insertion_sort(t);
        std::println("{}", t);
    }
}
```

```java
// Java 25
import java.util.Arrays;

public class WstawianieLiniowe {
    // w miejscu
    static void insertionSort(int[] A) {
        for (int i = 1; i < A.length; i++) {
            int liczba = A[i];
            int j = i;
            while (j > 0 && A[j - 1] > liczba) {  // przesuwamy większe elementy w prawo
                A[j] = A[j - 1];
                j--;
            }
            A[j] = liczba;
        }
    }

    public static void main(String[] args) {
        int[][] testy = {{12, 11, 13, 5, 6}, {5, 1, 4, 2, 8, 0, -3}, {}, {42}, {3, 3, 2, 1}};
        for (int[] t : testy) {
            insertionSort(t);
            System.out.println(Arrays.toString(t));
        }
    }
}
```

### Wstawianie binarne
Miejsce dla kolejnego elementu w posortowanej części tablicy szukamy wyszukiwaniem binarnym (mniej porównań), a potem przesuwamy elementy w prawo i wstawiamy go.

```python
#In place

def binary_insertion_sort(A):
    for i in range(1, len(A)):
        liczba = A[i]
        # szukamy binarnie pierwszej pozycji w A[0..i-1], na której stoi element > liczba
        lewy, prawy = 0, i
        while lewy < prawy:
            srodek = (lewy + prawy) // 2
            if A[srodek] <= liczba:
                lewy = srodek + 1
            else:
                prawy = srodek
        # przesuwamy A[lewy..i-1] o jedno miejsce w prawo
        for j in range(i, lewy, -1):
            A[j] = A[j - 1]
        A[lewy] = liczba
```
<b>

```
n - długość tablicy
A[1..n] - sortowana tablica
div - dzielenie całkowite

Dla i = 2, 3, ... n
	liczba <- A[i]
	lewy <- 1
	prawy <- i
	Dopóki lewy < prawy
		srodek <- (lewy + prawy) div 2
		Jeżeli A[srodek] <= liczba
			lewy <- srodek + 1
		W innym wypadku
			prawy <- srodek
	Dla j = i, i - 1, ... lewy + 1
		A[j] <- A[j - 1]
	A[lewy] <- liczba
```
</b>

```cpp
// C++23
#include <print>
#include <vector>

// w miejscu
void binary_insertion_sort(std::vector<int>& A) {
    for (int i = 1; i < std::ssize(A); i++) {
        int liczba = A[i];
        // szukamy binarnie pierwszej pozycji w A[0..i-1], na której stoi element > liczba
        // (to samo robi std::upper_bound(A.begin(), A.begin() + i, liczba))
        int lewy = 0, prawy = i;
        while (lewy < prawy) {
            int srodek = (lewy + prawy) / 2;
            if (A[srodek] <= liczba)
                lewy = srodek + 1;
            else
                prawy = srodek;
        }
        // przesuwamy A[lewy..i-1] o jedno miejsce w prawo
        for (int j = i; j > lewy; j--)
            A[j] = A[j - 1];
        A[lewy] = liczba;
    }
}

int main() {
    std::vector<std::vector<int>> testy = {{12, 11, 13, 5, 6}, {5, 1, 4, 2, 8, 0, -3}, {}, {42}, {3, 3, 2, 1}};
    for (auto t : testy) {
        binary_insertion_sort(t);
        std::println("{}", t);
    }
}
```

```java
// Java 25
import java.util.Arrays;

public class WstawianieBinarne {
    // w miejscu
    static void binaryInsertionSort(int[] A) {
        for (int i = 1; i < A.length; i++) {
            int liczba = A[i];
            // szukamy binarnie pierwszej pozycji w A[0..i-1], na której stoi element > liczba
            int lewy = 0, prawy = i;
            while (lewy < prawy) {
                int srodek = (lewy + prawy) / 2;
                if (A[srodek] <= liczba)
                    lewy = srodek + 1;
                else
                    prawy = srodek;
            }
            // przesuwamy A[lewy..i-1] o jedno miejsce w prawo
            for (int j = i; j > lewy; j--)
                A[j] = A[j - 1];
            A[lewy] = liczba;
        }
    }

    public static void main(String[] args) {
        int[][] testy = {{12, 11, 13, 5, 6}, {5, 1, 4, 2, 8, 0, -3}, {}, {42}, {3, 3, 2, 1}};
        for (int[] t : testy) {
            binaryInsertionSort(t);
            System.out.println(Arrays.toString(t));
        }
    }
}
```
</details>

<a name="scalanie"></a>
## Sortowanie przez scalanie [⬆️](#)
<details><summary>Rozwiń</summary>

```python
#In place (sortuje przekazaną tablicę, dodatkowo ją zwraca)

def merge_sort(tab):
    if len(tab) < 2:
        return tab

    i = j = k = 0
    mid = len(tab) // 2
    L, R = tab[:mid], tab[mid:]
    merge_sort(L)
    merge_sort(R)

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
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

    return tab
```
<b>

```
tab[1..n] - sortowana tablica
n - długość tablicy
dł() - długość tablicy
div - dzielenie całkowite

def merge_sort(tab):
	Jeżeli n < 2
		Zwróć tab
	mid <- n div 2
	L <- tab[1..mid]
	R <- tab[mid + 1..n]
	merge_sort(L)
	merge_sort(R)

	i <- 1
	j <- 1
	k <- 1
	Dopóki i <= dł(L) oraz j <= dł(R)
		Jeżeli L[i] <= R[j]
			tab[k] <- L[i]
			i <- i + 1
		W innym wypadku
			tab[k] <- R[j]
			j <- j + 1
		k <- k + 1

	Dopóki i <= dł(L)
		tab[k] <- L[i]
		i <- i + 1
		k <- k + 1

	Dopóki j <= dł(R)
		tab[k] <- R[j]
		j <- j + 1
		k <- k + 1
	Zwróć tab
```
</b>

```cpp
// C++23
#include <print>
#include <vector>

// w miejscu (sortuje przekazany wektor)
void merge_sort(std::vector<int>& tab) {
    if (tab.size() < 2)
        return;

    std::size_t mid = tab.size() / 2;
    std::vector<int> L(tab.begin(), tab.begin() + mid);  // lewa połowa
    std::vector<int> R(tab.begin() + mid, tab.end());    // prawa połowa
    merge_sort(L);
    merge_sort(R);

    std::size_t i = 0, j = 0, k = 0;
    while (i < L.size() && j < R.size()) {  // scalanie dwóch posortowanych połówek
        if (L[i] <= R[j]) {
            tab[k] = L[i];
            i++;
        } else {
            tab[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < L.size()) {
        tab[k] = L[i];
        i++;
        k++;
    }
    while (j < R.size()) {
        tab[k] = R[j];
        j++;
        k++;
    }
}

int main() {
    std::vector<std::vector<int>> testy = {{38, 27, 43, 3, 9, 82, 10}, {5, 1, 4, 2, 8, 0, -3}, {}, {42}, {2, 1, 2, 1}};
    for (auto t : testy) {
        merge_sort(t);
        std::println("{}", t);
    }
}
```

```java
// Java 25
import java.util.Arrays;

public class SortowaniePrzezScalanie {
    // w miejscu (sortuje przekazaną tablicę)
    static void mergeSort(int[] tab) {
        if (tab.length < 2)
            return;

        int mid = tab.length / 2;
        int[] L = Arrays.copyOfRange(tab, 0, mid);           // lewa połowa
        int[] R = Arrays.copyOfRange(tab, mid, tab.length);  // prawa połowa
        mergeSort(L);
        mergeSort(R);

        int i = 0, j = 0, k = 0;
        while (i < L.length && j < R.length) {  // scalanie dwóch posortowanych połówek
            if (L[i] <= R[j]) {
                tab[k] = L[i];
                i++;
            } else {
                tab[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < L.length) {
            tab[k] = L[i];
            i++;
            k++;
        }
        while (j < R.length) {
            tab[k] = R[j];
            j++;
            k++;
        }
    }

    public static void main(String[] args) {
        int[][] testy = {{38, 27, 43, 3, 9, 82, 10}, {5, 1, 4, 2, 8, 0, -3}, {}, {42}, {2, 1, 2, 1}};
        for (int[] t : testy) {
            mergeSort(t);
            System.out.println(Arrays.toString(t));
        }
    }
}
```
</details>

<a name="fast"></a>
## Sortowanie szybkie [⬆️](#)
<details><summary>Rozwiń</summary>

```python
def quicksort(t):
    # jeżeli tablica jest pusta lub ma jeden element, to nie trzeba nic robić, można ją zwrócić.
    if len(t) <= 1:
        return t

    # wybierasz pivot (tutaj na końcu)
    pivot = t[-1]
    smaller = []
    greater = []

    # wszystkie mniejsze lub równe wartości od pivota idą do listy smaller a większe do greater.
    # len(t) - 1, bo pracujemy na elementach bez ostatniego, którym jest pivot.
    for i in range(0, len(t) - 1):
        if t[i] <= pivot:
            smaller.append(t[i])
        else:
            greater.append(t[i])

    # zwracasz tablicę, gdzie wszystkie mniejsze wartości są po lewej, a większe po prawej od pivota,
    # a pivot trafia na miejsce końcowe w tablicy wyjściowej.
    return quicksort(smaller) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    arr = [60, 20, 11, 122, 214, 345, 1324, 1, 2, 3, 6, 74, 3, 9]
    print(quicksort(arr))

```
<b>

```
tab[1..n] - tablica wejściowa
dł() - funkcja zwracająca rozmiar tablicy

def quicksort(tab)
	Jeżeli dł(tab) <= 1:
		Zwróć tab

	pivot <- tab[dł(tab)]
	smaller <- []
	greater <- []

	Dla i = 1,2,3, ... , dł(tab) - 1
		Jeżeli tab[i] <= pivot
			Dodaj element tab[i] na koniec smaller
		W innym wypadku
			Dodaj element tab[i] na koniec greater

	Zwróć quicksort(smaller) + [pivot] + quicksort(greater)
```
</b>

```cpp
// C++23
#include <print>
#include <vector>

std::vector<int> quicksort(const std::vector<int>& t) {
    // pusta tablica lub jeden element - nie trzeba nic robić
    if (t.size() <= 1)
        return t;

    int pivot = t.back();  // pivot to ostatni element
    std::vector<int> smaller, greater;
    for (std::size_t i = 0; i + 1 < t.size(); i++) {  // wszystkie elementy oprócz pivota
        if (t[i] <= pivot)
            smaller.push_back(t[i]);
        else
            greater.push_back(t[i]);
    }

    // quicksort(smaller) + [pivot] + quicksort(greater)
    std::vector<int> wynik = quicksort(smaller);
    wynik.push_back(pivot);
    wynik.append_range(quicksort(greater));  // append_range - nowość w C++23
    return wynik;
}

int main() {
    std::vector<int> arr = {60, 20, 11, 122, 214, 345, 1324, 1, 2, 3, 6, 74, 3, 9};
    std::println("{}", quicksort(arr));
    std::println("{} {} {}", quicksort({}), quicksort({7}), quicksort({5, 1, 4, 2, 8, 0, -3}));
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;

public class SortowanieSzybkie {
    static List<Integer> quicksort(List<Integer> t) {
        // pusta lista lub jeden element - nie trzeba nic robić
        if (t.size() <= 1)
            return t;

        int pivot = t.getLast();  // pivot to ostatni element (getLast - od Javy 21)
        var smaller = new ArrayList<Integer>();
        var greater = new ArrayList<Integer>();
        for (int i = 0; i < t.size() - 1; i++) {  // wszystkie elementy oprócz pivota
            if (t.get(i) <= pivot)
                smaller.add(t.get(i));
            else
                greater.add(t.get(i));
        }

        // quicksort(smaller) + [pivot] + quicksort(greater)
        var wynik = new ArrayList<Integer>(quicksort(smaller));
        wynik.add(pivot);
        wynik.addAll(quicksort(greater));
        return wynik;
    }

    public static void main(String[] args) {
        var arr = List.of(60, 20, 11, 122, 214, 345, 1324, 1, 2, 3, 6, 74, 3, 9);
        System.out.println(quicksort(arr));
        System.out.println(quicksort(List.of()) + " " + quicksort(List.of(7)) + " " + quicksort(List.of(5, 1, 4, 2, 8, 0, -3)));
    }
}
```
</details>

<a name="box"></a>
## Sortowanie kubełkowe [⬆️](#)
<details><summary>Rozwiń</summary>

Założenia: sortujemy liczby (całkowite lub rzeczywiste), najlepiej nieujemne i w miarę równomiernie rozłożone w przedziale [min, max]. Przedział [min, max] dzielimy na n równych części (kubełków), każdą liczbę wrzucamy do odpowiedniego kubełka, sortujemy kubełki (np. przez wstawianie) i sklejamy je po kolei. Dzięki odejmowaniu minimum kod działa także dla liczb ujemnych.

```python
# Not in place - zwraca nową, posortowaną listę

def insertion_sort(A):
    for i in range(1, len(A)):
        liczba = A[i]
        j = i
        while j > 0 and A[j - 1] > liczba:
            A[j] = A[j - 1]
            j -= 1
        A[j] = liczba


def bucket_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr[:]
    mini, maks = min(arr), max(arr)  # liczone raz, przed pętlą
    if mini == maks:  # wszystkie elementy są równe
        return arr[:]

    buckets = [[] for _ in range(n)]
    szerokosc = (maks - mini) / n  # zakres wartości jednego kubełka

    for i in range(n):
        j = int((arr[i] - mini) / szerokosc)
        if j >= n:  # maksimum trafia do ostatniego kubełka
            j = n - 1
        buckets[j].append(arr[i])

    output = []
    for z in range(n):
        insertion_sort(buckets[z])
        output += buckets[z]
    return output
```
<b>

```
arr[1..n] - tablica liczb
n - długość tablicy
min(), max() - najmniejszy i największy element tablicy
int() - część całkowita liczby

def bucket_sort(arr):
	Jeżeli n <= 1
		Zwróć arr
	mini <- min(arr)
	maks <- max(arr)
	Jeżeli mini == maks
		Zwróć arr
	kubelki[1..n] <- n pustych list
	szerokosc <- (maks - mini) / n
	Dla i = 1, 2, ... n
		j <- int((arr[i] - mini) / szerokosc) + 1
		Jeżeli j > n
			j <- n
		Dodaj arr[i] na koniec kubelki[j]
	wynik <- []
	Dla j = 1, 2, ... n
		Posortuj kubelki[j] (np. przez wstawianie)
		Dopisz kubelki[j] na koniec wynik
	Zwróć wynik
```
</b>

```cpp
// C++23
#include <algorithm>
#include <print>
#include <vector>

void insertion_sort(std::vector<double>& A) {
    for (int i = 1; i < std::ssize(A); i++) {
        double liczba = A[i];
        int j = i;
        while (j > 0 && A[j - 1] > liczba) {
            A[j] = A[j - 1];
            j--;
        }
        A[j] = liczba;
    }
}

// zwraca nowy, posortowany wektor
std::vector<double> bucket_sort(const std::vector<double>& arr) {
    int n = std::ssize(arr);
    if (n <= 1)
        return arr;
    double mini = std::ranges::min(arr), maks = std::ranges::max(arr);  // liczone raz, przed pętlą
    if (mini == maks)  // wszystkie elementy są równe
        return arr;

    std::vector<std::vector<double>> buckets(n);  // n pustych kubełków
    double szerokosc = (maks - mini) / n;         // zakres wartości jednego kubełka

    for (double x : arr) {
        int j = static_cast<int>((x - mini) / szerokosc);
        if (j >= n)  // maksimum trafia do ostatniego kubełka
            j = n - 1;
        buckets[j].push_back(x);
    }

    std::vector<double> output;
    for (auto& kubelek : buckets) {
        insertion_sort(kubelek);
        output.append_range(kubelek);  // C++23: dopisanie całego kubełka na koniec
    }
    return output;
}

int main() {
    std::println("{}", bucket_sort({0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51}));
    std::println("{}", bucket_sort({29, 25, 3, 49, 9, 37, 21, 43}));
    std::println("{}", bucket_sort({-5, 3, -1, 0, 2, -5}));
    std::println("{} {} {}", bucket_sort({7, 7, 7}), bucket_sort({}), bucket_sort({1.5}));
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SortowanieKubelkowe {
    static void insertionSort(List<Double> A) {
        for (int i = 1; i < A.size(); i++) {
            double liczba = A.get(i);
            int j = i;
            while (j > 0 && A.get(j - 1) > liczba) {
                A.set(j, A.get(j - 1));
                j--;
            }
            A.set(j, liczba);
        }
    }

    // zwraca nową, posortowaną tablicę
    static double[] bucketSort(double[] arr) {
        int n = arr.length;
        if (n <= 1)
            return arr.clone();
        double mini = Arrays.stream(arr).min().getAsDouble();  // liczone raz, przed pętlą
        double maks = Arrays.stream(arr).max().getAsDouble();
        if (mini == maks)  // wszystkie elementy są równe
            return arr.clone();

        var buckets = new ArrayList<List<Double>>();  // n pustych kubełków
        for (int i = 0; i < n; i++)
            buckets.add(new ArrayList<>());
        double szerokosc = (maks - mini) / n;  // zakres wartości jednego kubełka

        for (double x : arr) {
            int j = (int) ((x - mini) / szerokosc);
            if (j >= n)  // maksimum trafia do ostatniego kubełka
                j = n - 1;
            buckets.get(j).add(x);
        }

        double[] output = new double[n];
        int k = 0;
        for (var kubelek : buckets) {
            insertionSort(kubelek);
            for (double x : kubelek)
                output[k++] = x;
        }
        return output;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(bucketSort(new double[] {0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51})));
        System.out.println(Arrays.toString(bucketSort(new double[] {29, 25, 3, 49, 9, 37, 21, 43})));
        System.out.println(Arrays.toString(bucketSort(new double[] {-5, 3, -1, 0, 2, -5})));
        System.out.println(Arrays.toString(bucketSort(new double[] {7, 7, 7})) + " "
                + Arrays.toString(bucketSort(new double[0])) + " " + Arrays.toString(bucketSort(new double[] {1.5})));
    }
}
```
</details>

<a name="fast_power"></a>
## Szybkie potęgowanie [⬆️](#)
<details><summary>Rozwiń</summary>

Zamiast mnożyć a przez siebie n razy (n mnożeń), korzystamy z tego, że a^n = (a^(n div 2))^2 dla parzystego n oraz a^n = a * a^(n - 1) dla nieparzystego n. Wystarczy wtedy ok. 2 * log2(n) mnożeń.

### Szybkie potęgowanie a^n (iteracyjnie, na bitach wykładnika)
```python
#Iterated version

def fast_power(a, n):  # a^n, n >= 0
    wynik = 1
    while n > 0:
        if n % 2 == 1:  # ostatni bit wykładnika to 1
            wynik *= a
        a *= a  # a, a^2, a^4, a^8, ...
        n //= 2
    return wynik
```
<b>

```
a - podstawa
n - wykładnik (n >= 0)
mod - reszta z dzielenia
div - dzielenie całkowite

def fast_power(a, n):
	wynik <- 1
	Dopóki n > 0
		Jeżeli n mod 2 == 1
			wynik <- wynik * a
		a <- a * a
		n <- n div 2
	Zwróć wynik
```
</b>

```cpp
// C++23
#include <print>
#include <utility>
#include <vector>

// a^n, n >= 0 (uwaga: long long mieści liczby do ok. 9,2 * 10^18, Python nie ma tego ograniczenia)
long long fast_power(long long a, int n) {
    long long wynik = 1;
    while (n > 0) {
        if (n % 2 == 1)  // ostatni bit wykładnika to 1
            wynik *= a;
        a *= a;          // a, a^2, a^4, a^8, ...
        n /= 2;
    }
    return wynik;
}

int main() {
    std::vector<std::pair<long long, int>> testy = {{2, 10}, {3, 13}, {0, 0}, {5, 3}, {-3, 5}, {2, 31}, {10, 9}, {7, 1}};
    for (auto [a, n] : testy)
        std::println("{}^{} = {}", a, n, fast_power(a, n));
}
```

```java
// Java 25
public class SzybkiePotegowanie {
    // a^n, n >= 0 (uwaga: long mieści liczby do ok. 9,2 * 10^18, Python nie ma tego ograniczenia)
    static long fastPower(long a, int n) {
        long wynik = 1;
        while (n > 0) {
            if (n % 2 == 1)  // ostatni bit wykładnika to 1
                wynik *= a;
            a *= a;          // a, a^2, a^4, a^8, ...
            n /= 2;
        }
        return wynik;
    }

    public static void main(String[] args) {
        long[][] testy = {{2, 10}, {3, 13}, {0, 0}, {5, 3}, {-3, 5}, {2, 31}, {10, 9}, {7, 1}};
        for (long[] t : testy)
            System.out.println(t[0] + "^" + t[1] + " = " + fastPower(t[0], (int) t[1]));
    }
}
```

### Szybkie potęgowanie modularne (szybko znajduje wartość base ^ power mod m, domyślnie m = 1000000007)
```python
#Iterated version

def fast_power_mod(base, power, m=1000000007):
    result = 1 % m
    base %= m
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % m
        power //= 2
        base = (base * base) % m
    return result
```
<b>

```
base - podstawa
power - wykładnik (power >= 0)
m - moduł
mod - reszta z dzielenia
div - dzielenie całkowite

def fast_power_mod(base, power, m):
	result <- 1
	base <- base mod m
	Dopóki power > 0
		Jeżeli power mod 2 == 1
			result <- (result * base) mod m
		power <- power div 2
		base <- (base * base) mod m
	Zwróć result mod m
```
</b>

```cpp
// C++23
#include <print>

// base^power mod m; m <= ok. 3 * 10^9, żeby iloczyny mieściły się w long long
long long fast_power_mod(long long base, long long power, long long m = 1000000007) {
    long long result = 1 % m;
    base %= m;
    if (base < 0)  // w C++ reszta z dzielenia liczby ujemnej jest ujemna (w Pythonie nie)
        base += m;
    while (power > 0) {
        if (power % 2 == 1)
            result = (result * base) % m;
        power /= 2;
        base = (base * base) % m;
    }
    return result;
}

int main() {
    std::println("{}", fast_power_mod(2, 10));             // 1024
    std::println("{}", fast_power_mod(2, 1000000));
    std::println("{}", fast_power_mod(3, 200, 13));
    std::println("{}", fast_power_mod(5, 0, 1));           // 0
    std::println("{}", fast_power_mod(-2, 3, 5));          // 2
    std::println("{}", fast_power_mod(123456789, 987654321));
    std::println("{}", fast_power_mod(10, 18));
}
```

```java
// Java 25
public class PotegowanieModularne {
    // base^power mod m; m <= ok. 3 * 10^9, żeby iloczyny mieściły się w long
    static long fastPowerMod(long base, long power, long m) {
        long result = 1 % m;
        base = Math.floorMod(base, m);  // reszta zawsze nieujemna, jak % w Pythonie
        while (power > 0) {
            if (power % 2 == 1)
                result = (result * base) % m;
            power /= 2;
            base = (base * base) % m;
        }
        return result;
    }

    // domyślny moduł m = 1000000007 (Java nie ma argumentów domyślnych, więc przeciążamy metodę)
    static long fastPowerMod(long base, long power) {
        return fastPowerMod(base, power, 1_000_000_007);
    }

    public static void main(String[] args) {
        System.out.println(fastPowerMod(2, 10));             // 1024
        System.out.println(fastPowerMod(2, 1000000));
        System.out.println(fastPowerMod(3, 200, 13));
        System.out.println(fastPowerMod(5, 0, 1));           // 0
        System.out.println(fastPowerMod(-2, 3, 5));          // 2
        System.out.println(fastPowerMod(123456789, 987654321));
        System.out.println(fastPowerMod(10, 18));
        // gotowe: java.math.BigInteger.valueOf(2).modPow(BigInteger.valueOf(10), BigInteger.valueOf(1000000007))
    }
}
```

### Szybkie potęgowanie a^n - wersja rekurencyjna (bez modulo, działa dla dowolnie dużych wyników).
```python
#Recursive version

def fast_pow(a, n):  # a^n, n >= 0 (przyjmujemy 0^0 = 1, tak jak pow w Pythonie)
    if n == 0:
        return 1
    # jeżeli wykładnik jest nieparzysty, to zmniejsz o jeden, by stał się parzysty,
    # a następnie oblicz potęgę a do parzystego wykładnika i pomnóż to przez a,
    # aby dostać a * a^parzysty_wykładnik.
    # na przykład: a^5 = a^4 * a
    if n % 2 == 1:
        return fast_pow(a, n - 1) * a
    # dla parzystego wykładnika szukamy potęgę z wykładnikiem o połowę mniejszym.
    # robiąc to, można dojść do a^2, co potem się składa na a^4 itd...
    # np. a^4 = a^2 * a^2.
    # kiedy n == 2, to funkcja szuka a^1, bo 2 div 2 == 1.
    # kiedy n == 1, to funkcja szuka a^0 * a, bo 1 jest liczbą nieparzystą, więc trafia do drugiego warunku.
    p = fast_pow(a, n // 2)
    return p * p
```
<b>

```
a - podstawa
n - wykładnik (n >= 0)
mod - reszta z dzielenia
div - dzielenie całkowite

def fast_pow(a, n):
	Jeżeli n == 0
		Zwróć 1
	Jeżeli n mod 2 == 1
		Zwróć fast_pow(a, n - 1) * a
	p <- fast_pow(a, n div 2)
	Zwróć p * p
```
</b>

```cpp
// C++23
#include <print>
#include <utility>
#include <vector>

long long fast_pow(long long a, int n) {  // a^n, n >= 0 (przyjmujemy 0^0 = 1)
    if (n == 0)
        return 1;
    if (n % 2 == 1)                    // nieparzysty wykładnik, np. a^5 = a^4 * a
        return fast_pow(a, n - 1) * a;
    long long p = fast_pow(a, n / 2);  // parzysty wykładnik, np. a^4 = a^2 * a^2
    return p * p;
}

int main() {
    std::vector<std::pair<long long, int>> testy = {{2, 10}, {3, 13}, {0, 0}, {0, 5}, {-3, 5}, {2, 62}, {10, 18}, {1, 1000000}};
    for (auto [a, n] : testy)
        std::println("{}^{} = {}", a, n, fast_pow(a, n));
}
```

```java
// Java 25
public class PotegowanieRekurencyjne {
    static long fastPow(long a, int n) {  // a^n, n >= 0 (przyjmujemy 0^0 = 1)
        if (n == 0)
            return 1;
        if (n % 2 == 1)               // nieparzysty wykładnik, np. a^5 = a^4 * a
            return fastPow(a, n - 1) * a;
        long p = fastPow(a, n / 2);   // parzysty wykładnik, np. a^4 = a^2 * a^2
        return p * p;
    }

    public static void main(String[] args) {
        long[][] testy = {{2, 10}, {3, 13}, {0, 0}, {0, 5}, {-3, 5}, {2, 62}, {10, 18}, {1, 1000000}};
        for (long[] t : testy)
            System.out.println(t[0] + "^" + t[1] + " = " + fastPow(t[0], (int) t[1]));
    }
}
```
</details>

<a name="bisekcja"></a>
## Bisekcja (miejsce zerowe funkcji) [⬆️](#)
<details><summary>Rozwiń</summary>

Funkcja f musi być ciągła w przedziale [a, b] i przyjmować na jego końcach wartości o przeciwnych znakach (f(a) * f(b) < 0). Wtedy w przedziale jest miejsce zerowe, a my w każdym kroku zostawiamy tę połowę przedziału, na której końcach znaki wciąż są przeciwne.

```python
def f(x):
    return -4 * x + 2


# bisection(od,do)
def bisection(a, b, precyzja=0.0001):
    if f(a) * f(b) >= 0:  # brak gwarancji miejsca zerowego w [a, b]
        return None
    c = a
    while b - a >= precyzja:
        c = (a + b) / 2
        if f(c) == 0.0:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c
```
<b>

```
f(x) - badana funkcja, ciągła w przedziale [a, b]
precyzja - dokładność wyniku

def f(x):
	Zwróć -4 * x + 2

def bisection(a, b, precyzja):
	Jeżeli f(a) * f(b) >= 0
		Zwróć "brak gwarancji miejsca zerowego"
	c <- a
	Dopóki b - a >= precyzja
		c <- (a + b) / 2
		Jeżeli f(c) == 0
			Zwróć c
		Jeżeli f(c) * f(a) < 0
			b <- c
		W innym wypadku
			a <- c
	Zwróć c
```
</b>

```cpp
// C++23
#include <optional>
#include <print>

double f(double x) {
    return -4 * x + 2;
}

// zwraca przybliżone miejsce zerowe z [a, b] albo std::nullopt, gdy f(a) i f(b) nie mają przeciwnych znaków
std::optional<double> bisection(double a, double b, double precyzja = 0.0001) {
    if (f(a) * f(b) >= 0)  // brak gwarancji miejsca zerowego w [a, b]
        return std::nullopt;
    double c = a;
    while (b - a >= precyzja) {
        c = (a + b) / 2;
        if (f(c) == 0.0)
            return c;
        if (f(c) * f(a) < 0)
            b = c;
        else
            a = c;
    }
    return c;
}

void pokaz(std::optional<double> wynik) {
    if (wynik)
        std::println("{}", *wynik);
    else
        std::println("brak");
}

int main() {
    pokaz(bisection(0, 1));         // 0.5
    pokaz(bisection(-5, 5));        // ok. 0.5
    pokaz(bisection(-100, 3));
    pokaz(bisection(-5, 5, 1e-12));
    pokaz(bisection(1, 2));         // brak - f(1) i f(2) są ujemne
    pokaz(bisection(0, 0.5));       // brak - f(0.5) = 0 (iloczyn równy 0)
}
```

```java
// Java 25
import java.util.Optional;

public class Bisekcja {
    static double f(double x) {
        return -4 * x + 2;
    }

    // zwraca przybliżone miejsce zerowe z [a, b] albo Optional.empty(), gdy f(a) i f(b) nie mają przeciwnych znaków
    static Optional<Double> bisection(double a, double b, double precyzja) {
        if (f(a) * f(b) >= 0)  // brak gwarancji miejsca zerowego w [a, b]
            return Optional.empty();
        double c = a;
        while (b - a >= precyzja) {
            c = (a + b) / 2;
            if (f(c) == 0.0)
                return Optional.of(c);
            if (f(c) * f(a) < 0)
                b = c;
            else
                a = c;
        }
        return Optional.of(c);
    }

    static Optional<Double> bisection(double a, double b) {  // domyślna precyzja
        return bisection(a, b, 0.0001);
    }

    static void pokaz(Optional<Double> wynik) {
        System.out.println(wynik.map(String::valueOf).orElse("brak"));
    }

    public static void main(String[] args) {
        pokaz(bisection(0, 1));         // 0.5
        pokaz(bisection(-5, 5));        // ok. 0.5
        pokaz(bisection(-100, 3));
        pokaz(bisection(-5, 5, 1e-12));
        pokaz(bisection(1, 2));         // brak - f(1) i f(2) są ujemne
        pokaz(bisection(0, 0.5));       // brak - f(0.5) = 0 (iloczyn równy 0)
    }
}
```
</details>

<a name="heron"></a>
## Pierwiastek metodą Herona [⬆️](#)
<details><summary>Rozwiń</summary>

Szukamy kwadratu o polu x. Zaczynamy od prostokąta o bokach a = x i b = 1 (pole x). W każdym kroku nowy bok a to średnia arytmetyczna boków, a drugi bok b = x / a (pole się nie zmienia). Prostokąt coraz bardziej przypomina kwadrat, a jego bok zbliża się do pierwiastka z x.

```python
def heron(x, precyzja=0.000001):  # pierwiastek kwadratowy z x >= 0
    if x == 0:
        return 0
    a = x
    b = 1
    while abs(a - b) > precyzja:
        a = (a + b) / 2
        b = x / a
    return a


print(heron(2))  # 1.41421356...
```
<b>

```
x - liczba, z której liczymy pierwiastek (x > 0)
precyzja - dokładność wyniku
|a - b| - wartość bezwzględna różnicy

def heron(x, precyzja):
	a <- x
	b <- 1
	Dopóki |a - b| > precyzja
		a <- (a + b) / 2
		b <- x / a
	Zwróć a
```
</b>

```cpp
// C++23
#include <cmath>
#include <print>

double heron(double x, double precyzja = 0.000001) {  // pierwiastek kwadratowy z x >= 0
    if (x == 0)
        return 0;
    double a = x;
    double b = 1;
    while (std::abs(a - b) > precyzja) {
        a = (a + b) / 2;  // nowy bok to średnia arytmetyczna boków
        b = x / a;        // drugi bok dobieramy tak, żeby pole wciąż było równe x
    }
    return a;
}

int main() {
    for (double x : {2.0, 9.0, 0.0, 0.25, 1000000.0, 10.0})
        std::println("{} {} {}", x, heron(x), std::sqrt(x));  // porównanie z std::sqrt
}
```

```java
// Java 25
public class Heron {
    static double heron(double x, double precyzja) {  // pierwiastek kwadratowy z x >= 0
        if (x == 0)
            return 0;
        double a = x;
        double b = 1;
        while (Math.abs(a - b) > precyzja) {
            a = (a + b) / 2;  // nowy bok to średnia arytmetyczna boków
            b = x / a;        // drugi bok dobieramy tak, żeby pole wciąż było równe x
        }
        return a;
    }

    static double heron(double x) {  // domyślna precyzja
        return heron(x, 0.000001);
    }

    public static void main(String[] args) {
        for (double x : new double[] {2, 9, 0, 0.25, 1000000, 10})
            System.out.println(x + " " + heron(x) + " " + Math.sqrt(x));  // porównanie z Math.sqrt
    }
}
```
</details>

<a name="horner"></a>
## Schemat Hornera [⬆️](#)
<details><summary>Rozwiń</summary>

Wielomian w(x) = a_n * x^n + ... + a_1 * x + a_0 zapisujemy jako w(x) = (...((a_n * x + a_(n-1)) * x + a_(n-2)) * x + ...) * x + a_0. Wystarczy wtedy n mnożeń i n dodawań (bez liczenia potęg). Współczynniki podajemy od najwyższej potęgi, np. 2x^3 - 6x^2 + 2x - 1 -> [2, -6, 2, -1].

```python
#Iterated version

def horner(wsp, x):  # wsp = [a_n, a_(n-1), ..., a_1, a_0]
    wynik = 0
    for i in range(len(wsp)):
        wynik = wynik * x + wsp[i]
    return wynik


print(horner([2, -6, 2, -1], 3))  # 2*27 - 6*9 + 2*3 - 1 = 5
```
<b>

```
wsp[0..n] - współczynniki wielomianu, od najwyższej potęgi
x - argument

def horner(wsp, x):
	wynik <- 0
	Dla i = 0, 1, ... n
		wynik <- wynik * x + wsp[i]
	Zwróć wynik
```
</b>

```python
#Recursive version - wywołanie: horner_rek(wsp, x, len(wsp) - 1)

def horner_rek(wsp, x, n):  # wartość wielomianu zbudowanego ze współczynników wsp[0..n]
    if n == 0:
        return wsp[0]
    return horner_rek(wsp, x, n - 1) * x + wsp[n]
```
<b>

```
wsp[0..n] - współczynniki wielomianu, od najwyższej potęgi
x - argument

def horner_rek(wsp, x, n):
	Jeżeli n == 0
		Zwróć wsp[0]
	W innym wypadku
		Zwróć horner_rek(wsp, x, n - 1) * x + wsp[n]
```
</b>

```cpp
// C++23
#include <print>
#include <vector>

// iteracyjnie; wsp = {a_n, a_(n-1), ..., a_1, a_0}
long long horner(const std::vector<long long>& wsp, long long x) {
    long long wynik = 0;
    for (long long a : wsp)
        wynik = wynik * x + a;
    return wynik;
}

// rekurencyjnie - wywołanie: horner_rek(wsp, x, wsp.size() - 1)
long long horner_rek(const std::vector<long long>& wsp, long long x, int n) {
    if (n == 0)
        return wsp[0];
    return horner_rek(wsp, x, n - 1) * x + wsp[n];
}

int main() {
    std::vector<long long> wsp = {2, -6, 2, -1};  // 2x^3 - 6x^2 + 2x - 1
    for (long long x : {3, 0, -2, 1, 10})
        std::println("{} {} {}", x, horner(wsp, x), horner_rek(wsp, x, std::ssize(wsp) - 1));  // dla x = 3: 5
    std::println("{}", horner({7}, 5));  // wielomian stały
}
```

```java
// Java 25
public class SchematHornera {
    // iteracyjnie; wsp = {a_n, a_(n-1), ..., a_1, a_0}
    static long horner(long[] wsp, long x) {
        long wynik = 0;
        for (long a : wsp)
            wynik = wynik * x + a;
        return wynik;
    }

    // rekurencyjnie - wywołanie: hornerRek(wsp, x, wsp.length - 1)
    static long hornerRek(long[] wsp, long x, int n) {
        if (n == 0)
            return wsp[0];
        return hornerRek(wsp, x, n - 1) * x + wsp[n];
    }

    public static void main(String[] args) {
        long[] wsp = {2, -6, 2, -1};  // 2x^3 - 6x^2 + 2x - 1
        for (long x : new long[] {3, 0, -2, 1, 10})
            System.out.println(x + " " + horner(wsp, x) + " " + hornerRek(wsp, x, wsp.length - 1));  // dla x = 3: 5
        System.out.println(horner(new long[] {7}, 5));  // wielomian stały
    }
}
```

### Zastosowanie: zamiana liczby z systemu o podstawie b na dziesiętny
Cyfry liczby to współczynniki wielomianu, a podstawa b to argument, np. 1011 (2) = 1 * 2^3 + 0 * 2^2 + 1 * 2 + 1 = ((1 * 2 + 0) * 2 + 1) * 2 + 1 = 11.

```python
def na_dziesietny(liczba, b):  # liczba jako napis, np. na_dziesietny("1F", 16) == 31
    wynik = 0
    for znak in liczba:
        if "0" <= znak <= "9":
            cyfra = ord(znak) - ord("0")
        else:
            cyfra = ord(znak.upper()) - ord("A") + 10  # A = 10, B = 11, ...
        wynik = wynik * b + cyfra
    return wynik
```
<b>

```
liczba[1..n] - napis z cyframi liczby w systemie o podstawie b
wartosc(c) - wartość cyfry c (0..9, A = 10, B = 11, ...)

def na_dziesietny(liczba, b):
	wynik <- 0
	Dla i = 1, 2, ... n
		wynik <- wynik * b + wartosc(liczba[i])
	Zwróć wynik
```
</b>

```cpp
// C++23
#include <cctype>
#include <print>
#include <string>

// liczba jako napis, np. na_dziesietny("1F", 16) == 31
long long na_dziesietny(const std::string& liczba, int b) {
    long long wynik = 0;
    for (char znak : liczba) {
        int cyfra;
        if ('0' <= znak && znak <= '9')
            cyfra = znak - '0';
        else
            cyfra = std::toupper(static_cast<unsigned char>(znak)) - 'A' + 10;  // A = 10, B = 11, ...
        wynik = wynik * b + cyfra;
    }
    return wynik;
}

int main() {
    std::println("{} {} {}", na_dziesietny("1F", 16), na_dziesietny("1011", 2), na_dziesietny("ff", 16));  // 31 11 255
    std::println("{} {} {} {}", na_dziesietny("777", 8), na_dziesietny("Z", 36), na_dziesietny("0", 10), na_dziesietny("zz", 36));
}
```

```java
// Java 25
public class NaDziesietny {
    // liczba jako napis, np. naDziesietny("1F", 16) == 31
    static long naDziesietny(String liczba, int b) {
        long wynik = 0;
        for (char znak : liczba.toCharArray()) {
            int cyfra;
            if ('0' <= znak && znak <= '9')
                cyfra = znak - '0';
            else
                cyfra = Character.toUpperCase(znak) - 'A' + 10;  // A = 10, B = 11, ...
            wynik = wynik * b + cyfra;
        }
        return wynik;
    }

    public static void main(String[] args) {
        System.out.println(naDziesietny("1F", 16) + " " + naDziesietny("1011", 2) + " " + naDziesietny("ff", 16));  // 31 11 255
        System.out.println(naDziesietny("777", 8) + " " + naDziesietny("Z", 36) + " " + naDziesietny("0", 10) + " " + naDziesietny("zz", 36));
    }
}
```
</details>

<a name="pole"></a>
## Pole pod wykresem funkcji [⬆️](#)
<details><summary>Rozwiń</summary>

Liczymy przybliżone pole obszaru ograniczonego wykresem funkcji f (f(x) >= 0), osią OX i prostymi x = a, x = b. Przedział [a, b] dzielimy na n części o szerokości h = (b - a) / n i sumujemy pola prostokątów (wysokość f w lewym końcu części) albo trapezów (podstawy f w obu końcach części). Przykład: f(x) = x^2 na [0, 1], dokładne pole to 1/3.

```python
def f(x):
    return x * x


def prostokaty(a, b, n):  # n - liczba prostokątów
    h = (b - a) / n
    pole = 0
    for i in range(n):
        pole += f(a + i * h) * h
    return pole


def trapezy(a, b, n):  # n - liczba trapezów
    h = (b - a) / n
    pole = 0
    for i in range(n):
        x1 = a + i * h
        x2 = a + (i + 1) * h
        pole += (f(x1) + f(x2)) / 2 * h
    return pole


print(prostokaty(0, 1, 1000))  # ok. 0.33283
print(trapezy(0, 1, 1000))     # ok. 0.3333335
```
<b>

```
f(x) - funkcja nieujemna w przedziale [a, b]
n - liczba części, na które dzielimy przedział

def prostokaty(a, b, n):
	h <- (b - a) / n
	pole <- 0
	Dla i = 0, 1, ... n - 1
		pole <- pole + f(a + i * h) * h
	Zwróć pole

def trapezy(a, b, n):
	h <- (b - a) / n
	pole <- 0
	Dla i = 0, 1, ... n - 1
		x1 <- a + i * h
		x2 <- a + (i + 1) * h
		pole <- pole + (f(x1) + f(x2)) / 2 * h
	Zwróć pole
```
</b>

```cpp
// C++23
#include <print>

double f(double x) {
    return x * x;
}

double prostokaty(double a, double b, int n) {  // n - liczba prostokątów
    double h = (b - a) / n;
    double pole = 0;
    for (int i = 0; i < n; i++)
        pole += f(a + i * h) * h;  // wysokość prostokąta: f w lewym końcu części
    return pole;
}

double trapezy(double a, double b, int n) {  // n - liczba trapezów
    double h = (b - a) / n;
    double pole = 0;
    for (int i = 0; i < n; i++) {
        double x1 = a + i * h;
        double x2 = a + (i + 1) * h;
        pole += (f(x1) + f(x2)) / 2 * h;
    }
    return pole;
}

int main() {
    std::println("{}", prostokaty(0, 1, 1000));  // ok. 0.33283
    std::println("{}", trapezy(0, 1, 1000));     // ok. 0.3333335
    std::println("{} {}", prostokaty(0, 1, 1), trapezy(0, 1, 1));
    std::println("{} {}", prostokaty(0, 2, 4), trapezy(0, 2, 4));
    std::println("{} {}", prostokaty(1, 3, 10), trapezy(1, 3, 10));
    std::println("{} {}", prostokaty(0, 1, 1000000), trapezy(0, 1, 1000000));
}
```

```java
// Java 25
public class PolePodWykresem {
    static double f(double x) {
        return x * x;
    }

    static double prostokaty(double a, double b, int n) {  // n - liczba prostokątów
        double h = (b - a) / n;
        double pole = 0;
        for (int i = 0; i < n; i++)
            pole += f(a + i * h) * h;  // wysokość prostokąta: f w lewym końcu części
        return pole;
    }

    static double trapezy(double a, double b, int n) {  // n - liczba trapezów
        double h = (b - a) / n;
        double pole = 0;
        for (int i = 0; i < n; i++) {
            double x1 = a + i * h;
            double x2 = a + (i + 1) * h;
            pole += (f(x1) + f(x2)) / 2 * h;
        }
        return pole;
    }

    public static void main(String[] args) {
        System.out.println(prostokaty(0, 1, 1000));  // ok. 0.33283
        System.out.println(trapezy(0, 1, 1000));     // ok. 0.3333335
        System.out.println(prostokaty(0, 1, 1) + " " + trapezy(0, 1, 1));
        System.out.println(prostokaty(0, 2, 4) + " " + trapezy(0, 2, 4));
        System.out.println(prostokaty(1, 3, 10) + " " + trapezy(1, 3, 10));
        System.out.println(prostokaty(0, 1, 1000000) + " " + trapezy(0, 1, 1000000));
    }
}
```
</details>

<a name="palindrom"></a>
## Palindrom [⬆️](#)
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
    if len(string) <= 1:  # pusty napis i napis jednoznakowy są palindromami
        return True
    if len(string) == 2:
        if string[0] == string[1]:
            return True
        return False
    return isPalindrom(string[1:-1]) if string[0] == string[-1] else False

# This code is contributed by Pixel
```
<b>

```
n - długość napisu
string[2..n-1] - napis bez pierwszego i ostatniego znaku

def isPalindrom(string):
	Jeżeli n <= 1
		Zwróć Prawdę
	Jeżeli string[1] != string[n]
		Zwróć Fałsz
	W innym wypadku
		Zwróć isPalindrom(string[2..n-1])
```
</b>

```python
#Iterated version (dwa wskaźniki: od początku i od końca)

def is_palindrom(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True
```
<b>

```
n - długość napisu
string[1..n] - sprawdzany napis

def is_palindrom(string):
	i <- 1
	j <- n
	Dopóki i < j
		Jeżeli string[i] != string[j]
			Zwróć Fałsz
		i <- i + 1
		j <- j - 1
	Zwróć Prawdę
```
</b>

```cpp
// C++23
#include <print>
#include <string>
#include <vector>

// porównanie z odwróconym napisem
bool is_palindrom(const std::string& napis) {
    std::string odwrocony(napis.rbegin(), napis.rend());
    return napis == odwrocony;
}

// rekurencyjnie
bool is_palindrom_rek(const std::string& napis) {
    if (napis.size() <= 1)  // pusty napis i napis jednoznakowy są palindromami
        return true;
    if (napis.front() != napis.back())
        return false;
    return is_palindrom_rek(napis.substr(1, napis.size() - 2));  // napis bez pierwszego i ostatniego znaku
}

// iteracyjnie (dwa wskaźniki: od początku i od końca)
bool is_palindrom_iter(const std::string& napis) {
    int i = 0;
    int j = std::ssize(napis) - 1;
    while (i < j) {
        if (napis[i] != napis[j])
            return false;
        i++;
        j--;
    }
    return true;
}

int main() {
    // uwaga: polskie litery w UTF-8 zajmują po 2 bajty, więc testujemy napisy bez nich
    std::vector<std::string> slowa = {"kajak", "abba", "ala", "kot", "", "a", "ab", "aa", "Kajak", "kobylamamalybok"};
    for (const auto& s : slowa)
        std::println("'{}' {} {} {}", s, is_palindrom(s), is_palindrom_rek(s), is_palindrom_iter(s));
}
```

```java
// Java 25
import java.util.List;

public class Palindrom {
    // porównanie z odwróconym napisem
    static boolean isPalindrom(String napis) {
        String odwrocony = new StringBuilder(napis).reverse().toString();
        return napis.equals(odwrocony);  // napisy porównujemy przez equals, nie przez ==
    }

    // rekurencyjnie
    static boolean isPalindromRek(String napis) {
        if (napis.length() <= 1)  // pusty napis i napis jednoznakowy są palindromami
            return true;
        if (napis.charAt(0) != napis.charAt(napis.length() - 1))
            return false;
        return isPalindromRek(napis.substring(1, napis.length() - 1));  // napis bez pierwszego i ostatniego znaku
    }

    // iteracyjnie (dwa wskaźniki: od początku i od końca)
    static boolean isPalindromIter(String napis) {
        int i = 0;
        int j = napis.length() - 1;
        while (i < j) {
            if (napis.charAt(i) != napis.charAt(j))
                return false;
            i++;
            j--;
        }
        return true;
    }

    public static void main(String[] args) {
        var slowa = List.of("kajak", "abba", "ala", "kot", "", "a", "ab", "aa", "Kajak", "kobylamamalybok");
        for (String s : slowa)
            System.out.println("'" + s + "' " + isPalindrom(s) + " " + isPalindromRek(s) + " " + isPalindromIter(s));
    }
}
```
</details>

<a name="anagram"></a>
## Anagram [⬆️](#)
<details><summary>Rozwiń</summary>

Dwa napisy są anagramami, jeżeli składają się z tych samych znaków, występujących tyle samo razy (np. "kebab" i "babek").

```python
#With sorting

def is_anagram(string,string2):
    if sorted(string) == sorted(string2):
        return True
    return False
```

```python
#With own sorting

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
n - długość napisów
dł() - długość napisu
sort_1() - sortuje znaki napisu (np. bąbelkowo)

def is_anagram(string, pattern):
	Jeżeli dł(string) != dł(pattern)
		Zwróć Fałsz
	string <- sort_1(string)
	pattern <- sort_1(pattern)
	Dla i = 1, 2, ... n
		Jeżeli string[i] != pattern[i]
			Zwróć Fałsz
	Zwróć Prawdę
```
</b>

```python
#Counting version (zliczanie wystąpień znaków w słowniku)

def is_anagram(string, pattern):
    if len(string) != len(pattern):
        return False

    licznik = {}
    for znak in string:
        licznik[znak] = licznik.get(znak, 0) + 1

    for znak in pattern:
        if licznik.get(znak, 0) == 0:  # znaku brak albo występuje za dużo razy
            return False
        licznik[znak] -= 1
    return True
```
<b>

```
n - długość napisów
dł() - długość napisu
licznik[z] - ile razy znak z wystąpił (na początku 0 dla każdego znaku)

def is_anagram(string, pattern):
	Jeżeli dł(string) != dł(pattern)
		Zwróć Fałsz
	Dla i = 1, 2, ... n
		licznik[string[i]] <- licznik[string[i]] + 1
	Dla i = 1, 2, ... n
		Jeżeli licznik[pattern[i]] == 0
			Zwróć Fałsz
		licznik[pattern[i]] <- licznik[pattern[i]] - 1
	Zwróć Prawdę
```
</b>

```cpp
// C++23
#include <algorithm>
#include <map>
#include <print>
#include <string>
#include <utility>
#include <vector>

// z sortowaniem (parametry przez wartość, bo sortujemy kopie)
bool is_anagram_sort(std::string napis, std::string pattern) {
    std::ranges::sort(napis);
    std::ranges::sort(pattern);
    return napis == pattern;
}

// własne sortowanie (bąbelkowe)
std::string sort_1(std::string s) {
    int n = std::ssize(s);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (s[j] > s[j + 1])
                std::swap(s[j], s[j + 1]);
    return s;
}

bool is_anagram_wlasne(const std::string& napis, const std::string& pattern) {
    if (napis.size() != pattern.size())
        return false;
    std::string a = sort_1(napis), b = sort_1(pattern);
    for (std::size_t i = 0; i < a.size(); i++)
        if (a[i] != b[i])
            return false;
    return true;
}

// zliczanie wystąpień znaków
bool is_anagram(const std::string& napis, const std::string& pattern) {
    if (napis.size() != pattern.size())
        return false;
    std::map<char, int> licznik;  // brakujący klucz ma na początku wartość 0
    for (char znak : napis)
        licznik[znak]++;
    for (char znak : pattern) {
        if (licznik[znak] == 0)  // znaku brak albo występuje za dużo razy
            return false;
        licznik[znak]--;
    }
    return true;
}

int main() {
    std::vector<std::pair<std::string, std::string>> pary = {
        {"kebab", "babek"}, {"kot", "tok"}, {"ala", "aal"}, {"abc", "abd"}, {"aab", "abb"}, {"", ""}, {"a", "aa"}, {"Kot", "tok"}};
    for (const auto& [s1, s2] : pary)
        std::println("{} {} {} {} {}", s1, s2, is_anagram_sort(s1, s2), is_anagram_wlasne(s1, s2), is_anagram(s1, s2));
}
```

```java
// Java 25
import java.util.Arrays;
import java.util.HashMap;

public class Anagram {
    // z sortowaniem
    static boolean isAnagramSort(String napis, String pattern) {
        char[] a = napis.toCharArray(), b = pattern.toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);
        return Arrays.equals(a, b);
    }

    // własne sortowanie (bąbelkowe)
    static String sort1(String s) {
        char[] t = s.toCharArray();
        for (int i = 0; i < t.length; i++)
            for (int j = 0; j < t.length - i - 1; j++)
                if (t[j] > t[j + 1]) {
                    char x = t[j];
                    t[j] = t[j + 1];
                    t[j + 1] = x;
                }
        return new String(t);
    }

    static boolean isAnagramWlasne(String napis, String pattern) {
        if (napis.length() != pattern.length())
            return false;
        String a = sort1(napis), b = sort1(pattern);
        for (int i = 0; i < a.length(); i++)
            if (a.charAt(i) != b.charAt(i))
                return false;
        return true;
    }

    // zliczanie wystąpień znaków
    static boolean isAnagram(String napis, String pattern) {
        if (napis.length() != pattern.length())
            return false;
        var licznik = new HashMap<Character, Integer>();
        for (char znak : napis.toCharArray())
            licznik.put(znak, licznik.getOrDefault(znak, 0) + 1);
        for (char znak : pattern.toCharArray()) {
            if (licznik.getOrDefault(znak, 0) == 0)  // znaku brak albo występuje za dużo razy
                return false;
            licznik.put(znak, licznik.get(znak) - 1);
        }
        return true;
    }

    public static void main(String[] args) {
        String[][] pary = {{"kebab", "babek"}, {"kot", "tok"}, {"ala", "aal"}, {"abc", "abd"}, {"aab", "abb"}, {"", ""}, {"a", "aa"}, {"Kot", "tok"}};
        for (String[] p : pary)
            System.out.println(p[0] + " " + p[1] + " " + isAnagramSort(p[0], p[1]) + " " + isAnagramWlasne(p[0], p[1]) + " " + isAnagram(p[0], p[1]));
    }
}
```
</details>

<a name="alfa"></a>
## Porządek alfabetyczny [⬆️](#)
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
<b>

```
tab[1..n] - litery napisu
litery porównujemy według ich kodów (kolejność w alfabecie)

Dla i = 1, 2, ... n
	Dla j = 1, 2, ... n – i
		Jeżeli tab[j] > tab[j + 1]
			Zamień tab[j] z tab[j + 1]
```
</b>

```python
#Porządek leksykograficzny słów (porównywanie napisów znak po znaku)

def mniejsze(s1, s2):  # czy s1 jest w słowniku przed s2
    i = 0
    while i < len(s1) and i < len(s2):
        if s1[i] != s2[i]:
            return s1[i] < s2[i]  # decyduje pierwszy różniący się znak
        i += 1
    return len(s1) < len(s2)  # jedno słowo jest początkiem drugiego, np. "kot" < "kotek"


def sortuj_slowa(slowa):  # sortowanie bąbelkowe listy słów
    slowa = slowa[:]
    for i in range(len(slowa)):
        for j in range(len(slowa) - i - 1):
            if mniejsze(slowa[j + 1], slowa[j]):
                slowa[j], slowa[j + 1] = slowa[j + 1], slowa[j]
    return slowa


print(sortuj_slowa(["kotek", "ala", "kot", "ma"]))  # ['ala', 'kot', 'kotek', 'ma']
```
<b>

```
dł() - długość napisu

def mniejsze(s1, s2):
	i <- 1
	Dopóki i <= dł(s1) oraz i <= dł(s2)
		Jeżeli s1[i] != s2[i]
			Zwróć s1[i] < s2[i]
		i <- i + 1
	Zwróć dł(s1) < dł(s2)
```
</b>

```cpp
// C++23
#include <print>
#include <string>
#include <utility>
#include <vector>

// sortowanie liter napisu bąbelkowo (litery porównujemy według ich kodów)
std::string bubble_sort(std::string tab) {
    int n = std::ssize(tab);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (tab[j] > tab[j + 1])
                std::swap(tab[j], tab[j + 1]);
    return tab;
}

// czy s1 jest w słowniku przed s2 (porównywanie znak po znaku)
bool mniejsze(const std::string& s1, const std::string& s2) {
    std::size_t i = 0;
    while (i < s1.size() && i < s2.size()) {
        if (s1[i] != s2[i])
            return s1[i] < s2[i];  // decyduje pierwszy różniący się znak
        i++;
    }
    return s1.size() < s2.size();  // jedno słowo jest początkiem drugiego, np. "kot" < "kotek"
}

// sortowanie bąbelkowe listy słów (zwraca posortowaną kopię)
std::vector<std::string> sortuj_slowa(std::vector<std::string> slowa) {
    int n = std::ssize(slowa);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (mniejsze(slowa[j + 1], slowa[j]))
                std::swap(slowa[j], slowa[j + 1]);
    return slowa;
}

int main() {
    std::println("{}", bubble_sort("niezdammatury"));
    std::println("{}", sortuj_slowa({"kotek", "ala", "kot", "ma"}));  // ["ala", "kot", "kotek", "ma"]
    std::println("{}", sortuj_slowa({"b", "a", "ab", "abc", "B", "", "aa"}));
    // w C++ napisy std::string porównuje się tak samo zwykłym "<", np. std::ranges::sort(slowa)
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;

public class PorzadekAlfabetyczny {
    // sortowanie liter napisu bąbelkowo (litery porównujemy według ich kodów)
    static String bubbleSort(String napis) {
        char[] tab = napis.toCharArray();
        for (int i = 0; i < tab.length; i++)
            for (int j = 0; j < tab.length - i - 1; j++)
                if (tab[j] > tab[j + 1]) {
                    char t = tab[j];
                    tab[j] = tab[j + 1];
                    tab[j + 1] = t;
                }
        return new String(tab);
    }

    // czy s1 jest w słowniku przed s2 (porównywanie znak po znaku)
    static boolean mniejsze(String s1, String s2) {
        int i = 0;
        while (i < s1.length() && i < s2.length()) {
            if (s1.charAt(i) != s2.charAt(i))
                return s1.charAt(i) < s2.charAt(i);  // decyduje pierwszy różniący się znak
            i++;
        }
        return s1.length() < s2.length();  // jedno słowo jest początkiem drugiego, np. "kot" < "kotek"
    }

    // sortowanie bąbelkowe listy słów (zwraca posortowaną kopię)
    static List<String> sortujSlowa(List<String> lista) {
        var slowa = new ArrayList<>(lista);
        for (int i = 0; i < slowa.size(); i++)
            for (int j = 0; j < slowa.size() - i - 1; j++)
                if (mniejsze(slowa.get(j + 1), slowa.get(j))) {
                    String t = slowa.get(j);
                    slowa.set(j, slowa.get(j + 1));
                    slowa.set(j + 1, t);
                }
        return slowa;
    }

    public static void main(String[] args) {
        System.out.println(bubbleSort("niezdammatury"));
        System.out.println(sortujSlowa(List.of("kotek", "ala", "kot", "ma")));  // [ala, kot, kotek, ma]
        System.out.println(sortujSlowa(List.of("b", "a", "ab", "abc", "B", "", "aa")));
        // w Javie to samo porównanie robi s1.compareTo(s2) < 0
    }
}
```
</details>

<a name="pattern"></a>
## Wyszukiwanie wzorca w tekście [⬆️](#)
<details><summary>Rozwiń</summary>

Algorytm naiwny: przykładamy wzorzec do każdej pozycji tekstu, od której jeszcze się mieści (i = 0 .. len(tekst) - len(pattern)), i porównujemy znak po znaku.

```py
def find_pattern(tekst, pattern):  # indeks pierwszego wystąpienia wzorca albo -1
    for i in range(len(tekst) - len(pattern) + 1):
        j = 0
        while j < len(pattern) and tekst[i + j] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i
    return -1


def is_pattern(tekst, pattern):
    return find_pattern(tekst, pattern) != -1


def find_all(tekst, pattern):  # lista wszystkich pozycji wystąpień (także nachodzących na siebie)
    pozycje = []
    for i in range(len(tekst) - len(pattern) + 1):
        j = 0
        while j < len(pattern) and tekst[i + j] == pattern[j]:
            j += 1
        if j == len(pattern):
            pozycje.append(i)
    return pozycje


print(find_pattern("abrakadabra", "abra"))  # 0
print(find_all("abrakadabra", "abra"))      # [0, 7]
```

<b>

```
tekst[1..n] - przeszukiwany tekst
pattern[1..m] - szukany wzorzec

def find_pattern(tekst, pattern):
	Dla i = 1, 2, ... n - m + 1
		j <- 1
		Dopóki j <= m oraz tekst[i + j - 1] == pattern[j]
			j <- j + 1
		Jeżeli j == m + 1
			Zwróć i
	Zwróć -1
```
</b>

```cpp
// C++23
#include <print>
#include <string>
#include <utility>
#include <vector>

int find_pattern(const std::string& tekst, const std::string& pattern) {  // indeks pierwszego wystąpienia albo -1
    int n = std::ssize(tekst), m = std::ssize(pattern);
    for (int i = 0; i <= n - m; i++) {
        int j = 0;
        while (j < m && tekst[i + j] == pattern[j])
            j++;
        if (j == m)
            return i;
    }
    return -1;
}

bool is_pattern(const std::string& tekst, const std::string& pattern) {
    return find_pattern(tekst, pattern) != -1;
}

std::vector<int> find_all(const std::string& tekst, const std::string& pattern) {  // także nachodzące na siebie
    std::vector<int> pozycje;
    int n = std::ssize(tekst), m = std::ssize(pattern);
    for (int i = 0; i <= n - m; i++) {
        int j = 0;
        while (j < m && tekst[i + j] == pattern[j])
            j++;
        if (j == m)
            pozycje.push_back(i);
    }
    return pozycje;
}

int main() {
    std::println("{}", find_pattern("abrakadabra", "abra"));  // 0
    std::println("{}", find_all("abrakadabra", "abra"));      // [0, 7]
    std::vector<std::pair<std::string, std::string>> testy = {{"aaaa", "aa"}, {"abc", "d"}, {"ab", "abc"}, {"abc", ""}, {"ala ma kota", "kot"}};
    for (const auto& [t, p] : testy)
        std::println("{} {} {}", find_pattern(t, p), is_pattern(t, p), find_all(t, p));
    // gotowe: tekst.find(pattern) zwraca pozycję albo std::string::npos
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;

public class WyszukiwanieWzorca {
    static int findPattern(String tekst, String pattern) {  // indeks pierwszego wystąpienia albo -1
        int n = tekst.length(), m = pattern.length();
        for (int i = 0; i <= n - m; i++) {
            int j = 0;
            while (j < m && tekst.charAt(i + j) == pattern.charAt(j))
                j++;
            if (j == m)
                return i;
        }
        return -1;
    }

    static boolean isPattern(String tekst, String pattern) {
        return findPattern(tekst, pattern) != -1;
    }

    static List<Integer> findAll(String tekst, String pattern) {  // także nachodzące na siebie
        var pozycje = new ArrayList<Integer>();
        int n = tekst.length(), m = pattern.length();
        for (int i = 0; i <= n - m; i++) {
            int j = 0;
            while (j < m && tekst.charAt(i + j) == pattern.charAt(j))
                j++;
            if (j == m)
                pozycje.add(i);
        }
        return pozycje;
    }

    public static void main(String[] args) {
        System.out.println(findPattern("abrakadabra", "abra"));  // 0
        System.out.println(findAll("abrakadabra", "abra"));      // [0, 7]
        String[][] testy = {{"aaaa", "aa"}, {"abc", "d"}, {"ab", "abc"}, {"abc", ""}, {"ala ma kota", "kot"}};
        for (String[] t : testy)
            System.out.println(findPattern(t[0], t[1]) + " " + isPattern(t[0], t[1]) + " " + findAll(t[0], t[1]));
        // gotowe: tekst.indexOf(pattern) zwraca pozycję albo -1
    }
}
```
</details>

<a name="onp"></a>
## Odwrotna notacja polska (ONP) [⬆️](#)
<details><summary>Rozwiń</summary>

W ONP operator stoi za argumentami, np. (3 + 4) * 2 zapisujemy jako 3 4 + 2 *. Nawiasy nie są potrzebne. Wyrażenie czytamy od lewej: liczbę wkładamy na stos, a operator zdejmuje ze stosu dwie liczby, wykonuje działanie i wkłada wynik na stos. Na końcu na stosie zostaje wynik.

```python
def onp(wyrazenie):  # elementy oddzielone spacjami, np. "3 4 + 2 *"
    stos = []
    for element in wyrazenie.split():
        if element in ["+", "-", "*", "/"]:
            b = stos.pop()  # najpierw zdejmujemy PRAWY argument
            a = stos.pop()
            if element == "+":
                stos.append(a + b)
            elif element == "-":
                stos.append(a - b)
            elif element == "*":
                stos.append(a * b)
            else:
                stos.append(a / b)
        else:
            stos.append(float(element))
    return stos.pop()


print(onp("3 4 + 2 *"))          # 14.0
print(onp("5 1 2 + 4 * + 3 -"))  # 14.0
```
<b>

```
wyrazenie[1..n] - kolejne elementy wyrażenia (liczby i operatory)
stos - na początku pusty

def onp(wyrazenie):
	Dla i = 1, 2, ... n
		Jeżeli wyrazenie[i] jest operatorem
			b <- zdejmij ze stosu
			a <- zdejmij ze stosu
			Połóż na stos wynik działania a wyrazenie[i] b
		W innym wypadku
			Połóż na stos liczbę wyrazenie[i]
	Zwróć zdejmij ze stosu
```
</b>

```cpp
// C++23
#include <print>
#include <sstream>
#include <stack>
#include <string>

double onp(const std::string& wyrazenie) {  // elementy oddzielone spacjami, np. "3 4 + 2 *"
    std::stack<double> stos;
    std::istringstream strumien(wyrazenie);
    std::string element;
    while (strumien >> element) {  // kolejne elementy oddzielone spacjami
        if (element == "+" || element == "-" || element == "*" || element == "/") {
            double b = stos.top();  // najpierw zdejmujemy PRAWY argument
            stos.pop();
            double a = stos.top();
            stos.pop();
            if (element == "+")
                stos.push(a + b);
            else if (element == "-")
                stos.push(a - b);
            else if (element == "*")
                stos.push(a * b);
            else
                stos.push(a / b);
        } else {
            stos.push(std::stod(element));  // napis -> liczba
        }
    }
    return stos.top();
}

int main() {
    std::println("{}", onp("3 4 + 2 *"));          // 14
    std::println("{}", onp("5 1 2 + 4 * + 3 -"));  // 14
    for (const char* w : {"10 4 /", "7 2 -", "-3 2 *", "2 3 4 * +", "42"})
        std::println("{}", onp(w));
}
```

```java
// Java 25
import java.util.ArrayDeque;

public class Onp {
    static double onp(String wyrazenie) {  // elementy oddzielone spacjami, np. "3 4 + 2 *"
        var stos = new ArrayDeque<Double>();  // push - połóż na stos, pop - zdejmij ze stosu
        for (String element : wyrazenie.trim().split("\\s+")) {
            switch (element) {
                case "+", "-", "*", "/" -> {
                    double b = stos.pop();  // najpierw zdejmujemy PRAWY argument
                    double a = stos.pop();
                    stos.push(switch (element) {
                        case "+" -> a + b;
                        case "-" -> a - b;
                        case "*" -> a * b;
                        default -> a / b;
                    });
                }
                default -> stos.push(Double.parseDouble(element));  // napis -> liczba
            }
        }
        return stos.pop();
    }

    public static void main(String[] args) {
        System.out.println(onp("3 4 + 2 *"));          // 14.0
        System.out.println(onp("5 1 2 + 4 * + 3 -"));  // 14.0
        for (String w : new String[] {"10 4 /", "7 2 -", "-3 2 *", "2 3 4 * +", "42"})
            System.out.println(onp(w));
    }
}
```
</details>

<a name="len"></a>
## Kod prefiksowy (kompresja) [⬆️](#)

### Kod prefiksowy (prefix free)
<details><summary>Rozwiń</summary>

Kody znaków o zmiennej długości są w wymaganiach (przykłady: kod prefiksowy poniżej, kod Huffmana, alfabet Morse’a). Częste znaki dostają krótkie kody, a rzadkie - dłuższe.

Kod jest nazywany "prefix (free) code", jeżeli w systemie nie ma kodu słowa, który byłby prefixem (początkiem) innego kodu słowa. Dzięki temu ciąg bitów da się odkodować jednoznacznie, bez żadnych separatorów.

Załóżmy, że mamy plik z 100,000 znakami, jedyne znaki jakie występują w pliku to: a,b,c,d,e,f i chcemy zmniejszyć rozmiar tego pliku kompresją, gdzie każdy kod znaku ma różną długość.

|                         |   a   |   b   |   c   |   d   |   e   |   f   |
| ----------------------: | :---: | :---: | :---: | :---: | :---: | :---: |
|  Częstość (w tysiącach) |  45   |  13   |  12   |  16   |   9   |   5   |
|    Kod o stałej długości |  000  |  001  |  010  |  011  |  100  |  101  |
| Kod o zmiennej długości |   0   |  101  |  100  |  111  | 1101  | 1100  |

Przy kodzie o stałej długości plik zajmie 100,000 * 3 = 300,000 bitów, a przy kodzie o zmiennej długości (45 * 1 + 13 * 3 + 12 * 3 + 16 * 3 + 9 * 4 + 5 * 4) * 1000 = 224,000 bitów.

```python
#Iterated version

# kod prefiksowy: żaden kod nie jest początkiem innego
cipher = {'00': ' ', '010': 'a', '011': 'm', '100': 'n', '101': 'i', '110': 'e', '1110': 'z', '1111': 'd'}

text = "1001011100011101111010011"


def decrypt(cipher, text):  # zwraca None, jeżeli text jest niepoprawny
    res = ""
    bufor = ""
    for bit in text:
        bufor += bit
        if bufor in cipher:  # bufor jest pełnym kodem znaku
            res += cipher[bufor]
            bufor = ""
    if bufor != "":  # zostały bity, które nie tworzą żadnego kodu
        return None
    return res


to_code = "zdam"


def encrypt(cipher, text):  # zwraca None, jeżeli w text jest znak spoza słownika
    res = ""
    for char in text:
        if char in cipher.values():
            for k, v in cipher.items():
                if v == char:
                    res += k
        else:
            return None
    return res


print(decrypt(cipher, text))     # nie zdam
print(encrypt(cipher, to_code))  # 11101111010011
```
<b>

```
cipher - słownik: kod -> znak (kod prefiksowy)
text[1..n] - ciąg bitów

def decrypt(cipher, text):
	res <- ""
	bufor <- ""
	Dla i = 1, 2, ... n
		bufor <- bufor + text[i]
		Jeżeli bufor jest kluczem w cipher
			res <- res + cipher[bufor]
			bufor <- ""
	Jeżeli bufor != ""
		Zwróć "błędny ciąg bitów"
	Zwróć res

def encrypt(cipher, text):
	res <- ""
	Dla i = 1, 2, ... dł(text)
		Znajdź kod k, dla którego cipher[k] == text[i]
		res <- res + k
	Zwróć res
```
</b>

```cpp
// C++23
#include <map>
#include <optional>
#include <print>
#include <string>

// zwraca odkodowany tekst albo std::nullopt, jeżeli ciąg bitów jest niepoprawny
std::optional<std::string> decrypt(const std::map<std::string, char>& cipher, const std::string& text) {
    std::string res = "";
    std::string bufor = "";
    for (char bit : text) {
        bufor += bit;
        if (cipher.contains(bufor)) {  // bufor jest pełnym kodem znaku (contains - od C++20)
            res += cipher.at(bufor);
            bufor = "";
        }
    }
    if (bufor != "")  // zostały bity, które nie tworzą żadnego kodu
        return std::nullopt;
    return res;
}

// zwraca ciąg bitów albo std::nullopt, jeżeli w tekście jest znak spoza słownika
std::optional<std::string> encrypt(const std::map<std::string, char>& cipher, const std::string& text) {
    std::string res = "";
    for (char znak : text) {
        bool znaleziony = false;
        for (const auto& [kod, z] : cipher)  // szukamy kodu, który oznacza ten znak
            if (z == znak) {
                res += kod;
                znaleziony = true;
            }
        if (!znaleziony)
            return std::nullopt;
    }
    return res;
}

int main() {
    // kod prefiksowy: żaden kod nie jest początkiem innego
    std::map<std::string, char> cipher = {{"00", ' '}, {"010", 'a'}, {"011", 'm'}, {"100", 'n'},
                                          {"101", 'i'}, {"110", 'e'}, {"1110", 'z'}, {"1111", 'd'}};

    std::println("{}", decrypt(cipher, "1001011100011101111010011").value_or("brak"));  // nie zdam
    std::println("{}", encrypt(cipher, "zdam").value_or("brak"));                       // 11101111010011
    std::println("{}", decrypt(cipher, "1").value_or("brak"));   // brak - niepełny kod
    std::println("{}", encrypt(cipher, "x").value_or("brak"));   // brak - znak spoza słownika
    std::string bity = encrypt(cipher, "nie zdam").value();
    std::println("{} {}", bity, decrypt(cipher, bity).value_or("brak"));
}
```

```java
// Java 25
import java.util.Map;
import java.util.Optional;

public class KodPrefiksowy {
    // zwraca odkodowany tekst albo Optional.empty(), jeżeli ciąg bitów jest niepoprawny
    static Optional<String> decrypt(Map<String, Character> cipher, String text) {
        var res = new StringBuilder();
        String bufor = "";
        for (char bit : text.toCharArray()) {
            bufor += bit;
            if (cipher.containsKey(bufor)) {  // bufor jest pełnym kodem znaku
                res.append(cipher.get(bufor));
                bufor = "";
            }
        }
        if (!bufor.isEmpty())  // zostały bity, które nie tworzą żadnego kodu
            return Optional.empty();
        return Optional.of(res.toString());
    }

    // zwraca ciąg bitów albo Optional.empty(), jeżeli w tekście jest znak spoza słownika
    static Optional<String> encrypt(Map<String, Character> cipher, String text) {
        var res = new StringBuilder();
        for (char znak : text.toCharArray()) {
            boolean znaleziony = false;
            for (var wpis : cipher.entrySet())  // szukamy kodu, który oznacza ten znak
                if (wpis.getValue() == znak) {
                    res.append(wpis.getKey());
                    znaleziony = true;
                }
            if (!znaleziony)
                return Optional.empty();
        }
        return Optional.of(res.toString());
    }

    public static void main(String[] args) {
        // kod prefiksowy: żaden kod nie jest początkiem innego
        Map<String, Character> cipher = Map.of("00", ' ', "010", 'a', "011", 'm', "100", 'n',
                                               "101", 'i', "110", 'e', "1110", 'z', "1111", 'd');

        System.out.println(decrypt(cipher, "1001011100011101111010011").orElse("brak"));  // nie zdam
        System.out.println(encrypt(cipher, "zdam").orElse("brak"));                       // 11101111010011
        System.out.println(decrypt(cipher, "1").orElse("brak"));   // brak - niepełny kod
        System.out.println(encrypt(cipher, "x").orElse("brak"));   // brak - znak spoza słownika
        String bity = encrypt(cipher, "nie zdam").orElseThrow();
        System.out.println(bity + " " + decrypt(cipher, bity).orElse("brak"));
    }
}
```
</details>

<a name="huffman"></a>
## Kod Huffmana [⬆️](#)
<details><summary>Rozwiń</summary>

Kod Huffmana to optymalny kod prefiksowy: daje najkrótszy zakodowany tekst spośród kodów, w których każdy znak ma stały ciąg bitów. Budowa drzewa: każdy znak to liść o wadze równej liczbie jego wystąpień. Dopóki mamy więcej niż jedno drzewo, łączymy dwa drzewa o najmniejszych wagach w jedno (waga = suma wag). Kod znaku to ścieżka od korzenia do liścia: krok w lewo = 0, w prawo = 1. Do wybierania najlżejszych drzew używamy kolejki priorytetowej (moduł heapq).

```python
import heapq


def huffman(tekst):  # zwraca słownik: znak -> kod
    if tekst == "":
        return {}
    czestosc = {}
    for znak in tekst:
        czestosc[znak] = czestosc.get(znak, 0) + 1

    # element kolejki: (waga, numer, drzewo); numer rozstrzyga remisy wag
    # drzewo to znak (liść) albo para (lewe poddrzewo, prawe poddrzewo)
    kolejka = []
    numer = 0
    for znak in czestosc:
        heapq.heappush(kolejka, (czestosc[znak], numer, znak))
        numer += 1

    if len(kolejka) == 1:  # tylko jeden rodzaj znaku
        return {kolejka[0][2]: "0"}

    while len(kolejka) > 1:
        waga1, _, lewe = heapq.heappop(kolejka)   # dwa najlżejsze drzewa
        waga2, _, prawe = heapq.heappop(kolejka)
        heapq.heappush(kolejka, (waga1 + waga2, numer, (lewe, prawe)))
        numer += 1

    kody = {}
    przypisz_kody(kolejka[0][2], "", kody)
    return kody


def przypisz_kody(wezel, kod, kody):
    if isinstance(wezel, str):  # liść - znak
        kody[wezel] = kod
    else:
        przypisz_kody(wezel[0], kod + "0", kody)
        przypisz_kody(wezel[1], kod + "1", kody)


def koduj(tekst, kody):
    wynik = ""
    for znak in tekst:
        wynik += kody[znak]
    return wynik


def dekoduj(bity, kody):
    odwrotne = {}
    for znak in kody:
        odwrotne[kody[znak]] = znak
    wynik = ""
    bufor = ""
    for bit in bity:
        bufor += bit
        if bufor in odwrotne:
            wynik += odwrotne[bufor]
            bufor = ""
    return wynik


tekst = "abrakadabra"
kody = huffman(tekst)
zakodowany = koduj(tekst, kody)
print(kody)
print(zakodowany, len(zakodowany), "bitów zamiast", 8 * len(tekst))
print(dekoduj(zakodowany, kody))
```
<b>

```
Q - kolejka priorytetowa drzew (na początku drzewo o najmniejszej wadze)
czestosc[z] - liczba wystąpień znaku z w tekście

def huffman(tekst):
	Dla każdego znaku z w tekście
		czestosc[z] <- czestosc[z] + 1
	Dla każdego różnego znaku z
		Wstaw do Q liść z o wadze czestosc[z]
	Dopóki w Q jest więcej niż jedno drzewo
		x <- usuń z Q drzewo o najmniejszej wadze
		y <- usuń z Q drzewo o najmniejszej wadze
		Wstaw do Q nowy węzeł o dzieciach x, y i wadze waga(x) + waga(y)
	korzen <- jedyne drzewo w Q
	przypisz_kody(korzen, "")

def przypisz_kody(wezel, kod):
	Jeżeli wezel jest liściem ze znakiem z
		kody[z] <- kod
	W innym wypadku
		przypisz_kody(lewe dziecko wezel, kod + "0")
		przypisz_kody(prawe dziecko wezel, kod + "1")
```
</b>

```cpp
// C++23
#include <functional>
#include <map>
#include <print>
#include <queue>
#include <string>
#include <utility>
#include <vector>

// węzeł drzewa; liść ma lewe = prawe = -1, węzeł wewnętrzny ma indeksy dzieci w wektorze drzewo
struct Wezel {
    char znak;
    int lewe;
    int prawe;
};

void przypisz_kody(const std::vector<Wezel>& drzewo, int wezel, const std::string& kod, std::map<char, std::string>& kody) {
    if (drzewo[wezel].lewe == -1) {  // liść - znak
        kody[drzewo[wezel].znak] = kod;
        return;
    }
    przypisz_kody(drzewo, drzewo[wezel].lewe, kod + "0", kody);
    przypisz_kody(drzewo, drzewo[wezel].prawe, kod + "1", kody);
}

std::map<char, std::string> huffman(const std::string& tekst) {  // zwraca słownik: znak -> kod
    if (tekst.empty())
        return {};
    std::map<char, int> czestosc;
    std::vector<char> kolejnosc;  // znaki w kolejności pierwszego wystąpienia (jak w słowniku Pythona)
    for (char znak : tekst)
        if (czestosc[znak]++ == 0)
            kolejnosc.push_back(znak);

    std::vector<Wezel> drzewo;
    // element kolejki: (waga, indeks węzła); indeks rozstrzyga remisy wag, tak jak numer w Pythonie
    using Element = std::pair<int, int>;
    std::priority_queue<Element, std::vector<Element>, std::greater<>> kolejka;  // najmniejsza waga na górze
    for (char znak : kolejnosc) {
        drzewo.push_back(Wezel{znak, -1, -1});
        int indeks = std::ssize(drzewo) - 1;
        kolejka.push({czestosc[znak], indeks});
    }

    if (kolejka.size() == 1)  // tylko jeden rodzaj znaku
        return {{tekst[0], "0"}};

    while (kolejka.size() > 1) {
        auto [waga1, lewe] = kolejka.top();  // dwa najlżejsze drzewa
        kolejka.pop();
        auto [waga2, prawe] = kolejka.top();
        kolejka.pop();
        drzewo.push_back(Wezel{'\0', lewe, prawe});
        int indeks = std::ssize(drzewo) - 1;
        kolejka.push({waga1 + waga2, indeks});
    }

    std::map<char, std::string> kody;
    przypisz_kody(drzewo, kolejka.top().second, "", kody);
    return kody;
}

std::string koduj(const std::string& tekst, const std::map<char, std::string>& kody) {
    std::string wynik = "";
    for (char znak : tekst)
        wynik += kody.at(znak);
    return wynik;
}

std::string dekoduj(const std::string& bity, const std::map<char, std::string>& kody) {
    std::map<std::string, char> odwrotne;
    for (const auto& [znak, kod] : kody)
        odwrotne[kod] = znak;
    std::string wynik = "", bufor = "";
    for (char bit : bity) {
        bufor += bit;
        if (odwrotne.contains(bufor)) {
            wynik += odwrotne[bufor];
            bufor = "";
        }
    }
    return wynik;
}

int main() {
    for (std::string tekst : {"abrakadabra", "aaaa", "mississippi river"}) {
        auto kody = huffman(tekst);
        std::string zakodowany = koduj(tekst, kody);
        for (const auto& [znak, kod] : kody)
            std::println("'{}': {}", znak, kod);
        std::println("{} {} bitów zamiast {}", zakodowany, zakodowany.size(), 8 * tekst.size());
        std::println("{}", dekoduj(zakodowany, kody));
    }
}
```

```java
// Java 25
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.TreeMap;

public class KodHuffmana {
    // węzeł drzewa: liść ma znak i nie ma dzieci, węzeł wewnętrzny ma dwoje dzieci
    record Wezel(char znak, Wezel lewe, Wezel prawe) {}

    // element kolejki: waga drzewa, numer (rozstrzyga remisy wag) i samo drzewo
    record Element(int waga, int numer, Wezel drzewo) {}

    static Map<Character, String> huffman(String tekst) {  // zwraca słownik: znak -> kod
        var kody = new TreeMap<Character, String>();
        if (tekst.isEmpty())
            return kody;
        var czestosc = new LinkedHashMap<Character, Integer>();  // pamięta kolejność pierwszego wystąpienia
        for (char znak : tekst.toCharArray())
            czestosc.merge(znak, 1, Integer::sum);

        var kolejka = new PriorityQueue<Element>(
                Comparator.comparingInt(Element::waga).thenComparingInt(Element::numer));
        int numer = 0;
        for (var wpis : czestosc.entrySet()) {
            kolejka.add(new Element(wpis.getValue(), numer, new Wezel(wpis.getKey(), null, null)));
            numer++;
        }

        if (kolejka.size() == 1) {  // tylko jeden rodzaj znaku
            kody.put(tekst.charAt(0), "0");
            return kody;
        }

        while (kolejka.size() > 1) {
            Element x = kolejka.poll();  // dwa najlżejsze drzewa
            Element y = kolejka.poll();
            kolejka.add(new Element(x.waga() + y.waga(), numer, new Wezel('\0', x.drzewo(), y.drzewo())));
            numer++;
        }

        przypiszKody(kolejka.peek().drzewo(), "", kody);
        return kody;
    }

    static void przypiszKody(Wezel wezel, String kod, Map<Character, String> kody) {
        if (wezel.lewe() == null) {  // liść - znak
            kody.put(wezel.znak(), kod);
        } else {
            przypiszKody(wezel.lewe(), kod + "0", kody);
            przypiszKody(wezel.prawe(), kod + "1", kody);
        }
    }

    static String koduj(String tekst, Map<Character, String> kody) {
        var wynik = new StringBuilder();
        for (char znak : tekst.toCharArray())
            wynik.append(kody.get(znak));
        return wynik.toString();
    }

    static String dekoduj(String bity, Map<Character, String> kody) {
        var odwrotne = new HashMap<String, Character>();
        for (var wpis : kody.entrySet())
            odwrotne.put(wpis.getValue(), wpis.getKey());
        var wynik = new StringBuilder();
        String bufor = "";
        for (char bit : bity.toCharArray()) {
            bufor += bit;
            if (odwrotne.containsKey(bufor)) {
                wynik.append(odwrotne.get(bufor));
                bufor = "";
            }
        }
        return wynik.toString();
    }

    public static void main(String[] args) {
        for (String tekst : new String[] {"abrakadabra", "aaaa", "mississippi river"}) {
            var kody = huffman(tekst);
            String zakodowany = koduj(tekst, kody);
            for (var wpis : kody.entrySet())
                System.out.println("'" + wpis.getKey() + "': " + wpis.getValue());
            System.out.println(zakodowany + " " + zakodowany.length() + " bitów zamiast " + 8 * tekst.length());
            System.out.println(dekoduj(zakodowany, kody));
        }
    }
}
```
</details>

<a name="morse"></a>
## Alfabet Morse’a [⬆️](#)
<details><summary>Rozwiń</summary>

W zakodowanym tekście litery oddzielamy jedną spacją, a wyrazy znakiem " / ".

```python
# słownik kodujący: znak -> kod Morse'a
morseEncode = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----',
}
# słownik dekodujący: kod Morse'a -> znak (odwrócony słownik kodujący)
morseDecode = {val: key for key, val in morseEncode.items()}

SEP = ' / '  # separator wyrazów


def morseCode(string, decode=False):
    if not decode:  # kodowanie
        wyrazy = []
        for wyraz in string.lower().split():
            litery = []
            for char in wyraz:
                litery.append(morseEncode.get(char, '*'))  # '*' dla nieznanych znaków
            wyrazy.append(' '.join(litery))
        return SEP.join(wyrazy)
    else:  # dekodowanie
        wyrazy = []
        for wyraz in string.split(SEP):
            litery = ''
            for kod in wyraz.split():
                litery += morseDecode.get(kod, '*')  # '*' dla nieznanych kodów
            wyrazy.append(litery)
        return ' '.join(wyrazy)


# test
string = "Keep learning"
coded = morseCode(string)
print("Coded:", coded)
decoded = morseCode(coded, decode=True)
print("Decoded:", decoded)
```

```cpp
// C++23
#include <cctype>
#include <map>
#include <print>
#include <ranges>
#include <sstream>
#include <string>
#include <vector>

// słownik kodujący: znak -> kod Morse'a
const std::map<char, std::string> morse_encode = {
    {'a', ".-"}, {'b', "-..."}, {'c', "-.-."}, {'d', "-.."},
    {'e', "."}, {'f', "..-."}, {'g', "--."}, {'h', "...."},
    {'i', ".."}, {'j', ".---"}, {'k', "-.-"}, {'l', ".-.."},
    {'m', "--"}, {'n', "-."}, {'o', "---"}, {'p', ".--."},
    {'q', "--.-"}, {'r', ".-."}, {'s', "..."}, {'t', "-"},
    {'u', "..-"}, {'v', "...-"}, {'w', ".--"}, {'x', "-..-"},
    {'y', "-.--"}, {'z', "--.."}, {'1', ".----"}, {'2', "..---"},
    {'3', "...--"}, {'4', "....-"}, {'5', "....."}, {'6', "-...."},
    {'7', "--..."}, {'8', "---.."}, {'9', "----."}, {'0', "-----"},
};

const std::string SEP = " / ";  // separator wyrazów

// napis.split() z Pythona - podział według białych znaków
std::vector<std::string> podziel(const std::string& napis) {
    std::vector<std::string> czesci;
    std::istringstream strumien(napis);
    std::string czesc;
    while (strumien >> czesc)
        czesci.push_back(czesc);
    return czesci;
}

// napis.split(sep) z Pythona - podział według podanego separatora
std::vector<std::string> podziel(const std::string& napis, const std::string& sep) {
    std::vector<std::string> czesci;
    std::size_t start = 0, poz;
    while ((poz = napis.find(sep, start)) != std::string::npos) {
        czesci.push_back(napis.substr(start, poz - start));
        start = poz + sep.size();
    }
    czesci.push_back(napis.substr(start));
    return czesci;
}

// sep.join(czesci) z Pythona (C++23: views::join_with + ranges::to)
std::string polacz(const std::vector<std::string>& czesci, const std::string& sep) {
    return czesci | std::views::join_with(sep) | std::ranges::to<std::string>();
}

std::string morse_code(const std::string& napis, bool decode = false) {
    if (!decode) {  // kodowanie
        std::vector<std::string> wyrazy;
        for (const std::string& wyraz : podziel(napis)) {
            std::vector<std::string> litery;
            for (char c : wyraz) {
                char znak = std::tolower(static_cast<unsigned char>(c));
                auto it = morse_encode.find(znak);
                litery.push_back(it != morse_encode.end() ? it->second : "*");  // '*' dla nieznanych znaków
            }
            wyrazy.push_back(polacz(litery, " "));
        }
        return polacz(wyrazy, SEP);
    }
    // dekodowanie - słownik odwrotny: kod Morse'a -> znak
    std::map<std::string, char> morse_decode;
    for (const auto& [znak, kod] : morse_encode)
        morse_decode[kod] = znak;
    std::vector<std::string> wyrazy;
    for (const std::string& wyraz : podziel(napis, SEP)) {
        std::string litery = "";
        for (const std::string& kod : podziel(wyraz)) {
            auto it = morse_decode.find(kod);
            litery += it != morse_decode.end() ? it->second : '*';  // '*' dla nieznanych kodów
        }
        wyrazy.push_back(litery);
    }
    return polacz(wyrazy, " ");
}

int main() {
    for (std::string napis : {"Keep learning", "SOS 2024", "Hej!"}) {
        std::string coded = morse_code(napis);
        std::println("Coded: {}", coded);
        std::println("Decoded: {}", morse_code(coded, true));
    }
    std::println("Decoded: {}", morse_code(".... . .--- / ....... / ...", true));
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AlfabetMorsea {
    static final String ZNAKI = "abcdefghijklmnopqrstuvwxyz1234567890";
    static final String[] KODY = {
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
        "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
        ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"};

    static final Map<Character, String> morseEncode = new HashMap<>();  // znak -> kod Morse'a
    static final Map<String, Character> morseDecode = new HashMap<>();  // kod Morse'a -> znak

    static {  // wypełniamy oba słowniki przy starcie programu
        for (int i = 0; i < ZNAKI.length(); i++) {
            morseEncode.put(ZNAKI.charAt(i), KODY[i]);
            morseDecode.put(KODY[i], ZNAKI.charAt(i));
        }
    }

    static final String SEP = " / ";  // separator wyrazów

    // napis.split() z Pythona - podział według białych znaków, bez pustych kawałków
    static List<String> podziel(String napis) {
        return napis.isBlank() ? List.of() : List.of(napis.trim().split("\\s+"));
    }

    static String morseCode(String napis, boolean decode) {
        if (!decode) {  // kodowanie
            var wyrazy = new ArrayList<String>();
            for (String wyraz : podziel(napis.toLowerCase())) {
                var litery = new ArrayList<String>();
                for (char znak : wyraz.toCharArray())
                    litery.add(morseEncode.getOrDefault(znak, "*"));  // '*' dla nieznanych znaków
                wyrazy.add(String.join(" ", litery));
            }
            return String.join(SEP, wyrazy);
        }
        var wyrazy = new ArrayList<String>();  // dekodowanie
        for (String wyraz : napis.split(SEP, -1)) {  // -1: nie pomijaj pustych kawałków na końcu
            var litery = new StringBuilder();
            for (String kod : podziel(wyraz))
                litery.append(morseDecode.getOrDefault(kod, '*'));  // '*' dla nieznanych kodów
            wyrazy.add(litery.toString());
        }
        return String.join(" ", wyrazy);
    }

    static String morseCode(String napis) {
        return morseCode(napis, false);
    }

    public static void main(String[] args) {
        for (String napis : new String[] {"Keep learning", "SOS 2024", "Hej!"}) {
            String coded = morseCode(napis);
            System.out.println("Coded: " + coded);
            System.out.println("Decoded: " + morseCode(coded, true));
        }
        System.out.println("Decoded: " + morseCode(".... . .--- / ....... / ...", true));
    }
}
```
</details>

<a name="przes"></a>
## Szyfr przestawieniowy [⬆️](#)
<details><summary>Rozwiń</summary>

Szyfry przestawieniowe dokonują przestawienia znaków w tekście. Tekst zaszyfrowany jest permutacją tekstu jawnego, tzn. zawiera wszystkie znaki tekstu jawnego, jednak ustawione w innej kolejności. Operacja taka nosi nazwę transpozycji.

### Zamiana sąsiednich znaków
Zamieniamy miejscami znaki na pozycjach i oraz i + 1 dla i = 0, jump, 2 * jump, ... Dla jump >= 2 pary się nie nakładają, więc ta sama funkcja (z tym samym jump) służy do szyfrowania i odszyfrowania.

```python
tekst = "aMtruaz  nifromtayik ot inct rdungeo"  # jump = 3 to decrypt


def przes(tekst, jump):  # jump >= 2
    tekst = list(tekst)
    for i in range(0, len(tekst) - 1, jump):
        tekst[i], tekst[i + 1] = tekst[i + 1], tekst[i]
    return "".join(tekst)


print(przes(tekst, 3))  # Matura z informatyki to nic trudnego
```
<b>

```
tekst[0..n-1] - szyfrowany tekst
jump - odstęp między początkami zamienianych par (jump >= 2)

def przes(tekst, jump):
	i <- 0
	Dopóki i < n - 1
		t <- tekst[i]
		tekst[i] <- tekst[i + 1]
		tekst[i + 1] <- t
		i <- i + jump
	Zwróć tekst
```
</b>

```cpp
// C++23
#include <print>
#include <string>
#include <utility>

std::string przes(std::string tekst, int jump) {  // jump >= 2; tekst przekazany przez wartość (kopia)
    for (int i = 0; i < std::ssize(tekst) - 1; i += jump)
        std::swap(tekst[i], tekst[i + 1]);
    return tekst;
}

int main() {
    std::string tekst = "aMtruaz  nifromtayik ot inct rdungeo";  // jump = 3 to decrypt
    std::println("{}", przes(tekst, 3));  // Matura z informatyki to nic trudnego
    std::println("{}", przes("abcdef", 2));                     // badcfe
    std::println("{}", przes(przes("szyfr przestawieniowy", 4), 4));  // szyfrujemy i odszyfrowujemy
    std::println("[{}] [{}]", przes("", 3), przes("a", 2));
}
```

```java
// Java 25
public class SzyfrPrzestawieniowy {
    static String przes(String napis, int jump) {  // jump >= 2
        char[] tekst = napis.toCharArray();
        for (int i = 0; i < tekst.length - 1; i += jump) {
            char t = tekst[i];
            tekst[i] = tekst[i + 1];
            tekst[i + 1] = t;
        }
        return new String(tekst);
    }

    public static void main(String[] args) {
        String tekst = "aMtruaz  nifromtayik ot inct rdungeo";  // jump = 3 to decrypt
        System.out.println(przes(tekst, 3));  // Matura z informatyki to nic trudnego
        System.out.println(przes("abcdef", 2));                     // badcfe
        System.out.println(przes(przes("szyfr przestawieniowy", 4), 4));  // szyfrujemy i odszyfrowujemy
        System.out.println("[" + przes("", 3) + "] [" + przes("a", 2) + "]");
    }
}
```

### Szyfr kolumnowy
Tekst wpisujemy wierszami do tabeli o k kolumnach, a odczytujemy kolumnami, np. dla k = 3 "ALA MA KOTA" -> "A  TLMKAAAO".

```python
def szyfruj_kolumnowo(tekst, k):  # k - liczba kolumn
    wynik = ""
    for kolumna in range(k):
        for i in range(kolumna, len(tekst), k):  # znaki z jednej kolumny
            wynik += tekst[i]
    return wynik


def deszyfruj_kolumnowo(szyfr, k):
    tekst = [""] * len(szyfr)
    pozycja = 0
    for kolumna in range(k):  # wpisujemy znaki z powrotem w tej samej kolejności
        for i in range(kolumna, len(szyfr), k):
            tekst[i] = szyfr[pozycja]
            pozycja += 1
    return "".join(tekst)


print(szyfruj_kolumnowo("ALA MA KOTA", 3))    # A  TLMKAAAO
print(deszyfruj_kolumnowo("A  TLMKAAAO", 3))  # ALA MA KOTA
```
<b>

```
tekst[0..n-1] - szyfrowany tekst
k - liczba kolumn

def szyfruj_kolumnowo(tekst, k):
	wynik <- ""
	Dla kolumna = 0, 1, ... k - 1
		i <- kolumna
		Dopóki i < n
			wynik <- wynik + tekst[i]
			i <- i + k
	Zwróć wynik

def deszyfruj_kolumnowo(szyfr, k):
	pozycja <- 0
	Dla kolumna = 0, 1, ... k - 1
		i <- kolumna
		Dopóki i < n
			tekst[i] <- szyfr[pozycja]
			pozycja <- pozycja + 1
			i <- i + k
	Zwróć tekst
```
</b>

```cpp
// C++23
#include <print>
#include <string>

std::string szyfruj_kolumnowo(const std::string& tekst, int k) {  // k - liczba kolumn
    std::string wynik = "";
    for (int kolumna = 0; kolumna < k; kolumna++)
        for (int i = kolumna; i < std::ssize(tekst); i += k)  // znaki z jednej kolumny
            wynik += tekst[i];
    return wynik;
}

std::string deszyfruj_kolumnowo(const std::string& szyfr, int k) {
    std::string tekst(szyfr.size(), ' ');
    int pozycja = 0;
    for (int kolumna = 0; kolumna < k; kolumna++)  // wpisujemy znaki z powrotem w tej samej kolejności
        for (int i = kolumna; i < std::ssize(szyfr); i += k) {
            tekst[i] = szyfr[pozycja];
            pozycja++;
        }
    return tekst;
}

int main() {
    std::println("[{}]", szyfruj_kolumnowo("ALA MA KOTA", 3));    // [A  TLMKAAAO]
    std::println("[{}]", deszyfruj_kolumnowo("A  TLMKAAAO", 3));  // [ALA MA KOTA]
    for (int k : {1, 4, 20}) {
        std::string szyfr = szyfruj_kolumnowo("MATURA Z INFORMATYKI", k);
        std::println("[{}] [{}]", szyfr, deszyfruj_kolumnowo(szyfr, k));
    }
}
```

```java
// Java 25
public class SzyfrKolumnowy {
    static String szyfrujKolumnowo(String tekst, int k) {  // k - liczba kolumn
        var wynik = new StringBuilder();
        for (int kolumna = 0; kolumna < k; kolumna++)
            for (int i = kolumna; i < tekst.length(); i += k)  // znaki z jednej kolumny
                wynik.append(tekst.charAt(i));
        return wynik.toString();
    }

    static String deszyfrujKolumnowo(String szyfr, int k) {
        char[] tekst = new char[szyfr.length()];
        int pozycja = 0;
        for (int kolumna = 0; kolumna < k; kolumna++)  // wpisujemy znaki z powrotem w tej samej kolejności
            for (int i = kolumna; i < szyfr.length(); i += k) {
                tekst[i] = szyfr.charAt(pozycja);
                pozycja++;
            }
        return new String(tekst);
    }

    public static void main(String[] args) {
        System.out.println("[" + szyfrujKolumnowo("ALA MA KOTA", 3) + "]");    // [A  TLMKAAAO]
        System.out.println("[" + deszyfrujKolumnowo("A  TLMKAAAO", 3) + "]");  // [ALA MA KOTA]
        for (int k : new int[] {1, 4, 20}) {
            String szyfr = szyfrujKolumnowo("MATURA Z INFORMATYKI", k);
            System.out.println("[" + szyfr + "] [" + deszyfrujKolumnowo(szyfr, k) + "]");
        }
    }
}
```
</details>

<a name="atbash"></a>
## Szyfr AtBash [⬆️](#)
<details><summary>Rozwiń</summary>

Jest to monoalfabetyczny szyfr podstawieniowy, ograniczony. Zasada jego działania polega na podstawieniu zamiast danej litery, litery leżącej po drugiej stronie alfabetu w takiej samej odległości. Np. zamiast litery A powinniśmy podstawić literę Z, za literę C wstawiamy literę X. Ta sama funkcja szyfruje i odszyfrowuje.

```python
txt = "Nie zdam maturki elo"


def atbash(txt):
    txt = list(txt)
    for i in range(len(txt)):
        if "A" <= txt[i] <= "Z":  # wielkie litery
            txt[i] = chr(ord("Z") - (ord(txt[i]) - ord("A")))
        elif "a" <= txt[i] <= "z":  # małe litery
            txt[i] = chr(ord("z") - (ord(txt[i]) - ord("a")))
        # pozostałe znaki (spacje, cyfry, polskie litery) zostają bez zmian

    return "".join(txt)


print(atbash(txt))  # Mrv awzn nzgfipr vol
```
<b>

```
txt[1..n] - szyfrowany tekst
ord() - kod znaku
chr() - znak o podanym kodzie

def atbash(txt):
	Dla i = 1, 2, ... n
		Jeżeli "A" <= txt[i] <= "Z"
			txt[i] <- chr(ord("Z") - (ord(txt[i]) - ord("A")))
		W innym wypadku Jeżeli "a" <= txt[i] <= "z"
			txt[i] <- chr(ord("z") - (ord(txt[i]) - ord("a")))
	Zwróć txt
```
</b>

```cpp
// C++23
#include <print>
#include <string>

std::string atbash(std::string txt) {  // ta sama funkcja szyfruje i odszyfrowuje
    for (char& c : txt) {  // char& - zmieniamy znaki bezpośrednio w napisie
        if ('A' <= c && c <= 'Z')       // wielkie litery
            c = 'Z' - (c - 'A');
        else if ('a' <= c && c <= 'z')  // małe litery
            c = 'z' - (c - 'a');
        // pozostałe znaki (spacje, cyfry, polskie litery) zostają bez zmian
    }
    return txt;
}

int main() {
    std::println("{}", atbash("Nie zdam maturki elo"));  // Mrv awzn nzgfipr vol
    std::println("{}", atbash("ABC xyz 123"));           // ZYX cba 123
    std::println("{}", atbash("Zażółć gęślą jaźń"));
    std::println("{}", atbash(atbash("Matura 2025")));   // dwa razy - tekst wraca do postaci jawnej
}
```

```java
// Java 25
public class SzyfrAtBash {
    static String atbash(String napis) {  // ta sama funkcja szyfruje i odszyfrowuje
        char[] txt = napis.toCharArray();
        for (int i = 0; i < txt.length; i++) {
            if ('A' <= txt[i] && txt[i] <= 'Z')       // wielkie litery
                txt[i] = (char) ('Z' - (txt[i] - 'A'));
            else if ('a' <= txt[i] && txt[i] <= 'z')  // małe litery
                txt[i] = (char) ('z' - (txt[i] - 'a'));
            // pozostałe znaki (spacje, cyfry, polskie litery) zostają bez zmian
        }
        return new String(txt);
    }

    public static void main(String[] args) {
        System.out.println(atbash("Nie zdam maturki elo"));  // Mrv awzn nzgfipr vol
        System.out.println(atbash("ABC xyz 123"));           // ZYX cba 123
        System.out.println(atbash("Zażółć gęślą jaźń"));
        System.out.println(atbash(atbash("Matura 2025")));   // dwa razy - tekst wraca do postaci jawnej
    }
}
```
</details>

<a name="cezar"></a>
## Szyfr Cezara [⬆️](#)
<details><summary>Rozwiń</summary>

Jest to rodzaj szyfru podstawieniowego, w którym każda litera tekstu jawnego (niezaszyfrowanego) zastępowana jest inną, oddaloną od niej o stałą liczbę pozycji w alfabecie. <br>

Jeżeli przesunięcie będzie równe 13, uzyskamy szyfr ROT13.
```python
def koduj(wiadomosc, klucz):
    wynik = ""
    wiadomosc = wiadomosc.upper().strip().replace(" ", "")
    for i in wiadomosc:
        if "A" <= i <= "Z":
            wynik += chr((ord(i) + klucz - 65) % 26 + 65)  # 65 = ord("A")
        else:
            wynik += i  # znaki inne niż litery A-Z zostają bez zmian
    return wynik


def dekoduj(wiadomosc, klucz):
    klucz *= -1
    return koduj(wiadomosc, klucz)


print(koduj("Ala ma kota", 3))  # DODPDNRWD
print(dekoduj("DODPDNRWD", 3))   # ALAMAKOTA
```
<b>

```
wiadomosc[1..n] - ciąg wielkich liter alfabetu angielskiego, bez spacji i znaków specjalnych
ord() - pokazuje kod znaku w unicode
chr() - pokazuje znak kodu unicode
mod - reszta z dzielenia (zawsze nieujemna)
n - długość ciągu znaków
klucz - liczba całkowita (przy deszyfrowaniu używamy -klucz)

koduj(wiadomosc, klucz):
	wynik <- ""
	Dla i = 1, 2, 3 ... n
		wynik <- wynik + chr((ord(wiadomosc[i]) + klucz - 65) mod 26 + 65)
	Zwróć wynik
```
</b>

```cpp
// C++23
#include <cctype>
#include <print>
#include <string>

// litery zamieniamy na wielkie, spacje pomijamy (jak w wersji w Pythonie); klucz może być ujemny
std::string koduj(const std::string& wiadomosc, int klucz) {
    std::string wynik = "";
    for (char znak : wiadomosc) {
        if (znak == ' ')
            continue;
        char i = std::toupper(static_cast<unsigned char>(znak));
        if ('A' <= i && i <= 'Z')
            // + 26, bo w C++ reszta z dzielenia liczby ujemnej jest ujemna (w Pythonie nie)
            wynik += static_cast<char>(((i - 'A' + klucz) % 26 + 26) % 26 + 'A');
        else
            wynik += i;  // znaki inne niż litery A-Z zostają bez zmian
    }
    return wynik;
}

std::string dekoduj(const std::string& wiadomosc, int klucz) {
    return koduj(wiadomosc, -klucz);
}

int main() {
    std::println("{}", koduj("Ala ma kota", 3));   // DODPDNRWD
    std::println("{}", dekoduj("DODPDNRWD", 3));   // ALAMAKOTA
    std::println("{}", koduj("Hello World", 13));  // ROT13: URYYBJBEYQ
    std::println("{}", koduj(koduj("Hello World", 13), 13));
    std::println("{} {} {} {}", koduj("xyz", 3), koduj("a1!b", 3), koduj("ABC", -1), koduj("ABC", 29));
    std::println("{}", dekoduj(koduj("abc", -55), -55));
}
```

```java
// Java 25
public class SzyfrCezara {
    // litery zamieniamy na wielkie, spacje pomijamy (jak w wersji w Pythonie); klucz może być ujemny
    static String koduj(String wiadomosc, int klucz) {
        var wynik = new StringBuilder();
        for (char i : wiadomosc.toUpperCase().replace(" ", "").toCharArray()) {
            if ('A' <= i && i <= 'Z')
                // Math.floorMod zwraca nieujemną resztę, jak % w Pythonie
                wynik.append((char) (Math.floorMod(i - 'A' + klucz, 26) + 'A'));
            else
                wynik.append(i);  // znaki inne niż litery A-Z zostają bez zmian
        }
        return wynik.toString();
    }

    static String dekoduj(String wiadomosc, int klucz) {
        return koduj(wiadomosc, -klucz);
    }

    public static void main(String[] args) {
        System.out.println(koduj("Ala ma kota", 3));   // DODPDNRWD
        System.out.println(dekoduj("DODPDNRWD", 3));   // ALAMAKOTA
        System.out.println(koduj("Hello World", 13));  // ROT13: URYYBJBEYQ
        System.out.println(koduj(koduj("Hello World", 13), 13));
        System.out.println(koduj("xyz", 3) + " " + koduj("a1!b", 3) + " " + koduj("ABC", -1) + " " + koduj("ABC", 29));
        System.out.println(dekoduj(koduj("abc", -55), -55));
    }
}
```
</details>

<a name="vigenere"></a>
## Szyfr Vigenère’a [⬆️](#)
<details><summary>Rozwiń</summary>

Szyfr podstawieniowy wieloalfabetowy - to szyfr Cezara, w którym przesunięcie zmienia się co literę. Kolejne litery klucza (powtarzanego w kółko) mówią, o ile przesunąć kolejne litery tekstu: A = 0, B = 1, ..., Z = 25. Przy odszyfrowaniu przesuwamy w drugą stronę.

```python
def vigenere(tekst, klucz, deszyfruj=False):  # tekst i klucz: wielkie litery A-Z
    wynik = ""
    j = 0  # pozycja w kluczu
    for znak in tekst:
        if "A" <= znak <= "Z":
            przesuniecie = ord(klucz[j % len(klucz)]) - ord("A")
            if deszyfruj:
                przesuniecie = -przesuniecie
            wynik += chr((ord(znak) - ord("A") + przesuniecie) % 26 + ord("A"))
            j += 1
        else:
            wynik += znak  # inne znaki bez zmian (nie zużywają litery klucza)
    return wynik


szyfr = vigenere("ATTACKATDAWN", "LEMON")
print(szyfr)                                    # LXFOPVEFRNHR
print(vigenere(szyfr, "LEMON", deszyfruj=True))  # ATTACKATDAWN
```
<b>

```
tekst[1..n] - wielkie litery A-Z
klucz[1..k] - wielkie litery A-Z
ord() - kod znaku
chr() - znak o podanym kodzie
mod - reszta z dzielenia (zawsze nieujemna)

def vigenere(tekst, klucz, deszyfruj):
	wynik <- ""
	Dla i = 1, 2, ... n
		przesuniecie <- ord(klucz[(i - 1) mod k + 1]) - ord("A")
		Jeżeli deszyfruj
			przesuniecie <- -przesuniecie
		wynik <- wynik + chr((ord(tekst[i]) - ord("A") + przesuniecie) mod 26 + ord("A"))
	Zwróć wynik
```
</b>

```cpp
// C++23
#include <print>
#include <string>

std::string vigenere(const std::string& tekst, const std::string& klucz, bool deszyfruj = false) {  // wielkie litery A-Z
    std::string wynik = "";
    std::size_t j = 0;  // pozycja w kluczu
    for (char znak : tekst) {
        if ('A' <= znak && znak <= 'Z') {
            int przesuniecie = klucz[j % klucz.size()] - 'A';
            if (deszyfruj)
                przesuniecie = -przesuniecie;
            wynik += static_cast<char>((znak - 'A' + przesuniecie + 26) % 26 + 'A');  // + 26, żeby nie było ujemnej reszty
            j++;
        } else {
            wynik += znak;  // inne znaki bez zmian (nie zużywają litery klucza)
        }
    }
    return wynik;
}

int main() {
    std::string szyfr = vigenere("ATTACKATDAWN", "LEMON");
    std::println("{}", szyfr);                            // LXFOPVEFRNHR
    std::println("{}", vigenere(szyfr, "LEMON", true));   // ATTACKATDAWN
    std::string s2 = vigenere("ALA MA KOTA", "KOT");
    std::println("{} | {}", s2, vigenere(s2, "KOT", true));
    std::println("{} {}", vigenere("XYZ", "B"), vigenere("ABC", "A"));
}
```

```java
// Java 25
public class SzyfrVigenere {
    static String vigenere(String tekst, String klucz, boolean deszyfruj) {  // wielkie litery A-Z
        var wynik = new StringBuilder();
        int j = 0;  // pozycja w kluczu
        for (char znak : tekst.toCharArray()) {
            if ('A' <= znak && znak <= 'Z') {
                int przesuniecie = klucz.charAt(j % klucz.length()) - 'A';
                if (deszyfruj)
                    przesuniecie = -przesuniecie;
                wynik.append((char) (Math.floorMod(znak - 'A' + przesuniecie, 26) + 'A'));
                j++;
            } else {
                wynik.append(znak);  // inne znaki bez zmian (nie zużywają litery klucza)
            }
        }
        return wynik.toString();
    }

    static String vigenere(String tekst, String klucz) {  // domyślnie szyfrowanie
        return vigenere(tekst, klucz, false);
    }

    public static void main(String[] args) {
        String szyfr = vigenere("ATTACKATDAWN", "LEMON");
        System.out.println(szyfr);                           // LXFOPVEFRNHR
        System.out.println(vigenere(szyfr, "LEMON", true));  // ATTACKATDAWN
        String s2 = vigenere("ALA MA KOTA", "KOT");
        System.out.println(s2 + " | " + vigenere(s2, "KOT", true));
        System.out.println(vigenere("XYZ", "B") + " " + vigenere("ABC", "A"));
    }
}
```
</details>

<a name="rsa"></a>
## RSA i rozszerzony Euklides [⬆️](#)
<details><summary>Rozwiń</summary>

### Rozszerzony algorytm Euklidesa
Oprócz d = nwd(a, b) znajduje liczby całkowite x, y, takie że a * x + b * y = d. Gdy nwd(e, m) = 1, to x mod m jest odwrotnością e modulo m, czyli (e * x) mod m = 1 - tego potrzebujemy w RSA.

```python
#Recursive version

def rozszerzony_nwd(a, b):  # zwraca (d, x, y), gdzie d = nwd(a, b) = a * x + b * y
    if b == 0:
        return a, 1, 0
    d, x1, y1 = rozszerzony_nwd(b, a % b)
    return d, y1, x1 - (a // b) * y1


def odwrotnosc_mod(e, m):  # liczba d taka, że (e * d) mod m == 1, albo None
    d, x, y = rozszerzony_nwd(e, m)
    if d != 1:
        return None  # odwrotność istnieje tylko, gdy nwd(e, m) == 1
    return x % m


print(rozszerzony_nwd(240, 46))  # (2, -9, 47), bo 240 * (-9) + 46 * 47 = 2
print(odwrotnosc_mod(17, 3120))  # 2753
```
<b>

```
a, b - liczby całkowite nieujemne
mod - reszta z dzielenia
div - dzielenie całkowite

def rozszerzony_nwd(a, b):
	Jeżeli b == 0
		Zwróć (a, 1, 0)
	(d, x1, y1) <- rozszerzony_nwd(b, a mod b)
	Zwróć (d, y1, x1 - (a div b) * y1)

def odwrotnosc_mod(e, m):
	(d, x, y) <- rozszerzony_nwd(e, m)
	Jeżeli d != 1
		Zwróć "brak odwrotności"
	Zwróć x mod m
```
</b>

```cpp
// C++23
#include <optional>
#include <print>
#include <tuple>

// zwraca (d, x, y), gdzie d = nwd(a, b) = a * x + b * y   (a, b >= 0)
std::tuple<long long, long long, long long> rozszerzony_nwd(long long a, long long b) {
    if (b == 0)
        return {a, 1, 0};
    auto [d, x1, y1] = rozszerzony_nwd(b, a % b);
    return {d, y1, x1 - (a / b) * y1};
}

// liczba d taka, że (e * d) mod m == 1, albo std::nullopt
std::optional<long long> odwrotnosc_mod(long long e, long long m) {
    auto [d, x, y] = rozszerzony_nwd(e, m);
    if (d != 1)
        return std::nullopt;  // odwrotność istnieje tylko, gdy nwd(e, m) == 1
    return (x % m + m) % m;   // + m, bo x może być ujemne
}

int main() {
    std::println("{}", rozszerzony_nwd(240, 46));  // (2, -9, 47), bo 240 * (-9) + 46 * 47 = 2
    std::println("{}", rozszerzony_nwd(17, 3120));
    std::println("{}", odwrotnosc_mod(17, 3120).value());  // 2753
    std::println("{}", odwrotnosc_mod(3, 7).value());      // 5, bo 3 * 5 = 15 = 2 * 7 + 1
    std::println("{}", odwrotnosc_mod(10, 17).value());
    std::println("{}", odwrotnosc_mod(2, 4).has_value());  // false - nwd(2, 4) = 2
}
```

```java
// Java 25
import java.util.Optional;

public class RozszerzonyEuklides {
    record Wynik(long d, long x, long y) {  // d = nwd(a, b) = a * x + b * y
        @Override
        public String toString() {
            return "(" + d + ", " + x + ", " + y + ")";
        }
    }

    static Wynik rozszerzonyNwd(long a, long b) {  // a, b >= 0
        if (b == 0)
            return new Wynik(a, 1, 0);
        Wynik w = rozszerzonyNwd(b, a % b);
        return new Wynik(w.d(), w.y(), w.x() - (a / b) * w.y());
    }

    // liczba d taka, że (e * d) mod m == 1, albo Optional.empty()
    static Optional<Long> odwrotnoscMod(long e, long m) {
        Wynik w = rozszerzonyNwd(e, m);
        if (w.d() != 1)
            return Optional.empty();  // odwrotność istnieje tylko, gdy nwd(e, m) == 1
        return Optional.of(Math.floorMod(w.x(), m));  // floorMod - wynik nieujemny, nawet gdy x < 0
    }

    public static void main(String[] args) {
        System.out.println(rozszerzonyNwd(240, 46));  // (2, -9, 47), bo 240 * (-9) + 46 * 47 = 2
        System.out.println(rozszerzonyNwd(17, 3120));
        System.out.println(odwrotnoscMod(17, 3120).orElseThrow());  // 2753
        System.out.println(odwrotnoscMod(3, 7).orElseThrow());      // 5, bo 3 * 5 = 15 = 2 * 7 + 1
        System.out.println(odwrotnoscMod(10, 17).orElseThrow());
        System.out.println(odwrotnoscMod(2, 4).isPresent());        // false - nwd(2, 4) = 2
    }
}
```

### RSA
Szyfr z kluczem jawnym (asymetryczny): klucz publiczny (e, n) służy do szyfrowania, a klucz prywatny (d, n) do odszyfrowania.
1. Wybieramy dwie różne liczby pierwsze p i q, liczymy n = p * q oraz phi = (p - 1) * (q - 1).
2. Wybieramy e względnie pierwsze z phi (nwd(e, phi) = 1).
3. Liczymy d - odwrotność e modulo phi, czyli (e * d) mod phi = 1.
4. Szyfrowanie liczby m (0 <= m < n): c = m^e mod n. Odszyfrowanie: m = c^d mod n.

```python
def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def rozszerzony_nwd(a, b):  # zwraca (d, x, y), gdzie d = nwd(a, b) = a * x + b * y
    if b == 0:
        return a, 1, 0
    d, x1, y1 = rozszerzony_nwd(b, a % b)
    return d, y1, x1 - (a // b) * y1


def generuj_klucze(p, q, e=None):  # p, q - różne liczby pierwsze
    n = p * q
    phi = (p - 1) * (q - 1)
    if e is None:  # najmniejsze e >= 3 względnie pierwsze z phi
        e = 3
        while nwd(e, phi) != 1:
            e += 2
    d = rozszerzony_nwd(e, phi)[1] % phi  # albo: d = pow(e, -1, phi) (Python 3.8+)
    return (e, n), (d, n)  # (klucz publiczny, klucz prywatny)


def szyfruj(m, klucz_publiczny):  # m - liczba, 0 <= m < n
    e, n = klucz_publiczny
    return pow(m, e, n)  # szybkie potęgowanie modularne


def deszyfruj(c, klucz_prywatny):
    d, n = klucz_prywatny
    return pow(c, d, n)


publiczny, prywatny = generuj_klucze(61, 53, 17)
print(publiczny, prywatny)  # (17, 3233) (2753, 3233)
c = szyfruj(65, publiczny)
print(c, deszyfruj(c, prywatny))  # 2790 65

# szyfrowanie tekstu - każdy znak osobno jako liczba (kod znaku < n)
zaszyfrowane = [szyfruj(ord(znak), publiczny) for znak in "MATURA"]
print("".join(chr(deszyfruj(c, prywatny)) for c in zaszyfrowane))  # MATURA
```
<b>

```
p, q - różne liczby pierwsze
nwd() - największy wspólny dzielnik
odwrotnosc_mod() - odwrotność modulo (rozszerzony algorytm Euklidesa)
mod - reszta z dzielenia

def generuj_klucze(p, q):
	n <- p * q
	phi <- (p - 1) * (q - 1)
	e <- 3
	Dopóki nwd(e, phi) != 1
		e <- e + 2
	d <- odwrotnosc_mod(e, phi)
	Zwróć (e, n), (d, n)

def szyfruj(m, e, n):
	Zwróć m^e mod n          (szybkie potęgowanie modularne)

def deszyfruj(c, d, n):
	Zwróć c^d mod n
```
</b>

```cpp
// C++23
#include <print>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

long long nwd(long long a, long long b) {
    while (b != 0) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

// zwraca (d, x, y), gdzie d = nwd(a, b) = a * x + b * y
std::tuple<long long, long long, long long> rozszerzony_nwd(long long a, long long b) {
    if (b == 0)
        return {a, 1, 0};
    auto [d, x1, y1] = rozszerzony_nwd(b, a % b);
    return {d, y1, x1 - (a / b) * y1};
}

// szybkie potęgowanie modularne (w Pythonie: pow(podstawa, wykladnik, m))
long long potega_mod(long long podstawa, long long wykladnik, long long m) {
    long long wynik = 1 % m;
    podstawa %= m;
    while (wykladnik > 0) {
        if (wykladnik % 2 == 1)
            wynik = wynik * podstawa % m;
        podstawa = podstawa * podstawa % m;
        wykladnik /= 2;
    }
    return wynik;
}

struct Klucz {
    long long wykladnik;  // e (klucz publiczny) albo d (klucz prywatny)
    long long n;
};

// p, q - różne liczby pierwsze; e = 0 oznacza: wybierz najmniejsze e >= 3 względnie pierwsze z phi
std::pair<Klucz, Klucz> generuj_klucze(long long p, long long q, long long e = 0) {
    long long n = p * q;
    long long phi = (p - 1) * (q - 1);
    if (e == 0) {
        e = 3;
        while (nwd(e, phi) != 1)
            e += 2;
    }
    long long x = std::get<1>(rozszerzony_nwd(e, phi));
    long long d = (x % phi + phi) % phi;  // odwrotność e modulo phi
    return {{e, n}, {d, n}};              // (klucz publiczny, klucz prywatny)
}

long long szyfruj(long long m, Klucz publiczny) {  // m - liczba, 0 <= m < n
    return potega_mod(m, publiczny.wykladnik, publiczny.n);
}

long long deszyfruj(long long c, Klucz prywatny) {
    return potega_mod(c, prywatny.wykladnik, prywatny.n);
}

int main() {
    auto [publiczny, prywatny] = generuj_klucze(61, 53, 17);
    std::println("({}, {}) ({}, {})", publiczny.wykladnik, publiczny.n, prywatny.wykladnik, prywatny.n);  // (17, 3233) (2753, 3233)
    long long c = szyfruj(65, publiczny);
    std::println("{} {}", c, deszyfruj(c, prywatny));  // 2790 65

    // szyfrowanie tekstu - każdy znak osobno jako liczba (kod znaku < n)
    std::vector<long long> zaszyfrowane;
    for (char znak : std::string("MATURA"))
        zaszyfrowane.push_back(szyfruj(znak, publiczny));
    std::string odszyfrowane = "";
    for (long long liczba : zaszyfrowane)
        odszyfrowane += static_cast<char>(deszyfruj(liczba, prywatny));
    std::println("{} {}", zaszyfrowane, odszyfrowane);  // ... MATURA

    auto [pub2, pryw2] = generuj_klucze(101, 113);  // e wybrane automatycznie
    std::println("({}, {}) ({}, {}) {}", pub2.wykladnik, pub2.n, pryw2.wykladnik, pryw2.n, deszyfruj(szyfruj(1234, pub2), pryw2));
}
```

```java
// Java 25
import java.util.ArrayList;

public class Rsa {
    record Klucz(long wykladnik, long n) {}  // wykladnik: e (klucz publiczny) albo d (klucz prywatny)

    record Klucze(Klucz publiczny, Klucz prywatny) {}

    static long nwd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    // zwraca {d, x, y}, gdzie d = nwd(a, b) = a * x + b * y
    static long[] rozszerzonyNwd(long a, long b) {
        if (b == 0)
            return new long[] {a, 1, 0};
        long[] w = rozszerzonyNwd(b, a % b);
        return new long[] {w[0], w[2], w[1] - (a / b) * w[2]};
    }

    // szybkie potęgowanie modularne (gotowe: BigInteger.modPow)
    static long potegaMod(long podstawa, long wykladnik, long m) {
        long wynik = 1 % m;
        podstawa %= m;
        while (wykladnik > 0) {
            if (wykladnik % 2 == 1)
                wynik = wynik * podstawa % m;
            podstawa = podstawa * podstawa % m;
            wykladnik /= 2;
        }
        return wynik;
    }

    // p, q - różne liczby pierwsze; e = 0 oznacza: wybierz najmniejsze e >= 3 względnie pierwsze z phi
    static Klucze generujKlucze(long p, long q, long e) {
        long n = p * q;
        long phi = (p - 1) * (q - 1);
        if (e == 0) {
            e = 3;
            while (nwd(e, phi) != 1)
                e += 2;
        }
        long d = Math.floorMod(rozszerzonyNwd(e, phi)[1], phi);  // odwrotność e modulo phi
        return new Klucze(new Klucz(e, n), new Klucz(d, n));
    }

    static long szyfruj(long m, Klucz publiczny) {  // m - liczba, 0 <= m < n
        return potegaMod(m, publiczny.wykladnik(), publiczny.n());
    }

    static long deszyfruj(long c, Klucz prywatny) {
        return potegaMod(c, prywatny.wykladnik(), prywatny.n());
    }

    static String opis(Klucz k) {
        return "(" + k.wykladnik() + ", " + k.n() + ")";
    }

    public static void main(String[] args) {
        Klucze klucze = generujKlucze(61, 53, 17);
        Klucz publiczny = klucze.publiczny(), prywatny = klucze.prywatny();
        System.out.println(opis(publiczny) + " " + opis(prywatny));  // (17, 3233) (2753, 3233)
        long c = szyfruj(65, publiczny);
        System.out.println(c + " " + deszyfruj(c, prywatny));  // 2790 65

        // szyfrowanie tekstu - każdy znak osobno jako liczba (kod znaku < n)
        var zaszyfrowane = new ArrayList<Long>();
        for (char znak : "MATURA".toCharArray())
            zaszyfrowane.add(szyfruj(znak, publiczny));
        var odszyfrowane = new StringBuilder();
        for (long liczba : zaszyfrowane)
            odszyfrowane.append((char) deszyfruj(liczba, prywatny));
        System.out.println(zaszyfrowane + " " + odszyfrowane);  // ... MATURA

        Klucze k2 = generujKlucze(101, 113, 0);  // e wybrane automatycznie
        System.out.println(opis(k2.publiczny()) + " " + opis(k2.prywatny()) + " " + deszyfruj(szyfruj(1234, k2.publiczny()), k2.prywatny()));
    }
}
```
</details>

<a name="trojkat"></a>
## Warunek trójkąta [⬆️](#)
<details><summary>Rozwiń</summary>

Z odcinków o długościach a, b, c da się zbudować trójkąt wtedy i tylko wtedy, gdy wszystkie długości są dodatnie, a suma każdych dwóch jest większa od trzeciej.

```python
def czy_trojkat(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a
```
<b>

```
a, b, c - długości odcinków

def czy_trojkat(a, b, c):
	Jeżeli a <= 0 lub b <= 0 lub c <= 0
		Zwróć Fałsz
	Jeżeli a + b > c oraz a + c > b oraz b + c > a
		Zwróć Prawdę
	W innym wypadku
		Zwróć Fałsz
```
</b>

```cpp
// C++23
#include <array>
#include <print>
#include <vector>

bool czy_trojkat(double a, double b, double c) {
    if (a <= 0 || b <= 0 || c <= 0)
        return false;
    return a + b > c && a + c > b && b + c > a;
}

int main() {
    std::vector<std::array<double, 3>> testy = {{3, 4, 5}, {1, 2, 3}, {1, 1, 1}, {0, 1, 1}, {-1, 2, 2}, {2.5, 2.5, 4.9}, {10, 1, 1}};
    for (auto [a, b, c] : testy)
        std::println("{} {} {} {}", a, b, c, czy_trojkat(a, b, c));
}
```

```java
// Java 25
public class WarunekTrojkata {
    static boolean czyTrojkat(double a, double b, double c) {
        if (a <= 0 || b <= 0 || c <= 0)
            return false;
        return a + b > c && a + c > b && b + c > a;
    }

    public static void main(String[] args) {
        double[][] testy = {{3, 4, 5}, {1, 2, 3}, {1, 1, 1}, {0, 1, 1}, {-1, 2, 2}, {2.5, 2.5, 4.9}, {10, 1, 1}};
        for (double[] t : testy)
            System.out.println(t[0] + " " + t[1] + " " + t[2] + " " + czyTrojkat(t[0], t[1], t[2]));
    }
}
```
</details>

<a name="punkt_prosta"></a>
## Punkt względem prostej [⬆️](#)
<details><summary>Rozwiń</summary>

Punkty zapisujemy jako pary (x, y). Położenie punktu C względem prostej przechodzącej przez A i B mówi znak wyznacznika (iloczynu wektorowego wektorów AB i AC):

det(A, B, C) = (xB - xA) * (yC - yA) - (yB - yA) * (xC - xA)

det > 0 - C leży po lewej stronie prostej (patrząc z A w stronę B), det < 0 - po prawej, det = 0 - C leży na prostej AB. Dwa punkty C i D leżą po tej samej stronie prostej AB, gdy det(A, B, C) i det(A, B, D) mają ten sam znak.

```python
def wyznacznik(A, B, C):  # iloczyn wektorowy AB x AC
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])


def polozenie(A, B, C):  # położenie punktu C względem prostej AB
    w = wyznacznik(A, B, C)
    if w > 0:
        return "po lewej"
    if w < 0:
        return "po prawej"
    return "na prostej"


def ta_sama_strona(A, B, C, D):  # czy C i D leżą po tej samej stronie prostej AB
    return wyznacznik(A, B, C) * wyznacznik(A, B, D) > 0


print(polozenie((0, 0), (2, 2), (0, 5)))  # po lewej
```
<b>

```
A = (xA, yA), B = (xB, yB) - punkty wyznaczające prostą
C = (xC, yC) - badany punkt

def wyznacznik(A, B, C):
	Zwróć (xB - xA) * (yC - yA) - (yB - yA) * (xC - xA)

def polozenie(A, B, C):
	w <- wyznacznik(A, B, C)
	Jeżeli w > 0
		Zwróć "po lewej"
	Jeżeli w < 0
		Zwróć "po prawej"
	Zwróć "na prostej"
```
</b>

```cpp
// C++23
#include <print>
#include <string>

struct Punkt {
    long long x, y;
};

long long wyznacznik(Punkt A, Punkt B, Punkt C) {  // iloczyn wektorowy AB x AC
    return (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x);
}

std::string polozenie(Punkt A, Punkt B, Punkt C) {  // położenie punktu C względem prostej AB
    long long w = wyznacznik(A, B, C);
    if (w > 0)
        return "po lewej";
    if (w < 0)
        return "po prawej";
    return "na prostej";
}

bool ta_sama_strona(Punkt A, Punkt B, Punkt C, Punkt D) {  // czy C i D leżą po tej samej stronie prostej AB
    return wyznacznik(A, B, C) * wyznacznik(A, B, D) > 0;
}

int main() {
    std::println("{}", polozenie({0, 0}, {2, 2}, {0, 5}));  // po lewej
    std::println("{}", polozenie({0, 0}, {2, 2}, {5, 0}));  // po prawej
    std::println("{}", polozenie({0, 0}, {2, 2}, {7, 7}));  // na prostej
    std::println("{}", ta_sama_strona({0, 0}, {2, 2}, {0, 5}, {1, 7}));  // true
    std::println("{}", ta_sama_strona({0, 0}, {2, 2}, {0, 5}, {5, 0}));  // false
    std::println("{}", ta_sama_strona({0, 0}, {2, 2}, {0, 5}, {3, 3}));  // false - D leży na prostej
}
```

```java
// Java 25
public class PunktWzgledemProstej {
    record Punkt(long x, long y) {}

    static long wyznacznik(Punkt A, Punkt B, Punkt C) {  // iloczyn wektorowy AB x AC
        return (B.x() - A.x()) * (C.y() - A.y()) - (B.y() - A.y()) * (C.x() - A.x());
    }

    static String polozenie(Punkt A, Punkt B, Punkt C) {  // położenie punktu C względem prostej AB
        long w = wyznacznik(A, B, C);
        if (w > 0)
            return "po lewej";
        if (w < 0)
            return "po prawej";
        return "na prostej";
    }

    static boolean taSamaStrona(Punkt A, Punkt B, Punkt C, Punkt D) {  // czy C i D leżą po tej samej stronie prostej AB
        return wyznacznik(A, B, C) * wyznacznik(A, B, D) > 0;
    }

    public static void main(String[] args) {
        var A = new Punkt(0, 0);
        var B = new Punkt(2, 2);
        System.out.println(polozenie(A, B, new Punkt(0, 5)));  // po lewej
        System.out.println(polozenie(A, B, new Punkt(5, 0)));  // po prawej
        System.out.println(polozenie(A, B, new Punkt(7, 7)));  // na prostej
        System.out.println(taSamaStrona(A, B, new Punkt(0, 5), new Punkt(1, 7)));  // true
        System.out.println(taSamaStrona(A, B, new Punkt(0, 5), new Punkt(5, 0)));  // false
        System.out.println(taSamaStrona(A, B, new Punkt(0, 5), new Punkt(3, 3)));  // false - D leży na prostej
    }
}
```
</details>

<a name="punkt_odcinek"></a>
## Punkt na odcinku [⬆️](#)
<details><summary>Rozwiń</summary>

Punkt C należy do odcinka AB, gdy leży na prostej AB (wyznacznik równy 0) i jego współrzędne mieszczą się między współrzędnymi końców odcinka.

```python
def wyznacznik(A, B, C):  # iloczyn wektorowy AB x AC
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])


def na_odcinku(A, B, C):  # czy punkt C należy do odcinka AB
    if wyznacznik(A, B, C) != 0:
        return False
    return (min(A[0], B[0]) <= C[0] <= max(A[0], B[0])
            and min(A[1], B[1]) <= C[1] <= max(A[1], B[1]))


print(na_odcinku((0, 0), (4, 4), (2, 2)))  # True
print(na_odcinku((0, 0), (4, 4), (5, 5)))  # False
```
<b>

```
A = (xA, yA), B = (xB, yB) - końce odcinka
C = (xC, yC) - badany punkt

def na_odcinku(A, B, C):
	Jeżeli wyznacznik(A, B, C) != 0
		Zwróć Fałsz
	Jeżeli min(xA, xB) <= xC <= max(xA, xB) oraz min(yA, yB) <= yC <= max(yA, yB)
		Zwróć Prawdę
	W innym wypadku
		Zwróć Fałsz
```
</b>

```cpp
// C++23
#include <algorithm>
#include <print>

struct Punkt {
    long long x, y;
};

long long wyznacznik(Punkt A, Punkt B, Punkt C) {  // iloczyn wektorowy AB x AC
    return (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x);
}

bool na_odcinku(Punkt A, Punkt B, Punkt C) {  // czy punkt C należy do odcinka AB
    if (wyznacznik(A, B, C) != 0)
        return false;
    return std::min(A.x, B.x) <= C.x && C.x <= std::max(A.x, B.x)
        && std::min(A.y, B.y) <= C.y && C.y <= std::max(A.y, B.y);
}

int main() {
    std::println("{}", na_odcinku({0, 0}, {4, 4}, {2, 2}));  // true
    std::println("{}", na_odcinku({0, 0}, {4, 4}, {5, 5}));  // false - na prostej, ale poza odcinkiem
    std::println("{}", na_odcinku({0, 0}, {4, 4}, {0, 0}));  // true - koniec odcinka
    std::println("{}", na_odcinku({0, 0}, {4, 4}, {2, 3}));  // false
    std::println("{}", na_odcinku({1, 0}, {1, 5}, {1, 3}));  // true - odcinek pionowy
    std::println("{}", na_odcinku({1, 0}, {1, 5}, {1, 6}));  // false
    std::println("{}", na_odcinku({2, 2}, {2, 2}, {2, 2}));  // true - odcinek zdegenerowany do punktu
}
```

```java
// Java 25
public class PunktNaOdcinku {
    record Punkt(long x, long y) {}

    static long wyznacznik(Punkt A, Punkt B, Punkt C) {  // iloczyn wektorowy AB x AC
        return (B.x() - A.x()) * (C.y() - A.y()) - (B.y() - A.y()) * (C.x() - A.x());
    }

    static boolean naOdcinku(Punkt A, Punkt B, Punkt C) {  // czy punkt C należy do odcinka AB
        if (wyznacznik(A, B, C) != 0)
            return false;
        return Math.min(A.x(), B.x()) <= C.x() && C.x() <= Math.max(A.x(), B.x())
            && Math.min(A.y(), B.y()) <= C.y() && C.y() <= Math.max(A.y(), B.y());
    }

    static boolean naOdcinku(long ax, long ay, long bx, long by, long cx, long cy) {  // skrót do testów
        return naOdcinku(new Punkt(ax, ay), new Punkt(bx, by), new Punkt(cx, cy));
    }

    public static void main(String[] args) {
        System.out.println(naOdcinku(0, 0, 4, 4, 2, 2));  // true
        System.out.println(naOdcinku(0, 0, 4, 4, 5, 5));  // false - na prostej, ale poza odcinkiem
        System.out.println(naOdcinku(0, 0, 4, 4, 0, 0));  // true - koniec odcinka
        System.out.println(naOdcinku(0, 0, 4, 4, 2, 3));  // false
        System.out.println(naOdcinku(1, 0, 1, 5, 1, 3));  // true - odcinek pionowy
        System.out.println(naOdcinku(1, 0, 1, 5, 1, 6));  // false
        System.out.println(naOdcinku(2, 2, 2, 2, 2, 2));  // true - odcinek zdegenerowany do punktu
    }
}
```
</details>

<a name="odcinki"></a>
## Przecinanie się odcinków [⬆️](#)
<details><summary>Rozwiń</summary>

Odcinki AB i CD przecinają się, gdy końce C i D leżą po przeciwnych stronach prostej AB, a jednocześnie końce A i B leżą po przeciwnych stronach prostej CD. Osobno sprawdzamy przypadki szczególne, gdy koniec jednego odcinka leży na drugim odcinku.

```python
def wyznacznik(A, B, C):  # iloczyn wektorowy AB x AC
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])


def na_odcinku(A, B, C):  # czy punkt C należy do odcinka AB
    if wyznacznik(A, B, C) != 0:
        return False
    return (min(A[0], B[0]) <= C[0] <= max(A[0], B[0])
            and min(A[1], B[1]) <= C[1] <= max(A[1], B[1]))


def przecinaja_sie(A, B, C, D):  # czy odcinki AB i CD mają punkt wspólny
    w1 = wyznacznik(A, B, C)
    w2 = wyznacznik(A, B, D)
    w3 = wyznacznik(C, D, A)
    w4 = wyznacznik(C, D, B)
    if w1 * w2 < 0 and w3 * w4 < 0:  # przypadek ogólny
        return True
    # przypadki szczególne: koniec jednego odcinka leży na drugim
    if na_odcinku(A, B, C) or na_odcinku(A, B, D) or na_odcinku(C, D, A) or na_odcinku(C, D, B):
        return True
    return False


print(przecinaja_sie((0, 0), (4, 4), (0, 4), (4, 0)))  # True
print(przecinaja_sie((0, 0), (1, 1), (2, 2), (3, 3)))  # False
```
<b>

```
A, B - końce pierwszego odcinka
C, D - końce drugiego odcinka

def przecinaja_sie(A, B, C, D):
	w1 <- wyznacznik(A, B, C)
	w2 <- wyznacznik(A, B, D)
	w3 <- wyznacznik(C, D, A)
	w4 <- wyznacznik(C, D, B)
	Jeżeli w1 * w2 < 0 oraz w3 * w4 < 0
		Zwróć Prawdę
	Jeżeli na_odcinku(A, B, C) lub na_odcinku(A, B, D) lub na_odcinku(C, D, A) lub na_odcinku(C, D, B)
		Zwróć Prawdę
	Zwróć Fałsz
```
</b>

```cpp
// C++23
#include <algorithm>
#include <print>

struct Punkt {
    long long x, y;
};

long long wyznacznik(Punkt A, Punkt B, Punkt C) {  // iloczyn wektorowy AB x AC
    return (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x);
}

bool na_odcinku(Punkt A, Punkt B, Punkt C) {  // czy punkt C należy do odcinka AB
    if (wyznacznik(A, B, C) != 0)
        return false;
    return std::min(A.x, B.x) <= C.x && C.x <= std::max(A.x, B.x)
        && std::min(A.y, B.y) <= C.y && C.y <= std::max(A.y, B.y);
}

bool przecinaja_sie(Punkt A, Punkt B, Punkt C, Punkt D) {  // czy odcinki AB i CD mają punkt wspólny
    long long w1 = wyznacznik(A, B, C);
    long long w2 = wyznacznik(A, B, D);
    long long w3 = wyznacznik(C, D, A);
    long long w4 = wyznacznik(C, D, B);
    if (w1 * w2 < 0 && w3 * w4 < 0)  // przypadek ogólny
        return true;
    // przypadki szczególne: koniec jednego odcinka leży na drugim
    return na_odcinku(A, B, C) || na_odcinku(A, B, D) || na_odcinku(C, D, A) || na_odcinku(C, D, B);
}

int main() {
    std::println("{}", przecinaja_sie({0, 0}, {4, 4}, {0, 4}, {4, 0}));  // true - "iks"
    std::println("{}", przecinaja_sie({0, 0}, {1, 1}, {2, 2}, {3, 3}));  // false - na jednej prostej, rozłączne
    std::println("{}", przecinaja_sie({0, 0}, {4, 0}, {2, 0}, {2, 5}));  // true - litera T
    std::println("{}", przecinaja_sie({0, 0}, {2, 2}, {2, 2}, {4, 0}));  // true - wspólny koniec
    std::println("{}", przecinaja_sie({0, 0}, {4, 0}, {0, 1}, {4, 1}));  // false - równoległe
    std::println("{}", przecinaja_sie({0, 0}, {3, 0}, {2, 0}, {5, 0}));  // true - nachodzą na siebie
    std::println("{}", przecinaja_sie({0, 0}, {2, 2}, {3, 0}, {3, 5}));  // false
}
```

```java
// Java 25
public class PrzecinanieOdcinkow {
    record Punkt(long x, long y) {}

    static long wyznacznik(Punkt A, Punkt B, Punkt C) {  // iloczyn wektorowy AB x AC
        return (B.x() - A.x()) * (C.y() - A.y()) - (B.y() - A.y()) * (C.x() - A.x());
    }

    static boolean naOdcinku(Punkt A, Punkt B, Punkt C) {  // czy punkt C należy do odcinka AB
        if (wyznacznik(A, B, C) != 0)
            return false;
        return Math.min(A.x(), B.x()) <= C.x() && C.x() <= Math.max(A.x(), B.x())
            && Math.min(A.y(), B.y()) <= C.y() && C.y() <= Math.max(A.y(), B.y());
    }

    static boolean przecinajaSie(Punkt A, Punkt B, Punkt C, Punkt D) {  // czy odcinki AB i CD mają punkt wspólny
        long w1 = wyznacznik(A, B, C);
        long w2 = wyznacznik(A, B, D);
        long w3 = wyznacznik(C, D, A);
        long w4 = wyznacznik(C, D, B);
        if (w1 * w2 < 0 && w3 * w4 < 0)  // przypadek ogólny
            return true;
        // przypadki szczególne: koniec jednego odcinka leży na drugim
        return naOdcinku(A, B, C) || naOdcinku(A, B, D) || naOdcinku(C, D, A) || naOdcinku(C, D, B);
    }

    static boolean test(long ax, long ay, long bx, long by, long cx, long cy, long dx, long dy) {
        return przecinajaSie(new Punkt(ax, ay), new Punkt(bx, by), new Punkt(cx, cy), new Punkt(dx, dy));
    }

    public static void main(String[] args) {
        System.out.println(test(0, 0, 4, 4, 0, 4, 4, 0));  // true - "iks"
        System.out.println(test(0, 0, 1, 1, 2, 2, 3, 3));  // false - na jednej prostej, rozłączne
        System.out.println(test(0, 0, 4, 0, 2, 0, 2, 5));  // true - litera T
        System.out.println(test(0, 0, 2, 2, 2, 2, 4, 0));  // true - wspólny koniec
        System.out.println(test(0, 0, 4, 0, 0, 1, 4, 1));  // false - równoległe
        System.out.println(test(0, 0, 3, 0, 2, 0, 5, 0));  // true - nachodzą na siebie
        System.out.println(test(0, 0, 2, 2, 3, 0, 3, 5));  // false
    }
}
```
</details>

<a name="punkt_wielokat"></a>
## Punkt w wielokącie [⬆️](#)
<details><summary>Rozwiń</summary>

Metoda półprostej (ray casting): z punktu P prowadzimy poziomą półprostą w prawo i liczymy, ile boków wielokąta przecina. Nieparzysta liczba przecięć - punkt leży wewnątrz, parzysta - na zewnątrz. Działa także dla wielokątów wklęsłych. Punkt leżący na brzegu traktujemy jako należący do obszaru.

```python
def wyznacznik(A, B, C):  # iloczyn wektorowy AB x AC
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])


def na_odcinku(A, B, C):  # czy punkt C należy do odcinka AB
    if wyznacznik(A, B, C) != 0:
        return False
    return (min(A[0], B[0]) <= C[0] <= max(A[0], B[0])
            and min(A[1], B[1]) <= C[1] <= max(A[1], B[1]))


def w_wielokacie(P, wielokat):  # wielokat - lista kolejnych wierzchołków
    x, y = P
    n = len(wielokat)
    wewnatrz = False
    for i in range(n):
        A = wielokat[i]
        B = wielokat[(i + 1) % n]  # ostatni wierzchołek łączy się z pierwszym
        if na_odcinku(A, B, P):
            return True  # punkt na brzegu
        if (A[1] > y) != (B[1] > y):  # bok przecina poziomą prostą y = P.y
            x_przeciecia = A[0] + (y - A[1]) * (B[0] - A[0]) / (B[1] - A[1])
            if x_przeciecia > x:  # przecięcie leży na prawo od P
                wewnatrz = not wewnatrz
    return wewnatrz


kwadrat = [(0, 0), (4, 0), (4, 4), (0, 4)]
print(w_wielokacie((2, 2), kwadrat))  # True
print(w_wielokacie((5, 2), kwadrat))  # False
```
<b>

```
P = (x, y) - badany punkt
W[0..n-1] - kolejne wierzchołki wielokąta

def w_wielokacie(P, W):
	wewnatrz <- Fałsz
	Dla i = 0, 1, ... n - 1
		A <- W[i]
		B <- W[(i + 1) mod n]
		Jeżeli na_odcinku(A, B, P)
			Zwróć Prawdę
		Jeżeli (yA > y) != (yB > y)
			x_przeciecia <- xA + (y - yA) * (xB - xA) / (yB - yA)
			Jeżeli x_przeciecia > x
				wewnatrz <- nie wewnatrz
	Zwróć wewnatrz
```
</b>

```cpp
// C++23
#include <algorithm>
#include <print>
#include <vector>

struct Punkt {
    long long x, y;
};

long long wyznacznik(Punkt A, Punkt B, Punkt C) {  // iloczyn wektorowy AB x AC
    return (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x);
}

bool na_odcinku(Punkt A, Punkt B, Punkt C) {  // czy punkt C należy do odcinka AB
    if (wyznacznik(A, B, C) != 0)
        return false;
    return std::min(A.x, B.x) <= C.x && C.x <= std::max(A.x, B.x)
        && std::min(A.y, B.y) <= C.y && C.y <= std::max(A.y, B.y);
}

bool w_wielokacie(Punkt P, const std::vector<Punkt>& wielokat) {  // wielokat - kolejne wierzchołki
    int n = std::ssize(wielokat);
    bool wewnatrz = false;
    for (int i = 0; i < n; i++) {
        Punkt A = wielokat[i];
        Punkt B = wielokat[(i + 1) % n];  // ostatni wierzchołek łączy się z pierwszym
        if (na_odcinku(A, B, P))
            return true;  // punkt na brzegu
        if ((A.y > P.y) != (B.y > P.y)) {  // bok przecina poziomą prostą y = P.y
            double x_przeciecia = A.x + static_cast<double>(P.y - A.y) * (B.x - A.x) / (B.y - A.y);
            if (x_przeciecia > P.x)  // przecięcie leży na prawo od P
                wewnatrz = !wewnatrz;
        }
    }
    return wewnatrz;
}

int main() {
    std::vector<Punkt> kwadrat = {{0, 0}, {4, 0}, {4, 4}, {0, 4}};
    std::println("{}", w_wielokacie({2, 2}, kwadrat));  // true
    std::println("{}", w_wielokacie({5, 2}, kwadrat));  // false
    std::println("{} {}", w_wielokacie({4, 2}, kwadrat), w_wielokacie({0, 0}, kwadrat));  // brzeg i wierzchołek

    std::vector<Punkt> wklesly = {{0, 0}, {6, 0}, {6, 6}, {3, 2}, {0, 6}};  // wielokąt z "wcięciem" od góry
    for (Punkt P : std::vector<Punkt>{{3, 4}, {1, 4}, {3, 1}, {5, 5}, {-1, 0}, {3, 2}, {7, 3}})
        std::println("({}, {}) {}", P.x, P.y, w_wielokacie(P, wklesly));
}
```

```java
// Java 25
import java.util.List;

public class PunktWWielokacie {
    record Punkt(long x, long y) {}

    static long wyznacznik(Punkt A, Punkt B, Punkt C) {  // iloczyn wektorowy AB x AC
        return (B.x() - A.x()) * (C.y() - A.y()) - (B.y() - A.y()) * (C.x() - A.x());
    }

    static boolean naOdcinku(Punkt A, Punkt B, Punkt C) {  // czy punkt C należy do odcinka AB
        if (wyznacznik(A, B, C) != 0)
            return false;
        return Math.min(A.x(), B.x()) <= C.x() && C.x() <= Math.max(A.x(), B.x())
            && Math.min(A.y(), B.y()) <= C.y() && C.y() <= Math.max(A.y(), B.y());
    }

    static boolean wWielokacie(Punkt P, List<Punkt> wielokat) {  // wielokat - kolejne wierzchołki
        int n = wielokat.size();
        boolean wewnatrz = false;
        for (int i = 0; i < n; i++) {
            Punkt A = wielokat.get(i);
            Punkt B = wielokat.get((i + 1) % n);  // ostatni wierzchołek łączy się z pierwszym
            if (naOdcinku(A, B, P))
                return true;  // punkt na brzegu
            if ((A.y() > P.y()) != (B.y() > P.y())) {  // bok przecina poziomą prostą y = P.y
                double xPrzeciecia = A.x() + (double) (P.y() - A.y()) * (B.x() - A.x()) / (B.y() - A.y());
                if (xPrzeciecia > P.x())  // przecięcie leży na prawo od P
                    wewnatrz = !wewnatrz;
            }
        }
        return wewnatrz;
    }

    public static void main(String[] args) {
        var kwadrat = List.of(new Punkt(0, 0), new Punkt(4, 0), new Punkt(4, 4), new Punkt(0, 4));
        System.out.println(wWielokacie(new Punkt(2, 2), kwadrat));  // true
        System.out.println(wWielokacie(new Punkt(5, 2), kwadrat));  // false
        System.out.println(wWielokacie(new Punkt(4, 2), kwadrat) + " " + wWielokacie(new Punkt(0, 0), kwadrat));  // brzeg i wierzchołek

        // wielokąt z "wcięciem" od góry
        var wklesly = List.of(new Punkt(0, 0), new Punkt(6, 0), new Punkt(6, 6), new Punkt(3, 2), new Punkt(0, 6));
        long[][] punkty = {{3, 4}, {1, 4}, {3, 1}, {5, 5}, {-1, 0}, {3, 2}, {7, 3}};
        for (long[] p : punkty)
            System.out.println("(" + p[0] + ", " + p[1] + ") " + wWielokacie(new Punkt(p[0], p[1]), wklesly));
    }
}
```
</details>

<a name="koch"></a>
## Krzywa Kocha [⬆️](#)
<details><summary>Rozwiń</summary>

Krzywa Kocha stopnia 0 to odcinek. Krzywą stopnia k otrzymujemy, dzieląc odcinek na 3 równe części i zastępując środkową częścią dwoma bokami trójkąta równobocznego - każdy z 4 nowych odcinków rysujemy jako krzywą stopnia k - 1. Trzy krzywe Kocha narysowane na bokach trójkąta równobocznego tworzą płatek Kocha.

```python
import turtle


def koch(dlugosc, stopien):
    if stopien == 0:
        turtle.forward(dlugosc)
        return
    dlugosc /= 3
    koch(dlugosc, stopien - 1)
    turtle.left(60)
    koch(dlugosc, stopien - 1)
    turtle.right(120)
    koch(dlugosc, stopien - 1)
    turtle.left(60)
    koch(dlugosc, stopien - 1)


turtle.speed(0)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
koch(400, 3)
# płatek Kocha: for _ in range(3): koch(400, 3); turtle.right(120)
turtle.done()
```
<b>

```
dlugosc - długość odcinka
stopien - stopień krzywej

def koch(dlugosc, stopien):
	Jeżeli stopien == 0
		Narysuj odcinek o długości dlugosc
		Zakończ
	koch(dlugosc / 3, stopien - 1)
	Obróć w lewo o 60 stopni
	koch(dlugosc / 3, stopien - 1)
	Obróć w prawo o 120 stopni
	koch(dlugosc / 3, stopien - 1)
	Obróć w lewo o 60 stopni
	koch(dlugosc / 3, stopien - 1)
```
</b>

```cpp
// C++23
#include <algorithm>
#include <cmath>
#include <fstream>
#include <numbers>
#include <ostream>
#include <print>
#include <string>
#include <vector>

struct Punkt {
    double x, y;
};

// prosty "żółw" jak w module turtle: pozycja, kierunek w stopniach (0 = w prawo) i narysowana łamana
struct Zolw {
    double x = 0, y = 0, kat = 0;
    std::vector<Punkt> punkty;

    void forward(double d) {
        x += d * std::cos(kat * std::numbers::pi / 180);
        y += d * std::sin(kat * std::numbers::pi / 180);
        punkty.push_back({x, y});
    }
    void left(double k) { kat += k; }
    void right(double k) { kat -= k; }
};

void koch(Zolw& zolw, double dlugosc, int stopien) {
    if (stopien == 0) {
        zolw.forward(dlugosc);
        return;
    }
    dlugosc /= 3;
    koch(zolw, dlugosc, stopien - 1);
    zolw.left(60);
    koch(zolw, dlugosc, stopien - 1);
    zolw.right(120);
    koch(zolw, dlugosc, stopien - 1);
    zolw.left(60);
    koch(zolw, dlugosc, stopien - 1);
}

// zapisuje łamaną do pliku SVG (otwórz go w przeglądarce)
void zapisz_svg(const std::vector<Punkt>& punkty, const std::string& nazwa) {
    double min_x = punkty[0].x, max_x = punkty[0].x, min_y = punkty[0].y, max_y = punkty[0].y;
    for (auto [x, y] : punkty) {
        min_x = std::min(min_x, x);
        max_x = std::max(max_x, x);
        min_y = std::min(min_y, y);
        max_y = std::max(max_y, y);
    }
    std::ofstream plik(nazwa);
    // w SVG oś y jest skierowana w dół, dlatego zapisujemy -y
    std::println(plik, R"(<svg xmlns="http://www.w3.org/2000/svg" viewBox="{:.0f} {:.0f} {:.0f} {:.0f}">)",
                 min_x - 10, -max_y - 10, max_x - min_x + 20, max_y - min_y + 20);
    std::print(plik, R"(<polyline fill="none" stroke="black" points=")");
    for (auto [x, y] : punkty)
        std::print(plik, "{:.2f},{:.2f} ", x, -y);
    std::println(plik, R"("/>)");
    std::println(plik, "</svg>");

    std::println("odcinki: {}", punkty.size() - 1);
    std::println("koniec: ({}, {})", std::lround(punkty.back().x), std::lround(punkty.back().y));
    std::println("x: [{}, {}], y: [{}, {}]", std::lround(min_x), std::lround(max_x), std::lround(min_y), std::lround(max_y));
    std::println("zapisano: {}", nazwa);
}

int main() {
    Zolw zolw;
    zolw.x = -200;  // jak turtle.goto(-200, 0)
    zolw.y = 0;
    zolw.punkty.push_back({zolw.x, zolw.y});
    koch(zolw, 400, 3);
    // płatek Kocha: for (int i = 0; i < 3; i++) { koch(zolw, 400, 3); zolw.right(120); }
    zapisz_svg(zolw.punkty, "koch.svg");
}
```

```java
// Java 25
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class KrzywaKocha {
    record Punkt(double x, double y) {}

    // prosty "żółw" jak w module turtle: pozycja, kierunek w stopniach (0 = w prawo) i narysowana łamana
    static class Zolw {
        double x, y, kat;
        List<Punkt> punkty = new ArrayList<>();

        Zolw(double x, double y) {
            this.x = x;
            this.y = y;
            punkty.add(new Punkt(x, y));
        }

        void forward(double d) {
            x += d * Math.cos(Math.toRadians(kat));
            y += d * Math.sin(Math.toRadians(kat));
            punkty.add(new Punkt(x, y));
        }

        void left(double k) { kat += k; }

        void right(double k) { kat -= k; }
    }

    static void koch(Zolw zolw, double dlugosc, int stopien) {
        if (stopien == 0) {
            zolw.forward(dlugosc);
            return;
        }
        dlugosc /= 3;
        koch(zolw, dlugosc, stopien - 1);
        zolw.left(60);
        koch(zolw, dlugosc, stopien - 1);
        zolw.right(120);
        koch(zolw, dlugosc, stopien - 1);
        zolw.left(60);
        koch(zolw, dlugosc, stopien - 1);
    }

    // zapisuje łamaną do pliku SVG (otwórz go w przeglądarce)
    static void zapiszSvg(List<Punkt> punkty, String nazwa) throws IOException {
        double minX = punkty.getFirst().x(), maxX = minX, minY = punkty.getFirst().y(), maxY = minY;
        for (Punkt p : punkty) {
            minX = Math.min(minX, p.x());
            maxX = Math.max(maxX, p.x());
            minY = Math.min(minY, p.y());
            maxY = Math.max(maxY, p.y());
        }
        var svg = new StringBuilder();
        // w SVG oś y jest skierowana w dół, dlatego zapisujemy -y; Locale.ROOT - kropka zamiast przecinka
        svg.append(String.format(Locale.ROOT, "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"%.0f %.0f %.0f %.0f\">%n",
                minX - 10, -maxY - 10, maxX - minX + 20, maxY - minY + 20));
        svg.append("<polyline fill=\"none\" stroke=\"black\" points=\"");
        for (Punkt p : punkty)
            svg.append(String.format(Locale.ROOT, "%.2f,%.2f ", p.x(), -p.y()));
        svg.append("\"/>\n</svg>\n");
        Files.writeString(Path.of(nazwa), svg);

        System.out.println("odcinki: " + (punkty.size() - 1));
        System.out.println("koniec: (" + Math.round(punkty.getLast().x()) + ", " + Math.round(punkty.getLast().y()) + ")");
        System.out.println("x: [" + Math.round(minX) + ", " + Math.round(maxX) + "], y: [" + Math.round(minY) + ", " + Math.round(maxY) + "]");
        System.out.println("zapisano: " + nazwa);
    }

    public static void main(String[] args) throws IOException {
        var zolw = new Zolw(-200, 0);  // jak turtle.goto(-200, 0)
        koch(zolw, 400, 3);
        // płatek Kocha: for (int i = 0; i < 3; i++) { koch(zolw, 400, 3); zolw.right(120); }
        zapiszSvg(zolw.punkty, "koch.svg");
    }
}
```
</details>

<a name="pitagoras"></a>
## Drzewo Pitagorasa [⬆️](#)
<details><summary>Rozwiń</summary>

Rysujemy kwadrat, a na jego górnym boku trójkąt prostokątny równoramienny. Na przyprostokątnych tego trójkąta budujemy (rekurencyjnie) dwa mniejsze drzewa, każde z kwadratem o boku bok * √2 / 2. Funkcja zaczyna i kończy rysowanie w tym samym miejscu (lewy dolny róg kwadratu) i z tym samym kierunkiem żółwia - dzięki temu wywołania rekurencyjne nie psują sobie położenia.

```python
import turtle


def drzewo(bok, stopien):  # żółw stoi w lewym dolnym rogu kwadratu i patrzy "w górę" kwadratu
    if stopien == 0:
        return
    for _ in range(4):  # kwadrat rysowany w prawo od żółwia
        turtle.forward(bok)
        turtle.right(90)
    nowy_bok = bok * 2 ** 0.5 / 2
    turtle.forward(bok)              # lewy górny róg kwadratu
    turtle.left(45)
    drzewo(nowy_bok, stopien - 1)    # lewa gałąź
    turtle.right(90)
    turtle.forward(nowy_bok)         # wierzchołek trójkąta
    drzewo(nowy_bok, stopien - 1)    # prawa gałąź
    turtle.back(nowy_bok)            # powrót do punktu startu
    turtle.left(45)
    turtle.back(bok)


turtle.speed(0)
turtle.penup()
turtle.goto(-50, -250)
turtle.pendown()
turtle.left(90)  # żółw patrzy w górę
drzewo(100, 8)
turtle.done()
```
<b>

```
bok - długość boku kwadratu
stopien - liczba poziomów drzewa

def drzewo(bok, stopien):
	Jeżeli stopien == 0
		Zakończ
	Narysuj kwadrat o boku bok
	nowy_bok <- bok * pierwiastek(2) / 2
	Idź naprzód o bok
	Obróć w lewo o 45 stopni
	drzewo(nowy_bok, stopien - 1)
	Obróć w prawo o 90 stopni
	Idź naprzód o nowy_bok
	drzewo(nowy_bok, stopien - 1)
	Cofnij się o nowy_bok
	Obróć w lewo o 45 stopni
	Cofnij się o bok
```
</b>

```cpp
// C++23
#include <algorithm>
#include <cmath>
#include <fstream>
#include <numbers>
#include <ostream>
#include <print>
#include <string>
#include <vector>

struct Punkt {
    double x, y;
};

// prosty "żółw" jak w module turtle: pozycja, kierunek w stopniach (0 = w prawo) i narysowana łamana
struct Zolw {
    double x = 0, y = 0, kat = 0;
    std::vector<Punkt> punkty;

    void forward(double d) {
        x += d * std::cos(kat * std::numbers::pi / 180);
        y += d * std::sin(kat * std::numbers::pi / 180);
        punkty.push_back({x, y});
    }
    void back(double d) { forward(-d); }
    void left(double k) { kat += k; }
    void right(double k) { kat -= k; }
};

// żółw stoi w lewym dolnym rogu kwadratu i patrzy "w górę" kwadratu
void drzewo(Zolw& zolw, double bok, int stopien) {
    if (stopien == 0)
        return;
    for (int i = 0; i < 4; i++) {  // kwadrat rysowany w prawo od żółwia
        zolw.forward(bok);
        zolw.right(90);
    }
    double nowy_bok = bok * std::sqrt(2.0) / 2;
    zolw.forward(bok);                       // lewy górny róg kwadratu
    zolw.left(45);
    drzewo(zolw, nowy_bok, stopien - 1);     // lewa gałąź
    zolw.right(90);
    zolw.forward(nowy_bok);                  // wierzchołek trójkąta
    drzewo(zolw, nowy_bok, stopien - 1);     // prawa gałąź
    zolw.back(nowy_bok);                     // powrót do punktu startu
    zolw.left(45);
    zolw.back(bok);
}

// zapisuje łamaną do pliku SVG (otwórz go w przeglądarce)
void zapisz_svg(const std::vector<Punkt>& punkty, const std::string& nazwa) {
    double min_x = punkty[0].x, max_x = punkty[0].x, min_y = punkty[0].y, max_y = punkty[0].y;
    for (auto [x, y] : punkty) {
        min_x = std::min(min_x, x);
        max_x = std::max(max_x, x);
        min_y = std::min(min_y, y);
        max_y = std::max(max_y, y);
    }
    std::ofstream plik(nazwa);
    // w SVG oś y jest skierowana w dół, dlatego zapisujemy -y
    std::println(plik, R"(<svg xmlns="http://www.w3.org/2000/svg" viewBox="{:.0f} {:.0f} {:.0f} {:.0f}">)",
                 min_x - 10, -max_y - 10, max_x - min_x + 20, max_y - min_y + 20);
    std::print(plik, R"(<polyline fill="none" stroke="green" stroke-width="0.5" points=")");
    for (auto [x, y] : punkty)
        std::print(plik, "{:.2f},{:.2f} ", x, -y);
    std::println(plik, R"("/>)");
    std::println(plik, "</svg>");

    std::println("odcinki: {}", punkty.size() - 1);
    std::println("koniec: ({}, {})", std::lround(punkty.back().x), std::lround(punkty.back().y));
    std::println("x: [{}, {}], y: [{}, {}]", std::lround(min_x), std::lround(max_x), std::lround(min_y), std::lround(max_y));
    std::println("zapisano: {}", nazwa);
}

int main() {
    Zolw zolw;
    zolw.x = -50;  // jak turtle.goto(-50, -250)
    zolw.y = -250;
    zolw.kat = 90;  // żółw patrzy w górę
    zolw.punkty.push_back({zolw.x, zolw.y});
    drzewo(zolw, 100, 8);
    zapisz_svg(zolw.punkty, "drzewo.svg");
}
```

```java
// Java 25
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class DrzewoPitagorasa {
    record Punkt(double x, double y) {}

    // prosty "żółw" jak w module turtle: pozycja, kierunek w stopniach (0 = w prawo) i narysowana łamana
    static class Zolw {
        double x, y, kat;
        List<Punkt> punkty = new ArrayList<>();

        Zolw(double x, double y, double kat) {
            this.x = x;
            this.y = y;
            this.kat = kat;
            punkty.add(new Punkt(x, y));
        }

        void forward(double d) {
            x += d * Math.cos(Math.toRadians(kat));
            y += d * Math.sin(Math.toRadians(kat));
            punkty.add(new Punkt(x, y));
        }

        void back(double d) { forward(-d); }

        void left(double k) { kat += k; }

        void right(double k) { kat -= k; }
    }

    // żółw stoi w lewym dolnym rogu kwadratu i patrzy "w górę" kwadratu
    static void drzewo(Zolw zolw, double bok, int stopien) {
        if (stopien == 0)
            return;
        for (int i = 0; i < 4; i++) {  // kwadrat rysowany w prawo od żółwia
            zolw.forward(bok);
            zolw.right(90);
        }
        double nowyBok = bok * Math.sqrt(2) / 2;
        zolw.forward(bok);                    // lewy górny róg kwadratu
        zolw.left(45);
        drzewo(zolw, nowyBok, stopien - 1);   // lewa gałąź
        zolw.right(90);
        zolw.forward(nowyBok);                // wierzchołek trójkąta
        drzewo(zolw, nowyBok, stopien - 1);   // prawa gałąź
        zolw.back(nowyBok);                   // powrót do punktu startu
        zolw.left(45);
        zolw.back(bok);
    }

    // zapisuje łamaną do pliku SVG (otwórz go w przeglądarce)
    static void zapiszSvg(List<Punkt> punkty, String nazwa) throws IOException {
        double minX = punkty.getFirst().x(), maxX = minX, minY = punkty.getFirst().y(), maxY = minY;
        for (Punkt p : punkty) {
            minX = Math.min(minX, p.x());
            maxX = Math.max(maxX, p.x());
            minY = Math.min(minY, p.y());
            maxY = Math.max(maxY, p.y());
        }
        var svg = new StringBuilder();
        // w SVG oś y jest skierowana w dół, dlatego zapisujemy -y; Locale.ROOT - kropka zamiast przecinka
        svg.append(String.format(Locale.ROOT, "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"%.0f %.0f %.0f %.0f\">%n",
                minX - 10, -maxY - 10, maxX - minX + 20, maxY - minY + 20));
        svg.append("<polyline fill=\"none\" stroke=\"green\" stroke-width=\"0.5\" points=\"");
        for (Punkt p : punkty)
            svg.append(String.format(Locale.ROOT, "%.2f,%.2f ", p.x(), -p.y()));
        svg.append("\"/>\n</svg>\n");
        Files.writeString(Path.of(nazwa), svg);

        System.out.println("odcinki: " + (punkty.size() - 1));
        System.out.println("koniec: (" + Math.round(punkty.getLast().x()) + ", " + Math.round(punkty.getLast().y()) + ")");
        System.out.println("x: [" + Math.round(minX) + ", " + Math.round(maxX) + "], y: [" + Math.round(minY) + ", " + Math.round(maxY) + "]");
        System.out.println("zapisano: " + nazwa);
    }

    public static void main(String[] args) throws IOException {
        var zolw = new Zolw(-50, -250, 90);  // jak turtle.goto(-50, -250) i turtle.left(90)
        drzewo(zolw, 100, 8);
        zapiszSvg(zolw.punkty, "drzewo.svg");
    }
}
```
</details>

[py]: https://img.shields.io/badge/Python-%E2%9C%94-green?style=flat-square&logo=python
[notpy]: https://img.shields.io/badge/Python-%E2%9C%98-red?style=flat-square&logo=python

[java]: https://img.shields.io/badge/Java-%E2%9C%94-green?style=flat-square&logo=Java&logoColor=yellow
[nojava]: https://img.shields.io/badge/Java-%E2%9C%98-red?style=flat-square&logo=Java&logoColor=yellow

[c++]: https://img.shields.io/badge/C++-%E2%9C%94-green?style=flat-square&logo=c%2B%2B&logoColor=blue
[noc++]: https://img.shields.io/badge/C++-%E2%9C%98-red?style=flat-square&logo=c%2B%2B&logoColor=blue 
