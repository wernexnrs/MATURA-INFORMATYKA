<h1 align="center">Matura 2020 — czerwiec (termin główny), poziom rozszerzony (stara formuła)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2020-czerwiec-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2020-czerwiec-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2020-czerwiec-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2020-czerwiec-matura-stara-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

> **Treść zadania:** Zadanie 1 (algorytm). Dane: dodatnia parzysta liczba całkowita `n` i tablica `A[0..n-1]`.
>
> ```
> i ← 0
> dopóki i < n-1 wykonuj
>     (*) jeżeli A[i] > A[i+1]
>             zamień A[i] z A[i+1]
>     i ← i + 2
> i ← 0
> x ← A[i]
> y ← A[i+1]
> dopóki i < n-3 wykonuj
>     (*) jeżeli A[i+2] < x wykonuj x ← A[i+2]
>     (*) jeżeli A[i+3] > y wykonuj y ← A[i+3]
>     i ← i + 2
> ```
>
> - 1.1 — podaj wartości `x` i `y` po wykonaniu algorytmu dla `A = [5, 8, 10, 14, 20, 12, 19, 23, 38, 30]`.
> - 1.2 — rozstrzygnij, czy po wykonaniu algorytmu `x` (podpunkt a) oraz `y` (podpunkt b) jest najmniejszą czy największą liczbą w tablicy `A`.
> - 1.3 — wskaż łączną liczbę porównań w wierszach oznaczonych (*): A. `n`, B. `2n`, C. `3n/2`, D. `3n/2 − 2`.

```py
def algorytm(A):
    # zwraca x, y oraz liczbę porównań w wierszach (*)
    A = A[:]
    n = len(A)
    porownania = 0
    # w każdej parze (A[i], A[i+1]) mniejszy element trafia na lewo
    i = 0
    while i < n - 1:
        porownania += 1
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
        i = i + 2
    # x - minimum z lewych elementów par, y - maksimum z prawych
    i = 0
    x = A[i]
    y = A[i + 1]
    while i < n - 3:
        porownania += 2
        if A[i + 2] < x:
            x = A[i + 2]
        if A[i + 3] > y:
            y = A[i + 3]
        i = i + 2
    return x, y, porownania


A = [5, 8, 10, 14, 20, 12, 19, 23, 38, 30]
x, y, porownania = algorytm(A)
print(x, y)
print(porownania, 3 * len(A) // 2 - 2)  # n/2 + 2*(n/2 - 1) = 3n/2 - 2
```

```cpp
// C++23
#include <print>
#include <tuple>
#include <utility>
#include <vector>

// zwraca x, y oraz liczbę porównań w wierszach (*)
std::tuple<int, int, int> algorytm(std::vector<int> A) {  // kopia tablicy, jak A[:] w Pythonie
    int n = A.size();
    int porownania = 0;
    // w każdej parze (A[i], A[i+1]) mniejszy element trafia na lewo
    int i = 0;
    while (i < n - 1) {
        porownania++;
        if (A[i] > A[i + 1])
            std::swap(A[i], A[i + 1]);
        i = i + 2;
    }
    // x - minimum z lewych elementów par, y - maksimum z prawych
    i = 0;
    int x = A[i];
    int y = A[i + 1];
    while (i < n - 3) {
        porownania += 2;
        if (A[i + 2] < x)
            x = A[i + 2];
        if (A[i + 3] > y)
            y = A[i + 3];
        i = i + 2;
    }
    return {x, y, porownania};
}

int main() {
    std::vector<int> A = {5, 8, 10, 14, 20, 12, 19, 23, 38, 30};
    auto [x, y, porownania] = algorytm(A);
    std::println("{} {}", x, y);
    int n = A.size();
    std::println("{} {}", porownania, 3 * n / 2 - 2);  // n/2 + 2*(n/2 - 1) = 3n/2 - 2
}
```

```java
// Java 25
public class Zadanie {
    // zwraca x, y oraz liczbę porównań w wierszach (*)
    static int[] algorytm(int[] tablica) {
        int[] A = tablica.clone();
        int n = A.length;
        int porownania = 0;
        // w każdej parze (A[i], A[i+1]) mniejszy element trafia na lewo
        int i = 0;
        while (i < n - 1) {
            porownania++;
            if (A[i] > A[i + 1]) {
                int t = A[i]; A[i] = A[i + 1]; A[i + 1] = t;
            }
            i = i + 2;
        }
        // x - minimum z lewych elementów par, y - maksimum z prawych
        i = 0;
        int x = A[i];
        int y = A[i + 1];
        while (i < n - 3) {
            porownania += 2;
            if (A[i + 2] < x)
                x = A[i + 2];
            if (A[i + 3] > y)
                y = A[i + 3];
            i = i + 2;
        }
        return new int[]{x, y, porownania};
    }

    public static void main(String[] args) throws Exception {
        int[] A = {5, 8, 10, 14, 20, 12, 19, 23, 38, 30};
        int[] wynik = algorytm(A);
        System.out.println(wynik[0] + " " + wynik[1]);
        System.out.println(wynik[2] + " " + (3 * A.length / 2 - 2));  // n/2 + 2*(n/2 - 1) = 3n/2 - 2
    }
}
```
**Odpowiedź:** 1.1: x = 5, y = 38. 1.2: a) A (najmniejsza liczba), b) B (największa liczba). 1.3: D (3n/2 − 2)

