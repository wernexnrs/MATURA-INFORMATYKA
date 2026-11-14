<h1 align="center">Matura 2024 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2024-czerwiec-matura-stara-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.2

> **Treść zadania:** Dodatnia liczba całkowita L jest *nieliczna*, jeśli w jej zapisie binarnym żadne dwie jedynki nie sąsiadują ze sobą.
>
> - 1.1 — Uzupełnij tabelę: podaj zapis binarny liczb 2001₈ i 3574₁₆ oraz rozstrzygnij (PRAWDA/FAŁSZ), czy są nieliczne. Przykład: 259₁₀ = 100000011₂ — FAŁSZ.
> - 1.2 — Napisz funkcję `czy_nieliczna(k)`, która dla dodatniej liczby k zwraca PRAWDA, gdy k jest nieliczna, a FAŁSZ w przeciwnym razie. Wolno używać tylko zmiennych całkowitych i podstawowych operacji arytmetycznych, porównań i instrukcji sterujących — bez funkcji wbudowanych i bez funkcji zamiany systemów liczbowych.

```py
# 1.2 - sprawdzamy kolejne cyfry binarne od końca
def czy_nieliczna(k):
    poprzednia = 0
    while k > 0:
        cyfra = k % 2
        if cyfra == 1 and poprzednia == 1:
            return False
        poprzednia = cyfra
        k = k // 2
    return True


# 1.1
for zapis, podstawa in [("20012", 8), ("3574", 16)]:
    L = int(zapis, podstawa)
    print(zapis, podstawa, bin(L)[2:], czy_nieliczna(L))
```
```cpp
// C++23
#include <print>
#include <string>

// 1.2 - sprawdzamy kolejne cyfry binarne od końca
bool czy_nieliczna(long long k) {
    int poprzednia = 0;
    while (k > 0) {
        int cyfra = k % 2;
        if (cyfra == 1 && poprzednia == 1) return false;
        poprzednia = cyfra;
        k = k / 2;
    }
    return true;
}

std::string binarnie(long long n) {
    std::string wynik;
    while (n > 0) {
        wynik = char('0' + n % 2) + wynik;
        n /= 2;
    }
    return wynik;
}

int main() {
    // 1.1
    std::string zapisy[] = {"20012", "3574"};
    int podstawy[] = {8, 16};
    for (int i = 0; i < 2; i++) {
        long long L = std::stoll(zapisy[i], nullptr, podstawy[i]);
        std::println("{} {} {} {}", zapisy[i], podstawy[i], binarnie(L), czy_nieliczna(L) ? "True" : "False");
    }
}
```
```java
// Java 25
public class Zadanie {
    // 1.2 - sprawdzamy kolejne cyfry binarne od końca
    static boolean czyNieliczna(long k) {
        long poprzednia = 0;
        while (k > 0) {
            long cyfra = k % 2;
            if (cyfra == 1 && poprzednia == 1) return false;
            poprzednia = cyfra;
            k = k / 2;
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        // 1.1
        String[] zapisy = {"20012", "3574"};
        int[] podstawy = {8, 16};
        for (int i = 0; i < 2; i++) {
            long L = Long.parseLong(zapisy[i], podstawy[i]);
            System.out.println(zapisy[i] + " " + podstawy[i] + " " + Long.toBinaryString(L) + " "
                    + (czyNieliczna(L) ? "True" : "False"));
        }
    }
}
```

**Odpowiedź:** 1.1: 20012₈ = 10000000001010₂ – PRAWDA; 3574₁₆ = 11010101110100₂ – FAŁSZ. 1.2: funkcja `czy_nieliczna`.

## 2.1, 2.2 i 2.3

> **Treść zadania:** Dana jest tablica A[1..n] i algorytm 1:
>
> ```
> p ← 1; m ← 1
> dla i = 1, 2, ..., n
>     licz ← 0
>     dla j = 1, 2, ..., n
>         jeżeli A[i] = A[j]: licz ← licz + 1
>     jeżeli licz > m: p ← i; m ← licz
> ```
>
> - 2.1 — Podaj wartości p, A[p] i m po wykonaniu algorytmu dla A = [7, 9, 15, 0, 6, 7, 6, 10, 15, 6, 0].
> - 2.2 — Podaj, ile razy wykonywane jest porównanie A[i] = A[j] dla n = 3 oraz dla dowolnego n (wzór).
> - 2.3 — Uzupełnij luki (zakres pętli po i, początkową wartość `licz`, zakres pętli po j) w algorytmie 2, który daje ten sam wynik co algorytm 1, ale wykonuje porównanie A[i] = A[j] nie więcej niż n(n−1)/2 razy.

