# Los datos string a su vez se pueden considerar manejar como listas
# tener pendiente que los datos string no se pueden modificar
# se comportan como datos inmutables

letra = "Actualmente existen dos posibilidades: 1- Pasar la Materia en A. 2- Volver a inscribir la materia"
print(letra)
letra = "Actualmente existen dos posibilidades:\n\t 1- Pasar la Materia en A. \n\t 2- Volver a inscribir la materia"
print(letra)

# segundo ejemplo

print(letra[0])
print(letra[0:11])
print(letra[:11])
print(letra[12:])


contrasena = "123456789"

print('@' in contrasena)

saludos = "Hola Mundo"

print(saludos.isupper())
print(saludos.islower())
print(saludos.istitle())
