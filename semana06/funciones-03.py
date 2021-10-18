# manejo de excepciones
def dividir(valor1, valor2):
    try:
        return (valor1 / valor2)
    except ZeroDivisionError:
        print('Error 001: Imposible dividir entre cero')
        return ('###')


vNumero1 = 4
vNumero2 = 0

print(f"El resultado es {dividir(vNumero1, vNumero2)}")
