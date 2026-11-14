<h1 align="center">Matura 2026 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2026-czerwiec-matura-stara-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

> **Treść zadania:** Algorytm Szyfr szyfruje tekst jawny T[1..n] (n znaków) kluczem k (dodatnia liczba całkowita) i zapisuje szyfrogram w tablicy S[1..n]:
>
> ```
> a ← n div k
> c ← n − a
> dla i = 1, 2, ..., n wykonuj
>     jeżeli i mod k = 0
>         b ← i div k
>         S[n − a + b] ← T[i]
>     w przeciwnym razie
>         S[c] ← T[i]
>         c ← c − 1
> ```
>
> - 1.1 — Podaj szyfrogramy dla tekstów: `korporacja` z kluczem k = 6, `tropikalny` z k = 5 oraz `defragmentacja` z k = 3.
> - 1.2 — Podaj wartość klucza k, dla której szyfrogram jest zawsze identyczny z tekstem jawnym.
> - 1.3 — Podaj wartość klucza k, dla której (przy każdym n) szyfrogram jest zawsze tekstem jawnym zapisanym od końca (np. `serwer` → `rewres`); wartość może zależeć od n.

```py
def szyfr(T, k):
    n = len(T)
    S = [""] * (n + 1)              # indeksy 1..n
    a = n // k
    c = n - a
    for i in range(1, n + 1):
        if i % k == 0:
            b = i // k
            S[n - a + b] = T[i - 1]
        else:
            S[c] = T[i - 1]
            c = c - 1
    return "".join(S[1:])


# 1.1
for tekst, k in [("korporacja", 6), ("tropikalny", 5), ("defragmentacja", 3)]:
    print(tekst, k, szyfr(tekst, k))

# 1.2 i 1.3 - szyfrogramy słowa "serwer" (n = 6) dla różnych kluczy
for k in range(1, 9):
    print(k, szyfr("serwer", k))
```

```cpp
// C++23
#include <print>
#include <string>
#include <utility>
#include <vector>

std::string szyfr(const std::string& T, int k) {
    int n = T.size();
    std::string S(n + 1, ' ');      // indeksy 1..n
    int a = n / k;
    int c = n - a;
    for (int i = 1; i <= n; i++) {
        if (i % k == 0) {
            int b = i / k;
            S[n - a + b] = T[i - 1];
        } else {
            S[c] = T[i - 1];
            c = c - 1;
        }
    }
    return S.substr(1);
}

int main() {
    // 1.1
    std::vector<std::pair<std::string, int>> dane = {{"korporacja", 6}, {"tropikalny", 5}, {"defragmentacja", 3}};
    for (const auto& [tekst, k] : dane) {
        std::println("{} {} {}", tekst, k, szyfr(tekst, k));
    }

    // 1.2 i 1.3 - szyfrogramy słowa "serwer" (n = 6) dla różnych kluczy
    for (int k = 1; k < 9; k++) {
        std::println("{} {}", k, szyfr("serwer", k));
    }
}
```

```java
// Java 25
public class Zadanie {
    static String szyfr(String T, int k) {
        int n = T.length();
        char[] S = new char[n + 1];     // indeksy 1..n
        int a = n / k;
        int c = n - a;
        for (int i = 1; i <= n; i++) {
            if (i % k == 0) {
                int b = i / k;
                S[n - a + b] = T.charAt(i - 1);
            } else {
                S[c] = T.charAt(i - 1);
                c = c - 1;
            }
        }
        return new String(S, 1, n);
    }

    public static void main(String[] args) throws Exception {
        // 1.1
        String[] teksty = {"korporacja", "tropikalny", "defragmentacja"};
        int[] klucze = {6, 5, 3};
        for (int j = 0; j < teksty.length; j++) {
            System.out.println(teksty[j] + " " + klucze[j] + " " + szyfr(teksty[j], klucze[j]));
        }

        // 1.2 i 1.3 - szyfrogramy słowa "serwer" (n = 6) dla różnych kluczy
        for (int k = 1; k < 9; k++) {
            System.out.println(k + " " + szyfr("serwer", k));
        }
    }
}
```

**Odpowiedź:** 1.1: korporacja (k = 6) → ajcaoprokr; tropikalny (k = 5) → nlakportiy; defragmentacja (k = 3) → ajatemaredfgnc. 1.2: k = 1. 1.3: k = n + 1 (lub dowolne k > n).

## 2.1 i 2.2

