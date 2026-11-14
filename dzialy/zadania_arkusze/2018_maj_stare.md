<h1 align="center">Matura 2018 — maj, poziom rozszerzony (stara formuła)</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2018-maj-matura-stara-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2018-maj-matura-stara-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2018-maj-matura-stara-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2018-maj-matura-stara-rozszerzona-odpowiedzi.pdf)

## 1.1, 1.2 i 1.4

> **Treść zadania:** Zadanie 1 (humor liczb). Algorytm sprawdza, czy liczba całkowita dodatnia `n` jest „wesoła”, czy „smutna”: wielokrotnie zastępuje liczbę sumą kwadratów jej cyfr, zapisując kolejne wartości w tablicy `T`.
>
> ```
> T[0] ← n
> i ← 0
> powtarzaj:
>     k ← T[i]
>     suma ← 0
>     dopóki k > 0 wykonuj                 (*)
>         suma ← suma + (k mod 10)*(k mod 10)
>         k ← k div 10
>     jeżeli suma = 1
>         wypisz "liczba wesoła" i zakończ
>     dla j = 0, ..., i
>         jeżeli T[j] = suma
>             wypisz "liczba smutna" i zakończ
>     i ← i + 1
>     T[i] ← suma
> ```
>
> - 1.1 — podaj, ile razy spełniony jest warunek `k > 0` w wierszu (*) dla początkowych wartości `k` = 15, 5005 oraz dla dowolnej liczby całkowitej `x > 0`.
> - 1.2 — dla `n` = 7 i `n` = 145 podaj zawartość tablicy `T` i wynik działania algorytmu.
> - 1.4 — uzupełnij brakujące trzy cyfry w liczbie `9 4 _ _ _` tak, aby powstała pięciocyfrowa liczba wesoła, i podaj zawartość tablicy `T` dla tej liczby.

```py
def humor(n):
    # zwraca: liczbę wykonań pętli (*) dla k = n, tablicę T i wynik algorytmu
    T = [n]
    i = 0
    while True:
        k = T[i]
        suma = 0
        while k > 0:
            suma = suma + (k % 10) * (k % 10)
            k = k // 10
        if suma == 1:
            return T, "liczba wesoła"
        for j in range(i + 1):
            if T[j] == suma:
                return T, "liczba smutna"
        i = i + 1
        T.append(suma)


def ile_obrotow(k):
    # ile razy warunek k > 0 w wierszu (*) daje prawdę = liczba cyfr k
    ile = 0
    while k > 0:
        ile += 1
        k = k // 10
    return ile


# 1.1
print(ile_obrotow(15), ile_obrotow(5005))

# 1.2
print(humor(7))
print(humor(145))

# 1.4 - szukamy cyfr a, b, c, dla których liczba 94abc jest wesoła
for n in range(94000, 95000):
    T, wynik = humor(n)
    if wynik == "liczba wesoła":
        print(n, T)
        break

print(humor(94111))   # inny przykład: 81 + 16 + 1 + 1 + 1 = 100, a 1 + 0 + 0 = 1
```

```cpp
// C++23
#include <print>
#include <string>
#include <utility>
#include <vector>

// zwraca: tablicę T i wynik algorytmu
std::pair<std::vector<long long>, std::string> humor(long long n) {
    std::vector<long long> T = {n};
    int i = 0;
    while (true) {
        long long k = T[i];
        long long suma = 0;
        while (k > 0) {
            suma = suma + (k % 10) * (k % 10);
            k = k / 10;
        }
        if (suma == 1)
            return {T, "liczba wesoła"};
        for (int j = 0; j <= i; j++)
            if (T[j] == suma)
                return {T, "liczba smutna"};
        i = i + 1;
        T.push_back(suma);
    }
}

int ile_obrotow(long long k) {
    // ile razy warunek k > 0 w wierszu (*) daje prawdę = liczba cyfr k
    int ile = 0;
    while (k > 0) {
        ile++;
        k = k / 10;
    }
    return ile;
}

// wypisuje wynik humor(n) w postaci ([...], 'napis')
void wypisz(const std::pair<std::vector<long long>, std::string>& w) {
    std::println("({}, '{}')", w.first, w.second);
}

int main() {
    // 1.1
    std::println("{} {}", ile_obrotow(15), ile_obrotow(5005));

    // 1.2
    wypisz(humor(7));
    wypisz(humor(145));

    // 1.4 - szukamy cyfr a, b, c, dla których liczba 94abc jest wesoła
    for (long long n = 94000; n < 95000; n++) {
        auto [T, wynik] = humor(n);
        if (wynik == "liczba wesoła") {
            std::println("{} {}", n, T);
            break;
        }
    }

    wypisz(humor(94111));  // inny przykład: 81 + 16 + 1 + 1 + 1 = 100, a 1 + 0 + 0 = 1
}
```

