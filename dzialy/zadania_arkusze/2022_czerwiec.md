<h1 align="center">Matura 2022 — czerwiec (termin dodatkowy), poziom rozszerzony (formuła 2015)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2022-czerwiec-matura-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2022-czerwiec-matura-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2022-czerwiec-matura-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2022-czerwiec-matura-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.3

> **Treść zadania:** Dodatniej liczbie całkowitej przyporządkowujemy sumę kwadratów jej cyfr (np. 123 → 1²+2²+3² = 14). Tworzymy ciąg zaczynający się od n, w którym każdy kolejny wyraz to wynik tej operacji na poprzednim. Jeśli w ciągu pojawi się 1, liczba n jest **nudna**, w przeciwnym razie — **ciekawa** (np. 13 → 10 → 1, więc 13 jest nudna; 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 …, więc 4 jest ciekawa).
>
> - **1.1** — Dla liczb z tabeli arkusza wpisz TAK, jeśli liczba jest nudna, albo NIE.
> - **1.2** — Napisz funkcję `SumaKwCyfr(n)` obliczającą sumę kwadratów cyfr dodatniej liczby n (bez funkcji wbudowanych).
> - **1.3** — Napisz algorytm, który dla dodatniej n < 1000 zwraca Prawda, gdy n jest nudna, i Fałsz, gdy ciekawa. Można użyć `SumaKwCyfr` i faktu, że suma kwadratów cyfr liczby co najwyżej trzycyfrowej nie przekracza 243.

```py
def suma_kw_cyfr(n):
    suma = 0
    while n > 0:
        cyfra = n % 10
        suma += cyfra * cyfra
        n //= 10
    return suma


def czy_nudna(n):
    # n < 1000, więc po pierwszym kroku wszystkie wyrazy ciągu są <= 243
    # zapamiętujemy, które liczby już wystąpiły - powtórzenie oznacza cykl bez 1
    byla = [False] * 1000
    while n != 1:
        if byla[n]:
            return False
        byla[n] = True
        n = suma_kw_cyfr(n)
    return True


# 1.1
for n in [4, 229, 82]:
    print(n, "TAK" if czy_nudna(n) else "NIE")

# 1.2
print(suma_kw_cyfr(123))
```
```cpp
// C++23
#include <print>
#include <vector>

int suma_kw_cyfr(int n) {
    int suma = 0;
    while (n > 0) {
        int cyfra = n % 10;
        suma += cyfra * cyfra;
        n /= 10;
    }
    return suma;
}

bool czy_nudna(int n) {
    // n < 1000, więc po pierwszym kroku wszystkie wyrazy ciągu są <= 243
    // zapamiętujemy, które liczby już wystąpiły - powtórzenie oznacza cykl bez 1
    std::vector<bool> byla(1000, false);
    while (n != 1) {
        if (byla[n]) return false;
        byla[n] = true;
        n = suma_kw_cyfr(n);
    }
    return true;
}

int main() {
    // 1.1
    for (int n : {4, 229, 82}) std::println("{} {}", n, czy_nudna(n) ? "TAK" : "NIE");

    // 1.2
    std::println("{}", suma_kw_cyfr(123));
}
```
```java
// Java 25
public class Zadanie {
    static int sumaKwCyfr(int n) {
        int suma = 0;
        while (n > 0) {
            int cyfra = n % 10;
            suma += cyfra * cyfra;
            n /= 10;
        }
        return suma;
    }

    static boolean czyNudna(int n) {
        // n < 1000, więc po pierwszym kroku wszystkie wyrazy ciągu są <= 243
        // zapamiętujemy, które liczby już wystąpiły - powtórzenie oznacza cykl bez 1
        boolean[] byla = new boolean[1000];
        while (n != 1) {
            if (byla[n]) return false;
            byla[n] = true;
            n = sumaKwCyfr(n);
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        // 1.1
        for (int n : new int[] {4, 229, 82}) System.out.println(n + " " + (czyNudna(n) ? "TAK" : "NIE"));

        // 1.2
        System.out.println(sumaKwCyfr(123));
    }
}
```

**Odpowiedź:** 1.1: 229 – NIE, 82 – TAK. 1.2: funkcja `suma_kw_cyfr`. 1.3: funkcja `czy_nudna` – liczymy kolejne sumy kwadratów cyfr aż do 1 (nudna) albo do powtórzenia wartości (ciekawa).

## 2.1, 2.2 i 2.3

> **Treść zadania:** Funkcja Koduj(n) dla dodatniej liczby n zwraca słowo (puste lub złożone z liter A i B):
>
> ```
> Koduj(n):
>     jeżeli n = 1: wynikiem jest ''
>     w przeciwnym wypadku:
>         k ← n div 2
>         jeżeli k mod 2 = 0: wynikiem jest Koduj(k) + 'A'
>         w przeciwnym wypadku: wynikiem jest 'B' + Koduj(k)
> ```
>
> - **2.1** — Podaj wynik Koduj(n) dla wartości n z tabeli arkusza (np. Koduj(1) = '', Koduj(2) = 'B').
> - **2.2** — Podaj łączną liczbę wywołań funkcji Koduj przy wywołaniu Koduj(12), Koduj(33) i Koduj(1022) (np. dla Koduj(2) — 2).
> - **2.3** — Podaj dwie różne dodatnie liczby, dla których Koduj zwraca ten sam sześcioznakowy kod.