> **Treść zadania:** Dana jest liczba n > 1 i tablica liczb całkowitych T[1..n]. Dla 1 ≤ k < n tablica T jest k-podobna, gdy T[1..k] = T[n − k + 1..n] (początkowe k elementów jest równe końcowym k elementom); ponadto każda tablica jest 0-podobna. Przykład: [1,2,1,1,2,1,1] jest 0-, 1- i 4-podobna; [1,2,2] jest tylko 0-podobna; [2,2,2] jest 0-, 1- i 2-podobna (ale nie 3-podobna, bo k < n).
>
> - 2.1 — Dla tablic [1,2,3,4], [1,3,4,1,1,3,4,1] oraz [3,5,3,5,3,5,3,5,3,5] podaj największe k, dla którego tablica jest k-podobna.
> - 2.2 — Zapisz (w pseudokodzie lub wybranym języku) algorytm, który dla n > 1 i tablicy T[1..n] wyznacza największe k, dla którego T jest k-podobna. Wolno używać tylko operatorów arytmetycznych i logicznych, porównań, odwołań do pojedynczych elementów tablicy, instrukcji sterujących i własnych funkcji — bez funkcji wbudowanych, w szczególności bez pobierania fragmentu tablicy (wycinków list).

```py
# 2.2
def najwieksze_k(T):
    n = len(T)
    k = n - 1
    while k > 0:
        jest = True
        for i in range(k):                  # porównujemy T[1..k] z T[n-k+1..n]
            if T[i] != T[n - k + i]:
                jest = False
        if jest:
            return k
        k -= 1
    return 0


# 2.1
for T in [[1, 2, 3, 4], [1, 3, 4, 1, 1, 3, 4, 1], [3, 5, 3, 5, 3, 5, 3, 5, 3, 5]]:
    print(T, najwieksze_k(T))
```

```cpp
// C++23
#include <print>
#include <vector>

// 2.2
int najwieksze_k(const std::vector<int>& T) {
    int n = T.size();
    int k = n - 1;
    while (k > 0) {
        bool jest = true;
        for (int i = 0; i < k; i++) {       // porównujemy T[1..k] z T[n-k+1..n]
            if (T[i] != T[n - k + i]) {
                jest = false;
            }
        }
        if (jest) {
            return k;
        }
        k -= 1;
    }
    return 0;
}

int main() {
    // 2.1 (wektor wypisuje się jak lista w Pythonie)
    std::vector<std::vector<int>> tablice = {{1, 2, 3, 4}, {1, 3, 4, 1, 1, 3, 4, 1}, {3, 5, 3, 5, 3, 5, 3, 5, 3, 5}};
    for (const auto& T : tablice) {
        std::println("{} {}", T, najwieksze_k(T));
    }
}
```

```java
// Java 25
import java.util.List;

public class Zadanie {
    // 2.2
    static int najwiekszeK(List<Integer> T) {
        int n = T.size();
        int k = n - 1;
        while (k > 0) {
            boolean jest = true;
            for (int i = 0; i < k; i++) {       // porównujemy T[1..k] z T[n-k+1..n]
                if (!T.get(i).equals(T.get(n - k + i))) {
                    jest = false;
                }
            }
            if (jest) {
                return k;
            }
            k -= 1;
        }
        return 0;
    }

    public static void main(String[] args) throws Exception {
        // 2.1 (lista wypisuje się jak w Pythonie)
        List<List<Integer>> tablice = List.of(List.of(1, 2, 3, 4), List.of(1, 3, 4, 1, 1, 3, 4, 1),
                List.of(3, 5, 3, 5, 3, 5, 3, 5, 3, 5));
        for (List<Integer> T : tablice) {
            System.out.println(T + " " + najwiekszeK(T));
        }
    }
}
```

**Odpowiedź:** 2.1: 0, 4, 8. 2.2: funkcja `najwieksze_k`.

## 4.1, 4.2, 4.3 i 4.4

