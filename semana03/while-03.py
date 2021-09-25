# trabajando con con ciclos repetitivos
# ciclo while - primero pregunta y luego ejecuta

username = 'joeli'
password = '123456'
limite = 3
intento = 0

while True:
    print('Por favor ingresa tu usuario')
    vNombre = input()
    print('Por favor ingresa tu contraseña')
    vPassword = input()
    intento = intento + 1

    if intento == limite:
        print(f"Supero el limite de intento {limite}")
        break

    if (username == vNombre.upper()) and (password == vPassword):
        print(f"Bienvenido al sistema")
        break
