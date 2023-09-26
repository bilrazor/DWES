from operaciones import *


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

    fin = input("¿Quieres intentarlo de nuevo? (Si/No)").capitalize()
    while fin != "Si" and fin != "No" :
        fin = input("¿Quieres intentarlo de nuevo? (Si/No): ")
        fin = fin.capitalize()

print("Estamos fuera")


