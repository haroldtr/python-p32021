# ordenar por seleccion
import os
os.system("cls")


def Listaorganizar(lista):
    for i in range(1, len(lista)):
        elemento = lista[i]  # 300
        indice = i  # 1
        print(f"Posicion {i} y valores en lista: {lista}")
        while indice > 0 and lista[indice - 1] > elemento:
            lista[indice] = lista[indice-1]
            indice = indice - 1

        lista[indice] = elemento
        # 0 - > 300


lista = [2000, 300, 25, 40, 31, 45, 45, 50, 19]
print(f"Valores sin organizados :  {lista}")
Listaorganizar(lista)
print(f"Valores organizados :  {lista}")

print("Gracias por participar")