```py
def algorytm1(A):                   # A[0] to element A[1] z treści
    n = len(A)
    p, m = 1, 1
    porownania = 0
    for i in range(1, n + 1):
        licz = 0
        for j in range(1, n + 1):
            porownania += 1
            if A[i - 1] == A[j - 1]:
                licz += 1
        if licz > m:
            p, m = i, licz
    return p, A[p - 1], m, porownania


# 2.3 - porównujemy A[i] tylko z elementami dalej w tablicy
def algorytm2(A):
    n = len(A)
    p, m = 1, 1
    porownania = 0
    for i in range(1, n):            # i = 1, 2, ..., n - 1
        licz = 1                     # A[i] liczy się samo
        for j in range(i + 1, n + 1):    # j = i + 1, ..., n
            porownania += 1
            if A[i - 1] == A[j - 1]:
                licz += 1
        if licz > m:
            p, m = i, licz
    return p, A[p - 1], m, porownania


A = [7, 9, 15, 0, 6, 7, 6, 10, 15, 6, 0]
print(algorytm1(A))                  # 2.1 (p, A[p], m, liczba porównań)
print(algorytm1([1, 2, 3])[3])       # 2.2 dla n = 3
print(algorytm2(A))                  # 2.3 - ten sam wynik, n(n-1)/2 = 55 porównań
```
```cpp
// C++23
#include <format>
#include <print>
#include <string>
#include <vector>

struct Wynik {
    int p, ap, m, porownania;  // p, A[p], m, liczba porównań
    std::string tekst() const { return std::format("({}, {}, {}, {})", p, ap, m, porownania); }
};

Wynik algorytm1(const std::vector<int>& A) {  // A[0] to element A[1] z treści
    int n = A.size();
    int p = 1, m = 1;
    int porownania = 0;
    for (int i = 1; i <= n; i++) {
        int licz = 0;
        for (int j = 1; j <= n; j++) {
            porownania++;
            if (A[i - 1] == A[j - 1]) licz++;
        }
        if (licz > m) {
            p = i;
            m = licz;
        }
    }
    return {p, A[p - 1], m, porownania};
}

// 2.3 - porównujemy A[i] tylko z elementami dalej w tablicy
Wynik algorytm2(const std::vector<int>& A) {
    int n = A.size();
    int p = 1, m = 1;
    int porownania = 0;
    for (int i = 1; i < n; i++) {          // i = 1, 2, ..., n - 1
        int licz = 1;                      // A[i] liczy się samo
        for (int j = i + 1; j <= n; j++) { // j = i + 1, ..., n
            porownania++;
            if (A[i - 1] == A[j - 1]) licz++;
        }
        if (licz > m) {
            p = i;
            m = licz;
        }
    }
    return {p, A[p - 1], m, porownania};
}

int main() {
    std::vector<int> A = {7, 9, 15, 0, 6, 7, 6, 10, 15, 6, 0};
    std::println("{}", algorytm1(A).tekst());                 // 2.1 (p, A[p], m, liczba porównań)
    std::println("{}", algorytm1({1, 2, 3}).porownania);      // 2.2 dla n = 3
    std::println("{}", algorytm2(A).tekst());                 // 2.3 - ten sam wynik, n(n-1)/2 = 55 porównań
}
```
```java
// Java 25
public class Zadanie {
    record Wynik(int p, int ap, int m, int porownania) {  // p, A[p], m, liczba porównań
        String tekst() { return "(" + p + ", " + ap + ", " + m + ", " + porownania + ")"; }
    }

    static Wynik algorytm1(int[] A) {  // A[0] to element A[1] z treści
        int n = A.length;
        int p = 1, m = 1;
        int porownania = 0;
        for (int i = 1; i <= n; i++) {
            int licz = 0;
            for (int j = 1; j <= n; j++) {
                porownania++;
                if (A[i - 1] == A[j - 1]) licz++;
            }
            if (licz > m) {
                p = i;
                m = licz;
            }
        }
        return new Wynik(p, A[p - 1], m, porownania);
    }

    // 2.3 - porównujemy A[i] tylko z elementami dalej w tablicy
    static Wynik algorytm2(int[] A) {
        int n = A.length;
        int p = 1, m = 1;
        int porownania = 0;
        for (int i = 1; i < n; i++) {          // i = 1, 2, ..., n - 1
            int licz = 1;                      // A[i] liczy się samo
            for (int j = i + 1; j <= n; j++) { // j = i + 1, ..., n
                porownania++;
                if (A[i - 1] == A[j - 1]) licz++;
            }
            if (licz > m) {
                p = i;
                m = licz;
            }
        }
        return new Wynik(p, A[p - 1], m, porownania);
    }

    public static void main(String[] args) throws Exception {
        int[] A = {7, 9, 15, 0, 6, 7, 6, 10, 15, 6, 0};
        System.out.println(algorytm1(A).tekst());                         // 2.1 (p, A[p], m, liczba porównań)
        System.out.println(algorytm1(new int[] {1, 2, 3}).porownania());  // 2.2 dla n = 3
        System.out.println(algorytm2(A).tekst());                         // 2.3 - ten sam wynik, n(n-1)/2 = 55 porównań
    }
}
```