> **Treść zadania:** Np-para to dwa kolejne znaki napisu, z których pierwszy stoi na pozycji nieparzystej, a drugi na parzystej (pozycje od 1): napis dzielimy na pary znaków 1–2, 3–4, 5–6… (np. w `MATURA` np-pary to MA, TU, RA). Plik `dane.txt` zawiera jeden napis parzystej długości złożony z wielkich liter alfabetu angielskiego. Odpowiedzi zapisz w pliku `wyniki4.txt`, poprzedzając każdą numerem zadania. Plik `dane_przyklad.txt` służy do testów. Para lub fragment złożony z całych np-par jest parzyście pierwszy, jeśli suma kodów ASCII jego znaków jest liczbą pierwszą (np. WIRY: 87 + 73 + 82 + 89 = 331).
>
> - 4.1 — Podaj, ile razy dwie bezpośrednio po sobie następujące np-pary są takie same (dla `CABABC` — 0, dla `ABABAB` — 2).
> - 4.2 — Wypisz wszystkie różne parzyście pierwsze np-pary z pliku (dla pliku przykładowego: `FO IN AT`).
> - 4.3 — Znajdź najdłuższy parzyście pierwszy fragment złożony z np-par i podaj go wraz z sumą kodów ASCII jego znaków (np. w `NEWSROOM` jest to WSROOM, suma 487; dla pliku przykładowego: `FORMYKINRMRMATYKYKATYKATFO 2029`).
> - 4.4 — Dla każdej różnej np-pary policz liczbę jej wystąpień, ustaw np-pary rosnąco według tej liczby (liczby wystąpień są różne, każdą parę zapisujemy raz) i podaj powstały napis oraz największą i najmniejszą liczbę wystąpień (np. `RAPARA` → `PARA`; dla pliku przykładowego: `INFORMATYK 5 1`).

