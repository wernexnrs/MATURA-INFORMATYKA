with open("Dane_PR/sygnaly.txt") as file:
    lista = file.read().splitlines()

for word in lista:
    if all(abs(ord(x) - ord(word[char-1])) < 10 for char in range(1, len(word)) for x in word):
        print(word)