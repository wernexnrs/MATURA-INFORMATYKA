<h1 align="center">Przykładowy arkusz CKE — formuła 2023</h1>

[ARKUSZ](https://arkusze.pl/maturalne/informatyka-2023-przykladowy-arkusz-cke-rozszerzona.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2023-przykladowy-arkusz-cke-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2023-przykladowy-arkusz-cke-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

> **Treść zadania:** Plik `szachy.txt` zawiera opisy 125 plansz (stanów partii szachowej). Każda plansza to 8 wierszy po 8 znaków: `.` — puste pole, wielkie litery — białe bierki, małe — czarne (K/k — król, H/h — hetman, W/w — wieża, G/g — goniec, S/s — skoczek, P/p — pionek). Po każdej planszy jest pusty wiersz. Plik `szachy_przyklad.txt` zawiera 9 plansz. Znajomość reguł szachów nie jest potrzebna.
>
> - 1.1 — Podaj, na ilu planszach jest co najmniej jedna pusta kolumna, oraz największą liczbę pustych kolumn na jednej planszy. Wynik (dwie liczby oddzielone spacją) zapisz w `zadanie1_1.txt` (przykład: `7 5`).
> - 1.2 — Plansza jest w *równowadze*, gdy białe i czarne mają dokładnie te same bierki w tych samych liczbach. Podaj liczbę takich plansz i najmniejszą łączną liczbę bierek na planszy w równowadze; zapisz w `zadanie1_2.txt` (przykład: `6 4`).
> - 1.3 — Wieża szachuje króla przeciwnika, gdy stoi z nim w tym samym wierszu lub kolumnie i nie ma między nimi innej bierki. Podaj, na ilu planszach biała wieża szachuje czarnego króla, a na ilu czarna wieża szachuje białego; zapisz w `zadanie1_3.txt` (przykład: `2 0`).

```py
def wczytaj_plansze(nazwa):
    plansze = []
    with open(nazwa) as file:
        wiersze = [linia.strip() for linia in file]
    for i in range(0, len(wiersze), 9):
        if len(wiersze[i:i + 8]) == 8 and wiersze[i]:
            plansze.append(wiersze[i:i + 8])
    return plansze


plansze = wczytaj_plansze("szachy.txt")

# 1.1
ile_plansz = 0
max_pustych = 0
for p in plansze:
    puste = 0
    for k in range(8):
        if all(p[w][k] == "." for w in range(8)):
            puste += 1
    if puste > 0:
        ile_plansz += 1
        max_pustych = max(max_pustych, puste)
print("1.1", ile_plansz, max_pustych)

# 1.2
ile_rownowag = 0
min_bierek = 64
for p in plansze:
    biale = []
    czarne = []
    for wiersz in p:
        for znak in wiersz:
            if znak.isupper():
                biale.append(znak)
            elif znak.islower():
                czarne.append(znak.upper())
    if sorted(biale) == sorted(czarne):
        ile_rownowag += 1
        min_bierek = min(min_bierek, len(biale) + len(czarne))
print("1.2", ile_rownowag, min_bierek)


# 1.3
def szachuje(p, wieza, krol):
    # czy jakaś wieża (znak wieza) szachuje króla (znak krol)
    for w in range(8):
        for k in range(8):
            if p[w][k] != wieza:
                continue
            for dw, dk in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = w + dw, k + dk
                while 0 <= x < 8 and 0 <= y < 8 and p[x][y] == ".":
                    x, y = x + dw, y + dk
                if 0 <= x < 8 and 0 <= y < 8 and p[x][y] == krol:
                    return True
    return False


biala = 0
czarna = 0
for p in plansze:
    if szachuje(p, "W", "k"):
        biala += 1
    if szachuje(p, "w", "K"):
        czarna += 1
print("1.3", biala, czarna)
```
```cpp
// C++23
#include <algorithm>
#include <cctype>
#include <fstream>
#include <print>
#include <string>
#include <vector>

using Plansza = std::vector<std::string>;

std::vector<Plansza> wczytaj_plansze(const std::string& nazwa) {
    std::vector<Plansza> plansze;
    std::ifstream plik(nazwa);
    std::vector<std::string> wiersze;
    std::string linia;
    while (std::getline(plik, linia)) {
        // usuwamy białe znaki z końców (np. \r), jak strip() w Pythonie
        while (!linia.empty() && std::isspace((unsigned char)linia.back())) linia.pop_back();
        while (!linia.empty() && std::isspace((unsigned char)linia.front())) linia.erase(0, 1);
        wiersze.push_back(linia);
    }
    for (size_t i = 0; i < wiersze.size(); i += 9)
        if (i + 8 <= wiersze.size() && !wiersze[i].empty())
            plansze.push_back(Plansza(wiersze.begin() + i, wiersze.begin() + i + 8));
    return plansze;
}

// 1.3 - czy jakaś wieża (znak wieza) szachuje króla (znak krol)
bool szachuje(const Plansza& p, char wieza, char krol) {
    int kierunki[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    for (int w = 0; w < 8; w++) {
        for (int k = 0; k < 8; k++) {
            if (p[w][k] != wieza) continue;
            for (auto& [dw, dk] : kierunki) {
                int x = w + dw, y = k + dk;
                while (0 <= x && x < 8 && 0 <= y && y < 8 && p[x][y] == '.') {
                    x += dw;
                    y += dk;
                }
                if (0 <= x && x < 8 && 0 <= y && y < 8 && p[x][y] == krol) return true;
            }
        }
    }
    return false;
}

int main() {
    std::vector<Plansza> plansze = wczytaj_plansze("szachy.txt");

    // 1.1
    int ile_plansz = 0;
    int max_pustych = 0;
    for (auto& p : plansze) {
        int puste = 0;
        for (int k = 0; k < 8; k++) {
            bool pusta = true;
            for (int w = 0; w < 8; w++)
                if (p[w][k] != '.') pusta = false;
            if (pusta) puste++;
        }
        if (puste > 0) {
            ile_plansz++;
            max_pustych = std::max(max_pustych, puste);
        }
    }
    std::println("1.1 {} {}", ile_plansz, max_pustych);

    // 1.2
    int ile_rownowag = 0;
    int min_bierek = 64;
    for (auto& p : plansze) {
        std::string biale, czarne;
        for (auto& wiersz : p) {
            for (char znak : wiersz) {
                if (std::isupper((unsigned char)znak))
                    biale += znak;
                else if (std::islower((unsigned char)znak))
                    czarne += (char)std::toupper((unsigned char)znak);
            }
        }
        std::ranges::sort(biale);
        std::ranges::sort(czarne);
        if (biale == czarne) {
            ile_rownowag++;
            min_bierek = std::min(min_bierek, (int)(biale.size() + czarne.size()));
        }
    }
    std::println("1.2 {} {}", ile_rownowag, min_bierek);

    // 1.3
    int biala = 0;
    int czarna = 0;
    for (auto& p : plansze) {
        if (szachuje(p, 'W', 'k')) biala++;
        if (szachuje(p, 'w', 'K')) czarna++;
    }
    std::println("1.3 {} {}", biala, czarna);
}
```
```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    static List<List<String>> wczytajPlansze(String nazwa) throws Exception {
        var plansze = new ArrayList<List<String>>();
        var wiersze = new ArrayList<String>();
        for (var linia : Files.readAllLines(Path.of(nazwa))) wiersze.add(linia.strip());
        for (int i = 0; i < wiersze.size(); i += 9)
            if (i + 8 <= wiersze.size() && !wiersze.get(i).isEmpty())
                plansze.add(wiersze.subList(i, i + 8));
        return plansze;
    }

    // 1.3 - czy jakaś wieża (znak wieza) szachuje króla (znak krol)
    static boolean szachuje(List<String> p, char wieza, char krol) {
        int[][] kierunki = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int w = 0; w < 8; w++) {
            for (int k = 0; k < 8; k++) {
                if (p.get(w).charAt(k) != wieza) continue;
                for (var d : kierunki) {
                    int x = w + d[0], y = k + d[1];
                    while (0 <= x && x < 8 && 0 <= y && y < 8 && p.get(x).charAt(y) == '.') {
                        x += d[0];
                        y += d[1];
                    }
                    if (0 <= x && x < 8 && 0 <= y && y < 8 && p.get(x).charAt(y) == krol) return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        var plansze = wczytajPlansze("szachy.txt");

        // 1.1
        int ilePlansz = 0;
        int maxPustych = 0;
        for (var p : plansze) {
            int puste = 0;
            for (int k = 0; k < 8; k++) {
                boolean pusta = true;
                for (int w = 0; w < 8; w++)
                    if (p.get(w).charAt(k) != '.') pusta = false;
                if (pusta) puste++;
            }
            if (puste > 0) {
                ilePlansz++;
                maxPustych = Math.max(maxPustych, puste);
            }
        }
        System.out.println("1.1 " + ilePlansz + " " + maxPustych);

        // 1.2
        int ileRownowag = 0;
        int minBierek = 64;
        for (var p : plansze) {
            var biale = new ArrayList<Character>();
            var czarne = new ArrayList<Character>();
            for (var wiersz : p) {
                for (char znak : wiersz.toCharArray()) {
                    if (Character.isUpperCase(znak))
                        biale.add(znak);
                    else if (Character.isLowerCase(znak))
                        czarne.add(Character.toUpperCase(znak));
                }
            }
            Collections.sort(biale);
            Collections.sort(czarne);
            if (biale.equals(czarne)) {
                ileRownowag++;
                minBierek = Math.min(minBierek, biale.size() + czarne.size());
            }
        }
        System.out.println("1.2 " + ileRownowag + " " + minBierek);

        // 1.3
        int biala = 0;
        int czarna = 0;
        for (var p : plansze) {
            if (szachuje(p, 'W', 'k')) biala++;
            if (szachuje(p, 'w', 'K')) czarna++;
        }
        System.out.println("1.3 " + biala + " " + czarna);
    }
}
```

**Odpowiedź:** 1.1: `36 3`. 1.2: `22 28`. 1.3: `3 1`.

## 2.1, 2.2 i 2.3

> **Treść zadania:** Plansza B ma pola 0..s; na początku pionek stoi tylko na B[0]. Gra składa się z n tur opisanych tablicą A[1..n] dodatnich liczb całkowitych. W k-tej turze:
>
> ```
> Tura(k):
>     dla i = s, s-1, ..., A[k]
>         jeśli na B[i - A[k]] stoi pionek i B[i] jest puste
>             postaw pionek na B[i]
> ```
>
> Gra kończy się sukcesem, gdy po n turach pionek stoi na B[s].
>
> - 2.1 — Rozstrzygnij (TAK/NIE), czy gra kończy się sukcesem dla: A = [1, 2, 5, 10], s = 14; A = [13, 5, 5, 2, 7], s = 17; A = [7, 6, 5, 4, 3, 2, 1], s = 25 (np. A = [1, 2, 3], s = 5 → TAK).
> - 2.2 — Dla A = [5, 10, 15, ..., 100] i s = 500 podaj, na ilu polach będą stały pionki po zakończeniu gry.
> - 2.3 — Podaj przykładową tablicę A o co najwyżej 10 elementach, dla której gra kończy się sukcesem dla każdego s = 1, 2, ..., 200.

```py
def gra(A, s):
    B = [False] * (s + 1)
    B[0] = True
    for a in A:  # Tura(k)
        for i in range(s, a - 1, -1):
            if B[i - a] and not B[i]:
                B[i] = True
    return B


# 2.1
for A, s in [([1, 2, 3], 5), ([1, 2, 5, 10], 14), ([13, 5, 5, 2, 7], 17), ([7, 6, 5, 4, 3, 2, 1], 25)]:
    print("2.1", A, s, "TAK" if gra(A, s)[s] else "NIE")

# 2.2
A = list(range(5, 101, 5))
print("2.2", sum(gra(A, 500)))

# 2.3 - sprawdzenie przykładowej odpowiedzi
A = [1, 2, 4, 8, 16, 32, 64, 128]
print("2.3", all(gra(A, s)[s] for s in range(1, 201)))
```
```cpp
// C++23
#include <print>
#include <vector>

std::vector<bool> gra(const std::vector<int>& A, int s) {
    std::vector<bool> B(s + 1, false);
    B[0] = true;
    for (int a : A)  // Tura(k)
        for (int i = s; i >= a; i--)
            if (B[i - a] && !B[i]) B[i] = true;
    return B;
}

int main() {
    // 2.1
    std::vector<std::vector<int>> tablice = {{1, 2, 3}, {1, 2, 5, 10}, {13, 5, 5, 2, 7}, {7, 6, 5, 4, 3, 2, 1}};
    int sumy[] = {5, 14, 17, 25};
    for (int t = 0; t < 4; t++)
        std::println("2.1 {} {} {}", tablice[t], sumy[t], gra(tablice[t], sumy[t])[sumy[t]] ? "TAK" : "NIE");

    // 2.2
    std::vector<int> A;
    for (int a = 5; a <= 100; a += 5) A.push_back(a);
    int prawdziwe = 0;
    for (bool b : gra(A, 500))
        if (b) prawdziwe++;
    std::println("2.2 {}", prawdziwe);

    // 2.3 - sprawdzenie przykładowej odpowiedzi
    A = {1, 2, 4, 8, 16, 32, 64, 128};
    bool wszystkie = true;
    for (int s = 1; s <= 200; s++)
        if (!gra(A, s)[s]) wszystkie = false;
    std::println("2.3 {}", wszystkie ? "True" : "False");
}
```
```java
// Java 25
import java.util.*;

public class Zadanie {
    static boolean[] gra(int[] A, int s) {
        boolean[] B = new boolean[s + 1];
        B[0] = true;
        for (int a : A)  // Tura(k)
            for (int i = s; i >= a; i--)
                if (B[i - a] && !B[i]) B[i] = true;
        return B;
    }

    public static void main(String[] args) throws Exception {
        // 2.1
        int[][] tablice = {{1, 2, 3}, {1, 2, 5, 10}, {13, 5, 5, 2, 7}, {7, 6, 5, 4, 3, 2, 1}};
        int[] sumy = {5, 14, 17, 25};
        for (int t = 0; t < 4; t++)
            System.out.println("2.1 " + Arrays.toString(tablice[t]) + " " + sumy[t] + " "
                    + (gra(tablice[t], sumy[t])[sumy[t]] ? "TAK" : "NIE"));

        // 2.2
        int[] A = new int[20];
        for (int i = 0; i < 20; i++) A[i] = 5 * (i + 1);
        int prawdziwe = 0;
        for (boolean b : gra(A, 500))
            if (b) prawdziwe++;
        System.out.println("2.2 " + prawdziwe);

        // 2.3 - sprawdzenie przykładowej odpowiedzi
        A = new int[] {1, 2, 4, 8, 16, 32, 64, 128};
        boolean wszystkie = true;
        for (int s = 1; s <= 200; s++)
            if (!gra(A, s)[s]) wszystkie = false;
        System.out.println("2.3 " + (wszystkie ? "True" : "False"));
    }
}
```

**Odpowiedź:** 2.1: TAK (dane), NIE, TAK, TAK. 2.2: 101 (pola B[0], B[5], …, B[500]). 2.3: np. A = [1, 2, 4, 8, 16, 32, 64, 128] (każde s od 1 do 255 da się zapisać jako sumę różnych potęg dwójki).

## 3.1, 3.2, 3.3, 3.4 i 3.5

> **Treść zadania:** Potęgowanie modularne: b = a^x mod M (a, M — dodatnie, x — nieujemna liczba całkowita). Np. 2^5 mod 7 = 4.
>
> - 3.1 — Uzupełnij brakującą liczbę (x lub b) w wierszach: M = 11, a = 3, x = 3; M = 31, a = 5, b = 25; M = 59, a = 2, b = 5.
> - 3.2 — Zapisz algorytm obliczający a^x mod M wykonujący O(log x) operacji (dozwolone tylko podstawowe operacje arytmetyczne, porównania, instrukcje sterujące).
>
> Plik `liczby.txt` ma 1000 wierszy, w każdym trzy liczby M, a, b (≤ 10 000; M, a ≥ 2) oddzielone spacjami. Odpowiedzi do 3.3–3.5 zapisz w `wyniki3.txt` z numerami zadań (przykład: `liczby_przyklad.txt`, 5 wierszy).
>
> - 3.3 — Podaj, w ilu wierszach M jest liczbą pierwszą (przykład: 2).
> - 3.4 — Podaj, w ilu wierszach M i a są względnie pierwsze (przykład: 3).
> - 3.5 — Podaj, dla ilu trójek (M, a, b) istnieje x z przedziału [0, M−1] takie, że a^x mod M = b (przykład: 4).

```py
def potega_mod(a, x, M):
    # szybkie potęgowanie modularne - O(log x) mnożeń
    wynik = 1
    a = a % M
    while x > 0:
        if x % 2 == 1:
            wynik = wynik * a % M
        a = a * a % M
        x = x // 2
    return wynik


def czy_pierwsza(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def nwd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 3.1
print("3.1", potega_mod(3, 3, 11), potega_mod(9, 2, 80))
for M, a, b in [(31, 5, 25), (59, 2, 5)]:
    x = 0
    while potega_mod(a, x, M) != b:
        x += 1
    print("3.1 x =", x)

trojki = []
with open("liczby.txt") as file:
    for linia in file:
        M, a, b = map(int, linia.split())
        trojki.append((M, a, b))

# 3.3
print("3.3", sum(1 for M, a, b in trojki if czy_pierwsza(M)))

# 3.4
print("3.4", sum(1 for M, a, b in trojki if nwd(M, a) == 1))

# 3.5
ile = 0
for M, a, b in trojki:
    potega = 1 % M  # a^0 mod M
    for x in range(M):
        if potega == b:
            ile += 1
            break
        potega = potega * a % M
print("3.5", ile)
```
```cpp
// C++23
#include <array>
#include <fstream>
#include <print>
#include <vector>

long long potega_mod(long long a, long long x, long long M) {
    // szybkie potęgowanie modularne - O(log x) mnożeń
    long long wynik = 1;
    a = a % M;
    while (x > 0) {
        if (x % 2 == 1) wynik = wynik * a % M;
        a = a * a % M;
        x = x / 2;
    }
    return wynik;
}

bool czy_pierwsza(long long n) {
    if (n < 2) return false;
    for (long long i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}

long long nwd(long long a, long long b) {
    while (b > 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    // 3.1
    std::println("3.1 {} {}", potega_mod(3, 3, 11), potega_mod(9, 2, 80));
    int przyklady[2][3] = {{31, 5, 25}, {59, 2, 5}};
    for (auto& [M, a, b] : przyklady) {
        int x = 0;
        while (potega_mod(a, x, M) != b) x++;
        std::println("3.1 x = {}", x);
    }

    std::vector<std::array<long long, 3>> trojki;
    std::ifstream plik("liczby.txt");
    long long M, a, b;
    while (plik >> M >> a >> b) trojki.push_back({M, a, b});

    // 3.3
    int ile_pierwszych = 0;
    for (auto& [M, a, b] : trojki)
        if (czy_pierwsza(M)) ile_pierwszych++;
    std::println("3.3 {}", ile_pierwszych);

    // 3.4
    int ile_wzglednie = 0;
    for (auto& [M, a, b] : trojki)
        if (nwd(M, a) == 1) ile_wzglednie++;
    std::println("3.4 {}", ile_wzglednie);

    // 3.5
    int ile = 0;
    for (auto& [M, a, b] : trojki) {
        long long potega = 1 % M;  // a^0 mod M
        for (long long x = 0; x < M; x++) {
            if (potega == b) {
                ile++;
                break;
            }
            potega = potega * a % M;
        }
    }
    std::println("3.5 {}", ile);
}
```
```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    static long potegaMod(long a, long x, long M) {
        // szybkie potęgowanie modularne - O(log x) mnożeń
        long wynik = 1;
        a = a % M;
        while (x > 0) {
            if (x % 2 == 1) wynik = wynik * a % M;
            a = a * a % M;
            x = x / 2;
        }
        return wynik;
    }

    static boolean czyPierwsza(long n) {
        if (n < 2) return false;
        for (long i = 2; i * i <= n; i++)
            if (n % i == 0) return false;
        return true;
    }

    static long nwd(long a, long b) {
        while (b > 0) {
            long r = a % b;
            a = b;
            b = r;
        }
        return a;
    }

    public static void main(String[] args) throws Exception {
        // 3.1
        System.out.println("3.1 " + potegaMod(3, 3, 11) + " " + potegaMod(9, 2, 80));
        int[][] przyklady = {{31, 5, 25}, {59, 2, 5}};
        for (var p : przyklady) {
            int x = 0;
            while (potegaMod(p[1], x, p[0]) != p[2]) x++;
            System.out.println("3.1 x = " + x);
        }

        var trojki = new ArrayList<long[]>();  // {M, a, b}
        for (var linia : Files.readAllLines(Path.of("liczby.txt"))) {
            if (linia.isBlank()) continue;
            var t = linia.trim().split("\\s+");
            trojki.add(new long[] {Long.parseLong(t[0]), Long.parseLong(t[1]), Long.parseLong(t[2])});
        }

        // 3.3
        int ilePierwszych = 0;
        for (var t : trojki)
            if (czyPierwsza(t[0])) ilePierwszych++;
        System.out.println("3.3 " + ilePierwszych);

        // 3.4
        int ileWzglednie = 0;
        for (var t : trojki)
            if (nwd(t[0], t[1]) == 1) ileWzglednie++;
        System.out.println("3.4 " + ileWzglednie);

        // 3.5
        int ile = 0;
        for (var t : trojki) {
            long M = t[0], a = t[1], b = t[2];
            long potega = 1 % M;  // a^0 mod M
            for (long x = 0; x < M; x++) {
                if (potega == b) {
                    ile++;
                    break;
                }
                potega = potega * a % M;
            }
        }
        System.out.println("3.5 " + ile);
    }
}
```

**Odpowiedź:** 3.1: b = 5 (M = 11), x = 2 (M = 31), x = 6 (M = 59), b = 1 (M = 80). 3.2: funkcja `potega_mod` (szybkie potęgowanie, O(log x)). 3.3: 343. 3.4: 712. 3.5: 764.
