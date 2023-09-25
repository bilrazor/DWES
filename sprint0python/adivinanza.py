print("¿Si tengo 4 manzanas, me como 3 y me regalan 2, cuántas manzanas tengo?")
opcion = input('Tu respuesta. Debe ser "4", "12" o "3": ')

while opcion != '3':
    if opcion == '4' or opcion == '12':
        print("Inténtalo de nuevo")
    else:
        print("Respuesta incorrecta. Debe ser '4', '12' o '3'.")
    
    opcion = input('Tu respuesta. Debe ser "4", "12" o "3": ')

print("¡Felicidades, acertaste!")