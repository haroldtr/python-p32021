# Trabajando con ciclos for
# import random

# valor = int(input('Introduce un numero'))
# valor = random.randint(1, 6)

for item1 in range(1, 3):
    for item2 in range(1, 13):
        print(f"{item2} X {item1} = {item1*item2}")
    print("------")
