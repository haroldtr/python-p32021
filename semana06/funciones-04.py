# recibiendo varios parametros
# pasando argumentos a funcion print

def datosEstudiantes(matricula, nombre, apellido, genero, edad, carrera):
    print('La matricula del estudiante es: \t %s' % matricula)
    print('El nombre del estudiante es: \t %s' % nombre)
    print('El apellido del estudiante es: \t %s' % apellido)
    print('El genero del estudiante es: \t %s' % genero)
    print('La edad del estudiante es: \t %s' % edad)
    print('La carrera del estudiante es: \t %s' % carrera)

    print('El estudiante %s que esta cursando la carrera de %s tiene %s años' %
          (nombre, carrera, edad))


vMatricula = input("Ingresa la matricula")
datosEstudiantes(vMatricula, 'David Jose', 'Tejada', 'Masculino', 18, 'ISC')
