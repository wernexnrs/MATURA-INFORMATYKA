def sort(lista):
    return sorted(lista)

lista = ["C","D","A","O"]

print(sort(lista))

#to jest python po co mam znac rozbudowana wersje..

#przez wstawianie
def sort_poco(lista):
    for i in range(len(lista)):
        mini = i 
        for j in range(i+1, len(lista)): 
            if lista[mini] > lista[j]: 
                mini = j         
        lista[i], lista[mini] = lista[mini], lista[i]
    return lista

print(sort_poco(lista))           