```java
// Java 25
import java.util.ArrayList;
import java.util.List;

public class Zadanie {
    // wynik algorytmu: tablica T i napis
    record Wynik(List<Long> T, String opis) {
        @Override
        public String toString() {
            return "(" + T + ", '" + opis + "')";
        }
    }

    static Wynik humor(long n) {
        var T = new ArrayList<Long>();
        T.add(n);
        int i = 0;
        while (true) {
            long k = T.get(i);
            long suma = 0;
            while (k > 0) {
                suma = suma + (k % 10) * (k % 10);
                k = k / 10;
            }
            if (suma == 1)
                return new Wynik(T, "liczba wesoła");
            for (int j = 0; j <= i; j++)
                if (T.get(j) == suma)
                    return new Wynik(T, "liczba smutna");
            i = i + 1;
            T.add(suma);
        }
    }

    static int ileObrotow(long k) {
        // ile razy warunek k > 0 w wierszu (*) daje prawdę = liczba cyfr k
        int ile = 0;
        while (k > 0) {
            ile++;
            k = k / 10;
        }
        return ile;
    }

    public static void main(String[] args) throws Exception {
        // 1.1
        System.out.println(ileObrotow(15) + " " + ileObrotow(5005));

        // 1.2
        System.out.println(humor(7));
        System.out.println(humor(145));

        // 1.4 - szukamy cyfr a, b, c, dla których liczba 94abc jest wesoła
        for (long n = 94000; n < 95000; n++) {
            Wynik w = humor(n);
            if (w.opis().equals("liczba wesoła")) {
                System.out.println(n + " " + w.T());
                break;
            }
        }

        System.out.println(humor(94111));  // inny przykład: 81 + 16 + 1 + 1 + 1 = 100, a 1 + 0 + 0 = 1
    }
}
```

**Odpowiedź:** 1.1: 15 → 2, 5005 → 4, x → liczba cyfr x, czyli ⌊log₁₀ x⌋ + 1. 1.2: n = 7: T = 7, 49, 97, 130, 10 – liczba wesoła; n = 145: T = 145, 42, 20, 4, 16, 37, 58, 89 – liczba smutna. 1.4: np. 94000 (T = [94000, 97, 130, 10]) albo 94111 (T = [94111, 100]).

> W kluczu przy 1.4 podano „94111, T=[100]” – według algorytmu T[0] = n, więc pełna zawartość tablicy to [94111, 100].

## 2.1 i 2.2

> **Treść zadania:** Zadanie 2 (liczba automorficzna). Liczba całkowita dodatnia `n` jest automorficzna, jeśli `n = n² mod 10^k`, gdzie `k` to liczba cyfr `n` w zapisie dziesiętnym (czyli kwadrat liczby kończy się nią samą).
>
> - 2.1 — oceń, które z liczb 5, 6, 11, 25, 36, 76 są automorficzne (dla 5 odpowiedź TAK jest podana).
> - 2.2 — napisz algorytm, który dla danej liczby `n` odpowie „Tak”, jeśli jest automorficzna, lub „Nie” w przeciwnym razie. Wolno używać tylko dodawania, odejmowania, mnożenia, dzielenia całkowitego i reszty z dzielenia.

```py
def czy_automorficzna(n):
    potega = 10                 # najmniejsza potęga 10 większa od n, czyli 10^k
    while potega <= n:
        potega = potega * 10
    return n * n % potega == n


# 2.1
for n in [5, 6, 11, 25, 36, 76]:
    print(n, "TAK" if czy_automorficzna(n) else "NIE")

# 2.2
n = int(input())
if czy_automorficzna(n):
    print("Tak")
else:
    print("Nie")
```

```cpp
// C++23
#include <iostream>
#include <print>

bool czy_automorficzna(long long n) {
    long long potega = 10;  // najmniejsza potęga 10 większa od n, czyli 10^k
    while (potega <= n)
        potega = potega * 10;
    return n * n % potega == n;
}

int main() {
    // 2.1
    for (int n : {5, 6, 11, 25, 36, 76})
        std::println("{} {}", n, czy_automorficzna(n) ? "TAK" : "NIE");

    // 2.2
    long long n;
    std::cin >> n;
    if (czy_automorficzna(n))
        std::println("Tak");
    else
        std::println("Nie");
}
```

```java
// Java 25
import java.util.Scanner;

public class Zadanie {
    static boolean czyAutomorficzna(long n) {
        long potega = 10;  // najmniejsza potęga 10 większa od n, czyli 10^k
        while (potega <= n)
            potega = potega * 10;
        return n * n % potega == n;
    }

    public static void main(String[] args) throws Exception {
        // 2.1
        for (int n : new int[]{5, 6, 11, 25, 36, 76})
            System.out.println(n + " " + (czyAutomorficzna(n) ? "TAK" : "NIE"));

        // 2.2
        var sc = new Scanner(System.in);
        long n = sc.nextLong();
        if (czyAutomorficzna(n))
            System.out.println("Tak");
        else
            System.out.println("Nie");
    }
}
```

