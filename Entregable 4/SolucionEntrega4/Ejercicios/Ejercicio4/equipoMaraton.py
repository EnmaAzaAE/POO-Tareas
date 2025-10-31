# Se importa la librería para las expresiones regulares
import re
# Se importa la librería para la gestión de interfaces gráficas
import tkinter as tk
from tkinter import messagebox

class Equipo:
    def __init__(self, nombre: str, universidad: str, lenguaje: str):
        self.nombre = nombre
        self.universidadRepresentacion = universidad
        self.lenguajeProgramacion = lenguaje
        # El tamaño del equipo se inicializa en 0
        self.nIntegrantes = 0
        self.integrantes = []

    # Método para definir si un equipo está lleno
    def equipoLleno(self) -> bool:
        return self.nIntegrantes == 3

    # Método para agregar programador
    def agregarProgramador(self, programador):
        self.integrantes.append(programador)
        self.nIntegrantes += 1

# Se define una clase para los programadores
class Programador:
    def __init__(self, nombre: str, apellido: str, contrasena: str):
        self.nombre = nombre
        self.apellido = apellido
        self.contrasena = contrasena

    # Método estático para validar info desde interfaz
    @staticmethod
    def validarInfo(nombre: str, apellido: str):
        if len(nombre) > 20 or len(apellido) > 20:
            raise Exception("Nombre o Apellido inválidos, tienen más de 20 caracteres")
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", nombre):
            raise Exception(f"Nombre {nombre} inválido, solo se admiten letras")
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", apellido):
            raise Exception(f"Apellido {apellido} inválido, solo se admiten letras")

    # Método para validar contraseña
    @staticmethod
    def validarContrasena(contrasena: str, validacion: str):
        patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9])(?!.*\s).{8,}$'
        if contrasena != validacion:
            raise Exception("Las contraseñas no coinciden")
        if not re.fullmatch(patron, contrasena):
            raise Exception("Contraseña inválida. Debe tener al menos 8 caracteres, incluir minúsculas, mayúsculas, números y símbolos, y no contener espacios.")


