import random

bolaOcho = ["Es cierto",
            "Decididamente es asi",
            "Si, definitivamente",
            "Pregunta confunsa, no se que responder",
            "Pregunta mas tarde estoy cansada",
            "Muy dificil",
            "Mi respuesta es NO"
            ]

pregunta = input("Ingresa una pregunta? ")
print(bolaOcho[random.randint(0, len(bolaOcho)-1)])
