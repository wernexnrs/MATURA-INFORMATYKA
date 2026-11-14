<h1 align="center">Przykładowy arkusz CKE — formuła 2015</h1>

[ARKUSZ CZ. I](https://arkusze.pl/maturalne/informatyka-2015-przykladowy-arkusz-cke-rozszerzona.pdf) --- [ARKUSZ CZ. II](https://arkusze.pl/maturalne/informatyka-2015-przykladowy-arkusz-cke-rozszerzona-2.pdf) --- [DANE](https://arkusze.pl/maturalne/informatyka-2015-przykladowy-arkusz-cke-rozszerzona-zalaczniki.zip) --- [ODPOWIEDZI](https://arkusze.pl/maturalne/informatyka-2015-przykladowy-arkusz-cke-rozszerzona-odpowiedzi.pdf)

## 2a, 2b i 2c

> **Treść zadania:** Całkowity pierwiastek kwadratowy. Dla dodatniej liczby całkowitej n całkowitym pierwiastkiem kwadratowym nazywamy dodatnią liczbę całkowitą k taką, że k·k ≤ n i (k+1)·(k+1) > n (np. 3 jest całkowitym pierwiastkiem z liczb 9–15). Specyfikacja: dane — dodatnia liczba całkowita `n`; wynik — `k`, całkowity pierwiastek kwadratowy z n. Przykład: dla n = 39 wynikiem jest k = 6.
>
> - a) Uzupełnij wiersz (3) algorytmu tak, aby był poprawny, i podaj, ile razy sprawdzany jest warunek w wierszu (2) dla n = 32 i dla n = 1024:
>
> ```
> (1) k ← 1
> (2) dopóki (k+1)*(k+1) ≤ n wykonuj
> (3)     k ← ......
> ```
>
> - b) Uzupełnij wiersz (5) algorytmu (div — dzielenie całkowite):
>
> ```
> (1) k ← 1; m ← n
> (2) dopóki (k+1)*(k+1) ≤ n wykonuj
> (3)     s ← (k+m) div 2
> (4)     jeśli s*s ≤ n to
> (5)         k ← ......
> (6)     w przeciwnym przypadku
> (7)         m ← s
> ```
>
> - c) Podaj, ile razy sprawdzany jest warunek w wierszu (2) algorytmu z punktu b) dla n = 32 i dla n = 1024.

```py
def pierwiastek_liniowo(n):
    # 2a - brakująca instrukcja: k <- k + 1
    k = 1
    sprawdzenia = 0
    while True:
        sprawdzenia += 1  # sprawdzenie warunku z wiersza (2)
        if not (k + 1) * (k + 1) <= n:
            break
        k = k + 1
    return k, sprawdzenia


def pierwiastek_binarnie(n):
    # 2b - brakująca instrukcja: k <- s (wyszukiwanie binarne w przedziale [k, m])
    k = 1
    m = n
    sprawdzenia = 0
    while True:
        sprawdzenia += 1
        if not (k + 1) * (k + 1) <= n:
            break
        s = (k + m) // 2
        if s * s <= n:
            k = s
        else:
            m = s
    return k, sprawdzenia


for n in [32, 1024]:
    print(n, pierwiastek_liniowo(n)[1], pierwiastek_binarnie(n)[1])
```

```cpp
// C++23
#include <iostream>
#include <utility>

std::pair<long long, int> pierwiastek_liniowo(long long n) {
    // 2a - brakująca instrukcja: k <- k + 1
    long long k = 1;
    int sprawdzenia = 0;
    while (true) {
        sprawdzenia++;  // sprawdzenie warunku z wiersza (2)
        if (!((k + 1) * (k + 1) <= n))
            break;
        k = k + 1;
    }
    return {k, sprawdzenia};
}

std::pair<long long, int> pierwiastek_binarnie(long long n) {
    // 2b - brakująca instrukcja: k <- s (wyszukiwanie binarne w przedziale [k, m])
    long long k = 1, m = n;
    int sprawdzenia = 0;
    while (true) {
        sprawdzenia++;
        if (!((k + 1) * (k + 1) <= n))
            break;
        long long s = (k + m) / 2;
        if (s * s <= n)
            k = s;
        else
            m = s;
    }
    return {k, sprawdzenia};
}

int main() {
    for (long long n : {32, 1024})
        std::cout << n << ' ' << pierwiastek_liniowo(n).second << ' ' << pierwiastek_binarnie(n).second << '\n';
}
```