**Odpowiedź:** 2.1: p = 5, A[p] = 6, m = 3. 2.2: n = 3 → 9, dla n → n². 2.3: `dla i = 1, 2, ..., n - 1`, `licz ← 1`, `dla j = i + 1, i + 2, ..., n`.

## 4.1, 4.2, 4.3 i 4.4

> **Treść zadania:** Plik `slowa.txt` zawiera 1000 słów z małych liter alfabetu angielskiego, o długości od 1 do 200. Odpowiedzi zapisz w `wyniki4.txt`, poprzedzając je numerami zadań (przykład: `slowa_przyklad.txt`, 10 słów).
>
> - 4.1 — Podaj, w ilu słowach występuje fragment `k?t`, gdzie `?` to dowolna jedna litera (np. „alamakota”, „brokat”, ale nie „krata”). Przykład: 2.
> - 4.2 — Wypisz wszystkie pięcioliterowe fragmenty słów zaczynające się i kończące literą `e` (przykład: `erefe efere`).
> - 4.3 — ROT13 zamienia każdą literę na literę o 13 pozycji dalej (cyklicznie). Podaj, ile słów po zakodowaniu ROT13 staje się swoim odwróceniem (np. `aren` → `nera`), i wypisz najdłuższe z nich. Przykład: `2` i `aren`.
> - 4.4 — Wypisz wszystkie słowa, w których ta sama litera zajmuje co najmniej połowę pozycji (np. „owocowo” tak, „ambaras” nie). Przykład: terefere, ananas, bo, alabama.

