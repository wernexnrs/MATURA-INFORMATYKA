<h1 align="center">Matura 2023 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2023)</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

> W archiwum z danymi pliki do tego arkusza są w folderze `DANE_M` (folder `DANE_E` dotyczy arkusza w formule 2015).

## 1.1, 1.2 i 1.3

> **Treść zadania (Mnożenie):** Rekurencyjny algorytm mnożenia liczb całkowitych dodatnich x, y korzysta tylko z dodawania i dzielenia całkowitego przez 2:
>
> ```
> iloczyn(x, y):
>   jeżeli y = 1: wynikiem jest x
>   w przeciwnym razie:
>     k ← y div 2;  z ← iloczyn(x, k)
>     jeżeli y mod 2 = 0: wynikiem jest z + z
>     w przeciwnym razie: wynikiem jest x + z + z
> ```
>
> Np. `iloczyn(9, 11)` wykonuje 5 dodawań (wywołania z y = 11, 5, 2, 1).
>
> - **1.1** — Uzupełnij tabelę kolejnych wywołań (parametry x, y, obliczone k, z oraz wynik) dla `iloczyn(10, 45)`.
> - **1.2** — Podaj liczbę operacji dodawania wykonanych przy obliczaniu `iloczyn(x, y)` dla par: (9, 11), (8, 32), (2, 47), (112, 112).
> - **1.3** — Uzupełnij trzy luki w iteracyjnej wersji algorytmu obliczającej z = x·y (wolno używać tylko dodawania, odejmowania, `div` i `mod`, bez mnożenia):
>
> ```
> z ← ____
> dopóki ____ wykonuj:
>   jeżeli y mod 2 = 1: z ← z + x
>   x ← x + x
>   y ← ____
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
        print(x, y, k, z, z + z)
        return z + z
    dodawania += 2
    print(x, y, k, z, x + z + z)
    return x + z + z


def iloczyn_iteracyjny(x, y):
    z = 0
    while y >= 1:
        if y % 2 == 1:
            z = z + x
        x = x + x
        y = y // 2
    return z


# 1.1 - wiersze tabeli (od najgłębszego wywołania): x, y, k, z, wynik
iloczyn(10, 45)

# 1.2
for x, y in [(9, 11), (8, 32), (2, 47), (112, 112)]:
    dodawania = 0
    iloczyn(x, y)
    print("dodawań:", dodawania)

# 1.3
print(iloczyn_iteracyjny(10, 45), iloczyn_iteracyjny(112, 112))
```
```cpp
// C++23
#include <print>

int dodawania = 0;

long long iloczyn(long long x, long long y) {
    if (y == 1) return x;
    long long k = y / 2;
    long long z = iloczyn(x, k);
    if (y % 2 == 0) {
        dodawania += 1;
        std::println("{} {} {} {} {}", x, y, k, z, z + z);
        return z + z;
    }
    dodawania += 2;
    std::println("{} {} {} {} {}", x, y, k, z, x + z + z);
    return x + z + z;
}

long long iloczyn_iteracyjny(long long x, long long y) {
    long long z = 0;
    while (y >= 1) {
        if (y % 2 == 1) z = z + x;
        x = x + x;
        y = y / 2;
    }
    return z;
}

int main() {
    // 1.1 - wiersze tabeli (od najgłębszego wywołania): x, y, k, z, wynik
    iloczyn(10, 45);

    // 1.2
    int dane[4][2] = {{9, 11}, {8, 32}, {2, 47}, {112, 112}};
    for (auto& [x, y] : dane) {
        dodawania = 0;
        iloczyn(x, y);
        std::println("dodawań: {}", dodawania);
    }

    // 1.3
    std::println("{} {}", iloczyn_iteracyjny(10, 45), iloczyn_iteracyjny(112, 112));
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
        if (y % 2 == 0) {
            dodawania += 1;
            System.out.println(x + " " + y + " " + k + " " + z + " " + (z + z));
            return z + z;
        }
        dodawania += 2;
        System.out.println(x + " " + y + " " + k + " " + z + " " + (x + z + z));
        return x + z + z;
    }

    static long iloczynIteracyjny(long x, long y) {
        long z = 0;
        while (y >= 1) {
            if (y % 2 == 1) z = z + x;
            x = x + x;
            y = y / 2;
        }
        return z;
    }

    public static void main(String[] args) throws Exception {
        // 1.1 - wiersze tabeli (od najgłębszego wywołania): x, y, k, z, wynik
        iloczyn(10, 45);

        // 1.2
        int[][] dane = {{9, 11}, {8, 32}, {2, 47}, {112, 112}};
        for (var d : dane) {
            dodawania = 0;
            iloczyn(d[0], d[1]);
            System.out.println("dodawań: " + dodawania);
        }

        // 1.3
        System.out.println(iloczynIteracyjny(10, 45) + " " + iloczynIteracyjny(112, 112));
    }
}
```

