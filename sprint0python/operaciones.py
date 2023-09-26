fin = "Si"
while fin != "No" :
    print("Programa que contiene operaciones suma , resta, multiplicación y división")


    def ingresar_numero(mensaje):
        while True:
            try:
                numero = int(input(mensaje))
                return numero
            except ValueError:
                print("El valor introducido no es un número. Intenta de nuevo")

    print("Introduzca 2 números: ")
    num1 = ingresar_numero("Primer número: ")
    num2 = ingresar_numero("Segundo número: ")

    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    #El ultimo ejercicio con Listas
    opcion = input("Escoja una de estas opciones : ")
    def sumaNUm( num1 , num2) :
        return print("la suma es: "+str(num1+num2))
    def restaNUm( num1 , num2) :
        return print("la resta es: "+str(num1-num2))
    def multiplicacionNUm( num1 , num2) :
        print("la multiplicación es: "+str(num1*num2))
    def divisionNUm( num1 , num2) :
        print("la división es: "+str(num1/num2))
    if opcion == '1':
        sumaNUm(num1,num2) 
    elif opcion == '2':
        restaNUm(num1,num2)
    elif opcion == '3':
        multiplicacionNUm(num1,num2)
    elif opcion == '4':
        try:
            divisionNUm(num1,num2)
        except ZeroDivisionError:
            print("Trataste de dividir entre cero :( ")

    fin = input("Quieres intentarlo de nuevo? (Si/No)").capitalize()
    while fin != "Si" and fin != "No" :
        fin = input("¿Quieres volver a jugar? (Si/No): ")
        fin = fin.capitalize()

print("Estamos fuera")


