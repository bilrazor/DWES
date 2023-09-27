from random import choice
from os import path


fin = "Si"
while fin != "No":
    print("----------Juego del ahorcado ----------")
    print("Nivel de dificultad")
    print("1)Facil")
    print("2)Medio")
    print("3)Dificil")
    opcion = input("Escoja la dificultad del juego : ")

    directorio = path.dirname(path.abspath(__file__))
    archivo = path.join(directorio, "palabras.txt")

    palabras_por_dificultad = {
        "Facil": [],
        "Normal": [],
        "Dificil": []
    }

    with open(archivo, 'r') as file:
        dificultad_actual = None
        for linea in file:
            linea = linea.strip()
            if linea in palabras_por_dificultad:
                dificultad_actual = linea
            else:
                palabras_por_dificultad[dificultad_actual].append(linea)

    if opcion == '1':
        palabras = palabras_por_dificultad['Facil']
    elif opcion == '2':
        palabras = palabras_por_dificultad['Normal']
    elif opcion == '3':
        palabras = palabras_por_dificultad['Dificil']
    else:
        print("Opción inválida")
        exit()

    adivinarP = choice(palabras) 
    palabra_oculta = ['_'] * len(adivinarP)
    intentos = 6

    print(" ".join(palabra_oculta))

    while '_' in palabra_oculta and intentos > 0:
        letra = input("Introduza una letra: ")
        acertado = False

        for i, letr in enumerate(adivinarP):
            if letr == letra:
                palabra_oculta[i] = letra
                acertado = True

        if not acertado:
            intentos -= 1
            print(f"Letra incorrecta. Quedan {intentos} intentos.")

        print(" ".join(palabra_oculta))

    if '_' not in palabra_oculta:
        print("¡Felicidades! Has adivinado la palabra.")
    else:
        print(f"Lo siento, la palabra era {adivinarP}.")
    fin = ""
    while fin not in ["Si", "No"]:
        fin = input("¿Quieres volver a jugar? (Si/No): ").capitalize()

print("Estamos fuera")
 

