<h1 align="center">Matura 2023 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-stara-rozszerzona-odpowiedzi.pdf)

> Pliki do zadania 4 są w archiwum w folderze `DANE/DANE_E`.

## 1.1 i 1.2

> **Treść zadania:** Dwie dodatnie liczby całkowite a i b są *przyjaciółkami*, gdy mają taką samą sumę cyfr. Są *dobrymi przyjaciółkami*, gdy są przyjaciółkami i dodatkowo pierwsza cyfra jednej z nich jest równa ostatniej cyfrze drugiej (pierwsza cyfra a = ostatnia cyfra b lub pierwsza cyfra b = ostatnia cyfra a). Np. 15 i 24 są przyjaciółkami, ale nie dobrymi; 124 i 61 oraz 431 i 17 są dobrymi przyjaciółkami.
>
> - 1.1 — Uzupełnij tabelę: dla par (131, 50), (416, 84), (32, 221) podaj sumy cyfr obu liczb oraz czy są przyjaciółkami i czy są dobrymi przyjaciółkami (PRAWDA/FAŁSZ). Przykład: 433 i 352 — sumy 10 i 10, PRAWDA, PRAWDA.
> - 1.2 — Zapisz w pseudokodzie lub języku programowania algorytm, który dla dodatnich liczb całkowitych a, b zwraca PRAWDA, gdy są dobrymi przyjaciółkami, a FAŁSZ w przeciwnym razie. Wolno używać tylko operacji arytmetycznych (w tym `div` i `mod`), porównań, instrukcji sterujących i własnych funkcji — bez funkcji wbudowanych i bez zamiany liczb na napisy.

```py
def suma_cyfr(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


# 1.2 - tylko operacje na liczbach całkowitych
def dobre_przyjaciolki(a, b):
    ostatnia_a = a % 10
    ostatnia_b = b % 10
    suma_a = 0
    while a > 0:
        if a < 10:
            pierwsza_a = a
        suma_a += a % 10
        a //= 10
    suma_b = 0
    while b > 0:
        if b < 10:
            pierwsza_b = b
        suma_b += b % 10
        b //= 10
    if suma_a != suma_b:
        return False
    return pierwsza_a == ostatnia_b or pierwsza_b == ostatnia_a


# 1.1
for a, b in [(131, 50), (416, 84), (32, 221)]:
    print(a, b, suma_cyfr(a), suma_cyfr(b), suma_cyfr(a) == suma_cyfr(b), dobre_przyjaciolki(a, b))
```
```cpp
// C++23
#include <print>
#include <string>

int suma_cyfr(int x) {
    int s = 0;
    while (x > 0) {
        s += x % 10;
        x /= 10;
    }
    return s;
}

// 1.2 - tylko operacje na liczbach całkowitych
bool dobre_przyjaciolki(int a, int b) {
    int ostatnia_a = a % 10;
    int ostatnia_b = b % 10;
    int pierwsza_a = 0, pierwsza_b = 0;
    int suma_a = 0;
    while (a > 0) {
        if (a < 10) pierwsza_a = a;
        suma_a += a % 10;
        a /= 10;
    }
    int suma_b = 0;
    while (b > 0) {
        if (b < 10) pierwsza_b = b;
        suma_b += b % 10;
        b /= 10;
    }
    if (suma_a != suma_b) return false;
    return pierwsza_a == ostatnia_b || pierwsza_b == ostatnia_a;
}

// wartość logiczna zapisana jak w Pythonie
std::string tekst(bool b) { return b ? "True" : "False"; }

int main() {
    // 1.1
    int dane[3][2] = {{131, 50}, {416, 84}, {32, 221}};
    for (auto& [a, b] : dane)
        std::println("{} {} {} {} {} {}", a, b, suma_cyfr(a), suma_cyfr(b),
                     tekst(suma_cyfr(a) == suma_cyfr(b)), tekst(dobre_przyjaciolki(a, b)));
}
```
```java
// Java 25
public class Zadanie {
    static int sumaCyfr(int x) {
        int s = 0;
        while (x > 0) {
            s += x % 10;
            x /= 10;
        }
        return s;
    }

    // 1.2 - tylko operacje na liczbach całkowitych
    static boolean dobrePrzyjaciolki(int a, int b) {
        int ostatniaA = a % 10;
        int ostatniaB = b % 10;
        int pierwszaA = 0, pierwszaB = 0;
        int sumaA = 0;
        while (a > 0) {
            if (a < 10) pierwszaA = a;
            sumaA += a % 10;
            a /= 10;
        }
        int sumaB = 0;
        while (b > 0) {
            if (b < 10) pierwszaB = b;
            sumaB += b % 10;
            b /= 10;
        }
        if (sumaA != sumaB) return false;
        return pierwszaA == ostatniaB || pierwszaB == ostatniaA;
    }

    // wartość logiczna zapisana jak w Pythonie
    static String tekst(boolean b) { return b ? "True" : "False"; }

    public static void main(String[] args) throws Exception {
        // 1.1
        int[][] dane = {{131, 50}, {416, 84}, {32, 221}};
        for (var d : dane) {
            int a = d[0], b = d[1];
            System.out.println(a + " " + b + " " + sumaCyfr(a) + " " + sumaCyfr(b) + " "
                    + tekst(sumaCyfr(a) == sumaCyfr(b)) + " " + tekst(dobrePrzyjaciolki(a, b)));
        }
    }
}
```

