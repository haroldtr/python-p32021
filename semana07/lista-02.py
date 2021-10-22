# recorriendo una lista
# usuario -> 1 administrador | 2 usuario normal

usuario = 1
lista = [2, 5, 4, 10]

for item in lista:
    if usuario == 1:
        print(item)
    else:
        if item == 4:
            print("Usuario no tiene privilegios para ver esta opcion")
        else:
            print(item)
