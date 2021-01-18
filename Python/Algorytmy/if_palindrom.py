def if_palindrom(string):
    lista = list(string)
    lista2 = lista[::-1]
    if lista == lista2:
        return True
    return False

string = "ala"

print(if_palindrom(string))
