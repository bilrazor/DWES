from random import *

jugadas = 0 
winH = 0
winM = 0
while jugadas != 5:
    opciones = ["piedra", "papel", "tijera"]
    jugadas +=  1
    print(f"Jugada numero {jugadas}")
    print("Juego de piedra , papel o tijera")

    print("Solo puedes lanzar piedra , papel o tijera")

    manoH = str(input("lanza tu jugada : ").lower())
    while manoH not in opciones  :
        try:
            manoH = str(input("lanza tu jugada : ").lower())
        except ValueError:
            print("El valor introducido no es un número. Intenta de nuevo")
    
    manoM = choice(opciones)

    print("mano lanzada -> "+manoH)
    print("mano de la maquina lanzada -> "+manoM)

    if manoH == opciones[0] and manoM == opciones[2] or manoH == opciones[1] and manoM == opciones[0] or manoH == opciones[2] and manoM == opciones[1]:
        print("ganasté")
        winH +=  1
    elif manoH == manoM :
        print("empate")
        jugadas -=  1
    else:
        print("perdisté")
        winM +=  1

if winH > winM :
    print("ganasté la partida eres un CRACK")
    print("quedaste "+str(winH)+" - "+str(winM))

else:
    print("perdisté la partida eres un LOSSER")
    print("quedaste "+str(winH)+" - "+str(winM))

