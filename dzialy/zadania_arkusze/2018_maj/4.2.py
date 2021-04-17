with open("Dane_PR/przyklad.txt") as file:
    lista = file.read().splitlines()

maxi = 0

for i in range(len(lista)):
    if len(set(lista[i])) > maxi:
        maxi = len(set(lista[i]))
        index = i
print(lista[index], maxi)