**Odpowiedź:** 1.1 (x, y, k, z, wynik): (10, 45, 22, 220, 450), (10, 22, 11, 110, 220), (10, 11, 5, 50, 110), (10, 5, 2, 20, 50), (10, 2, 1, 10, 20), (10, 1, –, –, 10). 1.2: 8, 32 → 5; 2, 47 → 9; 112, 112 → 8. 1.3: `z ← 0`, `dopóki y ≥ 1`, `y ← y div 2` (funkcja `iloczyn_iteracyjny`).

## 2.1, 2.2, 2.3 i 2.4

> **Treść zadania (Sufiksy):** Słowo to ciąg małych liter alfabetu angielskiego. Sufiks `s[k..n]` słowa `s[1..n]` nazywamy k-tym sufiksem (np. sufiksy słowa `mascarpone` posortowane alfabetycznie mają numery 5, 2, 4, 10, 1, 9, 8, 7, 6, 3). Funkcja `czy_mniejszy(n, s, k1, k2)` zwraca PRAWDA, gdy sufiks k1 jest alfabetycznie mniejszy od sufiksu k2:
>
> ```
> i ← k1;  j ← k2
> dopóki i ≤ n oraz j ≤ n:
>   jeżeli s[i] = s[j]: i ← i+1; j ← j+1
>   w przeciwnym razie: jeżeli s[i] < s[j] zakończ z PRAWDA, w p.p. zakończ z FAŁSZ
> jeżeli j ≤ n zakończ z PRAWDA, w p.p. zakończ z FAŁSZ
> ```
>
> - **2.1** — Podaj przykład słowa długości 10 i liczb k1 ≠ k2, dla których funkcja wykona dokładnie 6 porównań w pierwszej instrukcji `jeżeli` (np. dla `mascarpone`, k1=5, k2=2 wykonuje łącznie 3 porównania).
> - **2.2** — Pliki `slowa1.txt`, `slowa2.txt`, `slowa3.txt` zawierają: w 1. wierszu n, w 2. słowo s, w 3. liczby k1 i k2. Zaimplementuj `czy_mniejszy` i dla każdego pliku wypisz `TAK` lub `NIE` (poprzedzone nazwą pliku) do `wyniki2_2.txt`.
> - **2.3** — Z użyciem `czy_mniejszy` zapisz algorytm wyznaczający tablicę `T[1..n]` numerów sufiksów w porządku alfabetycznym (np. dla `kalafiorowa`: [11, 4, 2, 5, 6, 1, 3, 7, 9, 8, 10]); wolno używać tylko podstawowych operacji, bez funkcji wbudowanych.
> - **2.4** — Plik `slowa4.txt` zawiera 10 wierszy z liczbą n (1 ≤ n ≤ 100) i n-literowym słowem. Dla każdego słowa wypisz jego najmniejszy alfabetycznie sufiks (np. `mascarpone` → `arpone`, `truskawki` → `awki`), każdy w osobnym wierszu pliku `wyniki2_4.txt`.

