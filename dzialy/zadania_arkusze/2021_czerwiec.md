<h1 align="center">Matura 2021 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2021-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2021-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2021-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2021-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1 i 1.2

> **Treść zadania:** Każdą dodatnią liczbę całkowitą n można zapisać jako sumę kwadratów dodatnich liczb całkowitych (reprezentacja kwadratowa); długość reprezentacji to liczba składników (np. 9 = 3² = 2²+2²+1² = 2²+1²+1²+1²+1²+1², długości 1, 3 i 6). W metodzie zachłannej w każdym kroku bierze się największy kwadrat, przy którym suma nie przekracza n — nie zawsze daje to najkrótszą reprezentację.
>
> - **1.1** — Uzupełnij tabelę: podaj reprezentację liczby 23 krótszą niż zachłanna (zachłanna: 4²+2²+1²+1²+1²) oraz wymyśl własną liczbę n > 23, dla której reprezentacja zachłanna nie jest najkrótsza — zapisz obie reprezentacje (przykłady z tabeli: 12 = 3²+1²+1²+1² wobec 2²+2²+2²; 18 = 4²+1²+1² wobec 3²+3²).
> - **1.2** — Napisz algorytm, który dla dodatniej liczby całkowitej n oblicza długość `dl` jej reprezentacji kwadratowej wyznaczonej metodą zachłanną. Wolno używać tylko podstawowych operacji arytmetycznych (bez funkcji wbudowanych, w szczególności bez pierwiastka). Przykład: dla n = 12 wynikiem jest dl = 4.

```py
def zachlanna(n):
    # 1.2 - długość reprezentacji metodą zachłanną, bez funkcji pierwiastek
    kw = 1
    while (kw + 1) * (kw + 1) <= n:
        kw += 1
    dl = 0
    s = n
    while s > 0:
        if kw * kw <= s:
            s -= kw * kw
            dl += 1
        else:
            kw -= 1
    return dl


def najkrotsza(n):
    # długość najkrótszej reprezentacji (programowanie dynamiczne) - do sprawdzenia 1.1
    najkrotsze = [0] * (n + 1)
    for i in range(1, n + 1):
        najkrotsze[i] = i  # same jedynki
        k = 1
        while k * k <= i:
            najkrotsze[i] = min(najkrotsze[i], najkrotsze[i - k * k] + 1)
            k += 1
    return najkrotsze[n]


print(zachlanna(12))
print(zachlanna(23), najkrotsza(23))
# 1.1 - pierwsza liczba n > 23, dla której metoda zachłanna nie daje najkrótszej reprezentacji
n = 24
while zachlanna(n) == najkrotsza(n):
    n += 1
print(n, zachlanna(n), najkrotsza(n))
```
```cpp
// C++23
#include <algorithm>
#include <print>
#include <vector>

int zachlanna(int n) {
    // 1.2 - długość reprezentacji metodą zachłanną, bez funkcji pierwiastek
    int kw = 1;
    while ((kw + 1) * (kw + 1) <= n) kw++;
    int dl = 0;
    int s = n;
    while (s > 0) {
        if (kw * kw <= s) {
            s -= kw * kw;
            dl++;
        } else {
            kw--;
        }
    }
    return dl;
}

int najkrotsza(int n) {
    // długość najkrótszej reprezentacji (programowanie dynamiczne) - do sprawdzenia 1.1
    std::vector<int> najkrotsze(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        najkrotsze[i] = i;  // same jedynki
        for (int k = 1; k * k <= i; k++)
            najkrotsze[i] = std::min(najkrotsze[i], najkrotsze[i - k * k] + 1);
    }
    return najkrotsze[n];
}

int main() {
    std::println("{}", zachlanna(12));
    std::println("{} {}", zachlanna(23), najkrotsza(23));
    // 1.1 - pierwsza liczba n > 23, dla której metoda zachłanna nie daje najkrótszej reprezentacji
    int n = 24;
    while (zachlanna(n) == najkrotsza(n)) n++;
    std::println("{} {} {}", n, zachlanna(n), najkrotsza(n));
}
```
```java
// Java 25
public class Zadanie {
    static int zachlanna(int n) {
        // 1.2 - długość reprezentacji metodą zachłanną, bez funkcji pierwiastek
        int kw = 1;
        while ((kw + 1) * (kw + 1) <= n) kw++;
        int dl = 0;
        int s = n;
        while (s > 0) {
            if (kw * kw <= s) {
                s -= kw * kw;
                dl++;
            } else {
                kw--;
            }
        }
        return dl;
    }

    static int najkrotsza(int n) {
        // długość najkrótszej reprezentacji (programowanie dynamiczne) - do sprawdzenia 1.1
        int[] najkrotsze = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            najkrotsze[i] = i;  // same jedynki
            for (int k = 1; k * k <= i; k++)
                najkrotsze[i] = Math.min(najkrotsze[i], najkrotsze[i - k * k] + 1);
        }
        return najkrotsze[n];
    }

    public static void main(String[] args) throws Exception {
        System.out.println(zachlanna(12));
        System.out.println(zachlanna(23) + " " + najkrotsza(23));
        // 1.1 - pierwsza liczba n > 23, dla której metoda zachłanna nie daje najkrótszej reprezentacji
        int n = 24;
        while (zachlanna(n) == najkrotsza(n)) n++;
        System.out.println(n + " " + zachlanna(n) + " " + najkrotsza(n));
    }
}
```
**Odpowiedź:** 1.1: 23 = 3² + 3² + 2² + 1²; np. n = 32: zachłannie 5² + 2² + 1² + 1² + 1², krócej 4² + 4². 1.2: algorytm powyżej (dla n = 12: dl = 4)