```java
// Java 25
public class Zadanie {
    // zwracają {k, liczba sprawdzeń}
    static long[] pierwiastekLiniowo(long n) {
        // 2a - brakująca instrukcja: k <- k + 1
        long k = 1;
        int sprawdzenia = 0;
        while (true) {
            sprawdzenia++;  // sprawdzenie warunku z wiersza (2)
            if (!((k + 1) * (k + 1) <= n))
                break;
            k = k + 1;
        }
        return new long[] {k, sprawdzenia};
    }

    static long[] pierwiastekBinarnie(long n) {
        // 2b - brakująca instrukcja: k <- s (wyszukiwanie binarne w przedziale [k, m])
        long k = 1, m = n;
        int sprawdzenia = 0;
        while (true) {
            sprawdzenia++;
            if (!((k + 1) * (k + 1) <= n))
                break;
            long s = (k + m) / 2;
            if (s * s <= n)
                k = s;
            else
                m = s;
        }
        return new long[] {k, sprawdzenia};
    }

    public static void main(String[] args) {
        for (long n : new long[] {32, 1024})
            System.out.println(n + " " + pierwiastekLiniowo(n)[1] + " " + pierwiastekBinarnie(n)[1]);
    }
}
```
**Odpowiedź:** 2a: k ← k + 1; liczba sprawdzeń: 5 (n = 32) i 32 (n = 1024). 2b: k ← s. 2c: 6 (n = 32) i 6 (n = 1024).

## 3a

> **Treść zadania:** Progi i schody. W ciągu liczb naturalnych parę sąsiednich liczb nazywamy progiem, jeśli następna liczba jest mniejsza od poprzedniej. Schody do dołu to podciąg kolejnych elementów złożony z co najmniej dwóch liczb, w którym każda liczba (poza pierwszą) nie jest większa od poprzedniej i którego nie da się rozszerzyć w żadną stronę. Długość schodów to liczba ich elementów.
>
> Przykład: ciąg 3, 7, 7, 6, 5, 4, 4, 4, 5 zawiera schody 7, 7, 6, 5, 4, 4, 4 o długości 7, z 3 progami (7 i 6, 6 i 5, 5 i 4).
>
> Dla ciągu 2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7 wypisz kolejno wszystkie schody do dołu, podając przy każdych ich długość i liczbę progów.

```py
def schody(a):
    # zwraca listę (schody, długość, liczba progów)
    wynik = []
    n = len(a)
    i = 0
    while i < n - 1:
        if a[i + 1] <= a[i]:
            j = i
            progi = 0
            while j < n - 1 and a[j + 1] <= a[j]:
                if a[j + 1] < a[j]:
                    progi += 1
                j += 1
            wynik.append((a[i:j + 1], j - i + 1, progi))
            i = j
        else:
            i += 1
    return wynik


ciag = [2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7]
for schodki, dlugosc, progi in schody(ciag):
    print(schodki, dlugosc, progi)
```

```cpp
// C++23
#include <iostream>
#include <tuple>
#include <vector>

// zwraca listę (schody, długość, liczba progów)
std::vector<std::tuple<std::vector<int>, int, int>> schody(const std::vector<int>& a) {
    std::vector<std::tuple<std::vector<int>, int, int>> wynik;
    int n = a.size();
    int i = 0;
    while (i < n - 1) {
        if (a[i + 1] <= a[i]) {
            int j = i;
            int progi = 0;
            while (j < n - 1 && a[j + 1] <= a[j]) {
                if (a[j + 1] < a[j])
                    progi++;
                j++;
            }
            wynik.push_back({std::vector<int>(a.begin() + i, a.begin() + j + 1), j - i + 1, progi});
            i = j;
        } else {
            i++;
        }
    }
    return wynik;
}

int main() {
    std::vector<int> ciag = {2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7};
    for (const auto& [schodki, dlugosc, progi] : schody(ciag)) {
        std::cout << '[';  // lista wypisana jak w Pythonie
        for (size_t k = 0; k < schodki.size(); k++)
            std::cout << (k > 0 ? ", " : "") << schodki[k];
        std::cout << "] " << dlugosc << ' ' << progi << '\n';
    }
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    record Schody(List<Integer> schodki, int dlugosc, int progi) {}

    static List<Schody> schody(List<Integer> a) {
        var wynik = new ArrayList<Schody>();
        int n = a.size();
        int i = 0;
        while (i < n - 1) {
            if (a.get(i + 1) <= a.get(i)) {
                int j = i;
                int progi = 0;
                while (j < n - 1 && a.get(j + 1) <= a.get(j)) {
                    if (a.get(j + 1) < a.get(j))
                        progi++;
                    j++;
                }
                wynik.add(new Schody(a.subList(i, j + 1), j - i + 1, progi));
                i = j;
            } else {
                i++;
            }
        }
        return wynik;
    }

    public static void main(String[] args) {
        var ciag = List.of(2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7);
        for (var s : schody(ciag))
            System.out.println(s.schodki() + " " + s.dlugosc() + " " + s.progi());  // lista wypisuje się jak w Pythonie
    }
}
```
**Odpowiedź:** (2, 2, 2) 3 0; (3, 1, 1) 3 1; (3, 3, 1) 3 1; (11, 7, 7, 6) 4 2; (7, 7) 2 0; (9, 9, 7) 3 1