```py
porownania = 0


def czy_mniejszy(n, s, k1, k2):
    # s indeksowane od 0, k1 i k2 od 1 (jak w treści)
    global porownania
    i = k1
    j = k2
    while i <= n and j <= n:
        porownania += 1  # pierwsza instrukcja jeżeli
        if s[i - 1] == s[j - 1]:
            i += 1
            j += 1
        elif s[i - 1] < s[j - 1]:
            return True
        else:
            return False
    return j <= n


# 2.1 - sprawdzenie odpowiedzi: s = aaaaaaaaaa, k1 = 2, k2 = 5
for s, k1, k2 in [("aaaaaaaaaa", 2, 5), ("ababababb", 1, 3)]:
    porownania = 0
    czy_mniejszy(len(s), s, k1, k2)
    print("2.1", s, k1, k2, porownania)

# 2.2
with open("wyniki2_2.txt", "w") as wyniki:
    for nazwa in ["slowa1.txt", "slowa2.txt", "slowa3.txt"]:
        with open(nazwa) as file:
            n = int(file.readline())
            s = file.readline().strip()
            k1, k2 = map(int, file.readline().split())
        odp = "TAK" if czy_mniejszy(n, s, k1, k2) else "NIE"
        print(nazwa, odp)
        wyniki.write(nazwa + " " + odp + "\n")


# 2.3 - sortowanie bąbelkowe numerów sufiksów
def tablica_sufiksow(n, s):
    T = [i for i in range(1, n + 1)]
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if not czy_mniejszy(n, s, T[j], T[j + 1]):
                T[j], T[j + 1] = T[j + 1], T[j]
    return T


print("2.3", tablica_sufiksow(10, "mascarpone"), tablica_sufiksow(11, "kalafiorowa"))

# 2.4 - najmniejszy sufiks
with open("slowa4.txt") as file, open("wyniki2_4.txt", "w") as wyniki:
    for linia in file:
        n, s = linia.split()
        n = int(n)
        najmniejszy = n
        for k in range(1, n):
            if czy_mniejszy(n, s, k, najmniejszy):
                najmniejszy = k
        print(s[najmniejszy - 1:])
        wyniki.write(s[najmniejszy - 1:] + "\n")
```
```cpp
// C++23
#include <fstream>
#include <print>
#include <string>
#include <utility>
#include <vector>

int porownania = 0;

bool czy_mniejszy(int n, const std::string& s, int k1, int k2) {
    // s indeksowane od 0, k1 i k2 od 1 (jak w treści)
    int i = k1;
    int j = k2;
    while (i <= n && j <= n) {
        porownania++;  // pierwsza instrukcja jeżeli
        if (s[i - 1] == s[j - 1]) {
            i++;
            j++;
        } else if (s[i - 1] < s[j - 1]) {
            return true;
        } else {
            return false;
        }
    }
    return j <= n;
}

// 2.3 - sortowanie bąbelkowe numerów sufiksów
std::vector<int> tablica_sufiksow(int n, const std::string& s) {
    std::vector<int> T;
    for (int i = 1; i <= n; i++) T.push_back(i);
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (!czy_mniejszy(n, s, T[j], T[j + 1])) std::swap(T[j], T[j + 1]);
    return T;
}

int main() {
    // 2.1 - sprawdzenie odpowiedzi: s = aaaaaaaaaa, k1 = 2, k2 = 5
    std::vector<std::pair<std::string, std::pair<int, int>>> testy = {{"aaaaaaaaaa", {2, 5}}, {"ababababb", {1, 3}}};
    for (auto& [s, k] : testy) {
        porownania = 0;
        czy_mniejszy(s.size(), s, k.first, k.second);
        std::println("2.1 {} {} {} {}", s, k.first, k.second, porownania);
    }

    // 2.2
    std::ofstream wyniki("wyniki2_2.txt");
    for (std::string nazwa : {"slowa1.txt", "slowa2.txt", "slowa3.txt"}) {
        std::ifstream plik(nazwa);
        int n, k1, k2;
        std::string s;
        plik >> n >> s >> k1 >> k2;
        std::string odp = czy_mniejszy(n, s, k1, k2) ? "TAK" : "NIE";
        std::println("{} {}", nazwa, odp);
        wyniki << nazwa << " " << odp << "\n";
    }

    std::println("2.3 {} {}", tablica_sufiksow(10, "mascarpone"), tablica_sufiksow(11, "kalafiorowa"));

    // 2.4 - najmniejszy sufiks
    std::ifstream plik("slowa4.txt");
    std::ofstream wyniki4("wyniki2_4.txt");
    int n;
    std::string s;
    while (plik >> n >> s) {
        int najmniejszy = n;
        for (int k = 1; k < n; k++)
            if (czy_mniejszy(n, s, k, najmniejszy)) najmniejszy = k;
        std::println("{}", s.substr(najmniejszy - 1));
        wyniki4 << s.substr(najmniejszy - 1) << "\n";
    }
}
```
```java
// Java 25
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    static int porownania = 0;

    static boolean czyMniejszy(int n, String s, int k1, int k2) {
        // s indeksowane od 0, k1 i k2 od 1 (jak w treści)
        int i = k1;
        int j = k2;
        while (i <= n && j <= n) {
            porownania++;  // pierwsza instrukcja jeżeli
            if (s.charAt(i - 1) == s.charAt(j - 1)) {
                i++;
                j++;
            } else if (s.charAt(i - 1) < s.charAt(j - 1)) {
                return true;
            } else {
                return false;
            }
        }
        return j <= n;
    }

    // 2.3 - sortowanie bąbelkowe numerów sufiksów
    static List<Integer> tablicaSufiksow(int n, String s) {
        var T = new ArrayList<Integer>();
        for (int i = 1; i <= n; i++) T.add(i);
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - 1 - i; j++)
                if (!czyMniejszy(n, s, T.get(j), T.get(j + 1))) Collections.swap(T, j, j + 1);
        return T;
    }

    public static void main(String[] args) throws Exception {
        // 2.1 - sprawdzenie odpowiedzi: s = aaaaaaaaaa, k1 = 2, k2 = 5
        String[] slowa = {"aaaaaaaaaa", "ababababb"};
        int[][] k = {{2, 5}, {1, 3}};
        for (int t = 0; t < 2; t++) {
            porownania = 0;
            czyMniejszy(slowa[t].length(), slowa[t], k[t][0], k[t][1]);
            System.out.println("2.1 " + slowa[t] + " " + k[t][0] + " " + k[t][1] + " " + porownania);
        }

        // 2.2
        try (var wyniki = new PrintWriter("wyniki2_2.txt")) {
            for (String nazwa : new String[] {"slowa1.txt", "slowa2.txt", "slowa3.txt"}) {
                var sc = new Scanner(Path.of(nazwa));
                int n = sc.nextInt();
                String s = sc.next();
                int k1 = sc.nextInt(), k2 = sc.nextInt();
                sc.close();
                String odp = czyMniejszy(n, s, k1, k2) ? "TAK" : "NIE";
                System.out.println(nazwa + " " + odp);
                wyniki.print(nazwa + " " + odp + "\n");
            }
        }

        System.out.println("2.3 " + tablicaSufiksow(10, "mascarpone") + " " + tablicaSufiksow(11, "kalafiorowa"));

        // 2.4 - najmniejszy sufiks
        try (var wyniki = new PrintWriter("wyniki2_4.txt")) {
            for (var linia : Files.readAllLines(Path.of("slowa4.txt"))) {
                if (linia.isBlank()) continue;
                var czesci = linia.trim().split("\\s+");
                int n = Integer.parseInt(czesci[0]);
                String s = czesci[1];
                int najmniejszy = n;
                for (int j = 1; j < n; j++)
                    if (czyMniejszy(n, s, j, najmniejszy)) najmniejszy = j;
                System.out.println(s.substring(najmniejszy - 1));
                wyniki.print(s.substring(najmniejszy - 1) + "\n");
            }
        }
    }
}
```