> W kluczu CKE przykładowy pseudokod do 1.2 ma warunek `kw * kw < s` — powinno być `kw * kw ≤ s` (z `<` np. dla n = 12 pętla się nie kończy).

## 2.1 i 2.2

> **Treść zadania:** Dana jest liczba n, tablica liczb całkowitych T[1..n] oraz rekurencyjna procedura (s, k — dodatnie, s ≤ n):
>
> ```
> modyfikuj(s, k)
>     jeżeli s + k < n to
>         modyfikuj(s + k, k)
>     i ← s + 1
>     dopóki (i ≤ n) oraz (i ≤ s + k) wykonuj
>         T[s] ← T[s] + T[i]
>         i ← i + 1
> ```
>
> - **2.1** — Podaj zawartość T po wywołaniu `modyfikuj(s, k)` dla: n=10, T=[1,4,2,8,3,6,2,9,1,5], s=5, k=6; n=13, T=[4,2,6,2,9,3,5,2,7,4,3,2,3], s=3, k=5 oraz dla tej samej tablicy s=4, k=4. (Przykład: n=8, T=[1,…,1], s=3, k=3 daje [1,1,6,1,1,3,1,1].)
> - **2.2** — Podaj łączną liczbę wywołań procedury (licząc pierwsze) dla: n=5, s=1, k=3; n=2021, s=1, k=100; n=2021, s=20, k=35.

