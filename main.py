from src.preguntas import *

if __name__ == "__main__":
    # Leer el archivo CSV con las preguntas
    import os
    import tkinter as tk # Importar la librería tkinter

    # Obtener la ruta absoluta del archivo CSV
    script_dir = os.path.dirname(__file__)
    csv_path = os.path.join(script_dir, 'data/1.csv')

    # Leer el archivo CSV con las preguntas
    preguntas = leer_fichero(csv_path)

    # Crear la ventana principal de la aplicación
    root = tk.Tk()

    # Crear la aplicación de preguntas
    app = QuizApp(root, preguntas)

    # Iniciar el bucle principal de la interfaz gráfica
    root.mainloop()