## 3b

> **Treść zadania:** Próg to para sąsiednich liczb ciągu, w której następna liczba jest mniejsza od poprzedniej. Opracuj algorytm (schemat blokowy, lista kroków lub język programowania) zgodny ze specyfikacją:
> - Dane: dodatnia liczba całkowita `n` oraz tablica `a[1..n]` liczb całkowitych.
> - Wynik: `liczba_progów` — liczba wszystkich progów w ciągu zapisanym w tablicy a.

```py
def liczba_progow(a):
    licznik = 0
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            licznik += 1
    return licznik


print(liczba_progow([2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7]))
```

```cpp
// C++23
#include <iostream>
#include <vector>

int liczba_progow(const std::vector<int>& a) {
    int licznik = 0;
    for (size_t i = 0; i + 1 < a.size(); i++)
        if (a[i] > a[i + 1])
            licznik++;
    return licznik;
}

int main() {
    std::cout << liczba_progow({2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7}) << '\n';
}
```

```java
// Java 25
public class Zadanie {
    static int liczbaProgow(int[] a) {
        int licznik = 0;
        for (int i = 0; i < a.length - 1; i++)
            if (a[i] > a[i + 1])
                licznik++;
        return licznik;
    }

    public static void main(String[] args) {
        System.out.println(liczbaProgow(new int[] {2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7}));
    }
}
```
**Odpowiedź:** algorytm powyżej (dla ciągu z 3a: 5 progów)

## 3c i 3d

> **Treść zadania:** Próg to para sąsiednich liczb, w której następna jest mniejsza od poprzedniej; schody do dołu to nierozszerzalny podciąg co najmniej dwóch kolejnych elementów, w którym każdy element (poza pierwszym) nie jest większy od poprzedniego.
> - c) Opracuj algorytm zgodny ze specyfikacją — dane: dodatnia liczba całkowita `n` i tablica `a[1..n]` liczb całkowitych; wynik: `najw_liczba_progów` — największa liczba progów w jednych schodach do dołu w ciągu a.
> - d) Podaj, ile dokładnie porównań między elementami ciągu wykona Twój algorytm z punktu c) w przypadku pesymistycznym, i uzasadnij odpowiedź.

```py
def najw_liczba_progow(a):
    najw = 0
    w_schodach = 0
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            # a[i + 1] może być początkiem nowych schodów
            if w_schodach > najw:
                najw = w_schodach
            w_schodach = 0
        elif a[i] > a[i + 1]:
            w_schodach += 1
    # schody mogą kończyć się ostatnim elementem ciągu
    if w_schodach > najw:
        najw = w_schodach
    return najw


print(najw_liczba_progow([3, 7, 7, 6, 5, 4, 4, 4, 5]))
print(najw_liczba_progow([2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7]))
```

```cpp
// C++23
#include <iostream>
#include <vector>

int najw_liczba_progow(const std::vector<int>& a) {
    int najw = 0;
    int w_schodach = 0;
    for (size_t i = 0; i + 1 < a.size(); i++) {
        if (a[i] < a[i + 1]) {
            // a[i + 1] może być początkiem nowych schodów
            if (w_schodach > najw)
                najw = w_schodach;
            w_schodach = 0;
        } else if (a[i] > a[i + 1]) {
            w_schodach++;
        }
    }
    // schody mogą kończyć się ostatnim elementem ciągu
    if (w_schodach > najw)
        najw = w_schodach;
    return najw;
}

int main() {
    std::cout << najw_liczba_progow({3, 7, 7, 6, 5, 4, 4, 4, 5}) << '\n';
    std::cout << najw_liczba_progow({2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7}) << '\n';
}
```

