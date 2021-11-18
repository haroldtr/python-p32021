# lista de invitados y lo que deben traer

invitados = {'Juan': {'manzana': 5, 'uvas': 2},
             'Marifer': {'jugos': 2, 'panes': 4},
             'Nixon': {'jugos': 2, 'manzana': 3},
             }

# print(invitados)


def totalAlimentos(invitado, alimento):
    numAlimentos = 0
    for k, v in invitados.items():
        numAlimentos = numAlimentos + v.get(alimento, 0)
    return numAlimentos


print('Numero de cosas que traen los invitados')
print(' - Manzanas ' + str(totalAlimentos(invitados, 'manzana')))
print(' - Uvas ' + str(totalAlimentos(invitados, 'uvas')))
print(' - Jugo ' + str(totalAlimentos(invitados, 'jugos')))
print(' - Panes ' + str(totalAlimentos(invitados, 'panes')))
print(' - Refresco ' + str(totalAlimentos(invitados, 'refresco')))
