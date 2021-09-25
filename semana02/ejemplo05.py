# ejercicio final
import time

lloviendo = input('Esta lloviendo? Y/N ')

if (lloviendo == 'Y'):
    sombrilla = input('Tengo Sombrilla? Y/N ')
    if (sombrilla == 'Y'):
        print("Salgo a pasear")
    else:
        print("Espero un rato")
        time.sleep(5)
        lloviendo = input('Esta lloviendo? Y/N ')
        if (lloviendo == 'Y'):
            print("Me quedo estudiando Python")
        else:
            print("Salgo a pasear")
else:
    print("Salgo a pasear")
