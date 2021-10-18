# recibiendo parametros

# Declaracion de Funciones
def hola(nombre):
    print(f"Hola {nombre}")


def sumar(a, b):
    # imprimir valor
    resultado = a + b
    print(f"El resultado de la suma {resultado}")


def restar(a, b):
    # retornar valor
    resultado = a - b
    return(resultado)


# Cuerpo del Programa
# vNombre = input("Ingresa un nombre: ")
# hola(vNombre)

vValor1 = int(input("Ingresa un valor: "))
operacion = input()

if operacion.upper() == 'D':
    while True:
        vValor2 = int(input("Ingresa un valor: "))
        if vValor2 >= 1:
            break
else:
    vValor2 = int(input("Ingresa un valor: "))

# sumar(vValor1, vValor2)

vResultado = restar(vValor2, vValor1)
print(f"El resultado de la resta es {vResultado}")
