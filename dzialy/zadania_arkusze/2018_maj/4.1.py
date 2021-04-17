res = ""

with open("Dane_PR/przyklad.txt") as file:
    lista = file.read().splitlines()

for i in range(39, len(lista) + 1, 40):
    res += lista[i][9]

print(res)