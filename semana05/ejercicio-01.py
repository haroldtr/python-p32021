# identificando valores


menor = 50000
mayor = 0
contador = 1

for item in range(0, 4):
    valor1 = int(input("Ingresa valor"))
    if valor1 <= menor:
        menor = valor1

    if valor1 >= mayor:
        mayor = valor1


print(f"El menor es { menor}")
print(f"El mayor es { mayor}")
