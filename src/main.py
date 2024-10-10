from preguntas import *

if __name__ == "__main__":
    # Leer el archivo CSV con las preguntas
    preguntas = leer_fichero('data/solucionario.csv')

    # Crear la ventana principal de la aplicación
    root = tk.Tk()

    # Crear la aplicación de preguntas
    app = QuizApp(root, preguntas)

    # Iniciar el bucle principal de la interfaz gráfica
    root.mainloop()