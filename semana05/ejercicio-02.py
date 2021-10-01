print("Ingresa 4 notas con valores entre 0 y 100")

contador = 1
promedio = 0

while True:
    nota = int(input(f"Ingresa la nota {contador} : "))
    contador = contador + 1

    if nota >= 0 and nota <= 100:
        promedio = promedio + nota
    else:
        contador = contador - 1

    if contador > 4:
        contador = 4
        break


print(f"El promedio es {contador}")
print(f"El promedio es {promedio//contador}")
print("Gracias por participar")
