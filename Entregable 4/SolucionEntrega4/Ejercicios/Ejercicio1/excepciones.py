import tkinter as tk
from tkinter import messagebox

class ManejoExcepciones:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("6.4 Demostración de manejo de Excepciones")
        self.ventana.geometry("450x350")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#2C3E50")

        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(2, weight=1)

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = tk.Label(self.ventana,
                          text="DEMO DE MANEJO DE EXCEPCIONES",
                          font=("Arial", 16, "bold"),
                          foreground="#ECF0F1",
                          background="#2C3E50")
        titulo.grid(row=0, column=0, columnspan=3, pady=20)

        subtitulo = tk.Label(self.ventana,
                             text="Selecciona un bloque TRY para ejecutar:",
                             font=("Arial", 11),
                             foreground="#BDC3C7",
                             background="#2C3E50")
        subtitulo.grid(row=1, column=0, columnspan=3, pady=10)

        botones_frame = tk.Frame(self.ventana, bg="#2C3E50")
        botones_frame.grid(row=2, column=1, pady=20)

        self.boton_primer_try = tk.Button(botones_frame,
                                          text="PRIMER TRY",
                                          command=self.primer_try,
                                          width=18,
                                          height=2,
                                          font=("Arial", 10, "bold"),
                                          bg="#1B6F34",
                                          fg="white")
        self.boton_primer_try.grid(row=0, column=0, padx=10, pady=5)

        self.boton_segundo_try = tk.Button(botones_frame,
                                           text="SEGUNDO TRY",
                                           command=self.segundo_try,
                                           width=18,
                                           height=2,
                                           font=("Arial", 10, "bold"),
                                           bg="#AE5827",
                                           fg="white")
        self.boton_segundo_try.grid(row=0, column=1, padx=10, pady=5)

        info_label = tk.Label(self.ventana,
                              text="Cada botón ejecuta un bloque TRY/EXCEPT/FINALLY con diferentes excepciones.",
                              font=("Arial", 9),
                              foreground="#BDC3C7",
                              background="#2C3E50",
                              wraplength=350,
                              justify="center")
        info_label.grid(row=4, column=0, columnspan=3, pady=(20, 5))

        self.resultado_label = tk.Label(self.ventana,
                                        text="Esperando ejecución...",
                                        font=("Arial", 11),
                                        bg="#34495E",
                                        fg="#F39C12",
                                        padx=20,
                                        pady=10,
                                        width=35,
                                        anchor="center")
        self.resultado_label.grid(row=3, column=0, columnspan=3, pady=(10, 15))

        

    def primer_try(self):

        try:
            messagebox.showinfo("Procesando petición","Ingresando al primer caso de prueba (división por cero)")
            cociente = 10000 / 0  
            # lo siguiente en el bloque no se ejecuta
            messagebox.showinfo("Procesando información","Después de la división (1000/0)")
        except ZeroDivisionError:
            messagebox.showerror("Error","División por cero")
        finally:
            messagebox.showinfo("Finalización Ejecución","Ingresando al primer finally")
            self.resultado_label.config(text="Excepcion 1 ejecutada: División entre 0 indefinida.", fg="#FF0000")

    def segundo_try(self):
        try:
            messagebox.showinfo("Procesando petición","Ingresando al segundo caso de prueba")
            objeto = None
            objeto.toString()  
            messagebox.showinfo("Procesando información","Imprimiendo objeto")
        except ZeroDivisionError:
            messagebox.showerror("Error","División por cero")
        except Exception as e:
            messagebox.showerror("Error","Ocurrió una excepción")
        finally:
            messagebox.showinfo("Finalización Ejecución","Ingresando al segundo finally")
            self.resultado_label.config(text="Excepcion 2 ejecutada: operación \nobjeto.toString() ivalida.", fg="#FF0000")
            
class Main:
    @staticmethod
    def main():
        app = ManejoExcepciones()
        app.ventana.mainloop()

if __name__ == "__main__":
    Main.main()
