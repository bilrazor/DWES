import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random
import json

# Función para cargar imágenes desde una URL
def cargar_imagen_desde_url(url):
    response = requests.get(url)
    image_data = BytesIO(response.content)
    image = Image.open(image_data)
    photo = ImageTk.PhotoImage(image)
    return photo

# Función para obtener palabras desde un archivo JSON en GitHub
def obtener_palabras(url):
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        raise Exception("Error al cargar las palabras desde la URL.")

# Función para obtener las imágenes del ahorcado desde un archivo JSON
def obtener_imagenes(url):
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        raise Exception("Error al cargar las imágenes desde la URL.")

class JuegoAhorcado:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Ahorcado")

        # Dificultades del juego y carga de palabras e imágenes
        self.dificultades = {"Facil": 5, "Normal": 9, "Dificil": 12}
        self.palabras = obtener_palabras("https://raw.githubusercontent.com/bilrazor/DWES/main/EjercicioExtraAhorcado/resources/palabras.json")
        self.imagenes = obtener_imagenes("https://raw.githubusercontent.com/bilrazor/DWES/main/EjercicioExtraAhorcado/resources/imagenes.json")

        # Inicialización de variables del juego
        self.palabra_secreta = ""
        self.palabra_mostrada = ""
        self.errores = 0
        self.letras_introducidas = set()

        # Crear la interfaz del juego
        self.crear_interfaz()

    def crear_interfaz(self):
        # Botones para seleccionar la dificultad
        for dificultad in self.dificultades.keys():
            boton = tk.Button(self.root, text=dificultad, command=lambda d=dificultad: self.iniciar_juego(d))
            boton.pack()

        # Etiqueta para mostrar la imagen del ahorcado
        self.label_imagen = tk.Label(self.root)
        self.label_imagen.pack()

        # Etiqueta para mostrar la palabra
        self.label_palabra = tk.Label(self.root, font=('Helvetica', 18))
        self.label_palabra.pack()

        # Campo de entrada para la letra
        self.entry_letra = tk.Entry(self.root)
        self.entry_letra.pack()
        self.entry_letra.bind("<Return>", self.procesar_entrada)

    def iniciar_juego(self, dificultad):
        # Iniciar un nuevo juego
        self.palabra_secreta = random.choice(self.palabras[dificultad]).upper()
        self.palabra_mostrada = "_" * len(self.palabra_secreta)
        self.errores = 0
        self.letras_introducidas.clear()
        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        # Actualizar la imagen y la palabra mostrada
        url_imagen = self.imagenes[str(self.errores)]
        imagen_ahorcado = cargar_imagen_desde_url(url_imagen)
        self.label_imagen.configure(image=imagen_ahorcado)
        self.label_imagen.image = imagen_ahorcado

        self.label_palabra.config(text=" ".join(self.palabra_mostrada))

    def procesar_entrada(self, event=None):
        # Procesar la letra introducida por el usuario
        letra = self.entry_letra.get().upper()
        self.entry_letra.delete(0, tk.END)

        if letra and letra not in self.letras_introducidas and len(letra) == 1 and letra.isalpha():
            self.letras_introducidas.add(letra)
            if letra in self.palabra_secreta:
                self.palabra_mostrada = "".join([letra if self.palabra_secreta[i] == letra else self.palabra_mostrada[i] for i in range(len(self.palabra_secreta))])
            else:
                self.errores += 1

            self.actualizar_interfaz()
            self.verificar_estado_juego()

    def verificar_estado_juego(self):
        # Comprobar si el juego ha terminado y mostrar un mensaje
        if "_" not in self.palabra_mostrada:
            messagebox.showinfo("Ahorcado", "¡Has ganado!")
            self.iniciar_juego(random.choice(list(self.dificultades.keys())))
        elif self.errores >= 6:
            messagebox.showinfo("Ahorcado", f"Has perdido. La palabra era: {self.palabra_secreta}")
            self.iniciar_juego(random.choice(list(self.dificultades.keys())))