```java
// Java 25
public class Zadanie {
    static int najwLiczbaProgow(int[] a) {
        int najw = 0;
        int wSchodach = 0;
        for (int i = 0; i < a.length - 1; i++) {
            if (a[i] < a[i + 1]) {
                // a[i + 1] może być początkiem nowych schodów
                if (wSchodach > najw)
                    najw = wSchodach;
                wSchodach = 0;
            } else if (a[i] > a[i + 1]) {
                wSchodach++;
            }
        }
        // schody mogą kończyć się ostatnim elementem ciągu
        if (wSchodach > najw)
            najw = wSchodach;
        return najw;
    }

    public static void main(String[] args) {
        System.out.println(najwLiczbaProgow(new int[] {3, 7, 7, 6, 5, 4, 4, 4, 5}));
        System.out.println(najwLiczbaProgow(new int[] {2, 2, 2, 3, 1, 1, 3, 3, 1, 10, 11, 7, 7, 6, 7, 7, 8, 9, 9, 7}));
    }
}
```
**Odpowiedź:** 3c: algorytm powyżej (dla przykładu z treści: 3). 3d: 2(n − 1) porównań — w każdym z n − 1 obrotów pętli w najgorszym razie wykonywane są dwa porównania (wykrycie nowych schodów i wykrycie progu).

## 4a i 4b

> **Treść zadania:** Anagramy cyfrowe. Dwie liczby naturalne są anagramami cyfrowymi, jeśli zapis dziesiętny jednej da się utworzyć z cyfr drugiej, używając każdej cyfry dokładnie tyle razy, ile razy w niej występuje (liczby nie mają zer wiodących). W pliku `dane_anagramy.txt` jest 1000 par dodatnich liczb całkowitych nie większych niż 2 000 000, po jednej parze w wierszu, oddzielonych spacją. Odpowiedzi zapisz w pliku `wyniki_anagramy.txt`, każdą w osobnym wierszu poprzedzoną oznaczeniem pytania.
> - a) W ilu wierszach obie liczby są anagramami cyfrowymi?
> - b) Ile maksymalnie liczb z pliku można wybrać tak, aby każde dwie były anagramami cyfrowymi?
>
> Przykład: dla wierszy `232 322`, `112 111`, `223 121`, `223 322` odpowiedź na a) to 2 (pierwszy i ostatni wiersz), a na b) to 5 (232, 322, 223, 223, 322).

```py
wiersze_z_anagramami = 0
ile = {}  # posortowane cyfry liczby -> ile liczb ma taki zestaw cyfr

with open("dane_anagramy.txt") as file:
    for line in file:
        a, b = line.split()
        # anagramy cyfrowe mają ten sam posortowany zapis cyfr
        klucz_a = "".join(sorted(a))
        klucz_b = "".join(sorted(b))
        if klucz_a == klucz_b:
            wiersze_z_anagramami += 1
        ile[klucz_a] = ile.get(klucz_a, 0) + 1
        ile[klucz_b] = ile.get(klucz_b, 0) + 1

with open("wyniki_anagramy.txt", "w") as wynik:
    print("a)", wiersze_z_anagramami, file=wynik)
    print("b)", max(ile.values()), file=wynik)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <map>
#include <string>

int main() {
    int wiersze_z_anagramami = 0;
    std::map<std::string, int> ile;  // posortowane cyfry liczby -> ile liczb ma taki zestaw cyfr

    std::ifstream plik("dane_anagramy.txt");
    std::string a, b;
    while (plik >> a >> b) {
        // anagramy cyfrowe mają ten sam posortowany zapis cyfr
        std::string klucz_a = a, klucz_b = b;
        std::ranges::sort(klucz_a);
        std::ranges::sort(klucz_b);
        if (klucz_a == klucz_b)
            wiersze_z_anagramami++;
        ile[klucz_a]++;
        ile[klucz_b]++;
    }

    int najwiecej = 0;
    for (const auto& [klucz, liczba] : ile)
        najwiecej = std::max(najwiecej, liczba);

    std::ofstream wynik("wyniki_anagramy.txt");
    wynik << "a) " << wiersze_z_anagramami << '\n';
    wynik << "b) " << najwiecej << '\n';
}
```

```java
// Java 25
import java.io.PrintWriter;
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int wierszeZAnagramami = 0;
        var ile = new HashMap<String, Integer>();  // posortowane cyfry liczby -> ile liczb ma taki zestaw cyfr

        for (var line : Files.readAllLines(Path.of("dane_anagramy.txt"))) {
            var p = line.strip().split("\\s+");
            // anagramy cyfrowe mają ten sam posortowany zapis cyfr
            char[] a = p[0].toCharArray(), b = p[1].toCharArray();
            Arrays.sort(a);
            Arrays.sort(b);
            String kluczA = new String(a), kluczB = new String(b);
            if (kluczA.equals(kluczB))
                wierszeZAnagramami++;
            ile.merge(kluczA, 1, Integer::sum);
            ile.merge(kluczB, 1, Integer::sum);
        }

        try (var wynik = new PrintWriter("wyniki_anagramy.txt")) {
            wynik.println("a) " + wierszeZAnagramami);
            wynik.println("b) " + Collections.max(ile.values()));
        }
    }
}
```
**Odpowiedź:** a) 258; b) 11
