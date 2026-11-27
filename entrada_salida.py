import tkinter as tk
from tkinter import filedialog


def seleccionar_archivo(titulo="Seleccionar archivo", tipos_archivo=None):
    """Abre el explorador de archivos y devuelve la ruta elegida, o None si se cancela."""
    if tipos_archivo is None:
        tipos_archivo = [("Archivos de texto", "*.txt")]

    root = tk.Tk()
    root.withdraw()  
    root.attributes("-topmost", True)  

    ruta = filedialog.askopenfilename(
        title=titulo,
        filetypes=tipos_archivo,
    )

    root.destroy()  
    return ruta or None


def validar():
    """Verifica que el archivo .txt seleccionado no esté vacío ni tenga solo espacios."""
    while True:
        ruta = seleccionar_archivo()
        if ruta is None:
            print("No se seleccionó ningún archivo.")
            while True:
                opcion = input("¿Quieres salir del programa (s) o continuar (c)? ").strip().lower()
                if opcion == "s":
                    print("Saliendo del programa...")
                    return None
                if opcion == "c":
                    break
                print("Opción no válida. Escribe 's' para salir o 'c' para continuar.")
            continue

        with open(ruta, "r", encoding="utf-8") as archivo:
            texto = archivo.read()

        if texto.strip() == "":
            print("Texto no admitido: el archivo está vacío.")
        else:
            return texto