**Odpowiedź:** 2.1: np. s = aaaaaaaaaa, k1 = 2, k2 = 5 (6 porównań). 2.2: slowa1.txt TAK, slowa2.txt NIE, slowa3.txt NIE. 2.3: funkcja `tablica_sufiksow` (sortowanie bąbelkowe z porównaniem `czy_mniejszy`). 2.4: ato, a, abracadabrad, abecadlo, aaababbbbcaababaz, a, aaababbbbcaababaaabcaabb…, aaababbbbcaababaz, aaababbbbcaababacaacac…, aaababbbbcacbabaaabcaabb….

> W kluczu CKE do 2.1 pierwszy przykład (s = ababababb, k1 = 1, k2 = 3) daje 7 porównań, a nie 6 (6 równych par i jedna różna: s[7] = a, s[9] = b) — widać to w wyniku programu. Drugi przykład z klucza (aaaaaaaaaa, 2, 5) jest poprawny.

## 3.1, 3.2, 3.3 i 3.4

> **Treść zadania (Anagramy):** Plik `anagram.txt` zawiera 1000 różnych liczb binarnych (do 14 cyfr, każda zaczyna się od 1), po jednej w wierszu. Odpowiedzi zapisz w `wyniki3.txt` z numerami zadań (do testów: `przyklad.txt`, 100 wierszy).
>
> - **3.1** — Liczba binarna jest zrównoważona, gdy ma tyle samo zer co jedynek, a prawie zrównoważona, gdy te liczby różnią się o 1. Podaj, ile jest liczb zrównoważonych i ile prawie zrównoważonych (dla przykładu: 21 i 15).
> - **3.2** — Anagramy to liczby z tego samego zestawu cyfr w innej kolejności, bez zera na początku (np. z 11100 powstaje 6 anagramów). Wypisz, w kolejności z pliku, wszystkie 8-cyfrowe liczby, z których można utworzyć najwięcej anagramów.
> - **3.3** — Podaj w zapisie binarnym największą wartość bezwzględną różnicy między liczbami z sąsiednich wierszy (dla przykładu: `1110001010`).
> - **3.4** — Zamień liczby na dziesiętne i: a) podaj, w ilu nie występuje cyfra 0; b) podaj liczbę o największej sumie różnych cyfr (przy remisie – pierwszą w pliku), np. dla 20462 suma różnych cyfr to 12. Dla przykładu: 81 i 895.

