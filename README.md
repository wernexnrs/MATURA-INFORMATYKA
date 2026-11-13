<h1 align="center">Matura z informatyki — algorytmy i arkusze w Pythonie</h1>

<p align="center">
  <a href="https://wernexnrs.github.io/MATURA-INFORMATYKA/"><b>🌐 Otwórz stronę z materiałami</b></a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/wernexnrs/MATURA-INFORMATYKA?style=flat-square&logo=github&color=yellow" alt="Gwiazdki">
  <img src="https://img.shields.io/github/forks/wernexnrs/MATURA-INFORMATYKA?style=flat-square&logo=github&color=blue" alt="Forki">
  <img src="https://img.shields.io/github/license/wernexnrs/MATURA-INFORMATYKA?style=flat-square&color=green" alt="Licencja MIT">
  <img src="https://img.shields.io/github/last-commit/wernexnrs/MATURA-INFORMATYKA?style=flat-square&color=orange" alt="Ostatnia zmiana">
</p>

Darmowe materiały do **matury rozszerzonej z informatyki**: wszystkie algorytmy z wymagań egzaminacyjnych CKE napisane w **Pythonie** (z pseudokodem), dodatkowe algorytmy oraz **rozwiązania zadań z arkuszy maturalnych** z odpowiedziami. Bez reklam, bez logowania — wiedza dla każdego.

## Co tu znajdziesz

| Dział | Zawartość |
| --- | --- |
| [Algorytmy z wymagań CKE](dzialy/algorytmy_wymagania.md) | systemy liczbowe, liczby pierwsze i doskonałe, sito Eratostenesa, NWD/NWW, Fibonacci, wydawanie reszty, sortowania (bąbelkowe, przez wybór, wstawianie, scalanie, szybkie, kubełkowe), wyszukiwanie binarne, szybkie potęgowanie, schemat Hornera, bisekcja, pole pod wykresem, palindromy, anagramy, wzorzec w tekście, ONP, kompresja, Huffman, Morse, szyfry (Cezar, AtBash, przestawieniowy, Vigenère, RSA), geometria |
| [Dodatkowe algorytmy](dzialy/dodatkowe_algorytmy.md) | średnie, mediana, moda, wariancja, silnia, symbol Newtona, algorytmy tekstowe (KMP, Boyer-Moore, Karp-Rabin, Manacher, LCS), permutacje leksykograficzne, geometria analityczna |
| [Rozwiązania arkuszy](dzialy/zadania_arkusze.md) | matury 2005–2021 (rozszerzona, podstawowa, próbne) i zbiór zadań CKE — kod w Pythonie + oficjalne odpowiedzi |
| [Funkcje wbudowane](dzialy/funkcje_wbudowane.md) · [Metody](dzialy/metody.md) · [Moduły](dzialy/biblioteki.md) | ściąga z Pythona |
| [Przydatne linki](dzialy/przydatne_linki.md) | kursy, kanały YT i strony z rozwiązaniami |

Najwygodniej korzystać ze **[strony internetowej](https://wernexnrs.github.io/MATURA-INFORMATYKA/)**: wyszukiwarka (klawisz `/`), zakładki *Python / Pseudokod*, przycisk *Kopiuj*, tryb ciemny i wersja na telefon.

## Jak się uczyć

1. Przeczytaj algorytm i pseudokod, potem napisz go sam — dopiero na końcu porównaj z kodem.
2. Rozwiązuj arkusze na oficjalnych danych CKE (linki są przy każdym arkuszu) i sprawdzaj wynik z odpowiedzią.
3. Wracaj do wyszukiwarki, gdy zapomnisz, jak działa np. sito Eratostenesa albo bisekcja.

## Współtworzenie

Znalazłeś błąd albo masz lepsze rozwiązanie? [Zgłoś issue](https://github.com/wernexnrs/MATURA-INFORMATYKA/issues) lub wyślij pull request — edytujesz zwykłe pliki Markdown w folderze `dzialy/`.

Stronę w folderze `docs/` generuje skrypt bez zewnętrznych bibliotek:

```bash
python tools/build_site.py
```

Po każdej zmianie w `dzialy/` GitHub Actions przebudowuje stronę automatycznie.

### Serwery Discord

- [Do matury](https://discord.gg/3hyj3kXQkt) — wspólna nauka do matury, nie tylko z informatyki
- [EE.08 / EE.09](https://discord.gg/RJMZQEC) — przygotowanie do egzaminów zawodowych

## Licencja

Projekt jest dostępny na licencji [MIT](LICENSE) — możesz go za darmo używać, kopiować, zmieniać i udostępniać, także w szkole i na korepetycjach. Wystarczy zachować informację o autorach.

<sub>Słowa kluczowe: matura informatyka, matura z informatyki python, algorytmy maturalne, wymagania CKE informatyka, rozwiązania arkuszy maturalnych informatyka, matura rozszerzona informatyka zadania, pseudokod, sortowanie, sito Eratostenesa, schemat Hornera.</sub>
