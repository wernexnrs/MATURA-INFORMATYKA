<h1 align="center">  Zadania z arkuszy </h1>

1. 2015 maj

   - [x] [4.1](#bin1)
   - [x] [4.2](#bin2)
   - [x] [4.3](#bin3)
   
2. 2018 czerwiec

   - [x] [4.1](#e1)
   - [x] [4.2](#e2)
   - [x] [4.3](#e3)
 
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
