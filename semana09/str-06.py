# listado de articulos
def ListaCompra(articulosDic, izquierda, derecha):
    print('Listado de compra'.center(izquierda+derecha, '-'))
    for x, y in articulosDic.items():
        print(x.ljust(izquierda, '.') + str(y).rjust(derecha, '.'))

# trabajando con archivos


def ArchivoCompra(articulosDic, izquierda, derecha):
    f = open('listado3.txt', 'w')
    f.write('Listado de compra\n'.center(izquierda+derecha, '-'))
    for x, y in articulosDic.items():
        f.write(x.ljust(izquierda, '.') + str(y).rjust(derecha)+'\t\n')
    f.close()


articulosComprar = {'Pan': 4, 'Mayonesa': 1,
                    'Jamon': 2, 'Queso': 1, 'Refresco': 1}

# ListaCompra(articulosComprar, 10, 5)
ArchivoCompra(articulosComprar, 10, 5)