```py
with open("anagram.txt") as file:
    liczby = [linia.strip() for linia in file if linia.strip()]

# 3.1
zrownowazone = 0
prawie = 0
for x in liczby:
    roznica = x.count("1") - x.count("0")
    if roznica == 0:
        zrownowazone += 1
    elif abs(roznica) == 1:
        prawie += 1
print("3.1", zrownowazone, prawie, sep="\n")


# 3.2 - liczba anagramów: pierwsza cyfra to 1, pozostałe n-1 cyfr ustawiamy dowolnie
def silnia(n):
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik


def anagramy(x):
    jedynki = x.count("1") - 1
    zera = x.count("0")
    return silnia(jedynki + zera) // (silnia(jedynki) * silnia(zera))


osmiocyfrowe = [x for x in liczby if len(x) == 8]
najwiecej = max(anagramy(x) for x in osmiocyfrowe)
print("3.2")
for x in osmiocyfrowe:
    if anagramy(x) == najwiecej:
        print(x)

# 3.3
najwieksza = 0
for i in range(len(liczby) - 1):
    najwieksza = max(najwieksza, abs(int(liczby[i], 2) - int(liczby[i + 1], 2)))
print("3.3", bin(najwieksza)[2:])

# 3.4
bez_zera = 0
najlepsza = None
najlepsza_suma = -1
for x in liczby:
    dziesietna = str(int(x, 2))
    if "0" not in dziesietna:
        bez_zera += 1
    suma = sum(int(c) for c in set(dziesietna))
    if suma > najlepsza_suma:
        najlepsza_suma = suma
        najlepsza = dziesietna
print("3.4", bez_zera, najlepsza, sep="\n")
```
```cpp
// C++23
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <print>
#include <set>
#include <string>
#include <vector>

// 3.2 - liczba anagramów: pierwsza cyfra to 1, pozostałe n-1 cyfr ustawiamy dowolnie
long long silnia(int n) {
    long long wynik = 1;
    for (int i = 2; i <= n; i++) wynik *= i;
    return wynik;
}

long long anagramy(const std::string& x) {
    int jedynki = std::count(x.begin(), x.end(), '1') - 1;
    int zera = std::count(x.begin(), x.end(), '0');
    return silnia(jedynki + zera) / (silnia(jedynki) * silnia(zera));
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

    // 3.1
    int zrownowazone = 0;
    int prawie = 0;
    for (auto& x : liczby) {
        int roznica = std::count(x.begin(), x.end(), '1') - std::count(x.begin(), x.end(), '0');
        if (roznica == 0)
            zrownowazone++;
        else if (std::abs(roznica) == 1)
            prawie++;
    }
    std::println("3.1\n{}\n{}", zrownowazone, prawie);

    std::vector<std::string> osmiocyfrowe;
    for (auto& x : liczby)
        if (x.size() == 8) osmiocyfrowe.push_back(x);
    long long najwiecej = 0;
    for (auto& x : osmiocyfrowe) najwiecej = std::max(najwiecej, anagramy(x));
    std::println("3.2");
    for (auto& x : osmiocyfrowe)
        if (anagramy(x) == najwiecej) std::println("{}", x);

    // 3.3
    long long najwieksza = 0;
    for (size_t i = 0; i + 1 < liczby.size(); i++)
        najwieksza = std::max(najwieksza, std::llabs(std::stoll(liczby[i], nullptr, 2) - std::stoll(liczby[i + 1], nullptr, 2)));
    std::println("3.3 {}", na_dwojkowy(najwieksza));

    // 3.4
    int bez_zera = 0;
    std::string najlepsza;
    int najlepsza_suma = -1;
    for (auto& x : liczby) {
        std::string dziesietna = std::to_string(std::stoll(x, nullptr, 2));
        if (!dziesietna.contains('0')) bez_zera++;
        std::set<char> rozne(dziesietna.begin(), dziesietna.end());
        int suma = 0;
        for (char c : rozne) suma += c - '0';
        if (suma > najlepsza_suma) {
            najlepsza_suma = suma;
            najlepsza = dziesietna;
        }
    }
    std::println("3.4\n{}\n{}", bez_zera, najlepsza);
}
```
```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    static long ile(String x, char c) {
        return x.chars().filter(z -> z == c).count();
    }

    // 3.2 - liczba anagramów: pierwsza cyfra to 1, pozostałe n-1 cyfr ustawiamy dowolnie
    static long silnia(int n) {
        long wynik = 1;
        for (int i = 2; i <= n; i++) wynik *= i;
        return wynik;
    }

    static long anagramy(String x) {
        int jedynki = (int) ile(x, '1') - 1;
        int zera = (int) ile(x, '0');
        return silnia(jedynki + zera) / (silnia(jedynki) * silnia(zera));
    }

    public static void main(String[] args) throws Exception {
        var liczby = new ArrayList<String>();
        for (var linia : Files.readAllLines(Path.of("anagram.txt")))
            if (!linia.isBlank()) liczby.add(linia.strip());

        // 3.1
        int zrownowazone = 0;
        int prawie = 0;
        for (var x : liczby) {
            long roznica = ile(x, '1') - ile(x, '0');
            if (roznica == 0)
                zrownowazone++;
            else if (Math.abs(roznica) == 1)
                prawie++;
        }
        System.out.println("3.1\n" + zrownowazone + "\n" + prawie);

        var osmiocyfrowe = new ArrayList<String>();
        for (var x : liczby)
            if (x.length() == 8) osmiocyfrowe.add(x);
        long najwiecej = 0;
        for (var x : osmiocyfrowe) najwiecej = Math.max(najwiecej, anagramy(x));
        System.out.println("3.2");
        for (var x : osmiocyfrowe)
            if (anagramy(x) == najwiecej) System.out.println(x);

        // 3.3
        long najwieksza = 0;
        for (int i = 0; i + 1 < liczby.size(); i++)
            najwieksza = Math.max(najwieksza, Math.abs(Long.parseLong(liczby.get(i), 2) - Long.parseLong(liczby.get(i + 1), 2)));
        System.out.println("3.3 " + Long.toBinaryString(najwieksza));

        // 3.4
        int bezZera = 0;
        String najlepsza = null;
        int najlepszaSuma = -1;
        for (var x : liczby) {
            String dziesietna = Long.toString(Long.parseLong(x, 2));
            if (!dziesietna.contains("0")) bezZera++;
            var rozne = new HashSet<Character>();
            for (char c : dziesietna.toCharArray()) rozne.add(c);
            int suma = 0;
            for (char c : rozne) suma += c - '0';
            if (suma > najlepszaSuma) {
                najlepszaSuma = suma;
                najlepsza = dziesietna;
            }
        }
        System.out.println("3.4\n" + bezZera + "\n" + najlepsza);
    }
}
```