```py
def modyfikuj(T, n, s, k):
    # T[0] nieużywane - tablica indeksowana od 1; zwraca liczbę wywołań
    wywolania = 1
    if s + k < n:
        wywolania += modyfikuj(T, n, s + k, k)
    i = s + 1
    while i <= n and i <= s + k:
        T[s] = T[s] + T[i]
        i += 1
    return wywolania


# 2.1
for T, s, k in [([1, 4, 2, 8, 3, 6, 2, 9, 1, 5], 5, 6),
                ([4, 2, 6, 2, 9, 3, 5, 2, 7, 4, 3, 2, 3], 3, 5),
                ([4, 2, 6, 2, 9, 3, 5, 2, 7, 4, 3, 2, 3], 4, 4)]:
    T = [None] + T
    modyfikuj(T, len(T) - 1, s, k)
    print(T[1:])

# 2.2
for n, s, k in [(5, 1, 3), (2021, 1, 100), (2021, 20, 35)]:
    T = [None] + [0] * n
    print(n, s, k, modyfikuj(T, n, s, k))
```
```cpp
// C++23
#include <print>
#include <vector>

// T[0] nieużywane - tablica indeksowana od 1; zwraca liczbę wywołań
int modyfikuj(std::vector<long long>& T, int n, int s, int k) {
    int wywolania = 1;
    if (s + k < n) wywolania += modyfikuj(T, n, s + k, k);
    int i = s + 1;
    while (i <= n && i <= s + k) {
        T[s] = T[s] + T[i];
        i++;
    }
    return wywolania;
}

int main() {
    // 2.1
    std::vector<std::vector<long long>> tablice = {
        {1, 4, 2, 8, 3, 6, 2, 9, 1, 5},
        {4, 2, 6, 2, 9, 3, 5, 2, 7, 4, 3, 2, 3},
        {4, 2, 6, 2, 9, 3, 5, 2, 7, 4, 3, 2, 3}};
    int sk[3][2] = {{5, 6}, {3, 5}, {4, 4}};
    for (int t = 0; t < 3; t++) {
        std::vector<long long> T = {0};  // T[0] nieużywane
        T.insert(T.end(), tablice[t].begin(), tablice[t].end());
        modyfikuj(T, T.size() - 1, sk[t][0], sk[t][1]);
        std::vector<long long> bez0(T.begin() + 1, T.end());
        std::println("{}", bez0);  // format [1, 4, 2, ...] jak w Pythonie
    }
    // 2.2
    int dane[3][3] = {{5, 1, 3}, {2021, 1, 100}, {2021, 20, 35}};
    for (auto& d : dane) {
        int n = d[0], s = d[1], k = d[2];
        std::vector<long long> T(n + 1, 0);
        std::println("{} {} {} {}", n, s, k, modyfikuj(T, n, s, k));
    }
}
```
```java
// Java 25
import java.util.*;

public class Zadanie {
    // T[0] nieużywane - tablica indeksowana od 1; zwraca liczbę wywołań
    static int modyfikuj(long[] T, int n, int s, int k) {
        int wywolania = 1;
        if (s + k < n) wywolania += modyfikuj(T, n, s + k, k);
        int i = s + 1;
        while (i <= n && i <= s + k) {
            T[s] = T[s] + T[i];
            i++;
        }
        return wywolania;
    }

    public static void main(String[] args) throws Exception {
        // 2.1
        long[][] tablice = {
            {1, 4, 2, 8, 3, 6, 2, 9, 1, 5},
            {4, 2, 6, 2, 9, 3, 5, 2, 7, 4, 3, 2, 3},
            {4, 2, 6, 2, 9, 3, 5, 2, 7, 4, 3, 2, 3}};
        int[][] sk = {{5, 6}, {3, 5}, {4, 4}};
        for (int t = 0; t < 3; t++) {
            long[] T = new long[tablice[t].length + 1];  // T[0] nieużywane
            System.arraycopy(tablice[t], 0, T, 1, tablice[t].length);
            modyfikuj(T, T.length - 1, sk[t][0], sk[t][1]);
            System.out.println(Arrays.toString(Arrays.copyOfRange(T, 1, T.length)));
        }
        // 2.2
        int[][] dane = {{5, 1, 3}, {2021, 1, 100}, {2021, 20, 35}};
        for (var d : dane) {
            int n = d[0], s = d[1], k = d[2];
            long[] T = new long[n + 1];
            System.out.println(n + " " + s + " " + k + " " + modyfikuj(T, n, s, k));
        }
    }
}
```
**Odpowiedź:** 2.1: [1, 4, 2, 8, 26, 6, 2, 9, 1, 5]; [4, 2, 46, 2, 9, 3, 5, 21, 7, 4, 3, 2, 3]; [4, 2, 6, 40, 9, 3, 5, 21, 7, 4, 3, 5, 3]. 2.2: 21 i 58

> W kluczu CKE w drugim wierszu 2.1 jest literówka: [1,4,2,8,26,6,2,**6**,1,5] — ósmy element nie jest zmieniany i wynosi 9.

## 4.1, 4.2, 4.3 i 4.4

