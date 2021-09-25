userName = input('Ingresar usuario ')

if (userName == 'pablo'):
    print('Bienvenido')
    password = int(input('Ingresa pass: '))
    if (password == 123456):
        print('Acceso concedido')
    else:
        print('Acceso denegado')
else:
    print('Usuario Incorrecto')