```py
wywolania = 0


def koduj(n):
    global wywolania
    wywolania += 1
    if n == 1:
        return ""
    k = n // 2
    if k % 2 == 0:
        return koduj(k) + "A"
    else:
        return "B" + koduj(k)


# 2.1 i 2.2
for n in [1, 2, 12, 33, 158, 1022]:
    wywolania = 0
    kod = koduj(n)
    print(n, repr(kod), wywolania)

# 2.3 - kod ma 6 znaków dla liczb 7-bitowych (64..127); szukamy dwóch o tym samym kodzie
kody = {}
for n in range(64, 128):
    kody.setdefault(koduj(n), []).append(n)
for kod, lista in kody.items():
    if len(lista) > 1:
        print(kod, lista)
        break
```
```cpp
// C++23
#include <map>
#include <print>
#include <string>
#include <vector>

int wywolania = 0;

std::string koduj(int n) {
    wywolania++;
    if (n == 1) return "";
    int k = n / 2;
    if (k % 2 == 0)
        return koduj(k) + "A";
    else
        return "B" + koduj(k);
}

int main() {
    // 2.1 i 2.2
    for (int n : {1, 2, 12, 33, 158, 1022}) {
        wywolania = 0;
        std::string kod = koduj(n);
        std::println("{} '{}' {}", n, kod, wywolania);
    }

    // 2.3 - kod ma 6 znaków dla liczb 7-bitowych (64..127); szukamy dwóch o tym samym kodzie
    std::map<std::string, std::vector<int>> kody;
    std::vector<std::string> kolejnosc;  // kody w kolejności pojawienia się
    for (int n = 64; n < 128; n++) {
        std::string kod = koduj(n);
        if (!kody.contains(kod)) kolejnosc.push_back(kod);
        kody[kod].push_back(n);
    }
    for (auto& kod : kolejnosc) {
        if (kody[kod].size() > 1) {
            std::println("{} {}", kod, kody[kod]);
            break;
        }
    }
}
```
```java
// Java 25
import java.util.*;

public class Zadanie {
    static int wywolania = 0;

    static String koduj(int n) {
        wywolania++;
        if (n == 1) return "";
        int k = n / 2;
        if (k % 2 == 0)
            return koduj(k) + "A";
        else
            return "B" + koduj(k);
    }

    public static void main(String[] args) throws Exception {
        // 2.1 i 2.2
        for (int n : new int[] {1, 2, 12, 33, 158, 1022}) {
            wywolania = 0;
            String kod = koduj(n);
            System.out.println(n + " '" + kod + "' " + wywolania);
        }

        // 2.3 - kod ma 6 znaków dla liczb 7-bitowych (64..127); szukamy dwóch o tym samym kodzie
        var kody = new LinkedHashMap<String, List<Integer>>();
        for (int n = 64; n < 128; n++)
            kody.computeIfAbsent(koduj(n), k -> new ArrayList<>()).add(n);
        for (var e : kody.entrySet()) {
            if (e.getValue().size() > 1) {
                System.out.println(e.getKey() + " " + e.getValue());
                break;
            }
        }
    }
}
```

**Odpowiedź:** 2.1: 12 → BBA, 33 → BAAAA, 158 → BBBBBAA. 2.2: 12 → 4, 33 → 6, 1022 → 10. 2.3: np. 64 i 65 (kod BAAAAA) – liczby 7-cyfrowe binarnie, różniące się tylko ostatnim bitem (klucz podaje np. 66 i 67 albo 94 i 111).

## 4.1, 4.2, 4.3 i 4.4

> **Treść zadania:** Plik `liczby.txt` zawiera 100 nieparzystych liczb całkowitych z przedziału [10, 9999] (mogą się powtarzać). Odbiciem liczby nazywamy liczbę o odwróconej kolejności cyfr (np. 2019 → 9102). Odpowiedzi zapisz w `wyniki4.txt`, poprzedzając je numerem zadania; plik `przyklad.txt` (11 liczb) służy do testów.
>
> - **4.1** — Wypisz te odbicia liczb z pliku, które są podzielne przez 17. (Przykład: 51.)
> - **4.2** — Znajdź liczbę, dla której wartość bezwzględna różnicy liczby i jej odbicia jest największa (jest jedna); podaj ją i tę różnicę. (Przykład: 741 594.)
> - **4.3** — Wypisz, każdą w osobnym wierszu, liczby pierwsze z pliku, których odbicia też są pierwsze (np. 13 i 31, 131).
> - **4.4** — Podaj, ile różnych liczb jest w pliku, ile liczb występuje dokładnie dwa razy i ile dokładnie trzy razy. (Przykład: 10 1 0.)

