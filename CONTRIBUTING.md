# Jak współtworzyć projekt

Dzięki, że chcesz pomóc! Ten projekt istnieje po to, żeby każdy mógł za darmo przygotować się do matury z informatyki. Nie musisz być ekspertem — poprawienie literówki też jest wkładem.

## Spis treści

1. [Najprostsze sposoby pomocy](#1-najprostsze-sposoby-pomocy)
2. [Jak zbudowany jest projekt](#2-jak-zbudowany-jest-projekt)
3. [Pierwszy pull request krok po kroku](#3-pierwszy-pull-request-krok-po-kroku)
4. [Dodawanie algorytmu](#4-dodawanie-algorytmu)
5. [Dodawanie rozwiązań arkusza](#5-dodawanie-rozwiązań-arkusza)
6. [Sprawdzanie zmian i podgląd strony](#6-sprawdzanie-zmian-i-podgląd-strony)
7. [Co dzieje się z Twoją zmianą](#7-co-dzieje-się-z-twoją-zmianą)
8. [Zasady](#8-zasady)

---

## 1. Najprostsze sposoby pomocy

> **Najszybciej: prosto ze strony.** Pod każdym algorytmem i zadaniem na [stronie](https://wernexnrs.github.io/MATURA-INFORMATYKA/) są przyciski:
> - **✏️ Popraw lub dodaj** — otwiera ten plik w edytorze GitHuba. Wprowadzasz zmianę, klikasz *Commit changes → Propose changes → Create pull request*. GitHub sam zrobi Twoją kopię repozytorium.
> - **⚠ Zgłoś błąd** — otwiera gotowy formularz z adresem sekcji; wystarczy opisać problem.
>
> Potrzebujesz tylko darmowego konta na GitHubie. **Każda zmiana trafia do sprawdzenia** i pojawia się na stronie dopiero po zatwierdzeniu przez opiekuna projektu — nie bój się, że coś zepsujesz.

| Chcesz… | Zrób to |
| --- | --- |
| zgłosić błąd w kodzie lub odpowiedzi | [Nowe zgłoszenie → „Błąd w treści”](https://github.com/wernexnrs/MATURA-INFORMATYKA/issues/new/choose) |
| zaproponować algorytm lub arkusz | [Nowe zgłoszenie → „Propozycja”](https://github.com/wernexnrs/MATURA-INFORMATYKA/issues/new/choose) |
| poprawić literówkę | otwórz plik na GitHubie, kliknij ✏️ (Edit), popraw i zatwierdź — GitHub sam utworzy pull request |
| dodać rozwiązanie lub algorytm | przeczytaj punkty 3–6 |
| pomóc innym | odpowiadaj w [Dyskusjach](https://github.com/wernexnrs/MATURA-INFORMATYKA/discussions), przeglądaj pull requesty |

## 2. Jak zbudowany jest projekt

```
dzialy/                      ← CAŁA TREŚĆ (edytujesz tylko to)
  algorytmy_wymagania.md     ← algorytmy z wymagań CKE (Python, pseudokod, C++, Java)
  dodatkowe_algorytmy.md     ← algorytmy spoza wymagań
  zadania_arkusze.md         ← spis arkuszy (kafelki na stronie)
  zadania_arkusze/*.md       ← rozwiązania arkuszy, jeden plik = jeden arkusz
  zadania_zbior/*.md         ← zbiór zadań CKE
  funkcje_wbudowane.md, metody.md, biblioteki.md   ← ściągi z Pythona
  przydatne_linki.md
tools/build_site.py          ← generuje stronę z dzialy/ do docs/ (bez dodatkowych bibliotek)
tools/check.py               ← sprawdza Markdown i uruchamia kod
docs/                        ← gotowa strona (generowana automatycznie — nie edytuj ręcznie)
```

Po każdej zmianie na gałęzi `master` GitHub Actions sam przebudowuje stronę. Nie musisz commitować folderu `docs/`.

## 3. Pierwszy pull request krok po kroku

**Wersja w przeglądarce (bez instalowania czegokolwiek)** — dobra do małych zmian:

1. Otwórz plik w folderze `dzialy/` na GitHubie i kliknij ✏️ **Edit this file**.
2. Wprowadź zmiany. Zakładka **Preview** pokaże, jak wyglądają.
3. Na dole wpisz krótki opis (np. „Poprawka odpowiedzi 4.2 w maju 2019”) i kliknij **Propose changes**, a potem **Create pull request**.

**Wersja na komputerze** — do większych zmian:

```bash
# 1. Zrób fork (przycisk „Fork” na GitHubie), potem sklonuj swoją kopię
git clone https://github.com/TWOJ-LOGIN/MATURA-INFORMATYKA.git
cd MATURA-INFORMATYKA

# 2. Utwórz gałąź na swoją zmianę
git checkout -b dodaj-matura-2026-maj

# 3. Edytuj pliki w dzialy/, potem sprawdź
python tools/check.py --run

# 4. Zapisz i wyślij
git add dzialy
git commit -m "Dodaj rozwiązania matury 2026 maj"
git push -u origin dodaj-matura-2026-maj
```

Na GitHubie pojawi się przycisk **Compare & pull request** — kliknij go i opisz, co zmieniłeś. Automatyczne testy sprawdzą zmiany, a ktoś z zespołu je przejrzy.

## 4. Dodawanie algorytmu

Każdy algorytm to sekcja w `algorytmy_wymagania.md` (jeśli jest w wymaganiach CKE) albo w `dodatkowe_algorytmy.md`. Szablon:

````markdown
<a name="moja_kotwica"></a>
## Nazwa algorytmu [⬆️](#)
<details><summary>Rozwiń</summary>

Jedno–dwa zdania: co robi algorytm i kiedy się przydaje.

```python
def algorytm(dane):
    ...

print(algorytm([3, 1, 2]))  # [1, 2, 3]
```
<b>

```
dane - tablica liczb

Funkcja algorytm(dane):
	Dla i = 1, 2, ..., n
		Jeżeli ...
			Zwróć ...
```
</b>

```cpp
// C++23
#include <print>
...
int main() { ... }
```

```java
// Java 25
public class Algorytm {
    public static void main(String[] args) { ... }
}
```
</details>
````

Potem dodaj pozycję do spisu na górze pliku, np. `- ![py] ![c++] ![java] [Nazwa algorytmu](#moja_kotwica)`.

Zasady dla kodu:
- **Python** — prosty, „maturalny” kod, polskie nazwy zmiennych, bez zewnętrznych bibliotek (moduły standardowe są OK).
- **Pseudokod** — słowa `Jeżeli`, `W innym wypadku`, `Dopóki`, `Dla`, `Zwróć`, przypisanie `<-`, `mod`, `div`.
- **C++23** i **Java 25** — kompletny program z `main`, który da się skompilować i uruchomić. Pierwsza linia to komentarz `// C++23` / `// Java 25` — strona używa go jako podpisu zakładki.
- Bloki kodu stawiaj jeden po drugim (bez tekstu pomiędzy) — strona połączy je w zakładki *Python / Pseudokod / C++ / Java*.
- Dołącz krótki przykład użycia z wynikiem w komentarzu.

## 5. Dodawanie rozwiązań arkusza

Jeden arkusz = jeden plik w `dzialy/zadania_arkusze/`, np. `2026_maj.md`. Szablon:

````markdown
<h1 align="center">Matura 2026 — maj, poziom rozszerzony (formuła 2023)</h1>

[ARKUSZ CZ. I](link) --- [ARKUSZ CZ. II](link) --- [DANE](link) --- [ODPOWIEDZI](link)

## 1.2

```py
with open("dane.txt") as file:
    ...
```

**Odpowiedź:** 42
````

- Każdy podpunkt to `## numer`, blok kodu i linia `**Odpowiedź:**` z wynikiem z klucza CKE.
- Otwieraj pliki po samej nazwie z arkusza (`open("liczby.txt")`) — zakładamy, że plik leży obok skryptu.
- **Nie wrzucaj do repozytorium plików z danymi CKE** — linkuj do nich.
- Zadań na arkusz kalkulacyjny i bazy danych nie rozwiązujemy.
- Na koniec dodaj kafelek w `dzialy/zadania_arkusze.md`, w odpowiedniej grupie:
  `- ![py] [Maj 2026](zadania_arkusze/2026_maj.md) --- [POBIERZ ARKUSZ](link)`

Sprawdź wynik na prawdziwych danych CKE i porównaj z zasadami oceniania. Jeśli w kluczu jest błąd, opisz go w notce `> ...` pod odpowiedzią.

## 6. Sprawdzanie zmian i podgląd strony

Potrzebujesz tylko Pythona 3.8+ (do testów C++/Javy także `g++` z obsługą C++23 i JDK 25 — jeśli ich nie masz, test je pominie, a sprawdzi je GitHub).

```bash
python tools/check.py --run        # sprawdza Markdown i uruchamia kod algorytmów
python tools/build_site.py         # buduje stronę do docs/
python -m http.server 8000 --directory docs   # podgląd: http://localhost:8000
```

## 7. Co dzieje się z Twoją zmianą

1. Automatyczne testy sprawdzają pull request (Markdown, składnia, uruchomienie kodu algorytmów).
2. Opiekun projektu przegląda zmianę — może poprosić o poprawki w komentarzu.
3. Po zatwierdzeniu zmiana trafia do `master`, a strona przebudowuje się sama w ciągu kilku minut.

## 8. Zasady

- Bądź miły i pomocny — wszyscy się tu uczymy.
- Jeden pull request = jedna sprawa (np. jeden arkusz albo jeden algorytm). Łatwiej go przejrzeć.
- Nie kopiuj cudzych rozwiązań z płatnych kursów ani stron z zastrzeżonymi prawami — pisz własny kod.
- Wysyłając zmiany, zgadzasz się na udostępnienie ich na licencji [MIT](LICENSE).

Dziękujemy! 💜