class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("6.7 - Equipo Maratón Programación")
        self.root.resizable(False, False)

        # Aquí guardaremos la instancia de equipo creada
        self.miEquipo = None
        # Este será el contenedor que cambia según la etapa (formulario o resumen)
        self.frame_actual = None

        # Mostramos primero el formulario para crear el equipo
        self.mostrarVentanaEquipo()

    # Método que elimina el frame anterior y crea uno nuevo
    def limpiarFrame(self):
        if self.frame_actual:
            self.frame_actual.destroy()

    def mostrarVentanaEquipo(self):
        self.limpiarFrame()
        self.frame_actual = tk.Frame(self.root, padx=10, pady=10)
        self.frame_actual.pack()

        tk.Label(self.frame_actual, text="CREAR EQUIPO", font=("Arial", 10, "bold")).grid(row=0, columnspan=2, pady=10)
        tk.Label(self.frame_actual, text="Nombre:", pady=3).grid(row=1, column=0, sticky="e")
        tk.Label(self.frame_actual, text="Universidad:", pady=3).grid(row=2, column=0, sticky="e")
        tk.Label(self.frame_actual, text="Lenguaje:", pady=3).grid(row=3, column=0, sticky="e")

        self.nombreEquipo = tk.Entry(self.frame_actual)
        self.universidad = tk.Entry(self.frame_actual)
        self.lenguaje = tk.Entry(self.frame_actual)

        self.nombreEquipo.grid(row=1, column=1)
        self.universidad.grid(row=2, column=1)
        self.lenguaje.grid(row=3, column=1)

        tk.Button(self.frame_actual, text="Crear equipo", font=("Arial", 9, "bold"), bg="green", fg="white", command=self.crearEquipo).grid(row=4, columnspan=2, pady=10)

    def crearEquipo(self):
        try:
            nombre = self.nombreEquipo.get()
            universidad = self.universidad.get()
            lenguaje = self.lenguaje.get()
            if not nombre or not universidad or not lenguaje:
                raise Exception("Debe llenar todos los campos")

            self.miEquipo = Equipo(nombre, universidad, lenguaje)
            messagebox.showinfo("Éxito", f"Equipo '{nombre}' creado correctamente")
            self.formIntegrantes()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def formIntegrantes(self):
        self.limpiarFrame()
        self.root.title(f"Equipo {self.miEquipo.nombre}")
        self.frame_actual = tk.Frame(self.root, padx=10, pady=10)
        self.frame_actual.pack(expand=True)

        tk.Label(self.frame_actual, text=f"Agregar Integrantes ({self.miEquipo.nIntegrantes}/3)", font=("Arial", 10, "bold")).grid(row=0, columnspan=2, pady=5)
        tk.Label(self.frame_actual, text="Nombre:", pady=3).grid(row=1, column=0, sticky="e")
        tk.Label(self.frame_actual, text="Apellido:", pady=3).grid(row=2, column=0, sticky="e")
        tk.Label(self.frame_actual, text="Contraseña:", pady=3).grid(row=3, column=0, sticky="e")
        tk.Label(self.frame_actual, text="Validar contraseña:", pady=3).grid(row=4, column=0, sticky="e")

        self.nombreProg = tk.Entry(self.frame_actual)
        self.apellidoProg = tk.Entry(self.frame_actual)
        self.contraProg = tk.Entry(self.frame_actual)
        self.validarProg = tk.Entry(self.frame_actual)

        self.nombreProg.grid(row=1, column=1)
        self.apellidoProg.grid(row=2, column=1)
        self.contraProg.grid(row=3, column=1)
        self.validarProg.grid(row=4, column=1)

        tk.Button(
            self.frame_actual,
            text="Agregar programador",
            command=self.agregarProgramador,
            bg="green",
            fg="white",
            font=("Arial", 9, "bold")
        ).grid(row=5, column=1, pady=10, padx=10)
        if self.miEquipo.nIntegrantes>=2:
            tk.Button(
                self.frame_actual,
                text="Ver equipo",
                command=self.mostrarInfo,
                bg="cyan",
                fg="black",
                font=("Arial", 9, "bold")
            ).grid(row=5, column=0, pady=10, padx=10)

    def agregarProgramador(self):
        try:
            nombre = self.nombreProg.get()
            apellido = self.apellidoProg.get()
            contrasena = self.contraProg.get()
            validacion = self.validarProg.get()

            # Validaciones
            Programador.validarInfo(nombre, apellido)
            Programador.validarContrasena(contrasena, validacion)

            # Crear y agregar programador
            nuevo = Programador(nombre, apellido, contrasena)
            self.miEquipo.agregarProgramador(nuevo)

            messagebox.showinfo("Éxito", f"Programador {nombre} agregado correctamente ({self.miEquipo.nIntegrantes}/3)")

            self.formIntegrantes()


            # Si el equipo está lleno, pasar a resumen
            if self.miEquipo.equipoLleno():
                raise Exception("EquipoLleno")

        except Exception as e:
            if str(e)=="EquipoLleno":
                messagebox.showinfo("Equipo completo", "El equipo ya tiene 3 integrantes.")
                self.mostrarInfo()
            else:
                messagebox.showerror("Error", str(e))   
            


    def mostrarInfo(self):
        self.limpiarFrame()
        self.frame_actual = tk.Frame(self.root, padx=10, pady=10)
        self.frame_actual.pack(expand=True)

        tk.Label(self.frame_actual, text=f"Info Equipo", font=("Arial", 10, "bold")).pack(pady=5)
        tk.Label(self.frame_actual, text=f"Nombre: {self.miEquipo.nombre}").pack()
        tk.Label(self.frame_actual, text=f"Universidad: {self.miEquipo.universidadRepresentacion}").pack()
        tk.Label(self.frame_actual, text=f"Lenguaje: {self.miEquipo.lenguajeProgramacion}").pack()

        tk.Label(self.frame_actual, text="Info Integrantes:", font=("Arial", 10, "bold")).pack(pady=8)

        if self.miEquipo.integrantes:
            for p in self.miEquipo.integrantes:
                tk.Label(self.frame_actual, text=f"- {p.nombre} {p.apellido}").pack()
        else:
            tk.Label(self.frame_actual, text="(Sin integrantes aún)").pack()
        if self.miEquipo.nIntegrantes<3:
            tk.Button(
                self.frame_actual,
                text="Agregar más integrantes", 
                bg="green",
                fg="white",
                font=("Arial", 9, "bold"),
                command=self.formIntegrantes).pack(pady=10)

# Clase principal
class Main:
    # Metodo de ejecucion principal
    @staticmethod
    def main():
        root = tk.Tk()
        app= Interfaz(root)
        root.mainloop()


if __name__ == "__main__":
    Main.main()