## 2.1 i 2.2

> **Treść zadania:** Zadanie 2 (BCD). Kod BCD nieujemnej liczby całkowitej `L` powstaje przez zamianę każdej cyfry dziesiętnej `L` na jej czterobitowy kod binarny, np. `3768 → 0011 0111 0110 1000`.
>
> - 2.1 — uzupełnij tabelę: podaj kod BCD i liczbę jedynek dla 259 oraz 15893, a także liczby dziesiętne odpowiadające kodom `0010000000010111` (5 jedynek) i `00100011010101110100` (9 jedynek).
> - 2.2 — napisz algorytm, który dla dodatniej liczby całkowitej `L` poda `w` — liczbę jedynek w kodzie BCD liczby `L`. Wolno używać tylko operacji arytmetycznych (w tym div i mod), odwołań do elementów tablicy, porównań, instrukcji sterujących, przypisań i własnych funkcji.

```py
def kod_bcd(L):
    # każda cyfra dziesiętna -> 4 bity
    kod = ""
    for cyfra in str(L):
        kod += format(int(cyfra), "04b")
    return kod


def z_bcd(kod):
    liczba = ""
    for i in range(0, len(kod), 4):
        liczba += str(int(kod[i:i + 4], 2))
    return int(liczba)


def jedynki_bcd(L):
    # 2.2 - tylko operacje arytmetyczne
    w = 0
    while L > 0:
        cyfra = L % 10
        while cyfra > 0:
            if cyfra % 2 == 1:
                w += 1
            cyfra = cyfra // 2
        L = L // 10
    return w


# 2.1
for L in [259, 15893]:
    print(L, kod_bcd(L), jedynki_bcd(L))
for kod in ["0010000000010111", "00100011010101110100"]:
    print(z_bcd(kod), kod, kod.count("1"))
```

```cpp
// C++23
#include <algorithm>
#include <bitset>
#include <print>
#include <string>

std::string kod_bcd(long long L) {
    // każda cyfra dziesiętna -> 4 bity
    std::string kod = "";
    for (char cyfra : std::to_string(L))
        kod += std::bitset<4>(cyfra - '0').to_string();
    return kod;
}

long long z_bcd(const std::string& kod) {
    std::string liczba = "";
    for (size_t i = 0; i < kod.size(); i += 4)
        liczba += std::to_string(std::stoi(kod.substr(i, 4), nullptr, 2));
    return std::stoll(liczba);
}

int jedynki_bcd(long long L) {
    // 2.2 - tylko operacje arytmetyczne
    int w = 0;
    while (L > 0) {
        long long cyfra = L % 10;
        while (cyfra > 0) {
            if (cyfra % 2 == 1)
                w++;
            cyfra = cyfra / 2;
        }
        L = L / 10;
    }
    return w;
}

int main() {
    // 2.1
    for (long long L : {259, 15893})
        std::println("{} {} {}", L, kod_bcd(L), jedynki_bcd(L));
    for (std::string kod : {"0010000000010111", "00100011010101110100"})
        std::println("{} {} {}", z_bcd(kod), kod, std::ranges::count(kod, '1'));
}
```