> **Treść zadania:** Plik `napisy.txt` zawiera 1000 wierszy, każdy to napis długości 50 złożony z wielkich liter alfabetu angielskiego i cyfr. Odpowiedzi zapisz w pliku `wyniki4.txt`, poprzedzając każdą numerem zadania. Plik `przyklad.txt` zawiera dane przykładowe (wyniki dla niego podano niżej).
>
> - **4.1** — Podaj łączną liczbę cyfr we wszystkich napisach. (Przykład: 46504.)
> - **4.2** — W co dwudziestym wierszu (20, 40, …, 1000) ukryto jedną literę hasła: w wierszu 20 na pozycji 1., w wierszu 40 na pozycji 2., …, w wierszu 1000 na pozycji 50. Podaj to 50-znakowe hasło. (Przykład: `UDALOSIEIZDAJEMYEGZAMINYMATURALNEZWIELUPRZEDMIOTOW`.)
> - **4.3** — Niektóre napisy można zamienić w palindrom, dopisując dokładnie jeden znak na początku lub na końcu. Podaj hasło utworzone ze środkowych liter tak powstałych palindromów (w kolejności wierszy). (Przykład: `INFORMATYKA`.)
> - **4.4** — Cyfry z każdego wiersza grupuj kolejno po dwie (ostatnią pomiń, gdy cyfr jest nieparzyście wiele). Liczbę z przedziału [65, 90] zamień na znak ASCII o tym kodzie, pozostałe pomiń. Odczyt kończy się po otrzymaniu trzech kolejnych znaków `X`. Podaj odczytane hasło. (Przykład: `NAPISANIEMATURYXXX`.)