**Odpowiedź:** 1.1: 131 i 50: 5, 5, PRAWDA, FAŁSZ; 416 i 84: 11, 12, FAŁSZ, FAŁSZ; 32 i 221: 5, 5, PRAWDA, PRAWDA. 1.2: funkcja `dobre_przyjaciolki`.

## 2.1, 2.2 i 2.3

> **Treść zadania:** Dany jest rekurencyjny algorytm mnożenia dodatnich liczb całkowitych x, y, używający tylko dodawania i dzielenia całkowitego przez 2:
>
> ```
> iloczyn(x, y):
>     jeżeli y = 1: wynikiem jest x
>     w przeciwnym razie:
>         k ← y div 2
>         z ← iloczyn(x, k)
>         jeżeli y mod 2 = 0: wynikiem jest z + z
>         w przeciwnym razie: wynikiem jest x + z + z
> ```
>
> Interesuje nas liczba operacji dodawania wykonanych przy obliczaniu iloczyn(x, y) (np. iloczyn(9, 11) wykonuje 5 dodawań).
>
> - 2.1 — Uzupełnij tabelę kolejnych wywołań (x, y, k, z, wynik) dla iloczyn(10, 45) — łącznie 6 wywołań, ostatnie z y = 1.
> - 2.2 — Podaj liczbę dodawań wykonanych dla par (x, y): (9, 11), (8, 32), (2, 47), (112, 112).
> - 2.3 — Uzupełnij trzy luki w iteracyjnej wersji algorytmu (wynik z = x·y; wolno używać tylko dodawania, odejmowania, `div` i `mod`, bez mnożenia):
>
> ```
> z ← ____
> dopóki ____ wykonuj
>     jeżeli y mod 2 = 1: z ← z + x
>     x ← x + x
>     y ← ____
> ```

