# evaluando valores decimales dentro de un string
edad = input("Introduce tu edad: ")
if edad.isdecimal():
    print("Edad: ", edad)
else:
    print("Edad no valida")
