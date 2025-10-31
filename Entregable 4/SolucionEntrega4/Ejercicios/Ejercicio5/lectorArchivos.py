import tkinter as tk
from tkinter import messagebox
import os

class Archivo:
    # Capturamos la ruta, e inicializamos el atributo de archivo
    def __init__(self, ruta):
        self.archivo = str
        self.archivoNombre= ruta
        # Una vez inicializado se llama a la funcion leer archivo para asignarle al atributo
        # de archivo el contenido de este archivo en cuestion
        self.leerArchivo()

    def leerArchivo(self):
        # Capturamos la ruta actual en la que se esta ejecutando el programa, la cual
        # usaremos como base
        base = os.path.dirname(__file__)
        # Se concatena a la ruta pasada como usuario
        ruta_completa = os.path.join(base, "archivos", f"{self.archivoNombre}.txt")

        # Se abre el archivo
        with open(ruta_completa, "r", encoding="utf-8") as file:
            # Quita saltos de línea y une el texto en una sola cadena
            self.archivo = " ".join(linea.strip() for linea in file if linea.strip())

    def convertirArchivo(self) -> str:
        # Retorna todo el texto en mayúsculas
        return self.archivo.upper()


class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("6.8 - Lectura de archivos")
        self.root.resizable(False, False)
        self.miArchivo = str
        self.frame_actual = None
        self.buscarArchivo()

    def limpiarFrame(self):
        if self.frame_actual:
            self.frame_actual.destroy()

    def buscarArchivo(self):
        self.limpiarFrame()
        self.frame_actual = tk.Frame(self.root, padx=10, pady=10)
        self.frame_actual.pack()

        tk.Label(
            self.frame_actual, text="Consultar Archivo", 
            font=("Arial", 10, "bold")
        ).grid(row=0, columnspan=2, pady=10)

        tk.Label(
            self.frame_actual, text="Nombre Archivo:", pady=3
        ).grid(row=1, column=0, sticky="e")

        self.nombreArchivo = tk.Entry(self.frame_actual)
        self.nombreArchivo.insert(0, "prueba")  # nombre por defecto
        self.nombreArchivo.grid(row=1, column=1)

        tk.Button(
            self.frame_actual,
            text="Buscar",
            command=self.leerArchivo,
            bg="green",
            fg="white",
            font=("Arial", 9, "bold")
        ).grid(row=5, column=0, columnspan=2, pady=10, padx=10)

    def leerArchivo(self):
        try:
            nombre = self.nombreArchivo.get()
            base = os.path.dirname(__file__)
            ruta_completa = os.path.join(base, "archivos", f"{nombre}.txt")

            if not os.path.exists(ruta_completa):
                raise Exception(f"Archivo '{nombre}' no encontrado")

            self.miArchivo = Archivo(nombre)
            self.mostrarArchivo()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrarArchivo(self):
        self.limpiarFrame()
        self.frame_actual = tk.Frame(self.root, padx=10, pady=10)
        self.frame_actual.pack()

        tk.Label(
            self.frame_actual,
            text=f"Información Archivo: {self.miArchivo.archivoNombre}.txt",
            font=("Arial", 10, "bold"),
        ).grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

        tk.Label(
            self.frame_actual, text=self.miArchivo.archivo, 
            pady=3, wraplength=400, justify="center"
        ).grid(row=1, column=0, sticky="w")

        frame_botones = tk.Frame(self.frame_actual)
        frame_botones.grid(row=5, column=0, columnspan=2, pady=15)

        tk.Button(
            frame_botones,
            text="Volver",
            command=self.buscarArchivo,
            bg="green",
            fg="white",
            font=("Arial", 9, "bold"),
            width=12
        ).pack(side="left", padx=10)

        tk.Button(
            frame_botones,
            text="Convertir texto",
            command=self.convertirArchivo,
            bg="blue",
            fg="white",
            font=("Arial", 9, "bold"),
            width=15
        ).pack(side="left", padx=10)

    def convertirArchivo(self):
        self.limpiarFrame()
        self.frame_actual = tk.Frame(self.root, padx=10, pady=10)
        self.frame_actual.pack()

        tk.Label(
            self.frame_actual, text=f"{self.miArchivo.archivoNombre}.txt en Mayúsculas", 
            font=("Arial", 10, "bold")
        ).grid(row=0, columnspan=2, pady=10)

        tk.Label(
            self.frame_actual, text=self.miArchivo.convertirArchivo(), 
            pady=3, 
            wraplength=400,
            justify="center", 
        ).grid(row=1, column=0, sticky="w")

        tk.Button(
            self.frame_actual,
            text="Volver",
            command=self.buscarArchivo,
            bg="green",
            fg="white",
            font=("Arial", 9, "bold")
        ).grid(row=5, column=0, pady=10, padx=10)


class Main:
    @staticmethod
    def main():
        root = tk.Tk()
        app = Interfaz(root)
        root.mainloop()


if __name__ == "__main__":
    Main.main()