```py
dodawania = 0


def iloczyn(x, y):
    global dodawania
    if y == 1:
        return x
    k = y // 2
    z = iloczyn(x, k)
    if y % 2 == 0:
        dodawania += 1
        wynik = z + z
    else:
        dodawania += 2
        wynik = x + z + z
    print(x, y, k, z, wynik)        # 2.1 - wiersz tabeli (wypisywane od najgłębszego wywołania)
    return wynik


# 2.3 - wersja iteracyjna
def iloczyn_iter(x, y):
    z = 0
    while y >= 1:
        if y % 2 == 1:
            z = z + x
        x = x + x
        y = y // 2
    return z


# 2.1
iloczyn(10, 45)

# 2.2
for x, y in [(9, 11), (8, 32), (2, 47), (112, 112)]:
    dodawania = 0
    iloczyn(x, y)
    print("liczba dodawań:", x, y, dodawania)

# 2.3 - sprawdzenie
print(all(iloczyn_iter(x, y) == x * y for x in range(1, 50) for y in range(1, 50)))
```
```cpp
// C++23
#include <print>

int dodawania = 0;

long long iloczyn(long long x, long long y) {
    if (y == 1) return x;
    long long k = y / 2;
    long long z = iloczyn(x, k);
    long long wynik;
    if (y % 2 == 0) {
        dodawania += 1;
        wynik = z + z;
    } else {
        dodawania += 2;
        wynik = x + z + z;
    }
    std::println("{} {} {} {} {}", x, y, k, z, wynik);  // 2.1 - wiersz tabeli (wypisywane od najgłębszego wywołania)
    return wynik;
}

// 2.3 - wersja iteracyjna
long long iloczyn_iter(long long x, long long y) {
    long long z = 0;
    while (y >= 1) {
        if (y % 2 == 1) z = z + x;
        x = x + x;
        y = y / 2;
    }
    return z;
}

int main() {
    // 2.1
    iloczyn(10, 45);

    // 2.2
    int dane[4][2] = {{9, 11}, {8, 32}, {2, 47}, {112, 112}};
    for (auto& [x, y] : dane) {
        dodawania = 0;
        iloczyn(x, y);
        std::println("liczba dodawań: {} {} {}", x, y, dodawania);
    }

    // 2.3 - sprawdzenie
    bool wszystkie = true;
    for (int x = 1; x < 50; x++)
        for (int y = 1; y < 50; y++)
            if (iloczyn_iter(x, y) != x * y) wszystkie = false;
    std::println("{}", wszystkie ? "True" : "False");
}
```
```java
// Java 25
public class Zadanie {
    static int dodawania = 0;

    static long iloczyn(long x, long y) {
        if (y == 1) return x;
        long k = y / 2;
        long z = iloczyn(x, k);
        long wynik;
        if (y % 2 == 0) {
            dodawania += 1;
            wynik = z + z;
        } else {
            dodawania += 2;
            wynik = x + z + z;
        }
        System.out.println(x + " " + y + " " + k + " " + z + " " + wynik);  // 2.1 - wiersz tabeli (od najgłębszego wywołania)
        return wynik;
    }

    // 2.3 - wersja iteracyjna
    static long iloczynIter(long x, long y) {
        long z = 0;
        while (y >= 1) {
            if (y % 2 == 1) z = z + x;
            x = x + x;
            y = y / 2;
        }
        return z;
    }

    public static void main(String[] args) throws Exception {
        // 2.1
        iloczyn(10, 45);

        // 2.2
        int[][] dane = {{9, 11}, {8, 32}, {2, 47}, {112, 112}};
        for (var d : dane) {
            dodawania = 0;
            iloczyn(d[0], d[1]);
            System.out.println("liczba dodawań: " + d[0] + " " + d[1] + " " + dodawania);
        }

        // 2.3 - sprawdzenie
        boolean wszystkie = true;
        for (int x = 1; x < 50; x++)
            for (int y = 1; y < 50; y++)
                if (iloczynIter(x, y) != x * y) wszystkie = false;
        System.out.println(wszystkie ? "True" : "False");
    }
}
```

**Odpowiedź:** 2.1: (x, y, k, z, wynik): (10, 45, 22, 220, 450), (10, 22, 11, 110, 220), (10, 11, 5, 50, 110), (10, 5, 2, 20, 50), (10, 2, 1, 10, 20), (10, 1, –, –, 10). 2.2: 5, 5, 9, 8. 2.3: `z ← 0`, `dopóki y ≥ 1` (tzn. y > 0), `y ← y div 2`.

## 4.1, 4.2, 4.3 i 4.4

> **Treść zadania:** Plik `anagram.txt` zawiera 1000 wierszy, w każdym liczbę binarną o co najwyżej 14 cyfrach, zaczynającą się od 1; liczby się nie powtarzają. Odpowiedzi zapisz w pliku `wyniki4.txt`, poprzedzając każdą numerem zadania (plik `przyklad.txt` zawiera 100 przykładowych wierszy).
>
> - 4.1 — Liczba jest *zrównoważona*, gdy ma tyle samo zer i jedynek, a *prawie zrównoważona*, gdy liczby jedynek i zer różnią się o 1. Podaj, ile jest liczb zrównoważonych i ile prawie zrównoważonych (dla przykładu: 21 i 15).
> - 4.2 — Anagram to liczba utworzona z tych samych cyfr w innej kolejności, bez zera na początku (np. z 11100 da się utworzyć 6 anagramów). Wypisz, w kolejności z pliku, wszystkie 8-cyfrowe liczby binarne, z których można utworzyć największą liczbę anagramów.
> - 4.3 — Podaj największą wartość bezwzględną różnicy między liczbami z sąsiednich wierszy pliku, zapisaną binarnie (dla przykładu: 1110001010).
> - 4.4 — Zamień wszystkie liczby na system dziesiętny, a następnie: a) podaj, ile z nich nie zawiera cyfry 0; b) podaj liczbę o największej sumie *różnych* cyfr (np. dla 20462 suma ta wynosi 12); przy remisie — pierwszą w pliku. Dla przykładu: 81 i 895.