```java
// Java 25
public class Zadanie {
    static String kodBcd(long L) {
        // każda cyfra dziesiętna -> 4 bity
        var kod = new StringBuilder();
        for (char cyfra : String.valueOf(L).toCharArray()) {
            String bity = Integer.toBinaryString(cyfra - '0');
            kod.append("0".repeat(4 - bity.length())).append(bity);
        }
        return kod.toString();
    }

    static long zBcd(String kod) {
        var liczba = new StringBuilder();
        for (int i = 0; i < kod.length(); i += 4)
            liczba.append(Integer.parseInt(kod.substring(i, i + 4), 2));
        return Long.parseLong(liczba.toString());
    }

    static int jedynkiBcd(long L) {
        // 2.2 - tylko operacje arytmetyczne
        int w = 0;
        while (L > 0) {
            long cyfra = L % 10;
            while (cyfra > 0) {
                if (cyfra % 2 == 1)
                    w++;
                cyfra = cyfra / 2;
            }
            L = L / 10;
        }
        return w;
    }

    public static void main(String[] args) throws Exception {
        // 2.1
        for (long L : new long[]{259, 15893})
            System.out.println(L + " " + kodBcd(L) + " " + jedynkiBcd(L));
        for (String kod : new String[]{"0010000000010111", "00100011010101110100"})
            System.out.println(zBcd(kod) + " " + kod + " " + kod.chars().filter(c -> c == '1').count());
    }
}
```
**Odpowiedź:** 2.1: 259 — 001001011001, 5 jedynek; 2017 — 0010000000010111; 23574 — 00100011010101110100; 15893 — 00010101100010010011, 8 jedynek. 2.2: algorytm `jedynki_bcd` powyżej

## 4.1

> **Treść zadania:** Zadanie 4 (własności liczb). Plik `dane.txt` zawiera 5000 różnych liczb całkowitych z zakresu [100, 100 000], po jednej w wierszu (dane przykładowe: `dane_przyklad.txt`, 500 liczb).
>
> Podaj, ile liczb z pliku jest pierwszych, oraz największą i najmniejszą z nich. Wynik zapisz w pliku `wyniki4_1.txt`.
>
> Dla danych przykładowych: 47 liczb pierwszych, największa 97501, najmniejsza 1669.

```py
def czy_pierwsza(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


pierwsze = []
with open("dane.txt") as file:
    for line in file:
        liczba = int(line)
        if czy_pierwsza(liczba):
            pierwsze.append(liczba)

with open("wyniki4_1.txt", "w") as wynik:
    print("Liczba liczb pierwszych:", len(pierwsze), file=wynik)
    print("Największa liczba:", max(pierwsze), file=wynik)
    print("Najmniejsza liczba:", min(pierwsze), file=wynik)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <vector>

bool czy_pierwsza(long long n) {
    if (n < 2)
        return false;
    long long i = 2;
    while (i * i <= n) {
        if (n % i == 0)
            return false;
        i++;
    }
    return true;
}

int main() {
    std::vector<long long> pierwsze;
    std::ifstream plik("dane.txt");
    long long liczba;
    while (plik >> liczba)
        if (czy_pierwsza(liczba))
            pierwsze.push_back(liczba);

    std::ofstream wynik("wyniki4_1.txt");
    std::println(wynik, "Liczba liczb pierwszych: {}", pierwsze.size());
    std::println(wynik, "Największa liczba: {}", std::ranges::max(pierwsze));
    std::println(wynik, "Najmniejsza liczba: {}", std::ranges::min(pierwsze));
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;

public class Zadanie {
    static boolean czyPierwsza(long n) {
        if (n < 2)
            return false;
        long i = 2;
        while (i * i <= n) {
            if (n % i == 0)
                return false;
            i++;
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        var pierwsze = new ArrayList<Long>();
        for (String line : Files.readAllLines(Path.of("dane.txt"))) {
            if (line.isBlank())
                continue;
            long liczba = Long.parseLong(line.trim());
            if (czyPierwsza(liczba))
                pierwsze.add(liczba);
        }

        try (var wynik = new PrintWriter("wyniki4_1.txt", "UTF-8")) {
            wynik.println("Liczba liczb pierwszych: " + pierwsze.size());
            wynik.println("Największa liczba: " + Collections.max(pierwsze));
            wynik.println("Najmniejsza liczba: " + Collections.min(pierwsze));
        }
    }
}
```
**Odpowiedź:** liczb pierwszych: 501; największa: 99767; najmniejsza: 311

## 4.2

> **Treść zadania:** Dane z pliku `dane.txt` (5000 różnych liczb z zakresu [100, 100 000]).
>
> Liczba jest palindromiczna, jeśli jej zapis binarny (zaczynający się od 1) jest palindromem, np. 107 = `1101011₂`. Liczba jest prawie palindromiczna, jeśli jej zapis binarny poprzedzony jednym lub kilkoma zerami jest palindromem, np. 238 = `11101110₂` (`011101110` jest palindromem) albo 476 = `111011100₂` (`00111011100`).
>
> Podaj łączną liczbę liczb palindromicznych i prawie palindromicznych w pliku. Wynik zapisz w pliku `wyniki4_2.txt` (dla danych przykładowych: 10).

```py
licznik = 0
with open("dane.txt") as file:
    for line in file:
        zapis = bin(int(line))[2:]
        # dopisanie zer z przodu = usunięcie zer z końca zapisu
        zapis = zapis.rstrip("0")
        if zapis == zapis[::-1]:
            licznik += 1

with open("wyniki4_2.txt", "w") as wynik:
    print(licznik, file=wynik)
```