```py
with open("slowa.txt") as file:
    slowa = [linia.strip() for linia in file if linia.strip()]

wynik = open("wyniki4.txt", "w")

# 4.1
ile = 0
for slowo in slowa:
    for i in range(len(slowo) - 2):
        if slowo[i] == "k" and slowo[i + 2] == "t":
            ile += 1
            break
print("4.1", ile, file=wynik)

# 4.2
fragmenty = []
for slowo in slowa:
    for i in range(len(slowo) - 4):
        if slowo[i] == "e" and slowo[i + 4] == "e":
            fragmenty.append(slowo[i:i + 5])
print("4.2", *fragmenty, file=wynik)


# 4.3
def rot13(slowo):
    wynik_rot = ""
    for c in slowo:
        wynik_rot += chr((ord(c) - ord("a") + 13) % 26 + ord("a"))
    return wynik_rot


dobre = [slowo for slowo in slowa if rot13(slowo) == slowo[::-1]]
najdluzsze = max(dobre, key=len)
print("4.3", len(dobre), najdluzsze, file=wynik)

# 4.4
print("4.4", file=wynik)
for slowo in slowa:
    if 2 * max(slowo.count(c) for c in slowo) >= len(slowo):
        print(slowo, file=wynik)

wynik.close()
```
```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>

// 4.3
std::string rot13(const std::string& slowo) {
    std::string wynik_rot;
    for (char c : slowo) wynik_rot += (char)((c - 'a' + 13) % 26 + 'a');
    return wynik_rot;
}

int main() {
    std::vector<std::string> slowa;
    std::ifstream plik("slowa.txt");
    std::string linia;
    while (plik >> linia) slowa.push_back(linia);

    std::ofstream wynik("wyniki4.txt");

    // 4.1
    int ile = 0;
    for (auto& slowo : slowa) {
        for (size_t i = 0; i + 2 < slowo.size(); i++) {
            if (slowo[i] == 'k' && slowo[i + 2] == 't') {
                ile++;
                break;
            }
        }
    }
    wynik << "4.1 " << ile << "\n";

    // 4.2
    wynik << "4.2";
    for (auto& slowo : slowa)
        for (size_t i = 0; i + 4 < slowo.size(); i++)
            if (slowo[i] == 'e' && slowo[i + 4] == 'e') wynik << " " << slowo.substr(i, 5);
    wynik << "\n";

    std::vector<std::string> dobre;
    for (auto& slowo : slowa)
        if (rot13(slowo) == std::string(slowo.rbegin(), slowo.rend())) dobre.push_back(slowo);
    std::string najdluzsze = dobre[0];  // przy remisie pierwsze (jak max w Pythonie)
    for (auto& slowo : dobre)
        if (slowo.size() > najdluzsze.size()) najdluzsze = slowo;
    wynik << "4.3 " << dobre.size() << " " << najdluzsze << "\n";

    // 4.4
    wynik << "4.4\n";
    for (auto& slowo : slowa) {
        long najczestsza = 0;
        for (char c : slowo) najczestsza = std::max(najczestsza, (long)std::count(slowo.begin(), slowo.end(), c));
        if (2 * najczestsza >= (long)slowo.size()) wynik << slowo << "\n";
    }
}
```
```java
// Java 25
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    // 4.3
    static String rot13(String slowo) {
        var wynikRot = new StringBuilder();
        for (char c : slowo.toCharArray()) wynikRot.append((char) ((c - 'a' + 13) % 26 + 'a'));
        return wynikRot.toString();
    }

    public static void main(String[] args) throws Exception {
        var slowa = new ArrayList<String>();
        for (var linia : Files.readAllLines(Path.of("slowa.txt")))
            if (!linia.isBlank()) slowa.add(linia.strip());

        try (var wynik = new PrintWriter("wyniki4.txt")) {
            // 4.1
            int ile = 0;
            for (var slowo : slowa) {
                for (int i = 0; i + 2 < slowo.length(); i++) {
                    if (slowo.charAt(i) == 'k' && slowo.charAt(i + 2) == 't') {
                        ile++;
                        break;
                    }
                }
            }
            wynik.println("4.1 " + ile);

            // 4.2
            var fragmenty = new StringBuilder("4.2");
            for (var slowo : slowa)
                for (int i = 0; i + 4 < slowo.length(); i++)
                    if (slowo.charAt(i) == 'e' && slowo.charAt(i + 4) == 'e')
                        fragmenty.append(" ").append(slowo, i, i + 5);
            wynik.println(fragmenty);

            var dobre = new ArrayList<String>();
            for (var slowo : slowa)
                if (rot13(slowo).equals(new StringBuilder(slowo).reverse().toString())) dobre.add(slowo);
            String najdluzsze = dobre.get(0);  // przy remisie pierwsze (jak max w Pythonie)
            for (var slowo : dobre)
                if (slowo.length() > najdluzsze.length()) najdluzsze = slowo;
            wynik.println("4.3 " + dobre.size() + " " + najdluzsze);

            // 4.4
            wynik.println("4.4");
            for (var slowo : slowa) {
                int[] ileLiter = new int[128];
                int najczestsza = 0;
                for (char c : slowo.toCharArray()) najczestsza = Math.max(najczestsza, ++ileLiter[c]);
                if (2 * najczestsza >= slowo.length()) wynik.println(slowo);
            }
        }
    }
}
```

**Odpowiedź:** 4.1: 26. 4.2: ebeee eeeie eipqe eqgle ejoge ecype evuye enmje ellye elome exsxe ezobe elnne ehcye evrue esfxe etrfe eryae exdye etcce etuke evtte. 4.3: 5 słów, najdłuższe: rhszzohhubwbojohuubmmfue. 4.4: vzwzwgszezvzzlzzzzzzouz, azaaasfakaaaxbaaaaau, ppppppnoppnoclpop, zggggggpegpnovzgg, nyrpvqycpaylffffffffffffff, kkkkkkkkkkwpijccdbl, tstevttebttktnetitbttti, gvsvjvvvvvqppvuvcvvvi.
