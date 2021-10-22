# lista de nombres
# nUsername1 = "ayendri"
# nUsername2 = "bibeli"
# nUsername3 = "brian"
# nUsername4 = "cesarina"

# print("Lista de usuarios capturados por teclado")
# print(
#     f"No. 1 {nUsername1} No. 2 {nUsername2} No. 3 {nUsername3} No. 4 {nUsername4}")

# usando listas
nUsername = []
while True:
    nombre = input("Ingresa un nombre de usuario (escribe Y para terminar)")
    if nombre.upper() == "Y":
        print("Gracias por participar...")
        break
    else:
        # concatenando a la lista el valor capturado
        nUsername = nUsername + [nombre]

print("Los usuarios registrados son:")
for item in nUsername:
    print(f"{item}")
