import tkinter as tk
from tkinter import messagebox
import math

class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError("El logaritmo solo funciona con números positivos")
        return math.log(valor)
    
    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticError("La raíz cuadrada no funciona con números negativos")
        return math.sqrt(valor)

class Calculadora:
    def __init__(self):
        self.CalculadoraInt = tk.Tk()
        self.CalculadoraInt.title("6.6 Cálculos Numéricos")
        self.CalculadoraInt.geometry("400x380")
        self.CalculadoraInt.resizable(False, False)
        self.CalculadoraInt.configure(bg="#2C3E50")
        
        self.CalculadoraInt.grid_columnconfigure(0, weight=1)
        self.CalculadoraInt.grid_columnconfigure(1, weight=0)
        self.CalculadoraInt.grid_columnconfigure(2, weight=1)
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        
        titulo = tk.Label(self.CalculadoraInt, 
                         text="CALCULADORA NUMÉRICA", 
                         font=("Arial", 16, "bold"),
                         foreground="#ECF0F1",
                         background="#2C3E50")
        titulo.grid(row=0, column=0, columnspan=3, pady=15)
        
        
        label_entrada = tk.Label(self.CalculadoraInt, 
                                text="Ingrese un número:", 
                                font=("Arial", 10),
                                foreground="#ECF0F1",
                                background="#2C3E50")
        label_entrada.grid(row=1, column=1, pady=10)
        
        self.entrada = tk.Entry(self.CalculadoraInt, 
                               width=20, 
                               font=("Arial", 12),
                               bg="#FFFFFF",
                               justify='center')
        self.entrada.grid(row=2, column=1, pady=5)
        self.entrada.focus()
        
        
        botones_frame = tk.Frame(self.CalculadoraInt, bg="#2C3E50")
        botones_frame.grid(row=3, column=1, pady=15)
        
        self.boton_log = tk.Button(botones_frame, 
                                  text="LOGARITMO(BASE e)", 
                                  command=self.calcular_log,
                                  width=17,
                                  height=2,
                                  font=("Arial", 10, "bold"),
                                  bg="#1B6F34",
                                  fg="white")
        self.boton_log.grid(row=0, column=0, padx=5, pady=5)
        
        self.boton_raiz = tk.Button(botones_frame, 
                                   text="RAÍZ CUADRADA", 
                                   command=self.calcular_raiz,
                                   width=15,
                                   height=2,
                                   font=("Arial", 10, "bold"),
                                   bg="#AE5827",
                                   fg="white")
        self.boton_raiz.grid(row=0, column=1, padx=5, pady=5)
        
        
        label_resultado = tk.Label(self.CalculadoraInt, 
                                  text="RESULTADO:", 
                                  font=("Arial", 11, "bold"),
                                  foreground="#ECF0F1",
                                  background="#2C3E50")
        label_resultado.grid(row=4, column=1, pady=(10, 5))
        
        
        self.resultado = tk.Label(self.CalculadoraInt, 
                                 text="Recuerda ingresar valores validos ;)", 
                                 font=("Arial", 11),
                                 bg="#34495E",
                                 fg="#F39C12",
                                 padx=20,
                                 pady=10,
                                 width=30,
                                 anchor="center")
        self.resultado.grid(row=5, column=1, pady=(5, 10))
        
        
        info_enter = tk.Label(self.CalculadoraInt, 
                             text="Al presionar 'Enter' se calculara la raíz cuadrada", 
                             font=("Arial", 8),
                             foreground="#BDC3C7",
                             background="#2C3E50")
        info_enter.grid(row=6, column=1, pady=5)
        
        
        self.CalculadoraInt.bind('<Return>', lambda event: self.calcular_raiz())
    
    def calcular_log(self):
        try:
            valor = float(self.entrada.get())
            resultado = CalculosNumericos.calcular_logaritmo_neperiano(valor)
            self.resultado.config(text=f"ln({valor}) = {resultado:.4f}", fg="#27AE60")
        except ValueError:
            messagebox.showerror("Error","No se permiten letras o la celda esta vacia, Ingrese solo números.")
            self.resultado.config(text="Error: solo se permiten números.",
                                        fg="#E74C3C")
        except ArithmeticError as e:
            messagebox.showerror("Error", str(e))
    
    def calcular_raiz(self):
        try:
            valor = float(self.entrada.get())
            resultado = CalculosNumericos.calcular_raiz_cuadrada(valor)
            self.resultado.config(text=f"√{valor} = {resultado:.4f}", fg="#27AE60")
        except ValueError:
            messagebox.showerror("Error","No se permiten letras o la celda esta vacia. Ingrese solo números.")
            self.resultado.config(text="Error: solo se permiten números.",
                                        fg="#E74C3C")
        except ArithmeticError as e:
            messagebox.showerror("Error", str(e))


class Main:
    # Metodo de ejecucion principal
    @staticmethod
    def main():
        app = Calculadora()
        app.CalculadoraInt.mainloop()

if __name__ == "__main__":
    Main.main()