```py
with open("dane.txt") as file:
    napis = file.read().strip()

pary = [napis[i:i + 2] for i in range(0, len(napis), 2)]      # kolejne np-pary
wynik = open("wyniki4.txt", "w")


def pierwsza(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def suma_kodow(tekst):
    return sum(ord(c) for c in tekst)


# 4.1
ile = 0
for i in range(1, len(pary)):
    if pary[i] == pary[i - 1]:
        ile += 1
print("4.1", ile, file=wynik)

# 4.2
wypisane = []
for para in pary:
    if pierwsza(suma_kodow(para)) and para not in wypisane:
        wypisane.append(para)
print("4.2", *wypisane, file=wynik)

# 4.3 - sprawdzamy wszystkie fragmenty pary[p..q]
najlepszy = ""
for p in range(len(pary)):
    suma = 0
    for q in range(p, len(pary)):
        suma += suma_kodow(pary[q])
        if pierwsza(suma) and 2 * (q - p + 1) > len(najlepszy):
            najlepszy = "".join(pary[p:q + 1])
print("4.3", najlepszy, suma_kodow(najlepszy), file=wynik)

# 4.4
licznik = {}
for para in pary:
    licznik[para] = licznik.get(para, 0) + 1
kolejnosc = sorted(licznik, key=lambda para: licznik[para])
print("4.4", "".join(kolejnosc), licznik[kolejnosc[-1]], licznik[kolejnosc[0]], file=wynik)

wynik.close()
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <string>
#include <utility>
#include <vector>

bool pierwsza(int x) {
    if (x < 2) {
        return false;
    }
    int d = 2;
    while (d * d <= x) {
        if (x % d == 0) {
            return false;
        }
        d += 1;
    }
    return true;
}

int suma_kodow(const std::string& tekst) {
    int suma = 0;
    for (char c : tekst) {
        suma += c;  // kod ASCII znaku
    }
    return suma;
}

int main() {
    std::ifstream plik("dane.txt");
    std::string napis;
    plik >> napis;  // wczytanie słowa pomija białe znaki - jak strip()

    std::vector<std::string> pary;      // kolejne np-pary
    for (size_t i = 0; i < napis.size(); i += 2) {
        pary.push_back(napis.substr(i, 2));
    }
    std::ofstream wynik("wyniki4.txt");

    // 4.1
    int ile = 0;
    for (size_t i = 1; i < pary.size(); i++) {
        if (pary[i] == pary[i - 1]) {
            ile += 1;
        }
    }
    std::println(wynik, "4.1 {}", ile);

    // 4.2
    std::vector<std::string> wypisane;
    for (const std::string& para : pary) {
        if (pierwsza(suma_kodow(para)) && std::ranges::find(wypisane, para) == wypisane.end()) {
            wypisane.push_back(para);
        }
    }
    std::print(wynik, "4.2");
    for (const std::string& para : wypisane) {
        std::print(wynik, " {}", para);
    }
    std::println(wynik);

    // 4.3 - sprawdzamy wszystkie fragmenty pary[p..q]
    std::string najlepszy = "";
    for (size_t p = 0; p < pary.size(); p++) {
        int suma = 0;
        for (size_t q = p; q < pary.size(); q++) {
            suma += suma_kodow(pary[q]);
            if (pierwsza(suma) && 2 * (q - p + 1) > najlepszy.size()) {
                najlepszy = napis.substr(2 * p, 2 * (q - p + 1));  // sklejone pary[p..q]
            }
        }
    }
    std::println(wynik, "4.3 {} {}", najlepszy, suma_kodow(najlepszy));

    // 4.4 - pary w kolejności pierwszego wystąpienia (jak klucze słownika w Pythonie)
    std::vector<std::pair<std::string, int>> licznik;
    for (const std::string& para : pary) {
        auto it = std::ranges::find(licznik, para, &std::pair<std::string, int>::first);
        if (it == licznik.end()) {
            licznik.push_back({para, 1});
        } else {
            it->second += 1;
        }
    }
    // sortowanie stabilne - przy remisie zostaje kolejność pierwszego wystąpienia
    std::ranges::stable_sort(licznik, {}, &std::pair<std::string, int>::second);
    std::string kolejnosc = "";
    for (const auto& [para, liczba] : licznik) {
        kolejnosc += para;
    }
    std::println(wynik, "4.4 {} {} {}", kolejnosc, licznik.back().second, licznik.front().second);
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Zadanie {
    static boolean pierwsza(int x) {
        if (x < 2) {
            return false;
        }
        int d = 2;
        while (d * d <= x) {
            if (x % d == 0) {
                return false;
            }
            d += 1;
        }
        return true;
    }

    static int sumaKodow(String tekst) {
        int suma = 0;
        for (char c : tekst.toCharArray()) {
            suma += c;  // kod ASCII znaku
        }
        return suma;
    }

    public static void main(String[] args) throws Exception {
        String napis = Files.readString(Path.of("dane.txt")).strip();

        List<String> pary = new ArrayList<>();      // kolejne np-pary
        for (int i = 0; i < napis.length(); i += 2) {
            pary.add(napis.substring(i, Math.min(i + 2, napis.length())));
        }
        PrintWriter wynik = new PrintWriter("wyniki4.txt");

        // 4.1
        int ile = 0;
        for (int i = 1; i < pary.size(); i++) {
            if (pary.get(i).equals(pary.get(i - 1))) {
                ile += 1;
            }
        }
        wynik.println("4.1 " + ile);

        // 4.2
        List<String> wypisane = new ArrayList<>();
        for (String para : pary) {
            if (pierwsza(sumaKodow(para)) && !wypisane.contains(para)) {
                wypisane.add(para);
            }
        }
        wynik.println("4.2 " + String.join(" ", wypisane));

        // 4.3 - sprawdzamy wszystkie fragmenty pary[p..q]
        String najlepszy = "";
        for (int p = 0; p < pary.size(); p++) {
            int suma = 0;
            for (int q = p; q < pary.size(); q++) {
                suma += sumaKodow(pary.get(q));
                if (pierwsza(suma) && 2 * (q - p + 1) > najlepszy.length()) {
                    najlepszy = String.join("", pary.subList(p, q + 1));
                }
            }
        }
        wynik.println("4.3 " + najlepszy + " " + sumaKodow(najlepszy));

        // 4.4 - LinkedHashMap pamięta kolejność dodawania (jak słownik w Pythonie)
        Map<String, Integer> licznik = new LinkedHashMap<>();
        for (String para : pary) {
            licznik.put(para, licznik.getOrDefault(para, 0) + 1);
        }
        // List.sort jest stabilne - przy remisie zostaje kolejność pierwszego wystąpienia
        List<String> kolejnosc = new ArrayList<>(licznik.keySet());
        kolejnosc.sort((p1, p2) -> Integer.compare(licznik.get(p1), licznik.get(p2)));
        wynik.println("4.4 " + String.join("", kolejnosc) + " " + licznik.get(kolejnosc.get(kolejnosc.size() - 1))
                + " " + licznik.get(kolejnosc.get(0)));

        wynik.close();
    }
}
```

**Odpowiedź:** 4.1: 17. 4.2: IN IL NY UR. 4.3: fragment INRZWZASEKYPYPYIEKDLEKODASINWNWNUP… (272 np-pary, kończy się …JNRAINYIRAWZODNY), suma kodów 42923. 4.4: BYLTOZIELONYUPRAWNYIURODZAJNYPASWZDLUZRZEKINIL, najwięcej wystąpień 23, najmniej 1.
