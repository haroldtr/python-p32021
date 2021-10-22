# Trabajando con listas
'''
Entrada de datos
Salida de datos
Procesos de datos
'''

lista01 = [70, 2, 3, 4, 6]
lista02 = [71, 3, 4, 5, 7]
# print(lista01)

while True:
    n = int(input("Ingresa un valor"))
    elementos = len(lista01)
    if n < elementos:
        print(lista01[n])
    else:
        print("Valor supera la cantidad de elementos")

    s = input("Deseas Salir (y/n)?: ")
    if s.upper() == 'Y':
        print("Gracias por participar...")
        break
lista03 = lista02+lista01
print(lista01+lista02)
print(lista03)
# print(elementos)
# print(lista01[:3])

# lista02 = [1, "2", True, [70, 2, 3, 4, 6], 6]
# print(lista02)
