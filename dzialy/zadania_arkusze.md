<a name="main"/>

<h1 align="center">  Zadania z arkuszy </h1>

1. 2020 czerwiec

   - [x] [4.1](#czerwiec1)
   - [x] [4.2](#czerwiec2)
   - [x] [4.3](#czerwiec3)
   
2. 2020 kwiecien
   
   - [x] [4.1](#kwiecien1)
   - [x] [4.2](#kwiecien2)
   - [x] [4.3](#kwiecien3)
   
3. 2019 czerwiec
   
   - [x] [4.1](#2019czerwiec1)
   - [x] [4.2](#2019czerwiec2)
   - [x] [4.3](#2019czerwiec3)

3. 2019 maj

   - [x] [4.1](#2019maj1)
   - [x] [4.2](#2019maj2)
   - [x] [4.3](#2019maj3)
   
4. 2018 czerwiec

   - [x] [4.1](#e1)
   - [x] [4.2](#e2)
   - [x] [4.3](#e3)

5. 2018 maj

   - [x] [4.1](#2018maj1)
   - [x] [4.2](#2018maj2)
   - [x] [4.3](#2018maj3)
   
6. 2017 czerwiec

   - [x] [4.1](#2017czerwiec1)
   - [x] [4.2](#2017czerwiec2)
   - [x] [4.3](#2017czerwiec3)
   
7. 2017 maju (nowa)

   - [x] [4.1](#2017maj1)
   - [x] [4.2](#2017maj2)
   - [x] [4.3](#2017maj3)
   
8. 2015 maj (nowa)

   - [x] [4.1](#bin1)
   - [x] [4.2](#bin2)
   - [x] [4.3](#bin3)
   

 
 # 2020 czerwiec [⬆️](#main)
W pliku pary.txt znajduje się 100 wierszy. Każdy wiersz zawiera parę danych składającą się z liczby całkowitej z przedziału od 3 do 100 i słowa (ciągu znaków) złożonego z małych liter alfabetu angielskiego o długości od 1 do 50 znaków. Liczba i słowo są oddzielone znakiem spacji. 

Mocna hipoteza Goldbacha mówi, że każda parzysta liczba całkowita większa od 4 jest sumą  dwóch nieparzystych liczb pierwszych, np. liczba 20 jest równa sumie 3 + 17 lub sumie 7 + 13. Każdą liczbę parzystą z pliku pary.txt przedstaw w postaci sumy dwóch liczb pierwszych. Wypisz tę liczbę oraz dwa składniki sumy w kolejności niemalejącej. Jeżeli istnieje więcej rozwiązań (tak jak dla liczby 20) należy wypisać składniki sumy o największej różnicy. Wyniki podaj w oddzielnych wierszach, w kolejności zgodnej z kolejnością danych w pliku pary.txt. Liczby w każdym wierszu rozdziel znakiem spacji, np. dla liczby 20 należy wypisać 20 3 17. 

 <a name="czerwiec1"/>
 
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
Dla każdego słowa z pliku pary.txt znajdź długość najdłuższego spójnego fragmentu tego słowa złożonego z identycznych liter. Wypisz znalezione fragmenty słów i ich długości oddzielone spacją, po jednej parze w każdym wierszu. Jeżeli istnieją dwa fragmenty o takiej samej największej długości, podaj pierwszy z nich. Wyniki podaj w kolejności zgodnej z kolejnością danych w pliku pary.txt. 

<a name="czerwiec2"/>
   
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
  
Para (liczba1, słowo1) jest mniejsza od pary (liczba2, słowo2), gdy:
– liczba1 < liczba2,
albo
– liczba1 = liczba2 oraz słowo1 jest leksykograficznie (w porządku alfabetycznym) mniejsze od słowo2.

Przykład:

para (1, bbbb) jest mniejsza od pary (2, aaa), natomiast para (3, aaa) jest mniejsza od pary (3, ab).

Rozważ wszystkie pary (liczba, słowo) zapisane w wierszach pliku pary.txt, dla których liczba jest równa długości słowa, i wypisz spośród nich taką parę, która jest mniejsza od wszystkich pozostałych. W pliku pary.txt jest jedna taka para. 

  
<a name="czerwiec3"/>
   
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
 # 2020 kwiecień [⬆️](#main)
Luką w ciągu liczbowym nazywamy bezwzględną wartość różnicy między dwoma kolejnymi elementami.
Przykładowo – w czteroelementowym ciągu: 5, 2, 7, 10 są trzy luki:
   − luka pomiędzy pierwszym a drugim elementem wynosi 3;
   − luka pomiędzy drugim a trzecim elementem wynosi 5;
   − luka pomiędzy trzecim a czwartym elementem wynosi 3.
Największa luka w tym ciągu ma wartość 5. W pliku dane4.txt znajduje się ciąg złożony z 1 000 dodatnich liczb całkowitych nie większych od 2⋅10^9

<a name="kwiecien1"/>
   
Podaj wartość największej luki oraz wartość najmniejszej luki pomiędzy elementami ciągu z pliku dane4.txt. 
   
  ```python
lista = []
luki = []
with open("dane\dane4.txt") as file:
    for line in file:
        line = int(line.strip())
        lista.append(line)

wartownik = lista[0]
for i in lista[1:]:
    wynik = abs(wartownik - i)
    luki.append(wynik)
    wartownik = i

print(min(luki))
print(max(luki))
  ```
  
<a name="kwiecien2"/>

Fragment ciągu nazywamy regularnym, jeśli wszystkie jego luki mają tę samą wartość. Przykładowo – w ciągu:
4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3 

regularnymi są następujące fragmenty:

   − 4, 11, 4 – luka między jego elementami wynosi 7;
   − 4, 1, 4, 7 – luka między jego elementami wynosi 3;
   − 7, 11 – luka między jego elementami wynosi 4;
   − 11, 12, 13, 14 – luka między jego elementami wynosi 1;
   − 14, 7, 0 – luka między jego elementami wynosi 7;
   − 0, 3 – luka między jego elementami wynosi 3.
   
Znajdź najdłuższy fragment regularny w ciągu z pliku dane4.txt. Podaj jego długość oraz wartości (liczby) znajdujące się na początku i końcu tego fragmentu. W pliku z danymi jest jeden taki fragment. W powyższym przykładzie długość najdłuższego fragmentu regularnego jest równa 4. Takie fragmenty w przykładzie są dwa. Jeden zaczyna się od liczby 4 i kończy liczbą 7, a drugi zaczyna się od liczby 11 i kończy liczbą 14.

```python
lista,luki,max_list = [],[],[]

with open("dane/dane4.txt") as file:
    for line in file:
        line = int(line.strip())
        lista.append(line)

for i in range(len(lista)):
    luki.append(abs(lista[i-1] - lista[i]))

longest = count = 1

for i in range(len(luki)):
    if luki[i-1] == luki[i]:
        count += 1
    else:
        count = 1
    max_list.append(count)
    
print(max(max_list)+1)
print("poczatek",lista[max_list.index(max(max_list))-max(max_list)])  
print("koniec",lista[max_list.index(max(max_list))])
  ```

 <a name="kwiecien3"/>
 
Krotnością luki nazywamy liczbę jej wystąpień. Najczęstszą luką nazywamy lukę o największej krotności.
Przykładowo – w ciągu:
5, 2, 7, 10

luka 5 ma krotność 1, a luka 3 ma krotność 2 i wobec tego jest najczęstszą luką.

Podaj krotność najczęstszej luki oraz wartości wszystkich najczęstszych luk w ciągu z pliku dane4.txt.
W przykładzie z zadania 4.2 (ciąg 4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3) krotność najczęstszej luki wynosi 4. Tę krotność mają luki 7 i 3.

  ```python
from collections import Counter

lista,luki = [],[]

with open("dane/dane4.txt") as file:
    for line in file:
        line = int(line.strip())
        lista.append(line)

for i in range(1,len(lista)):
    luki.append(abs(lista[i-1] - lista[i]))

print(Counter(luki))
  ```
  
 # 2019 czerwiec [⬆️](#main)
 
<a name="2019czerwiec1"/>
   
 ```python
def is_prime(x):
    if x > 2:
        for i in range(2,x):
            if x% i == 0:
                return False
        return True
    else: return False

with open("MIN-R2A1P-193_dane/liczby.txt") as file:
    for line in file:
        line = int(line)
        if is_prime(line) and line in range(100,5001):
            print(line)
 ```
 
 <a name="2019czerwiec2"/>
   
 ```python
def is_prime(x):
    if x > 2:
        for i in range(2,x):
            if x% i == 0:
                return False
        return True
    else: return False

with open("MIN-R2A1P-193_dane/pierwsze.txt") as file:
    for line in file:
        line = line.strip()
        liczba = int(line[::-1])
        if is_prime(liczba):
            print(line)
 ```
 
 <a name="2019czerwiec3"/>
   
 ```python
def waga(n=''):
    wynik = 0
    while len(str(n)) > 1:
        for char in n:
            char = int(char)
            wynik += char
        n = str(wynik)
        wynik = 0
    return n

count = 0

with open("MIN-R2A1P-193_dane/pierwsze_przyklad.txt") as file:
    for line in file:
        line = line.strip()
        if waga(line) == '1':
            count+=1
print(count)
 ```
 
  # 2019 maj [⬆️](#main)
W pliku liczby.txt zapisano 500 liczb całkowitych dodatnich po jednej w każdym wierszu. Każda liczba jest z zakresu od 1 do 100 000. 

<a name="2019maj1"/>

Podaj, ile z podanych liczb jest potęgami liczby 3 (czyli liczbami postaci 1 = 3^0, 3 = 3^1, 9 = 3^2 itd.). 

 ```python
 lista = []
count = i = liczba = 0

while liczba < 100000:
    liczba = 3**i
    lista.append(liczba)
    i+=1

with open("Dane_PR/liczby.txt") as file:
    for line in file:
        if int(line) in lista:
            count +=1

print(count)
 ```
 
 <a name="2019maj2"/>

Silnią liczby naturalnej k większej od 0 nazywamy wartość iloczynu 1·2·…·k i oznaczamy przez k!.
Przyjmujemy, że 0!=1. Zatem mamy:
0! = 1,
1! = 1,
2! = 1·2 = 2,
3! = 1·2·3 = 6,
4! = 1·2·3·4 = 24 itd.
Dowolną liczbę naturalną możemy rozbić na cyfry, a następnie policzyć sumę silni jej cyfr. Na przykład dla liczby 343 mamy 3! + 4! + 3! = 6 + 24 + 6 = 36. Podaj, w kolejności ich występowania w pliku liczby.txt, wszystkie liczby, które są równe sumie silni swoich cyfr. 

 ```python
import math
wynik = 0
with open("Dane_PR/liczby.txt") as file:
    for line in file:
        line = line.strip()
        for char in line:
            char = int(char)
            wynik += math.factorial(char)
        if wynik == int(line):
            print(line)
        wynik = 0
 ```
 
 <a name="2019maj3"/>

W pliku liczby.txt znajdź najdłuższy ciąg liczb występujących kolejno po sobie i taki, że największy wspólny dzielnik ich wszystkich jest większy od 1 (innymi słowy: istnieje taka liczba całkowita większa od 1, która jest dzielnikiem każdej z tych liczb). Jako odpowiedź podaj wartość pierwszej liczby w takim ciągu, długość ciągu oraz największą liczbę całkowitą, która jest dzielnikiem każdej liczby w tym ciągu. W pliku z danymi jest tylko jeden taki ciąg o największej długości. 
Uwaga: Możesz skorzystać z zależności NWD(a, b, c) = NWD(NWD(a, b), c). 

 ```python
def NWD(a,b):
    if b > 0:
        return NWD(b,(a%b))
    else:
        return a


lista = [3, 7, 4, 6, 10, 2, 5]

first = NWD(NWD(lista[0],lista[0]+1),lista[0]+2)

for i in range(1,len(lista)):
    if first == NWD(NWD(i,i+1),i+2):
        print(first)
    first = NWD(NWD(i,i+1),i+2)   
'''
with open("Dane_PR/liczby.txt") as file:
    for line in file:
'''
 ```

# 2018 czerwiec [⬆️](#main)
Pliki dane1.txt i dane2.txt zawierają po 1000 wierszy. W każdym wierszu tych plików zapisany jest uporządkowany niemalejąco ciąg dziesięciu liczb całkowitych o wartościach z przedziału 〈0,100〉 , oddzielonych spacjami. 

<a name="e1"/>

Porównaj ciągi zapisane w odpowiadających sobie wierszach w plikach dane1.txt i dane2.txt. Podaj, w ilu wierszach zapisane są ciągi, których ostania liczba jest taka sama. 

 ```python
count = 0
with open("NM_DANE_PR/dane1.txt") as dane1,open("NM_DANE_PR/dane2.txt") as dane2:
    for (a,b) in zip(dane1,dane2):
        a,b = a.strip(),b.strip()
        if a[-3:] == b[-3:]:
            count +=1
print(count)
 ```
 
 <a name="e2"/>

Podaj, ile jest par ciągów (w odpowiadających sobie wierszach plików dane1.txt i dane2.txt) takich, że w jednym i drugim ciągu jest 5 liczb parzystych i 5 liczb nieparzystych. 

 ```python
count = parzyste = parzyste2 =0

with open("NM_DANE_PR/dane1.txt") as dane1,open("NM_DANE_PR/dane2.txt") as dane2:
    for (a,b) in zip(dane1,dane2):
        a,b = a.strip().split(),b.strip().split()
        for i,j in zip(a,b):
            i,j = int(i),int(j)
            if i % 2 == 0:
                parzyste+=1
            if j % 2 == 0:
                parzyste2+=1
        if parzyste == 5 and parzyste2 == 5:
            count+=1
        parzyste = parzyste2 = 0
print(count)

 ```
 
 <a name="e3"/>

Policz, ile jest par ciągów (w odpowiadających sobie wierszach plików dane1.txt i dane2.txt), które utworzone są z takich samych liczb. Liczba powtórzeń takich samych liczb w ciągach może być różna. Wypisz numery wierszy, w których takie pary ciągów się znajdują. 

 ```python
index = 1
with open("NM_DANE_PR/dane1.txt") as dane1,open("NM_DANE_PR/dane2.txt") as dane2:
    for (a,b) in zip(dane1,dane2):
        a = list(set(a.strip().split()))
        b = list(set(b.strip().split()))

        if a == b:
            print(index)
        index += 1
 ```

# 2018 maj , DO POPRAWY [⬆️](#main)

W ramach projektu WEGA naukowcom udało się odczytać sygnały radiowe pochodzące z przestrzeni kosmicznej. Po wstępnej obróbce zapisali je do pliku sygnaly.txt. W pliku sygnaly.txt znajduje się 1000 wierszy. Każdy wiersz zawiera jedno niepuste słowo złożone z wielkich liter alfabetu angielskiego. Długość jednego słowa nie przekracza 100 znaków. 

<a name="2018maj1"/>

Naukowcy zauważyli, że po złączeniu dziesiątych liter co czterdziestego słowa (zaczynając od słowa czterdziestego) otrzymamy pewne przesłanie. Wypisz to przesłanie. Uwaga: Każde co czterdzieste słowo ma co najmniej 10 znaków. 

 ```python
wynik = ""
lista = []
lista2 = []

with open("Dane_PR/przyklad.txt") as file:
    for line in file:
        lista.append(line.strip())

for word in range(39,len(lista),40):
    lista2.append(lista[word])

for line in lista2:
    wynik += line[9]
print(wynik)
 ```
 
 <a name="2018maj2"/>
 
Znajdź słowo, w którym występuje największa liczba różnych liter. Wypisz to słowo i liczbę występujących w nim różnych liter. Jeśli słów o największej liczbie różnych liter jest więcej niż jedno, wypisz pierwsze z nich pojawiające się w pliku z danymi. 


  ```python
from collections import Counter

slownik = dict()

with open("Dane_PR/przyklad.txt") as file:
    for line in file:
        slowo = line.strip()
        line = Counter(list(line.strip()))
        
        for k in line:
            if line[k] > 1:
                line[k] = 1
        slownik[slowo] = sum(line.values())

print({k: v for k, v in sorted(slownik.items(), reverse=True, key = lambda item: item[1])})
 ```
 
W tym zadaniu rozważmy odległość liter w alfabecie – np. litery A i B są od siebie oddalone o 1, A i E o 4, F i D o 2, a każda litera od siebie samej jest oddalona o 0. Wypisz wszystkie słowa, w których każde dwie litery oddalone są od siebie w alfabecie co najwyżej o 10. Słowa wypisz w kolejności występowania w pliku sygnaly.txt, po jednym w wierszu. Na przykład CGECF jest takim słowem, ale ABEZA nie jest (odległość A – Z wynosi 25). 
 
 <a name="2018maj3"/>
 
  ```python
lista,temp  = [],""

with open("Dane_PR/przyklad.txt") as file:
    for line in file:
        line = list(line.strip())
        for i, c in enumerate(line):
            if abs(ord(c) - ord(line[i-1])) <= 10:
                temp += c
            else:
                temp = ""
        lista.append(temp)

try:
    for i in range(len(lista)):
        lista.remove("")
except ValueError:
        for i in lista:
            print(i)
 ```
 
 # 2015 maj (nowa) [⬆️](#main)
 
W pliku liczby.txt znajduje się 1000 liczb naturalnych zapisanych binarnie. Każda liczba zapisana jest w osobnym wierszu.

<a name="bin1"/>

Podaj, ile liczb z pliku liczby.txt ma w swoim zapisie binarnym więcej zer niż jedynek.

 ```python
zera = jedynki = wynik = 0

with open("Dane_PR/liczby.txt") as file:
    for line in file:
        for char in line:
            if char == "0": zera+=1
            elif char == "1": jedynki+=1
        if zera>jedynki:
            wynik+=1
        zera = 0
        jedynki = 0
        
print(wynik)
 ```
 
 <a name="bin2"/>
 
 Podaj, ile liczb w pliku liczby.txt jest podzielnych przez 2 oraz ile liczb jest podzielnych przez 8. 
 
 ```python
przezdwa = przezosiem = 0

with open("Dane_PR/liczby.txt") as file:
    for line in file:
        line = int(line,2)

        if line%2 == 0:
            przezdwa += 1
        if line%8 == 0:
            przezosiem += 1
            
print(przezdwa,"|",przezosiem)
 ```

 <a name="bin3"/>
 
Znajdź najmniejszą i największą liczbę w pliku liczby.txt. Jako odpowiedź podaj numery wierszy, w których się one znajdują. 

 ```python
lista = []

with open("Dane_PR/liczby.txt") as file:
    for line in file:
        lista.append(int(line,2))
        
print(lista.index(max(lista))+1,"|",lista.index(min(lista))+1)
 ```

 