```cpp
// C++23
#include <fstream>
#include <print>
#include <string>

// zapis binarny liczby (bez wiodących zer), jak bin(n)[2:] w Pythonie
std::string binarnie(long long n) {
    if (n == 0)
        return "0";
    std::string zapis = "";
    while (n > 0) {
        zapis = char('0' + n % 2) + zapis;
        n /= 2;
    }
    return zapis;
}

int main() {
    int licznik = 0;
    std::ifstream plik("dane.txt");
    long long liczba;
    while (plik >> liczba) {
        std::string zapis = binarnie(liczba);
        // dopisanie zer z przodu = usunięcie zer z końca zapisu
        while (!zapis.empty() && zapis.back() == '0')
            zapis.pop_back();
        if (zapis == std::string(zapis.rbegin(), zapis.rend()))
            licznik++;
    }

    std::ofstream wynik("wyniki4_2.txt");
    std::println(wynik, "{}", licznik);
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int licznik = 0;
        for (String line : Files.readAllLines(Path.of("dane.txt"))) {
            if (line.isBlank())
                continue;
            String zapis = Long.toBinaryString(Long.parseLong(line.trim()));
            // dopisanie zer z przodu = usunięcie zer z końca zapisu
            zapis = zapis.replaceAll("0+$", "");
            if (zapis.equals(new StringBuilder(zapis).reverse().toString()))
                licznik++;
        }

        try (var wynik = new PrintWriter("wyniki4_2.txt", "UTF-8")) {
            wynik.println(licznik);
        }
    }
}
```
**Odpowiedź:** 107

## 4.3

> **Treść zadania:** Dane z pliku `dane.txt` (5000 różnych liczb z zakresu [100, 100 000]).
>
> Podaj, ile różnych par liczb z pliku ma w zapisie dziesiętnym ten sam zbiór cyfr (liczby mogą mieć różną długość), np. 178 i 817, 1037 i 30071, 10122 i 120. Pary (a, b) i (b, a) liczymy jako jedną. Wynik zapisz w pliku `wyniki4_3.txt` (dla danych przykładowych: 240).

```py
ile = {}  # zbiór cyfr liczby (jako napis) -> ile liczb ma dokładnie te cyfry
with open("dane.txt") as file:
    for line in file:
        cyfry = "".join(sorted(set(line.strip())))
        ile[cyfry] = ile.get(cyfry, 0) + 1

# z k liczb o tym samym zbiorze cyfr można utworzyć k*(k-1)/2 par
pary = 0
for k in ile.values():
    pary += k * (k - 1) // 2

with open("wyniki4_3.txt", "w") as wynik:
    print(pary, file=wynik)
```

```cpp
// C++23
#include <fstream>
#include <map>
#include <print>
#include <set>
#include <string>

int main() {
    std::map<std::string, long long> ile;  // zbiór cyfr liczby (jako napis) -> ile liczb ma dokładnie te cyfry
    std::ifstream plik("dane.txt");
    std::string liczba;
    while (plik >> liczba) {
        std::set<char> zbior(liczba.begin(), liczba.end());  // std::set trzyma cyfry posortowane
        std::string cyfry(zbior.begin(), zbior.end());
        ile[cyfry]++;
    }

    // z k liczb o tym samym zbiorze cyfr można utworzyć k*(k-1)/2 par
    long long pary = 0;
    for (const auto& [cyfry, k] : ile)
        pary += k * (k - 1) / 2;

    std::ofstream wynik("wyniki4_3.txt");
    std::println(wynik, "{}", pary);
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.TreeSet;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        var ile = new HashMap<String, Long>();  // zbiór cyfr liczby (jako napis) -> ile liczb ma dokładnie te cyfry
        for (String line : Files.readAllLines(Path.of("dane.txt"))) {
            if (line.isBlank())
                continue;
            var zbior = new TreeSet<Character>();  // TreeSet trzyma cyfry posortowane
            for (char c : line.strip().toCharArray())
                zbior.add(c);
            var cyfry = new StringBuilder();
            for (char c : zbior)
                cyfry.append(c);
            ile.merge(cyfry.toString(), 1L, Long::sum);
        }

        // z k liczb o tym samym zbiorze cyfr można utworzyć k*(k-1)/2 par
        long pary = 0;
        for (long k : ile.values())
            pary += k * (k - 1) / 2;

        try (var wynik = new PrintWriter("wyniki4_3.txt", "UTF-8")) {
            wynik.println(pary);
        }
    }
}
```
**Odpowiedź:** 23515
