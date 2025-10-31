import tkinter as tk
from tkinter import messagebox

class Vendedor:
    def __init__(self, nombre, apellidos, edad):
        # Validar la edad antes de asignar
        self.verificar_edad(edad)
        self.verificar_nombre(nombre) 
        self.verificar_nombre(apellidos) 
        self.nombre = nombre   
        self.apellidos = apellidos
        self.edad = edad
    
    def verificar_nombre(self, nombre): 
        if nombre.strip() == "": 
            raise ValueError("Rellene todos los campos")
        if nombre.replace(" ", "").isalpha() == False: 
            raise ValueError("Los campos nombre y apellido solo admite letras")
            
    def verificar_edad(self, edad):
        
        if edad == "" or edad == " ": 
            raise ValueError("Rellene todos los campos")
        edad = int(edad)  
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120") 
        elif edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años") 
     
            
    def imprimir(self)->str:
        texto = f"{self.nombre} {self.apellidos}\n {self.edad} años"
        # messagebox.showinfo("Datos del Vendedor", texto)
        return(texto)
    
class VentanaVendedor:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("6.5 Registro de Vendedor")
        self.ventana.geometry("400x480")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#2C3E50")

        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(2, weight=1)

        self.crear_interfaz()

    def crear_interfaz(self):

        titulo = tk.Label(self.ventana,
                          text="REGISTRO DE VENDEDOR",
                          font=("Arial", 16, "bold"),
                          foreground="#ECF0F1",
                          background="#2C3E50")
        titulo.grid(row=0, column=0, columnspan=3, pady=20)


        label_nombre = tk.Label(self.ventana,
                                text="Nombre:",
                                font=("Arial", 10),
                                foreground="#ECF0F1",
                                background="#2C3E50")
        label_nombre.grid(row=1, column=1, pady=5)
        self.entrada_nombre = tk.Entry(self.ventana,
                                       width=25,
                                       font=("Arial", 12),
                                       bg="#FFFFFF",
                                       justify='center')
        self.entrada_nombre.grid(row=2, column=1, pady=5)


        label_apellidos = tk.Label(self.ventana,
                                   text="Apellido:",
                                   font=("Arial", 10),
                                   foreground="#ECF0F1",
                                   background="#2C3E50")
        label_apellidos.grid(row=3, column=1, pady=5)
        self.entrada_apellidos = tk.Entry(self.ventana,
                                          width=25,
                                          font=("Arial", 12),
                                          bg="#FFFFFF",
                                          justify='center')
        self.entrada_apellidos.grid(row=4, column=1, pady=5)


        label_edad = tk.Label(self.ventana,
                              text="Edad:",
                              font=("Arial", 10),
                              foreground="#ECF0F1",
                              background="#2C3E50")
        label_edad.grid(row=5, column=1, pady=5)
        self.entrada_edad = tk.Entry(self.ventana,
                                     width=25,
                                     font=("Arial", 12),
                                     bg="#FFFFFF",
                                     justify='center')
        self.entrada_edad.grid(row=6, column=1, pady=5)


        botones_frame = tk.Frame(self.ventana, bg="#2C3E50")
        botones_frame.grid(row=7, column=1, pady=20)


        self.boton_crear = tk.Button(botones_frame,
                                     text="CREAR VENDEDOR",
                                     command=self.crear_vendedor,
                                     width=18,
                                     height=2,
                                     font=("Arial", 10, "bold"),
                                     bg="#1B6F34",
                                     fg="white")
        self.boton_crear.grid(row=0, column=0, padx=5, pady=5)


        self.boton_limpiar = tk.Button(botones_frame,
                                       text="LIMPIAR",
                                       command=self.limpiar_informacion,
                                       width=15,
                                       height=2,
                                       font=("Arial", 10, "bold"),
                                       bg="#AE5827",
                                       fg="white")
        self.boton_limpiar.grid(row=0, column=1, padx=5, pady=5)


        self.info_label = tk.Label(self.ventana,
                                   text="Ingrese todos los campos antes de crear un vendedor.",
                                   font=("Arial", 9),
                                   foreground="#BDC3C7",
                                   background="#2C3E50")
        self.info_label.grid(row=9, column=1, pady=(10, 5))


        self.resultado_label = tk.Label(self.ventana,
                                        text="Esperando registro...",
                                        font=("Arial", 11),
                                        bg="#34495E",
                                        fg="#F39C12",
                                        padx=20,
                                        pady=10,
                                        width=30,
                                        anchor="center")
        self.resultado_label.grid(row=8, column=1, pady=(10, 10))


        self.ventana.bind('<Return>', lambda event: self.crear_vendedor())



    def crear_vendedor(self):
        try:
            nombre = self.entrada_nombre.get().strip()
            apellidos = self.entrada_apellidos.get().strip()
            edad = self.entrada_edad.get().strip()

            if not nombre or not apellidos or not edad:
                raise ValueError("Todos los campos son obligatorios.")

            vendedor = Vendedor(nombre, apellidos, edad)
            self.limpiar_informacion()
            # vendedor.imprimir()

            self.resultado_label.config(text=f"Vendedor { vendedor.imprimir()} registrado exitosamente.",
                                        fg="#27AE60")

        except ValueError as error:
            messagebox.showerror("Error", str(error))
            self.resultado_label.config(text="Error: revise los datos ingresados.",
                                        fg="#E74C3C")
        except Exception:
            messagebox.showerror("Error", "Ha ocurrido un error inesperado")
            self.resultado_label.config(text="Error inesperado.",
                                        fg="#E74C3C")

    def limpiar_informacion(self):
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_apellidos.delete(0, tk.END)
        self.entrada_edad.delete(0, tk.END)
        self.resultado_label.config(text="Campos limpiados.",
                                    fg="#F39C12")

class Main:
    # Metodo de ejecucion principal
    @staticmethod
    def main():
        app = VentanaVendedor()
        app.ventana.mainloop()

if __name__ == "__main__":
    Main.main()
