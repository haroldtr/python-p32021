# Trabajando con ciclos for
import random

# valor = int(input('Introduce un numero'))
valor = random.randint(1, 6)

for item in range(1, 13):
    print(f"{item} X {valor} = {item*valor}")
