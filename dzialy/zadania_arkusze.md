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
   
2. 2015 maj

   - [x] [4.1](#bin1)
   - [x] [4.2](#bin2)
   - [x] [4.3](#bin3)
   
3. 2018 czerwiec

   - [x] [4.1](#e1)
   - [x] [4.2](#e2)
   - [x] [4.3](#e3)
 
 # 2020 czerwiec
 
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
 # 2020 kwiecień
 
<a name="kwiecien1"/>
   
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
  
 # 2019 czerwiec
 
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


 # 2015 maj
 
<a name="bin1"/>
W pliku liczby.txt znajduje się 1000 liczb naturalnych zapisanych binarnie. Każda liczba zapisana jest w osobnym wierszu.


 ## Podaj, ile liczb z pliku liczby.txt ma w swoim zapisie binarnym więcej zer niż jedynek.
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
 
 ## Podaj, ile liczb w pliku liczby.txt jest podzielnych przez 2 oraz ile liczb jest podzielnych przez 8. 
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
 
 ## Znajdź najmniejszą i największą liczbę w pliku liczby.txt. Jako odpowiedź podaj numery wierszy, w których się one znajdują. 
 ```python
lista = []

with open("Dane_PR/liczby.txt") as file:
    for line in file:
        lista.append(int(line,2))
        
print(lista.index(max(lista))+1,"|",lista.index(min(lista))+1)
 ```

 # 2018 czerwiec
Pliki dane1.txt i dane2.txt zawierają po 1000 wierszy. W każdym wierszu tych plików zapisany jest uporządkowany niemalejąco ciąg dziesięciu liczb całkowitych o wartościach z przedziału 〈0,100〉 , oddzielonych spacjami. 

<a name="e1"/>

 ## Porównaj ciągi zapisane w odpowiadających sobie wierszach w plikach dane1.txt i dane2.txt. Podaj, w ilu wierszach zapisane są ciągi, których ostania liczba jest taka sama. 
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

 ## Podaj, ile jest par ciągów (w odpowiadających sobie wierszach plików dane1.txt i dane2.txt) takich, że w jednym i drugim ciągu jest 5 liczb parzystych i 5 liczb nieparzystych. 
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

 ## Policz, ile jest par ciągów (w odpowiadających sobie wierszach plików dane1.txt i dane2.txt), które utworzone są z takich samych liczb. Liczba powtórzeń takich samych liczb w ciągach może być różna. Wypisz numery wierszy, w których takie pary ciągów się znajdują. 
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