```py
with open("anagram.txt") as file:
    liczby = [linia.strip() for linia in file if linia.strip()]

wynik = open("wyniki4.txt", "w")

# 4.1
zrownowazone = 0
prawie = 0
for liczba in liczby:
    roznica = abs(liczba.count("1") - liczba.count("0"))
    if roznica == 0:
        zrownowazone += 1
    elif roznica == 1:
        prawie += 1
print("4.1", zrownowazone, prawie, file=wynik)


# 4.2 - pierwsza cyfra musi być 1, pozostałe jedynki rozmieszczamy na 7 miejscach: C(7, jedynki - 1)
def silnia(n):
    s = 1
    for i in range(2, n + 1):
        s *= i
    return s


def anagramy(liczba):
    reszta = len(liczba) - 1
    jedynki = liczba.count("1") - 1
    return silnia(reszta) // (silnia(jedynki) * silnia(reszta - jedynki))


osmiocyfrowe = [liczba for liczba in liczby if len(liczba) == 8]
najwiecej = max(anagramy(liczba) for liczba in osmiocyfrowe)
print("4.2", file=wynik)
for liczba in osmiocyfrowe:
    if anagramy(liczba) == najwiecej:
        print(liczba, file=wynik)

# 4.3
dziesietne = [int(liczba, 2) for liczba in liczby]
najwieksza = 0
for i in range(1, len(dziesietne)):
    najwieksza = max(najwieksza, abs(dziesietne[i] - dziesietne[i - 1]))
print("4.3", bin(najwieksza)[2:], file=wynik)

# 4.4
bez_zera = 0
najlepsza = dziesietne[0]
for x in dziesietne:
    if "0" not in str(x):
        bez_zera += 1
    if sum(int(c) for c in set(str(x))) > sum(int(c) for c in set(str(najlepsza))):
        najlepsza = x
print("4.4", bez_zera, najlepsza, file=wynik)

wynik.close()
```
```cpp
// C++23
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <set>
#include <string>
#include <vector>

// 4.2 - pierwsza cyfra musi być 1, pozostałe jedynki rozmieszczamy na 7 miejscach: C(7, jedynki - 1)
long long silnia(int n) {
    long long s = 1;
    for (int i = 2; i <= n; i++) s *= i;
    return s;
}

long long anagramy(const std::string& liczba) {
    int reszta = liczba.size() - 1;
    int jedynki = std::count(liczba.begin(), liczba.end(), '1') - 1;
    return silnia(reszta) / (silnia(jedynki) * silnia(reszta - jedynki));
}

// suma różnych cyfr liczby (sum(int(c) for c in set(str(x))))
int suma_roznych_cyfr(long long x) {
    std::string s = std::to_string(x);
    std::set<char> rozne(s.begin(), s.end());
    int suma = 0;
    for (char c : rozne) suma += c - '0';
    return suma;
}

std::string na_dwojkowy(long long n) {
    if (n == 0) return "0";
    std::string wynik;
    while (n > 0) {
        wynik = char('0' + n % 2) + wynik;
        n /= 2;
    }
    return wynik;
}

int main() {
    std::vector<std::string> liczby;
    std::ifstream plik("anagram.txt");
    std::string linia;
    while (plik >> linia) liczby.push_back(linia);

    std::ofstream wynik("wyniki4.txt");

    // 4.1
    int zrownowazone = 0;
    int prawie = 0;
    for (auto& liczba : liczby) {
        int roznica = std::abs((int)std::count(liczba.begin(), liczba.end(), '1') -
                               (int)std::count(liczba.begin(), liczba.end(), '0'));
        if (roznica == 0)
            zrownowazone++;
        else if (roznica == 1)
            prawie++;
    }
    wynik << "4.1 " << zrownowazone << " " << prawie << "\n";

    std::vector<std::string> osmiocyfrowe;
    for (auto& liczba : liczby)
        if (liczba.size() == 8) osmiocyfrowe.push_back(liczba);
    long long najwiecej = 0;
    for (auto& liczba : osmiocyfrowe) najwiecej = std::max(najwiecej, anagramy(liczba));
    wynik << "4.2\n";
    for (auto& liczba : osmiocyfrowe)
        if (anagramy(liczba) == najwiecej) wynik << liczba << "\n";

    // 4.3
    std::vector<long long> dziesietne;
    for (auto& liczba : liczby) dziesietne.push_back(std::stoll(liczba, nullptr, 2));
    long long najwieksza = 0;
    for (size_t i = 1; i < dziesietne.size(); i++)
        najwieksza = std::max(najwieksza, std::llabs(dziesietne[i] - dziesietne[i - 1]));
    wynik << "4.3 " << na_dwojkowy(najwieksza) << "\n";

    // 4.4
    int bez_zera = 0;
    long long najlepsza = dziesietne[0];
    for (long long x : dziesietne) {
        if (!std::to_string(x).contains('0')) bez_zera++;
        if (suma_roznych_cyfr(x) > suma_roznych_cyfr(najlepsza)) najlepsza = x;
    }
    wynik << "4.4 " << bez_zera << " " << najlepsza << "\n";
}
```
```java
// Java 25
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    static int ile(String x, char c) {
        return (int) x.chars().filter(z -> z == c).count();
    }

    // 4.2 - pierwsza cyfra musi być 1, pozostałe jedynki rozmieszczamy na 7 miejscach: C(7, jedynki - 1)
    static long silnia(int n) {
        long s = 1;
        for (int i = 2; i <= n; i++) s *= i;
        return s;
    }

    static long anagramy(String liczba) {
        int reszta = liczba.length() - 1;
        int jedynki = ile(liczba, '1') - 1;
        return silnia(reszta) / (silnia(jedynki) * silnia(reszta - jedynki));
    }

    // suma różnych cyfr liczby (sum(int(c) for c in set(str(x))))
    static int sumaRoznychCyfr(long x) {
        var rozne = new HashSet<Character>();
        for (char c : Long.toString(x).toCharArray()) rozne.add(c);
        int suma = 0;
        for (char c : rozne) suma += c - '0';
        return suma;
    }

    public static void main(String[] args) throws Exception {
        var liczby = new ArrayList<String>();
        for (var linia : Files.readAllLines(Path.of("anagram.txt")))
            if (!linia.isBlank()) liczby.add(linia.strip());

        try (var wynik = new PrintWriter("wyniki4.txt")) {
            // 4.1
            int zrownowazone = 0;
            int prawie = 0;
            for (var liczba : liczby) {
                int roznica = Math.abs(ile(liczba, '1') - ile(liczba, '0'));
                if (roznica == 0)
                    zrownowazone++;
                else if (roznica == 1)
                    prawie++;
            }
            wynik.println("4.1 " + zrownowazone + " " + prawie);

            var osmiocyfrowe = new ArrayList<String>();
            for (var liczba : liczby)
                if (liczba.length() == 8) osmiocyfrowe.add(liczba);
            long najwiecej = 0;
            for (var liczba : osmiocyfrowe) najwiecej = Math.max(najwiecej, anagramy(liczba));
            wynik.println("4.2");
            for (var liczba : osmiocyfrowe)
                if (anagramy(liczba) == najwiecej) wynik.println(liczba);

            // 4.3
            var dziesietne = new ArrayList<Long>();
            for (var liczba : liczby) dziesietne.add(Long.parseLong(liczba, 2));
            long najwieksza = 0;
            for (int i = 1; i < dziesietne.size(); i++)
                najwieksza = Math.max(najwieksza, Math.abs(dziesietne.get(i) - dziesietne.get(i - 1)));
            wynik.println("4.3 " + Long.toBinaryString(najwieksza));

            // 4.4
            int bezZera = 0;
            long najlepsza = dziesietne.get(0);
            for (long x : dziesietne) {
                if (!Long.toString(x).contains("0")) bezZera++;
                if (sumaRoznychCyfr(x) > sumaRoznychCyfr(najlepsza)) najlepsza = x;
            }
            wynik.println("4.4 " + bezZera + " " + najlepsza);
        }
    }
}
```

**Odpowiedź:** 4.1: 118 zrównoważonych, 219 prawie zrównoważonych. 4.2: 10110101, 11010100, 10100101, 11001001, 10110100, 11001101, 11000110. 4.3: 10011000111001. 4.4: a) 728, b) 7896.
