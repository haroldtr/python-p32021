# Agenda de cumpleaños

cumpleanos = {'brian': '14-Oct', 'gabriela': '12-May', 'joel': '07-Abr'}

while True:
    print('Ingrese el un nombre: (Espacio en blanco para cerrar el programa)')
    nombre = input()
    if nombre == '':
        print('Gracias por usar el programa')
        break

    if nombre in cumpleanos:
        # si encuentra el nombre lo muestra en pantalla
        print(f"El {cumpleanos[nombre]} cumple años {nombre}")
    else:
        # de lo contrario lo agrega
        print(f"No tenemos registrado el cumpleaños de {nombre}")
        print('Ingrese la fecha de nacimiento:')
        cDia = input()
        cumpleanos[nombre] = cDia
        print("La base de datos fue actualizada")
