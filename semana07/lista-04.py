# Buscando elementos

utiles = ["Libreta", "Lapicero", "Borra",
          "Sacapunta", "Corrector", "Lapiz", "Mochila"]

# Recorrer una lista
for item in range(len(utiles)):
    # print(f"El indice {item} con el valor {utiles[item]}")
    print(f"{item+1} - {utiles[item]}")

# Buscar elementos
buscar = input("Ingresa un elemento a bsucar: ")

if buscar in utiles:
    print(f"El valor {buscar} se encuentra en la lista")
else:
    print(f"El valor {buscar} no se encuentra en la lista")
