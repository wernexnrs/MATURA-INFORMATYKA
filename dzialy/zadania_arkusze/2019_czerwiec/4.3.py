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
            count += 1
print(count)