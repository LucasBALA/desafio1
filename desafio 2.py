def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


lista = [1, 1, 1, 2, 3, 3, 5, 6, 7, 8, 8, 9, 10]

lista = remove_repetidos(lista)
print(lista)