```py
napisy = []
with open("napisy.txt") as file:
    for line in file:
        napisy.append(line.strip())

# 4.1
cyfry_razem = 0
for napis in napisy:
    for znak in napis:
        if znak.isdigit():
            cyfry_razem += 1

# 4.2 - w wierszu 20*j litera na pozycji j (numeracja od 1)
haslo2 = ""
for nr in range(20, 1001, 20):
    haslo2 += napisy[nr - 1][nr // 20 - 1]

# 4.3 - dopisanie znaku na końcu: napis[1:] musi być palindromem, środek to napis[25];
#       dopisanie na początku: napis[:-1] musi być palindromem, środek to napis[24]
haslo3 = ""
for napis in napisy:
    if napis[1:] == napis[1:][::-1]:
        haslo3 += napis[25]
    elif napis[:-1] == napis[:-1][::-1]:
        haslo3 += napis[24]

# 4.4 - cyfry z wiersza w parach, koniec po trzech kolejnych X (także z różnych wierszy)
haslo4 = ""
for napis in napisy:
    cyfry = []
    for znak in napis:
        if znak.isdigit():
            cyfry.append(znak)
    for j in range(0, len(cyfry) - 1, 2):
        liczba = int(cyfry[j] + cyfry[j + 1])
        if 65 <= liczba <= 90:
            haslo4 += chr(liczba)
            if haslo4.endswith("XXX"):
                break
    if haslo4.endswith("XXX"):
        break

with open("wyniki4.txt", "w") as wynik:
    print("4.1.", cyfry_razem, file=wynik)
    print("4.2.", haslo2, file=wynik)
    print("4.3.", haslo3, file=wynik)
    print("4.4.", haslo4, file=wynik)
```
```cpp
// C++23
#include <algorithm>
#include <cctype>
#include <fstream>
#include <string>
#include <vector>

bool palindrom(const std::string& s) {
    return std::equal(s.begin(), s.end(), s.rbegin());
}

int main() {
    std::vector<std::string> napisy;
    std::ifstream plik("napisy.txt");
    std::string linia;
    while (plik >> linia) napisy.push_back(linia);

    // 4.1
    int cyfry_razem = 0;
    for (auto& napis : napisy)
        for (char znak : napis)
            if (std::isdigit((unsigned char)znak)) cyfry_razem++;

    // 4.2 - w wierszu 20*j litera na pozycji j (numeracja od 1)
    std::string haslo2;
    for (int nr = 20; nr <= 1000; nr += 20) haslo2 += napisy[nr - 1][nr / 20 - 1];

    // 4.3 - dopisanie znaku na końcu: napis[1:] musi być palindromem, środek to napis[25];
    //       dopisanie na początku: napis[:-1] musi być palindromem, środek to napis[24]
    std::string haslo3;
    for (auto& napis : napisy) {
        if (palindrom(napis.substr(1)))
            haslo3 += napis[25];
        else if (palindrom(napis.substr(0, napis.size() - 1)))
            haslo3 += napis[24];
    }

    // 4.4 - cyfry z wiersza w parach, koniec po trzech kolejnych X (także z różnych wierszy)
    std::string haslo4;
    for (auto& napis : napisy) {
        std::string cyfry;
        for (char znak : napis)
            if (std::isdigit((unsigned char)znak)) cyfry += znak;
        for (size_t j = 0; j + 1 < cyfry.size(); j += 2) {
            int liczba = (cyfry[j] - '0') * 10 + (cyfry[j + 1] - '0');
            if (65 <= liczba && liczba <= 90) {
                haslo4 += (char)liczba;
                if (haslo4.ends_with("XXX")) break;
            }
        }
        if (haslo4.ends_with("XXX")) break;
    }

    std::ofstream wynik("wyniki4.txt");
    wynik << "4.1. " << cyfry_razem << "\n";
    wynik << "4.2. " << haslo2 << "\n";
    wynik << "4.3. " << haslo3 << "\n";
    wynik << "4.4. " << haslo4 << "\n";
}
```
```java
// Java 25
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    static boolean palindrom(String s) {
        return s.equals(new StringBuilder(s).reverse().toString());
    }

    public static void main(String[] args) throws Exception {
        var napisy = new ArrayList<String>();
        for (var linia : Files.readAllLines(Path.of("napisy.txt")))
            napisy.add(linia.strip());

        // 4.1
        int cyfryRazem = 0;
        for (var napis : napisy)
            for (char znak : napis.toCharArray())
                if (Character.isDigit(znak)) cyfryRazem++;

        // 4.2 - w wierszu 20*j litera na pozycji j (numeracja od 1)
        var haslo2 = new StringBuilder();
        for (int nr = 20; nr <= 1000; nr += 20) haslo2.append(napisy.get(nr - 1).charAt(nr / 20 - 1));

        // 4.3 - dopisanie znaku na końcu: napis[1:] musi być palindromem, środek to napis[25];
        //       dopisanie na początku: napis[:-1] musi być palindromem, środek to napis[24]
        var haslo3 = new StringBuilder();
        for (var napis : napisy) {
            if (palindrom(napis.substring(1)))
                haslo3.append(napis.charAt(25));
            else if (palindrom(napis.substring(0, napis.length() - 1)))
                haslo3.append(napis.charAt(24));
        }

        // 4.4 - cyfry z wiersza w parach, koniec po trzech kolejnych X (także z różnych wierszy)
        var haslo4 = new StringBuilder();
        for (var napis : napisy) {
            var cyfry = new StringBuilder();
            for (char znak : napis.toCharArray())
                if (Character.isDigit(znak)) cyfry.append(znak);
            for (int j = 0; j + 1 < cyfry.length(); j += 2) {
                int liczba = Integer.parseInt(cyfry.substring(j, j + 2));
                if (65 <= liczba && liczba <= 90) {
                    haslo4.append((char) liczba);
                    if (haslo4.toString().endsWith("XXX")) break;
                }
            }
            if (haslo4.toString().endsWith("XXX")) break;
        }

        try (var wynik = new PrintWriter("wyniki4.txt")) {
            wynik.println("4.1. " + cyfryRazem);
            wynik.println("4.2. " + haslo2);
            wynik.println("4.3. " + haslo3);
            wynik.println("4.4. " + haslo4);
        }
    }
}
```
**Odpowiedź:** 4.1: 11844; 4.2: SZYBKOROZWIAZUJEPROGRAMISTYCZNEZADANIAZINFORMATYKI; 4.3: ZADANIEMATURALNE; 4.4: LITWOOJCZYZNOMOJATYJESTESJAKZDROWIEILECIETRZEBACENIC…KRETYJAKWAZBOAXXX