**Odpowiedź:** 3.1: 118 zrównoważonych, 219 prawie zrównoważonych. 3.2: 10110101, 11010100, 10100101, 11001001, 10110100, 11001101, 11000110 (po 35 anagramów). 3.3: 10011000111001. 3.4: a) 728, b) 7896.

## 4

> **Treść zadania:** Uzupełnij tabelę: liczbę (101201)₃ zapisz w systemie o podstawie 9, a liczbę (2487)₉ – w systemie o podstawie 3.

```py
def na_dziesietny(napis, podstawa):
    liczba = 0
    for c in napis:
        liczba = liczba * podstawa + int(c)
    return liczba


def z_dziesietnego(liczba, podstawa):
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % podstawa) + wynik
        liczba = liczba // podstawa
    return wynik


print(z_dziesietnego(na_dziesietny("101201", 3), 9))
print(z_dziesietnego(na_dziesietny("2487", 9), 3))
```
```cpp
// C++23
#include <print>
#include <string>

long long na_dziesietny(const std::string& napis, int podstawa) {
    long long liczba = 0;
    for (char c : napis) liczba = liczba * podstawa + (c - '0');
    return liczba;
}

std::string z_dziesietnego(long long liczba, int podstawa) {
    std::string wynik;
    while (liczba > 0) {
        wynik = std::to_string(liczba % podstawa) + wynik;
        liczba = liczba / podstawa;
    }
    return wynik;
}

int main() {
    std::println("{}", z_dziesietnego(na_dziesietny("101201", 3), 9));
    std::println("{}", z_dziesietnego(na_dziesietny("2487", 9), 3));
}
```
```java
// Java 25
public class Zadanie {
    static long naDziesietny(String napis, int podstawa) {
        long liczba = 0;
        for (char c : napis.toCharArray()) liczba = liczba * podstawa + (c - '0');
        return liczba;
    }

    static String zDziesietnego(long liczba, int podstawa) {
        String wynik = "";
        while (liczba > 0) {
            wynik = (liczba % podstawa) + wynik;
            liczba = liczba / podstawa;
        }
        return wynik;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(zDziesietnego(naDziesietny("101201", 3), 9));
        System.out.println(zDziesietnego(naDziesietny("2487", 9), 3));
    }
}
```

**Odpowiedź:** 101201₃ = 351₉, 2487₉ = 2112221₃.
