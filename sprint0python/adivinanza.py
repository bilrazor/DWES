from random import sample

puntos = 0
def primeraAdivinanza():
    global puntos
    print("Primera adivinanza")
    print("¿Si tengo 4 manzanas, me como 3 y me regalan 2, cuántas manzanas tengo?")
    print("a)4")
    print("b)3")
    print("c)2")
    opcion = input('Tu respuesta. Debe ser a->"4", b->"12" o c->"3": ')
    
    while opcion not in ['a', 'b', 'c']:
        print("Introduce una de las opciones validas. Debe ser a ->'4', b ->'12' o c ->'3'.")
        opcion = input('Tu respuesta. Debe ser a ->"4", b ->"12" o c ->"3": ')

    if opcion == 'a':
        puntos += 10
        print("¡Felicidades, acertaste!")
    else:
        print("Inténtalo de nuevo")
        puntos -= 5

    return print("puntos =", puntos)

def segundaAdivinanza():
    global puntos
    print("Segunda adivinanza")
    print("Pablo saco un clavito de la cabeza de pedrito")
    print("¿Que saco pablo?")
    print("a)Una motocierra")
    print("b)Un clavito")
    print("c)A pedrito")
    opcion = input("escoje una de las 3 opciones : ")

    while opcion not in ['a', 'b', 'c']:
        print("Introduce valores correctos")
        opcion = input("escoje una de las 3 opciones : ")

    if opcion == 'b':
        puntos += 10
        print("Felicidades acertasté")
    else:
        puntos -= 5
        print("fallasté se te restarán 5 puntos")
    return print("puntos =", puntos)

def terceraAdivinanza():
    global puntos
    print("Tercera adivinanza")
    print("Tengo 3 gatos uno se llama bolt otro se llama miau y el ultimo black")
    print("¿Cual es el gato negro?")
    print("a)bolt")
    print("b)miau")
    print("c)black")
    opcion = input("escoje una de las 3 opciones : ")

    while opcion not in ['a', 'b', 'c']:
        print("Introduce valores correctos")
        opcion = input("escoje una de las 3 opciones : ")

    if opcion == 'c':
        puntos += 10
        print("Felicidades acertasté")
    else:
        puntos -= 5
        print("fallasté se te restarán 5 puntos")
    return print("puntos =", puntos)

fin = "Si"
while fin != "No":
    print("Se harán 3 adivinanzas")
    print("Espero que puedas acertar todas")
    
    adivinanza = [primeraAdivinanza, segundaAdivinanza, terceraAdivinanza]
    funciones_adivinanza = sample(adivinanza, 2)
  
    for funcion in funciones_adivinanza:
        funcion()
    
    print("Puntos totales", puntos)
    fin = input("¿Quieres volver a jugar? (Si/No): ").capitalize()
    
    puntos = 0
    while fin not in ["Si", "No"]:
        fin = input("¿Quieres volver a jugar? (Si/No): ").capitalize()

print("Estamos fuera")