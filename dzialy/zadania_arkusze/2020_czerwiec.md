<a name="czerwiec1"/>
  
 # 2020 czerwiec [⬆️](#main)
W pliku pary.txt znajduje się 100 wierszy. Każdy wiersz zawiera parę danych składającą się z liczby całkowitej z przedziału od 3 do 100 i słowa (ciągu znaków) złożonego z małych liter alfabetu angielskiego o długości od 1 do 50 znaków. Liczba i słowo są oddzielone znakiem spacji. 

### 4.1

Mocna hipoteza Goldbacha mówi, że każda parzysta liczba całkowita większa od 4 jest sumą  dwóch nieparzystych liczb pierwszych, np. liczba 20 jest równa sumie 3 + 17 lub sumie 7 + 13. Każdą liczbę parzystą z pliku pary.txt przedstaw w postaci sumy dwóch liczb pierwszych. Wypisz tę liczbę oraz dwa składniki sumy w kolejności niemalejącej. Jeżeli istnieje więcej rozwiązań (tak jak dla liczby 20) należy wypisać składniki sumy o największej różnicy. Wyniki podaj w oddzielnych wierszach, w kolejności zgodnej z kolejnością danych w pliku pary.txt. Liczby w każdym wierszu rozdziel znakiem spacji, np. dla liczby 20 należy wypisać 20 3 17. 

  ```python
  def is_prime(x):
    if x > 1:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True
    else:
        return False

with open("Dane_PR2\pary.txt") as file:
    for line in file:
        num,word = line.strip().split()
        num = int(num)
        if num > 4 and num % 2 == 0:
            for j in range(3,num+1):
                if is_prime(j) and is_prime(num-j):
                    print(num,j,num-j)
                    break
  ```
  
<a name="czerwiec2"/> 

### 4.2

Dla każdego słowa z pliku pary.txt znajdź długość najdłuższego spójnego fragmentu tego słowa złożonego z identycznych liter. Wypisz znalezione fragmenty słów i ich długości oddzielone spacją, po jednej parze w każdym wierszu. Jeżeli istnieją dwa fragmenty o takiej samej największej długości, podaj pierwszy z nich. Wyniki podaj w kolejności zgodnej z kolejnością danych w pliku pary.txt. 

  ```python
  with open("Dane_PR2\pary.txt") as file:
    for line in file:
        num,word = line.strip().split()
        
        seq = word[0]
        longest_seq = word[0]
        for char in word[1:]:
            if char == seq[-1]:
                seq += char
            else:
                seq = char
            if len(seq) > len(longest_seq):
                longest_seq = seq
        print(longest_seq, len(longest_seq))  
  ```
  
<a name="czerwiec3"/>

### 4.3

Para (liczba1, słowo1) jest mniejsza od pary (liczba2, słowo2), gdy:
– liczba1 < liczba2,
albo
– liczba1 = liczba2 oraz słowo1 jest leksykograficznie (w porządku alfabetycznym) mniejsze od słowo2.

Przykład:

para (1, bbbb) jest mniejsza od pary (2, aaa), natomiast para (3, aaa) jest mniejsza od pary (3, ab).

Rozważ wszystkie pary (liczba, słowo) zapisane w wierszach pliku pary.txt, dla których liczba jest równa długości słowa, i wypisz spośród nich taką parę, która jest mniejsza od wszystkich pozostałych. W pliku pary.txt jest jedna taka para. 
   
  ```python
  lista = []
with open("Dane_PR2\pary.txt") as file:
    for line in file:
        num,word = line.strip().split()
        num = int(num)
        if num == len(word):
            lista.append((num,word))
lista.sort()
print(lista[0])
  ```
