fin = "Si"
while fin != "No" :
    print("Se harán 3 adivinanzas")
    print("Espero que puedas acertar todas")

    print("Primera adivinanza")
    print("¿Si tengo 4 manzanas, me como 3 y me regalan 2, cuántas manzanas tengo?")
    opcion = input('Tu respuesta. Debe ser a->"4", b->"12" o c->"3": ')
    a = 3
    b = 4
    c = 12
    puntos = 0
    while opcion != 'a':
        if opcion == 'b' or opcion == 'c':
            print("Inténtalo de nuevo")
            print("puntos = "+ str(puntos))
        else:
            print("Introduce una de las opciones validas. Debe ser a ->'4', b ->'12' o c ->'3'.")
        
        opcion = input('Tu respuesta. Debe ser a ->"4", b ->"12" o c ->"3": ')

    if opcion == 'a':
        puntos = puntos + 10
        print("¡Felicidades, acertaste!")
        print("puntos = "+ str(puntos))


    print("Segunda adivinanza")
    print("Pablo saco un clavito de la cabeza de pedrito")
    print("¿Que saco pablo?")
    print("a)Una motocierra")
    print("b)Un clavito")
    print("c)A pedrito")
    opcion = input("escoje una de las 3 opciones : ")

    while opcion != 'a' and opcion != 'b' and opcion != 'c':
        print("a)Una motocierra")
        print("b)Un clavito")
        print("c)A pedrito")
        print("introduce valores correctos")
        opcion = input("escoje una de las 3 opciones : ")

    if opcion == 'b' :
        puntos = puntos + 10
        print("Felicidades acertasté")
        print("puntos = "+str(puntos))
    elif opcion == 'a' or opcion == 'c':
        puntos = puntos - 5
        print("fallasté se te restarán 5 puntos")
        print("puntos = "+str(puntos))
 

    print("Tercera adivinanza")
    print("Tengo 3 gatos uno se llama bolt otro se llama miau y el ultimo black")
    print("¿Cual es el gato negro?")
    print("a)bolt")
    print("b)miau")
    print("c)black")
    opcion = input("escoje una de las 3 opciones : ")

    while opcion != 'a' and opcion != 'b' and opcion != 'c':
        print("a)bolt")
        print("b)miau")
        print("c)black")
        print("introduce valores correctos")
        opcion = input("escoje una de las 3 opciones : ")

    if opcion == 'c' :
        puntos = puntos + 10
        print("Felicidades acertasté")
        print("puntos = "+str(puntos))
    elif opcion == 'a' or opcion == 'b':
        puntos = puntos - 5
        print("fallasté se te restarán 5 puntos")
        print("puntos = "+str(puntos))

    print("Puntos totales "+str(puntos))
    fin = input("¿Quieres volver a jugar? (Si/No): ").capitalize()
    while fin != "Si" and fin != "No" :
        fin = input("¿Quieres volver a jugar? (Si/No): ")
        fin = fin.capitalize()
print("estamos fuera")