```py
liczby = []
with open("liczby.txt") as file:
    for line in file:
        liczby.append(int(line))


def odbicie(n):
    return int(str(n)[::-1])


def czy_pierwsza(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


# 4.1
print("4.1")
for n in liczby:
    if odbicie(n) % 17 == 0:
        print(odbicie(n))

# 4.2
najwieksza_roznica = -1
najlepsza = 0
for n in liczby:
    roznica = abs(n - odbicie(n))
    if roznica > najwieksza_roznica:
        najwieksza_roznica = roznica
        najlepsza = n
print("4.2", najlepsza, najwieksza_roznica)

# 4.3
print("4.3")
for n in liczby:
    if czy_pierwsza(n) and czy_pierwsza(odbicie(n)):
        print(n)

# 4.4
ile_razy = {}
for n in liczby:
    ile_razy[n] = ile_razy.get(n, 0) + 1
dwa = 0
trzy = 0
for n in ile_razy:
    if ile_razy[n] == 2:
        dwa += 1
    if ile_razy[n] == 3:
        trzy += 1
print("4.4", len(ile_razy), dwa, trzy)
```
```cpp
// C++23
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <map>
#include <print>
#include <string>
#include <vector>

long long odbicie(long long n) {
    std::string s = std::to_string(n);
    std::reverse(s.begin(), s.end());
    return std::stoll(s);
}

bool czy_pierwsza(long long n) {
    if (n < 2) return false;
    for (long long d = 2; d * d <= n; d++)
        if (n % d == 0) return false;
    return true;
}

int main() {
    std::vector<long long> liczby;
    std::ifstream plik("liczby.txt");
    long long x;
    while (plik >> x) liczby.push_back(x);

    // 4.1
    std::println("4.1");
    for (long long n : liczby)
        if (odbicie(n) % 17 == 0) std::println("{}", odbicie(n));

    // 4.2
    long long najwieksza_roznica = -1;
    long long najlepsza = 0;
    for (long long n : liczby) {
        long long roznica = std::llabs(n - odbicie(n));
        if (roznica > najwieksza_roznica) {
            najwieksza_roznica = roznica;
            najlepsza = n;
        }
    }
    std::println("4.2 {} {}", najlepsza, najwieksza_roznica);

    // 4.3
    std::println("4.3");
    for (long long n : liczby)
        if (czy_pierwsza(n) && czy_pierwsza(odbicie(n))) std::println("{}", n);

    // 4.4
    std::map<long long, int> ile_razy;
    for (long long n : liczby) ile_razy[n]++;
    int dwa = 0;
    int trzy = 0;
    for (auto& [n, ile] : ile_razy) {
        if (ile == 2) dwa++;
        if (ile == 3) trzy++;
    }
    std::println("4.4 {} {} {}", ile_razy.size(), dwa, trzy);
}
```
```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    static long odbicie(long n) {
        return Long.parseLong(new StringBuilder(Long.toString(n)).reverse().toString());
    }

    static boolean czyPierwsza(long n) {
        if (n < 2) return false;
        for (long d = 2; d * d <= n; d++)
            if (n % d == 0) return false;
        return true;
    }

    public static void main(String[] args) throws Exception {
        var liczby = new ArrayList<Long>();
        for (var linia : Files.readAllLines(Path.of("liczby.txt")))
            if (!linia.isBlank()) liczby.add(Long.parseLong(linia.trim()));

        // 4.1
        System.out.println("4.1");
        for (long n : liczby)
            if (odbicie(n) % 17 == 0) System.out.println(odbicie(n));

        // 4.2
        long najwiekszaRoznica = -1;
        long najlepsza = 0;
        for (long n : liczby) {
            long roznica = Math.abs(n - odbicie(n));
            if (roznica > najwiekszaRoznica) {
                najwiekszaRoznica = roznica;
                najlepsza = n;
            }
        }
        System.out.println("4.2 " + najlepsza + " " + najwiekszaRoznica);

        // 4.3
        System.out.println("4.3");
        for (long n : liczby)
            if (czyPierwsza(n) && czyPierwsza(odbicie(n))) System.out.println(n);

        // 4.4
        var ileRazy = new HashMap<Long, Integer>();
        for (long n : liczby) ileRazy.merge(n, 1, Integer::sum);
        int dwa = 0;
        int trzy = 0;
        for (int ile : ileRazy.values()) {
            if (ile == 2) dwa++;
            if (ile == 3) trzy++;
        }
        System.out.println("4.4 " + ileRazy.size() + " " + dwa + " " + trzy);
    }
}
```

**Odpowiedź:** 4.1: 1156, 102, 51, 765, 119, 119, 731; 4.2: 1129 8082; 4.3: 157, 31, 347, 929, 941, 761; 4.4: 85 13 1
