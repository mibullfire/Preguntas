import tkinter as tk
from tkinter import messagebox
from preguntas import *
from soluciones import *
from collections import namedtuple
import random
import csv

soluciones = namedtuple('Soluciones', 'numero, tema, pregunta, respuestas, correctas')

def leer_fichero(ruta):
    res = []
    with open(ruta, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)
        for numero, tema, pregunta, respuestas, correctas in lector:
            res.append(soluciones(int(numero), tema, pregunta, respuestas.split(';'), correctas.split(';')))
    return res

class QuizApp:
    def __init__(self, root, preguntas):
        self.root = root
        self.root.title("Intentando Aprobar ISSI")
        
        self.preguntas = preguntas
        self.preguntas_filtradas = []
        self.pregunta_actual = None
        self.respuestas_seleccionadas = []
        self.preguntas_mostradas = set()
        
        # Crear widgets de la interfaz
        self.tema_label = tk.Label(root, text="Selecciona un tema:")
        self.tema_label.pack(pady=20)

        self.tema_var = tk.StringVar(root)
        temas = list(set(pregunta.tema for pregunta in preguntas))
        self.tema_menu = tk.OptionMenu(root, self.tema_var, *temas)
        self.tema_menu.pack(pady=20)

        self.tema_button = tk.Button(root, text="Seleccionar Tema", command=self.seleccionar_tema)
        self.tema_button.pack(pady=20)

        self.pregunta_label = tk.Label(root, text="", wraplength=400)
        self.checkbuttons_frame = tk.Frame(root)
        self.respuestas_vars = []
        self.enviar_button = tk.Button(root, text="Enviar Respuesta", command=self.verificar_respuesta)
        self.siguiente_button = tk.Button(root, text="Siguiente Pregunta", command=self.mostrar_pregunta)
        self.resultado_label = tk.Label(root, text="", fg="green")
        
    def seleccionar_tema(self):
        tema_seleccionado = self.tema_var.get()
        self.preguntas_filtradas = [pregunta for pregunta in self.preguntas if pregunta.tema == tema_seleccionado]
        
        # Ocultar los widgets de selección de tema
        self.tema_label.pack_forget()
        self.tema_menu.pack_forget()
        self.tema_button.pack_forget()
        
        # Mostrar los widgets de preguntas
        self.pregunta_label.pack(pady=20)
        self.checkbuttons_frame.pack()
        self.enviar_button.pack(pady=20)
        self.siguiente_button.pack(pady=10)
        self.resultado_label.pack(pady=10)
        
        # Cargar la primera pregunta
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        if len(self.preguntas_mostradas) == len(self.preguntas_filtradas):
            messagebox.showinfo("Fin del Quiz", "No quedan más preguntas.")
            self.root.quit()
            return
        
        while True:
            pregunta = random.choice(self.preguntas_filtradas)
            if pregunta.numero not in self.preguntas_mostradas:
                self.pregunta_actual = pregunta
                self.preguntas_mostradas.add(pregunta.numero)
                break
        
        # Mostrar la pregunta
        self.pregunta_label.config(text=self.pregunta_actual.pregunta)

        # Limpiar las respuestas anteriores
        for widget in self.checkbuttons_frame.winfo_children():
            widget.destroy()

        # Crear variables para las respuestas seleccionadas
        self.respuestas_vars = []
        for respuesta in self.pregunta_actual.respuestas:
            var = tk.IntVar()
            self.respuestas_vars.append(var)
            check = tk.Checkbutton(self.checkbuttons_frame, text=respuesta, variable=var)
            check.pack(anchor='w')

        # Limpiar el resultado anterior
        self.resultado_label.config(text="")

    def verificar_respuesta(self):
        seleccionadas = [self.pregunta_actual.respuestas[i] for i, var in enumerate(self.respuestas_vars) if var.get() == 1]
        
        # Imprimir las respuestas seleccionadas y las correctas en la terminal
        print(f"Respuestas seleccionadas: {seleccionadas}")
        print(f"Respuestas correctas: {self.pregunta_actual.correctas}")
        
        # Asegurarse de que ambas listas estén ordenadas antes de comparar
        if sorted([respuesta[0] for respuesta in seleccionadas]) == sorted([respuesta[0] for respuesta in self.pregunta_actual.correctas]):
            self.resultado_label.config(text="¡Has acertado todo!", fg="green")
        else:
            respuesta_correcta = ', '.join([respuesta[0] for respuesta in self.pregunta_actual.correctas])
            self.resultado_label.config(text=f"Respuestas correctas: {respuesta_correcta}", fg="red")


if __name__ == "__main__":
    # Leer el archivo CSV con las preguntas
    preguntas = leer_fichero('data/solucionario.csv')

    # Crear la ventana principal de la aplicación
    root = tk.Tk()

    # Crear la aplicación de preguntas
    app = QuizApp(root, preguntas)

    # Iniciar el bucle principal de la interfaz gráfica
    root.mainloop()