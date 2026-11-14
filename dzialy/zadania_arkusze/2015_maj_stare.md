<h1 align="center">Matura 2015 — maj, poziom rozszerzony (stara formuła)</h1>
 
[SPIS ARKUSZY](https://github.com/wernexnrs/MATURA-INFORMATYKA/blob/master/dzialy/zadania_arkusze.md)

[ARKUSZ I](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_do_2014/MIN-R1_1P-152.pdf) --- [ARKUSZ II](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_do_2014/MIN-R2_1P-152.pdf) --- [DANE](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_do_2014/Dane_PR2.zip) --- [ODPOWIEDZI](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_do_2014/odpowiedzi/MIN-R1-S.pdf)

## 1.1

> **Treść zadania:** Potęgi dwójki. Każdą dodatnią liczbę całkowitą n można zapisać jako sumę różnych potęg liczby 2, np. 11 = 1 + 2 + 8 = 2⁰ + 2¹ + 2³, 18 = 2 + 16 = 2¹ + 2⁴.
>
> Zapisz liczby 23 i 50 jako sumy różnych potęg liczby 2 (dla 11 odpowiedzią jest 1 + 2 + 8).

```py
def skladniki(n):
    wynik = []
    potega = 1
    while n > 0:
        if n % 2 == 1:
            wynik.append(potega)
        n = n // 2
        potega *= 2
    return wynik


for n in [11, 23, 50]:
    print(n, "=", " + ".join(str(x) for x in skladniki(n)))
```

```cpp
// C++23
#include <iostream>
#include <vector>

std::vector<int> skladniki(int n) {
    std::vector<int> wynik;
    int potega = 1;
    while (n > 0) {
        if (n % 2 == 1)
            wynik.push_back(potega);
        n = n / 2;
        potega *= 2;
    }
    return wynik;
}

int main() {
    for (int n : {11, 23, 50}) {
        std::cout << n << " =";
        auto s = skladniki(n);
        for (size_t i = 0; i < s.size(); i++)
            std::cout << (i == 0 ? " " : " + ") << s[i];
        std::cout << '\n';
    }
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    static List<Integer> skladniki(int n) {
        var wynik = new ArrayList<Integer>();
        int potega = 1;
        while (n > 0) {
            if (n % 2 == 1)
                wynik.add(potega);
            n = n / 2;
            potega *= 2;
        }
        return wynik;
    }

    public static void main(String[] args) {
        for (int n : new int[] {11, 23, 50}) {
            var s = new StringJoiner(" + ");
            for (int x : skladniki(n)) s.add(String.valueOf(x));
            System.out.println(n + " = " + s);
        }
    }
}
```

**Odpowiedź:** 23 = 1 + 2 + 4 + 16, 50 = 2 + 16 + 32

## 1.2

> **Treść zadania:** Każdą dodatnią liczbę całkowitą n można zapisać jako sumę różnych potęg liczby 2. Zapisz algorytm (lista kroków, schemat blokowy lub język programowania), który oblicza, ile różnych potęg dwójki daje w sumie n. Można używać dodawania, odejmowania, mnożenia, dzielenia, dzielenia całkowitego i reszty z dzielenia lub własnych funkcji.
>
> Specyfikacja — dane: `n` — dodatnia liczba całkowita; wynik: `lp` — liczba różnych potęg dwójki, których suma wynosi n.
>
> Przykład: dla n = 18 wynikiem jest lp = 2.

```py
def liczba_poteg(n):
    lp = 0
    while n > 0:
        lp += n % 2
        n = n // 2
    return lp


print(liczba_poteg(18))
```

```cpp
// C++23
#include <iostream>

int liczba_poteg(int n) {
    int lp = 0;
    while (n > 0) {
        lp += n % 2;
        n = n / 2;
    }
    return lp;
}

int main() {
    std::cout << liczba_poteg(18) << '\n';
}
```

```java
// Java 25
public class Zadanie {
    static int liczbaPoteg(int n) {
        int lp = 0;
        while (n > 0) {
            lp += n % 2;
            n = n / 2;
        }
        return lp;
    }

    public static void main(String[] args) {
        System.out.println(liczbaPoteg(18));
    }
}
```

**Odpowiedź:** dla n = 18 wynik lp = 2 (liczba jedynek w zapisie binarnym n)

## 2.1 i 2.2

> **Treść zadania:** Koszyk zabawek. Wygrałeś koszyk zakupów o łącznej masie co najwyżej 10 kg i chcesz, by wartość zabawek była jak największa. Dostępne zabawki (masa, cena): rowerek 8 kg, 320 zł; wózek dla lalek 4 kg, 152 zł; lalka 1 kg, 37 zł; duży miś 2 kg, 70 zł; klocki 3 kg, 99 zł; hulajnoga 5 kg, 155 zł; mały miś 1 kg, 30 zł. Strategie wyboru (zawsze pilnując limitu masy):
> - I — od najdroższej do najtańszej (przy równej cenie lżejsza),
> - II — od najlżejszej do najcięższej (przy równej masie droższa),
> - III — od największego do najmniejszego ilorazu cena/masa.
>
> Przy kilku zabawkach spełniających kryterium wybierasz dowolną.
>
> - 2.1 — Zakładając, że te same zabawki można brać wielokrotnie, podaj dla każdej strategii I, II, III zawartość koszyka (nazwy i liczby egzemplarzy) oraz jego łączną wartość.
> - 2.2 — Uzupełnij brakujące kroki 2 i 7 algorytmu obliczającego wartość koszyka dla strategii III (zabawki mogą się powtarzać). Dane: `mk` — limit masy, `n` — liczba artykułów, `MASA[1..n]`, `CENA[1..n]` — masy i ceny uporządkowane nierosnąco według ilorazu cena/masa (wszystko dodatnie całkowite). Wynik: `K[1..n]` — liczby egzemplarzy kolejnych zabawek w koszyku, `w` — łączna wartość koszyka.
>
> ```
> krok 1: dla i = 1 do n wykonaj K[i] ← 0
> krok 2: ............
> krok 3: i ← 1
> krok 4: dopóki i <= n oraz mk > 0
> krok 5:     K[i] ← mk div MASA[i]
> krok 6:     mk ← mk mod MASA[i]
> krok 7:     ............
> krok 8:     i ← i + 1
> ```

```py
# zabawki: (nazwa, masa, cena)
zabawki = [("rowerek", 8, 320), ("wozek dla lalek", 4, 152), ("lalka", 1, 37), ("duzy mis", 2, 70),
           ("klocki", 3, 99), ("hulajnoga", 5, 155), ("maly mis", 1, 30)]


def koszyk_z_powtorzeniami(lista, mk):
    # algorytm z zadania 2.2 - zachlannie, kazda zabawka moze wystapic wiele razy
    K = [0] * len(lista)
    w = 0                              # krok 2
    i = 0
    while i < len(lista) and mk > 0:
        nazwa, masa, cena = lista[i]
        K[i] = mk // masa
        mk = mk % masa
        w = w + K[i] * cena            # krok 7
        i += 1
    return K, w


strategie = {
    "I": sorted(zabawki, key=lambda z: (-z[2], z[1])),     # od najdrozszej, przy remisie lzejsza
    "II": sorted(zabawki, key=lambda z: (z[1], -z[2])),    # od najlzejszej, przy remisie drozsza
    "III": sorted(zabawki, key=lambda z: -z[2] / z[1]),    # od najwiekszego ilorazu cena/masa
}

for nazwa_strategii, lista in strategie.items():
    K, w = koszyk_z_powtorzeniami(lista, 10)
    zawartosc = [f"{K[i]}x {lista[i][0]}" for i in range(len(lista)) if K[i] > 0]
    print(nazwa_strategii, zawartosc, w)
```

```cpp
// C++23
#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

struct Zabawka {
    std::string nazwa;
    int masa, cena;
};

// zabawki: (nazwa, masa, cena)
const std::vector<Zabawka> zabawki = {{"rowerek", 8, 320}, {"wozek dla lalek", 4, 152}, {"lalka", 1, 37}, {"duzy mis", 2, 70},
                                      {"klocki", 3, 99}, {"hulajnoga", 5, 155}, {"maly mis", 1, 30}};

std::pair<std::vector<int>, int> koszyk_z_powtorzeniami(const std::vector<Zabawka>& lista, int mk) {
    // algorytm z zadania 2.2 - zachlannie, kazda zabawka moze wystapic wiele razy
    std::vector<int> K(lista.size(), 0);
    int w = 0;  // krok 2
    size_t i = 0;
    while (i < lista.size() && mk > 0) {
        K[i] = mk / lista[i].masa;
        mk = mk % lista[i].masa;
        w = w + K[i] * lista[i].cena;  // krok 7
        i++;
    }
    return {K, w};
}

// stable_sort zachowuje kolejność przy remisie, tak jak sorted() w Pythonie
template <typename Porownanie>
std::vector<Zabawka> posortowane(Porownanie mniejsza) {
    auto lista = zabawki;
    std::ranges::stable_sort(lista, mniejsza);
    return lista;
}

int main() {
    std::vector<std::pair<std::string, std::vector<Zabawka>>> strategie = {
        // od najdrozszej, przy remisie lzejsza
        {"I", posortowane([](const Zabawka& a, const Zabawka& b) {
             return std::pair(-a.cena, a.masa) < std::pair(-b.cena, b.masa); })},
        // od najlzejszej, przy remisie drozsza
        {"II", posortowane([](const Zabawka& a, const Zabawka& b) {
             return std::pair(a.masa, -a.cena) < std::pair(b.masa, -b.cena); })},
        // od najwiekszego ilorazu cena/masa
        {"III", posortowane([](const Zabawka& a, const Zabawka& b) {
             return -static_cast<double>(a.cena) / a.masa < -static_cast<double>(b.cena) / b.masa; })},
    };

    for (const auto& [nazwa_strategii, lista] : strategie) {
        auto [K, w] = koszyk_z_powtorzeniami(lista, 10);
        std::cout << nazwa_strategii << " [";
        bool pierwszy = true;
        for (size_t i = 0; i < lista.size(); i++) {
            if (K[i] > 0) {
                std::cout << (pierwszy ? "" : ", ") << "'" << K[i] << "x " << lista[i].nazwa << "'";
                pierwszy = false;
            }
        }
        std::cout << "] " << w << '\n';
    }
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    record Zabawka(String nazwa, int masa, int cena) {}

    // zabawki: (nazwa, masa, cena)
    static List<Zabawka> zabawki = List.of(new Zabawka("rowerek", 8, 320), new Zabawka("wozek dla lalek", 4, 152),
            new Zabawka("lalka", 1, 37), new Zabawka("duzy mis", 2, 70), new Zabawka("klocki", 3, 99),
            new Zabawka("hulajnoga", 5, 155), new Zabawka("maly mis", 1, 30));

    static int[] K;  // ile sztuk każdej zabawki z listy trafiło do koszyka

    static int koszykZPowtorzeniami(List<Zabawka> lista, int mk) {
        // algorytm z zadania 2.2 - zachlannie, kazda zabawka moze wystapic wiele razy
        K = new int[lista.size()];
        int w = 0;  // krok 2
        int i = 0;
        while (i < lista.size() && mk > 0) {
            K[i] = mk / lista.get(i).masa();
            mk = mk % lista.get(i).masa();
            w = w + K[i] * lista.get(i).cena();  // krok 7
            i++;
        }
        return w;
    }

    static List<Zabawka> posortowane(Comparator<Zabawka> porownanie) {
        var lista = new ArrayList<>(zabawki);
        lista.sort(porownanie);  // sortowanie stabilne, jak sorted() w Pythonie
        return lista;
    }

    public static void main(String[] args) {
        var strategie = new LinkedHashMap<String, List<Zabawka>>();
        // od najdrozszej, przy remisie lzejsza
        strategie.put("I", posortowane(Comparator.comparingInt((Zabawka z) -> -z.cena()).thenComparingInt(Zabawka::masa)));
        // od najlzejszej, przy remisie drozsza
        strategie.put("II", posortowane(Comparator.comparingInt(Zabawka::masa).thenComparingInt((Zabawka z) -> -z.cena())));
        // od najwiekszego ilorazu cena/masa
        strategie.put("III", posortowane(Comparator.comparingDouble((Zabawka z) -> -(double) z.cena() / z.masa())));

        for (var e : strategie.entrySet()) {
            var lista = e.getValue();
            int w = koszykZPowtorzeniami(lista, 10);
            var zawartosc = new StringJoiner(", ", "[", "]");
            for (int i = 0; i < lista.size(); i++)
                if (K[i] > 0) zawartosc.add("'" + K[i] + "x " + lista.get(i).nazwa() + "'");
            System.out.println(e.getKey() + " " + zawartosc + " " + w);
        }
    }
}
```

**Odpowiedź:** I: rowerek + duży miś, 390 zł; II: 10x lalka, 370 zł; III: rowerek + 2x lalka, 394 zł. Uzupełnienie algorytmu: krok 2: `w ← 0`, krok 7: `w ← w + K[i] * CENA[i]`

## 2.3 i 2.4

> **Treść zadania:** Koszyk zabawek o limicie 10 kg i zabawki jak w zadaniu 2.1 (rowerek 8 kg/320 zł, wózek 4 kg/152 zł, lalka 1 kg/37 zł, duży miś 2 kg/70 zł, klocki 3 kg/99 zł, hulajnoga 5 kg/155 zł, mały miś 1 kg/30 zł); strategie I (od najdroższej), II (od najlżejszej), III (od największego ilorazu cena/masa).
> - 2.3 — Zakładając, że zabawki nie mogą się powtarzać, podaj dla każdej strategii I, II, III nazwy wybranych zabawek i łączną wartość koszyka.
> - 2.4 — Zapisz algorytm doboru zabawek według strategii III bez powtórzeń. Dane: `mk`, `n`, `MASA[1..n]`, `CENA[1..n]` (uporządkowane nierosnąco według ilorazu cena/masa). Wynik: `K[1..n]`, gdzie K[i] = 1, gdy i-ta zabawka trafiła do koszyka, a 0 w przeciwnym razie, oraz `w` — łączna wartość koszyka.

```py
zabawki = [("rowerek", 8, 320), ("wozek dla lalek", 4, 152), ("lalka", 1, 37), ("duzy mis", 2, 70),
           ("klocki", 3, 99), ("hulajnoga", 5, 155), ("maly mis", 1, 30)]


def koszyk_bez_powtorzen(lista, mk):
    # algorytm z zadania 2.4 - kazda zabawka co najwyzej raz
    K = [0] * len(lista)
    w = 0
    for i in range(len(lista)):
        nazwa, masa, cena = lista[i]
        if masa <= mk:
            K[i] = 1
            mk -= masa
            w += cena
    return K, w


strategie = {
    "I": sorted(zabawki, key=lambda z: (-z[2], z[1])),
    "II": sorted(zabawki, key=lambda z: (z[1], -z[2])),
    "III": sorted(zabawki, key=lambda z: -z[2] / z[1]),
}

for nazwa_strategii, lista in strategie.items():
    K, w = koszyk_bez_powtorzen(lista, 10)
    zawartosc = [lista[i][0] for i in range(len(lista)) if K[i] == 1]
    print(nazwa_strategii, zawartosc, w)
```

```cpp
// C++23
#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

struct Zabawka {
    std::string nazwa;
    int masa, cena;
};

const std::vector<Zabawka> zabawki = {{"rowerek", 8, 320}, {"wozek dla lalek", 4, 152}, {"lalka", 1, 37}, {"duzy mis", 2, 70},
                                      {"klocki", 3, 99}, {"hulajnoga", 5, 155}, {"maly mis", 1, 30}};

std::pair<std::vector<int>, int> koszyk_bez_powtorzen(const std::vector<Zabawka>& lista, int mk) {
    // algorytm z zadania 2.4 - kazda zabawka co najwyzej raz
    std::vector<int> K(lista.size(), 0);
    int w = 0;
    for (size_t i = 0; i < lista.size(); i++) {
        if (lista[i].masa <= mk) {
            K[i] = 1;
            mk -= lista[i].masa;
            w += lista[i].cena;
        }
    }
    return {K, w};
}

template <typename Porownanie>
std::vector<Zabawka> posortowane(Porownanie mniejsza) {
    auto lista = zabawki;
    std::ranges::stable_sort(lista, mniejsza);  // stabilne, jak sorted() w Pythonie
    return lista;
}

int main() {
    std::vector<std::pair<std::string, std::vector<Zabawka>>> strategie = {
        {"I", posortowane([](const Zabawka& a, const Zabawka& b) {
             return std::pair(-a.cena, a.masa) < std::pair(-b.cena, b.masa); })},
        {"II", posortowane([](const Zabawka& a, const Zabawka& b) {
             return std::pair(a.masa, -a.cena) < std::pair(b.masa, -b.cena); })},
        {"III", posortowane([](const Zabawka& a, const Zabawka& b) {
             return -static_cast<double>(a.cena) / a.masa < -static_cast<double>(b.cena) / b.masa; })},
    };

    for (const auto& [nazwa_strategii, lista] : strategie) {
        auto [K, w] = koszyk_bez_powtorzen(lista, 10);
        std::cout << nazwa_strategii << " [";
        bool pierwszy = true;
        for (size_t i = 0; i < lista.size(); i++) {
            if (K[i] == 1) {
                std::cout << (pierwszy ? "" : ", ") << "'" << lista[i].nazwa << "'";
                pierwszy = false;
            }
        }
        std::cout << "] " << w << '\n';
    }
}
```

```java
// Java 25
import java.util.*;

public class Zadanie {
    record Zabawka(String nazwa, int masa, int cena) {}

    static List<Zabawka> zabawki = List.of(new Zabawka("rowerek", 8, 320), new Zabawka("wozek dla lalek", 4, 152),
            new Zabawka("lalka", 1, 37), new Zabawka("duzy mis", 2, 70), new Zabawka("klocki", 3, 99),
            new Zabawka("hulajnoga", 5, 155), new Zabawka("maly mis", 1, 30));

    static int[] K;  // 1 - zabawka z listy trafiła do koszyka

    static int koszykBezPowtorzen(List<Zabawka> lista, int mk) {
        // algorytm z zadania 2.4 - kazda zabawka co najwyzej raz
        K = new int[lista.size()];
        int w = 0;
        for (int i = 0; i < lista.size(); i++) {
            if (lista.get(i).masa() <= mk) {
                K[i] = 1;
                mk -= lista.get(i).masa();
                w += lista.get(i).cena();
            }
        }
        return w;
    }

    static List<Zabawka> posortowane(Comparator<Zabawka> porownanie) {
        var lista = new ArrayList<>(zabawki);
        lista.sort(porownanie);  // sortowanie stabilne, jak sorted() w Pythonie
        return lista;
    }

    public static void main(String[] args) {
        var strategie = new LinkedHashMap<String, List<Zabawka>>();
        strategie.put("I", posortowane(Comparator.comparingInt((Zabawka z) -> -z.cena()).thenComparingInt(Zabawka::masa)));
        strategie.put("II", posortowane(Comparator.comparingInt(Zabawka::masa).thenComparingInt((Zabawka z) -> -z.cena())));
        strategie.put("III", posortowane(Comparator.comparingDouble((Zabawka z) -> -(double) z.cena() / z.masa())));

        for (var e : strategie.entrySet()) {
            var lista = e.getValue();
            int w = koszykBezPowtorzen(lista, 10);
            var zawartosc = new StringJoiner(", ", "[", "]");
            for (int i = 0; i < lista.size(); i++)
                if (K[i] == 1) zawartosc.add("'" + lista.get(i).nazwa() + "'");
            System.out.println(e.getKey() + " " + zawartosc + " " + w);
        }
    }
}
```

**Odpowiedź:** I: rowerek, duży miś — 390 zł; II: lalka, mały miś, duży miś, klocki — 236 zł; III: rowerek, lalka, mały miś — 387 zł

## 4.1

> **Treść zadania:** W pliku `slowa.txt` jest 1000 słów zerojedynkowych o długości od 2 do 25 znaków, po jednym w wierszu. Odpowiedzi zapisz w pliku `wynik4.txt`, poprzedzając każdą numerem zadania. Blokiem nazywamy maksymalny (niedający się wydłużyć) ciąg kolejnych jednakowych znaków — np. słowo 100110001 ma 5 bloków: 1, 00, 11, 000, 1.
>
> Podaj, ile słów z pliku ma więcej zer niż jedynek.
>
> Przykład: dla słów 101011010011001100111, 10001001, 0001000, 101010011100, 000011, 1111100 wynikiem jest 3.

```py
licznik = 0

with open("slowa.txt") as file:
    for line in file:
        slowo = line.strip()
        if slowo.count("0") > slowo.count("1"):
            licznik += 1

print(licznik)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>

int main() {
    int licznik = 0;
    std::ifstream plik("slowa.txt");
    std::string slowo;
    while (plik >> slowo)
        if (std::ranges::count(slowo, '0') > std::ranges::count(slowo, '1'))
            licznik++;
    std::cout << licznik << '\n';
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int licznik = 0;
        for (var line : Files.readAllLines(Path.of("slowa.txt"))) {
            var slowo = line.strip();
            long zera = slowo.chars().filter(c -> c == '0').count();
            long jedynki = slowo.chars().filter(c -> c == '1').count();
            if (zera > jedynki) licznik++;
        }
        System.out.println(licznik);
    }
}
```

**Odpowiedź:** 441

## 4.2

> **Treść zadania:** Plik `slowa.txt` zawiera 1000 słów zerojedynkowych. Podaj, ile słów składa się z dokładnie dwóch niepustych bloków: pierwszego złożonego z samych zer i drugiego — z samych jedynek (czyli postaci 0…01…1). Odpowiedź zapisz w `wynik4.txt`.
>
> Przykład: dla słów 100010000100, 000000111111, 00000000, 11111111110000, 00000000000000001 wynikiem jest 2.

```py
licznik = 0

with open("slowa.txt") as file:
    for line in file:
        slowo = line.strip()
        # dokladnie dwa bloki: najpierw same zera, potem same jedynki
        zera = len(slowo) - len(slowo.lstrip("0"))
        if 0 < zera < len(slowo) and slowo[zera:] == "1" * (len(slowo) - zera):
            licznik += 1

print(licznik)
```

```cpp
// C++23
#include <fstream>
#include <iostream>
#include <string>

int main() {
    int licznik = 0;
    std::ifstream plik("slowa.txt");
    std::string slowo;
    while (plik >> slowo) {
        // dokladnie dwa bloki: najpierw same zera, potem same jedynki
        size_t zera = 0;
        while (zera < slowo.size() && slowo[zera] == '0') zera++;
        if (0 < zera && zera < slowo.size() && slowo.substr(zera) == std::string(slowo.size() - zera, '1'))
            licznik++;
    }
    std::cout << licznik << '\n';
}
```

```java
// Java 25
import java.nio.file.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        int licznik = 0;
        for (var line : Files.readAllLines(Path.of("slowa.txt"))) {
            var slowo = line.strip();
            // dokladnie dwa bloki: najpierw same zera, potem same jedynki
            int zera = 0;
            while (zera < slowo.length() && slowo.charAt(zera) == '0') zera++;
            if (0 < zera && zera < slowo.length() && slowo.substring(zera).equals("1".repeat(slowo.length() - zera)))
                licznik++;
        }
        System.out.println(licznik);
    }
}
```

**Odpowiedź:** 44

## 4.3

> **Treść zadania:** Plik `slowa.txt` zawiera 1000 słów zerojedynkowych. Podaj długość najdłuższego bloku złożonego z samych zer, występującego w słowach z pliku, i wypisz wszystkie słowa zawierające blok zer o tej długości. Odpowiedź zapisz w `wynik4.txt`.
>
> Przykład: dla słów 100010000100, 001, 000, 10101001110000, 000011 wynikiem jest 4 oraz słowa 100010000100, 10101001110000 i 000011.

```py
def najdluzszy_blok_zer(slowo):
    najdluzszy = biezacy = 0
    for znak in slowo:
        if znak == "0":
            biezacy += 1
            najdluzszy = max(najdluzszy, biezacy)
        else:
            biezacy = 0
    return najdluzszy


slowa = []
with open("slowa.txt") as file:
    for line in file:
        slowa.append(line.strip())

maks = 0
for slowo in slowa:
    maks = max(maks, najdluzszy_blok_zer(slowo))

print(maks)
for slowo in slowa:
    if najdluzszy_blok_zer(slowo) == maks:
        print(slowo)
```

```cpp
// C++23
#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int najdluzszy_blok_zer(const std::string& slowo) {
    int najdluzszy = 0, biezacy = 0;
    for (char znak : slowo) {
        if (znak == '0') {
            biezacy++;
            najdluzszy = std::max(najdluzszy, biezacy);
        } else {
            biezacy = 0;
        }
    }
    return najdluzszy;
}

int main() {
    std::vector<std::string> slowa;
    std::ifstream plik("slowa.txt");
    std::string slowo;
    while (plik >> slowo)
        slowa.push_back(slowo);

    int maks = 0;
    for (const auto& s : slowa)
        maks = std::max(maks, najdluzszy_blok_zer(s));

    std::cout << maks << '\n';
    for (const auto& s : slowa)
        if (najdluzszy_blok_zer(s) == maks)
            std::cout << s << '\n';
}
```

```java
// Java 25
import java.nio.file.*;
import java.util.*;

public class Zadanie {
    static int najdluzszyBlokZer(String slowo) {
        int najdluzszy = 0, biezacy = 0;
        for (char znak : slowo.toCharArray()) {
            if (znak == '0') {
                biezacy++;
                najdluzszy = Math.max(najdluzszy, biezacy);
            } else {
                biezacy = 0;
            }
        }
        return najdluzszy;
    }

    public static void main(String[] args) throws Exception {
        var slowa = new ArrayList<String>();
        for (var line : Files.readAllLines(Path.of("slowa.txt")))
            slowa.add(line.strip());

        int maks = 0;
        for (var slowo : slowa)
            maks = Math.max(maks, najdluzszyBlokZer(slowo));

        System.out.println(maks);
        for (var slowo : slowa)
            if (najdluzszyBlokZer(slowo) == maks)
                System.out.println(slowo);
    }
}
```

**Odpowiedź:** 10; 001010000000000, 1001010001000000000011001

## 6.1, 6.2, 6.3 i 6.4

*Zadanie na arkusz kalkulacyjny — rozwiązanie w Pythonie.*

> **Treść zadania:** Ogródki działkowe: 100 działek po 500 m². Plik `deszcz.txt` zawiera dla dni od 1 maja do 30 września 2014 roku datę i liczbę 0 (brak opadów) lub 1 (deszcz), rozdzielone tabulatorem (pierwszy wiersz to nagłówek `data opady`). Zbiornik na deszczówkę ma pojemność 2 500 000 litrów; w nocy z 30 kwietnia na 1 maja był pełny. Zasady:
> - w dzień bez deszczu rano zrasza się działki (2 litry na 1 m²), a wieczorem z pozostałej wody ubywa 1% przez parowanie,
> - w dzień deszczowy zraszacze nie działają, a wieczorem woda w zbiorniku zwiększa się o 3% względem stanu z rana; nadmiar ponad pojemność trafia do kanalizacji,
> - na koniec każdej soboty wodociągi dolewają wodę — maksymalnie 500 000 litrów, nie przekraczając pojemności zbiornika.
>
> Obliczenia prowadź bez zaokrągleń, odpowiedzi podaj zaokrąglone do liczb całkowitych. Wskazówka: 1 czerwca 2014 rano w zbiorniku było ok. 2 336 406 litrów. Odpowiedzi zapisz w pliku `wynik6.txt`.
>
> - 6.1 — W ilu dniach w badanym okresie deszczówka będzie odprowadzana do kanalizacji?
> - 6.2 — Ile łącznie wody pobrano z wodociągów na uzupełnianie zbiornika?
> - 6.3 — Którego dnia rano w zbiorniku będzie najmniej wody? Podaj datę i ilość wody.
> - 6.4 — Dla każdej majowej soboty podaj jej datę, ilość wody odprowadzonej tego dnia do kanalizacji i ilość wody dolanej z wodociągów.
> - (6.5 — narysuj wykres kolumnowy ilości dolewanej wody w sobotach maja.)

```py
from datetime import date

POJEMNOSC = 2500000
woda = POJEMNOSC
dni_odprowadzania = 0
z_wodociagow = 0
najmniej = None
soboty_maja = []

with open("deszcz.txt") as file:
    next(file)
    for line in file:
        data, opady = line.split()
        dzien = date.fromisoformat(data)
        # stan rano
        if najmniej is None or woda < najmniej[1]:
            najmniej = (data, woda)
        odprowadzono = 0
        if opady == "1":
            woda *= 1.03
            if woda > POJEMNOSC:
                odprowadzono = woda - POJEMNOSC
                woda = POJEMNOSC
                dni_odprowadzania += 1
        else:
            woda -= 100 * 500 * 2      # zraszanie 100 dzialek po 500 m2, 2 l/m2
            woda *= 0.99               # parowanie
        dolano = 0
        if dzien.weekday() == 5:       # sobota
            dolano = min(500000, POJEMNOSC - woda)
            woda += dolano
            z_wodociagow += dolano
            if dzien.month == 5:
                soboty_maja.append((data, round(odprowadzono), round(dolano)))

print("6.1", dni_odprowadzania)
print("6.2", round(z_wodociagow))
print("6.3", najmniej[0], round(najmniej[1]))
print("6.4")
for wiersz in soboty_maja:
    print(*wiersz)
```

```cpp
// C++23
#include <algorithm>
#include <chrono>
#include <cmath>
#include <fstream>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>

int main() {
    const double POJEMNOSC = 2500000;
    double woda = POJEMNOSC;
    int dni_odprowadzania = 0;
    double z_wodociagow = 0;
    std::string najmniej_data;  // pusty napis - jeszcze nic (None w Pythonie)
    double najmniej_woda = 0;
    std::vector<std::tuple<std::string, long long, long long>> soboty_maja;

    // std::nearbyint zaokrągla połówki do parzystej, tak jak round() w Pythonie
    auto zaokraglij = [](double x) { return static_cast<long long>(std::nearbyint(x)); };

    std::ifstream plik("deszcz.txt");
    std::string naglowek, data, opady;
    std::getline(plik, naglowek);
    while (plik >> data >> opady) {
        int r = std::stoi(data.substr(0, 4)), m = std::stoi(data.substr(5, 2)), d = std::stoi(data.substr(8, 2));
        std::chrono::year_month_day dzien{std::chrono::year(r), std::chrono::month(m), std::chrono::day(d)};
        // stan rano
        if (najmniej_data.empty() || woda < najmniej_woda) {
            najmniej_data = data;
            najmniej_woda = woda;
        }
        double odprowadzono = 0;
        if (opady == "1") {
            woda *= 1.03;
            if (woda > POJEMNOSC) {
                odprowadzono = woda - POJEMNOSC;
                woda = POJEMNOSC;
                dni_odprowadzania++;
            }
        } else {
            woda -= 100 * 500 * 2;  // zraszanie 100 dzialek po 500 m2, 2 l/m2
            woda *= 0.99;           // parowanie
        }
        double dolano = 0;
        if (std::chrono::weekday(std::chrono::sys_days(dzien)) == std::chrono::Saturday) {
            dolano = std::min(500000.0, POJEMNOSC - woda);
            woda += dolano;
            z_wodociagow += dolano;
            if (m == 5)
                soboty_maja.push_back({data, zaokraglij(odprowadzono), zaokraglij(dolano)});
        }
    }

    std::cout << "6.1 " << dni_odprowadzania << '\n';
    std::cout << "6.2 " << zaokraglij(z_wodociagow) << '\n';
    std::cout << "6.3 " << najmniej_data << ' ' << zaokraglij(najmniej_woda) << '\n';
    std::cout << "6.4\n";
    for (const auto& [d, odp, dol] : soboty_maja)
        std::cout << d << ' ' << odp << ' ' << dol << '\n';
}
```

```java
// Java 25
import java.nio.file.*;
import java.time.*;
import java.util.*;

public class Zadanie {
    public static void main(String[] args) throws Exception {
        final double POJEMNOSC = 2500000;
        double woda = POJEMNOSC;
        int dniOdprowadzania = 0;
        double zWodociagow = 0;
        String najmniejData = null;
        double najmniejWoda = 0;
        var sobotyMaja = new ArrayList<String>();

        var linie = Files.readAllLines(Path.of("deszcz.txt"));
        for (var line : linie.subList(1, linie.size())) {  // pomijamy nagłówek
            var p = line.strip().split("\\s+");
            String data = p[0], opady = p[1];
            var dzien = LocalDate.parse(data);
            // stan rano
            if (najmniejData == null || woda < najmniejWoda) {
                najmniejData = data;
                najmniejWoda = woda;
            }
            double odprowadzono = 0;
            if (opady.equals("1")) {
                woda *= 1.03;
                if (woda > POJEMNOSC) {
                    odprowadzono = woda - POJEMNOSC;
                    woda = POJEMNOSC;
                    dniOdprowadzania++;
                }
            } else {
                woda -= 100 * 500 * 2;  // zraszanie 100 dzialek po 500 m2, 2 l/m2
                woda *= 0.99;           // parowanie
            }
            double dolano = 0;
            if (dzien.getDayOfWeek() == DayOfWeek.SATURDAY) {
                dolano = Math.min(500000, POJEMNOSC - woda);
                woda += dolano;
                zWodociagow += dolano;
                if (dzien.getMonthValue() == 5)
                    // Math.rint zaokrągla połówki do parzystej, tak jak round() w Pythonie
                    sobotyMaja.add(data + " " + (long) Math.rint(odprowadzono) + " " + (long) Math.rint(dolano));
            }
        }

        System.out.println("6.1 " + dniOdprowadzania);
        System.out.println("6.2 " + (long) Math.rint(zWodociagow));
        System.out.println("6.3 " + najmniejData + " " + (long) Math.rint(najmniejWoda));
        System.out.println("6.4");
        for (var wiersz : sobotyMaja)
            System.out.println(wiersz);
    }
}
```

**Odpowiedź:** 6.1: 13; 6.2: 8 289 356 (lub 8 289 355); 6.3: 2014-09-20, 1 303 938 l; 6.4: 2014-05-03 0 176 193, 2014-05-10 75 000 0, 2014-05-17 0 109 538, 2014-05-24 0 354 118, 2014-05-31 0 500 000; 6.5 — wykres kolumnowy z kolumny „dolano” zestawienia 6.4