**Odpowiedź:** 2.1: 6 – TAK, 11 – NIE, 25 – TAK, 36 – NIE, 76 – TAK. 2.2: funkcja `czy_automorficzna` (10^k liczymy jako najmniejszą potęgę 10 większą od n).

## 6.1, 6.2 i 6.3

> **Treść zadania:** Zadanie 6 (słowa). Plik `slowa.txt` zawiera 1000 wierszy; w każdym dwa niepuste słowa z wielkich liter alfabetu angielskiego, oddzielone spacją (np. `ACUO KORNL`). Odpowiedzi zapisz w pliku `wyniki6.txt`, poprzedzając je numerem zadania.
>
> - 6.1 — podaj, ile słów w pliku (licząc oba słowa w wierszu) kończy się literą `A`.
> - 6.2 — podaj liczbę wierszy, w których pierwsze słowo zawiera się (jako spójny fragment) w drugim. Np. `ADC` zawiera się w `ASWADCF` i w `ADC`, ale nie w `ASWADFC`.
> - 6.3 — anagram to słowo powstałe z przestawienia wszystkich liter danego słowa (np. `MASLO` dla `SLOMA`). Podaj liczbę wierszy, w których pierwsze słowo jest anagramem drugiego, i wypisz te pary.

```py
pary = []
with open("slowa.txt") as file:
    for line in file:
        pary.append(line.split())

# 6.1
ile = 0
for slowo1, slowo2 in pary:
    if slowo1[-1] == "A":
        ile += 1
    if slowo2[-1] == "A":
        ile += 1
print("6.1", ile)

# 6.2
ile = 0
for slowo1, slowo2 in pary:
    if slowo1 in slowo2:
        ile += 1
print("6.2", ile)

# 6.3
anagramy = []
for slowo1, slowo2 in pary:
    if sorted(slowo1) == sorted(slowo2):
        anagramy.append((slowo1, slowo2))
print("6.3", len(anagramy))
for slowo1, slowo2 in anagramy:
    print(slowo1, slowo2)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <print>
#include <string>
#include <utility>
#include <vector>

int main() {
    std::vector<std::pair<std::string, std::string>> pary;
    std::ifstream plik("slowa.txt");
    std::string a, b;
    while (plik >> a >> b)
        pary.push_back({a, b});

    // 6.1
    int ile = 0;
    for (const auto& [slowo1, slowo2] : pary) {
        if (slowo1.back() == 'A')
            ile++;
        if (slowo2.back() == 'A')
            ile++;
    }
    std::println("6.1 {}", ile);

    // 6.2
    ile = 0;
    for (const auto& [slowo1, slowo2] : pary)
        if (slowo2.find(slowo1) != std::string::npos)
            ile++;
    std::println("6.2 {}", ile);

    // 6.3
    std::vector<std::pair<std::string, std::string>> anagramy;
    for (const auto& [slowo1, slowo2] : pary) {
        std::string s1 = slowo1, s2 = slowo2;
        std::ranges::sort(s1);
        std::ranges::sort(s2);
        if (s1 == s2)
            anagramy.push_back({slowo1, slowo2});
    }
    std::println("6.3 {}", anagramy.size());
    for (const auto& [slowo1, slowo2] : anagramy)
        std::println("{} {}", slowo1, slowo2);
}
```

```java
// Java 25
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;

public class Zadanie {
    static String posortuj(String s) {
        char[] litery = s.toCharArray();
        Arrays.sort(litery);
        return new String(litery);
    }

    public static void main(String[] args) throws Exception {
        var pary = new ArrayList<String[]>();
        for (String line : Files.readAllLines(Path.of("slowa.txt")))
            if (!line.isBlank())
                pary.add(line.trim().split("\\s+"));

        // 6.1
        int ile = 0;
        for (String[] p : pary) {
            if (p[0].endsWith("A"))
                ile++;
            if (p[1].endsWith("A"))
                ile++;
        }
        System.out.println("6.1 " + ile);

        // 6.2
        ile = 0;
        for (String[] p : pary)
            if (p[1].contains(p[0]))
                ile++;
        System.out.println("6.2 " + ile);

        // 6.3
        var anagramy = new ArrayList<String[]>();
        for (String[] p : pary)
            if (posortuj(p[0]).equals(posortuj(p[1])))
                anagramy.add(p);
        System.out.println("6.3 " + anagramy.size());
        for (String[] p : anagramy)
            System.out.println(p[0] + " " + p[1]);
    }
}
```

**Odpowiedź:** 6.1: 71; 6.2: 234; 6.3: 38 par (AYE YEA, BRD RDB, BWRHQ BWRHQ, DANHC DANHC, DCCD CDDC, …)
