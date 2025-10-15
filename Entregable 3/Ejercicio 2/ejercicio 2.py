import math
import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod



class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_volumen(self):
        pass
    
    @abstractmethod
    def calcular_superficie(self):
        pass

class Cilindro(FiguraGeometrica):
    def __init__(self, radio=0, altura=0):
        self.radio = radio
        self.altura = altura
    
    def calcular_volumen(self):
        return math.pi * (self.radio ** 2) * self.altura
    
    def calcular_superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)

class Esfera(FiguraGeometrica):
    def __init__(self, radio=0):
        self.radio = radio
    
    def calcular_volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)
    
    def calcular_superficie(self):
        return 4 * math.pi * (self.radio ** 2)

class Piramide(FiguraGeometrica):
    def __init__(self, base=0, altura=0, apotema=0):
        self.base = base
        self.altura = altura
        self.apotema = apotema
    
    def calcular_volumen(self):
        return (1/3) * (self.base ** 2) * self.altura
    
    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lateral = 2 * self.base * self.apotema
        return area_base + area_lateral


class VentanaCilindro:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Cilindro - Cálculos")
        self.ventana.geometry("400x400")
        self.ventana.configure(bg='#E8F5E8')
        self.ventana.resizable(False, False)
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        
        tk.Label(self.ventana, text="CILINDRO", font=("Arial", 16, "bold"), 
                bg='#E8F5E8', fg='#2E7D32').pack(pady=10)
        
        
        tk.Label(self.ventana, text="Ingrese radio y altura en centímetros",
                font=("Arial", 10), bg='#E8F5E8', fg='#555').pack(pady=5)
        
        
        frame_entradas = tk.Frame(self.ventana, bg='#E8F5E8')
        frame_entradas.pack(pady=15)
        
        tk.Label(frame_entradas, text="Radio (cm):", font=("Arial", 10), 
                bg='#E8F5E8').grid(row=0, column=0, padx=10, pady=8, sticky='e')
        self.entry_radio = tk.Entry(frame_entradas, width=12, font=("Arial", 10), justify='center')
        self.entry_radio.grid(row=0, column=1, padx=10, pady=8)
        
        tk.Label(frame_entradas, text="Altura (cm):", font=("Arial", 10), 
                bg='#E8F5E8').grid(row=1, column=0, padx=10, pady=8, sticky='e')
        self.entry_altura = tk.Entry(frame_entradas, width=12, font=("Arial", 10), justify='center')
        self.entry_altura.grid(row=1, column=1, padx=10, pady=8)
        
        
        boton_calcular = tk.Button(self.ventana, text="CALCULAR", 
                                  command=self.calcular,
                                  font=("Arial", 11, "bold"),
                                  bg='#4CAF50', fg='white',
                                  width=12, height=1)
        boton_calcular.pack(pady=15)
        
        
        frame_resultados = tk.Frame(self.ventana, bg='#C8E6C9', relief='raised', bd=1)
        frame_resultados.pack(pady=10, padx=20, fill='x')
        
        tk.Label(frame_resultados, text="RESULTADOS:", font=("Arial", 11, "bold"), 
                bg='#C8E6C9').pack(pady=8)
        
        self.label_volumen = tk.Label(frame_resultados, text="Volumen: ---", 
                                     font=("Arial", 10), bg='#C8E6C9')
        self.label_volumen.pack(pady=3)
        
        self.label_superficie = tk.Label(frame_resultados, text="Superficie: ---", 
                                        font=("Arial", 10), bg='#C8E6C9')
        self.label_superficie.pack(pady=3)
    
    def calcular(self):
        try:
            radio = float(self.entry_radio.get())
            altura = float(self.entry_altura.get())
            
            if radio <= 0 or altura <= 0:
                messagebox.showerror("Error", "Los valores deben ser mayores a cero")
                return
            
            cilindro = Cilindro(radio, altura)
            volumen = cilindro.calcular_volumen()
            superficie = cilindro.calcular_superficie()
            
            self.label_volumen.config(text=f"Volumen: {volumen:.2f} cm³")
            self.label_superficie.config(text=f"Superficie: {superficie:.2f} cm²")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

class VentanaEsfera:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Esfera - Cálculos")
        self.ventana.geometry("400x350")
        self.ventana.configure(bg='#E3F2FD')
        self.ventana.resizable(False, False)
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        
        tk.Label(self.ventana, text="ESFERA", font=("Arial", 16, "bold"), 
                bg='#E3F2FD', fg='#1565C0').pack(pady=10)
        
        
        tk.Label(self.ventana, text="Ingrese el radio en centímetros",
                font=("Arial", 10), bg='#E3F2FD', fg='#555').pack(pady=5)
        
        
        frame_entradas = tk.Frame(self.ventana, bg='#E3F2FD')
        frame_entradas.pack(pady=15)
        
        tk.Label(frame_entradas, text="Radio (cm):", font=("Arial", 10), 
                bg='#E3F2FD').grid(row=0, column=0, padx=10, pady=8, sticky='e')
        self.entry_radio = tk.Entry(frame_entradas, width=12, font=("Arial", 10), justify='center')
        self.entry_radio.grid(row=0, column=1, padx=10, pady=8)
        
        
        boton_calcular = tk.Button(self.ventana, text="CALCULAR", 
                                  command=self.calcular,
                                  font=("Arial", 11, "bold"),
                                  bg='#2196F3', fg='white',
                                  width=12, height=1)
        boton_calcular.pack(pady=15)
        
        
        frame_resultados = tk.Frame(self.ventana, bg='#BBDEFB', relief='raised', bd=1)
        frame_resultados.pack(pady=10, padx=20, fill='x')
        
        tk.Label(frame_resultados, text="RESULTADOS:", font=("Arial", 11, "bold"), 
                bg='#BBDEFB').pack(pady=8)
        
        self.label_volumen = tk.Label(frame_resultados, text="Volumen: ---", 
                                     font=("Arial", 10), bg='#BBDEFB')
        self.label_volumen.pack(pady=3)
        
        self.label_superficie = tk.Label(frame_resultados, text="Superficie: ---", 
                                        font=("Arial", 10), bg='#BBDEFB')
        self.label_superficie.pack(pady=3)
    
    def calcular(self):
        try:
            radio = float(self.entry_radio.get())
            
            if radio <= 0:
                messagebox.showerror("Error", "El radio debe ser mayor a cero")
                return
            
            esfera = Esfera(radio)
            volumen = esfera.calcular_volumen()
            superficie = esfera.calcular_superficie()
            
            self.label_volumen.config(text=f"Volumen: {volumen:.2f} cm³")
            self.label_superficie.config(text=f"Superficie: {superficie:.2f} cm²")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un valor numérico válido")

class VentanaPiramide:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Pirámide - Cálculos")
        self.ventana.geometry("400x450")
        self.ventana.configure(bg='#FFF3E0')
        self.ventana.resizable(False, False)
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        
        tk.Label(self.ventana, text="PIRÁMIDE", font=("Arial", 16, "bold"), 
                bg='#FFF3E0', fg='#E65100').pack(pady=10)
        
        
        tk.Label(self.ventana, text="Ingrese base, altura y apotema en centímetros",
                font=("Arial", 10), bg='#FFF3E0', fg='#555').pack(pady=5)
        
        
        frame_entradas = tk.Frame(self.ventana, bg='#FFF3E0')
        frame_entradas.pack(pady=15)
        
        tk.Label(frame_entradas, text="Base (cm):", font=("Arial", 10), 
                bg='#FFF3E0').grid(row=0, column=0, padx=10, pady=8, sticky='e')
        self.entry_base = tk.Entry(frame_entradas, width=12, font=("Arial", 10), justify='center')
        self.entry_base.grid(row=0, column=1, padx=10, pady=8)
        
        tk.Label(frame_entradas, text="Altura (cm):", font=("Arial", 10), 
                bg='#FFF3E0').grid(row=1, column=0, padx=10, pady=8, sticky='e')
        self.entry_altura = tk.Entry(frame_entradas, width=12, font=("Arial", 10), justify='center')
        self.entry_altura.grid(row=1, column=1, padx=10, pady=8)
        
        tk.Label(frame_entradas, text="Apotema (cm):", font=("Arial", 10), 
                bg='#FFF3E0').grid(row=2, column=0, padx=10, pady=8, sticky='e')
        self.entry_apotema = tk.Entry(frame_entradas, width=12, font=("Arial", 10), justify='center')
        self.entry_apotema.grid(row=2, column=1, padx=10, pady=8)
        
        
        boton_calcular = tk.Button(self.ventana, text="CALCULAR", 
                                  command=self.calcular,
                                  font=("Arial", 11, "bold"),
                                  bg='#FF9800', fg='white',
                                  width=12, height=1)
        boton_calcular.pack(pady=15)
        
        
        frame_resultados = tk.Frame(self.ventana, bg='#FFE0B2', relief='raised', bd=1)
        frame_resultados.pack(pady=10, padx=20, fill='x')
        
        tk.Label(frame_resultados, text="RESULTADOS:", font=("Arial", 11, "bold"), 
                bg='#FFE0B2').pack(pady=8)
        
        self.label_volumen = tk.Label(frame_resultados, text="Volumen: ---", 
                                     font=("Arial", 10), bg='#FFE0B2')
        self.label_volumen.pack(pady=3)
        
        self.label_superficie = tk.Label(frame_resultados, text="Superficie: ---", 
                                        font=("Arial", 10), bg='#FFE0B2')
        self.label_superficie.pack(pady=3)
    
    def calcular(self):
        try:
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            apotema = float(self.entry_apotema.get())
            
            if base <= 0 or altura <= 0 or apotema <= 0:
                messagebox.showerror("Error", "Todos los valores deben ser mayores a cero")
                return
            
            piramide = Piramide(base, altura, apotema)
            volumen = piramide.calcular_volumen()
            superficie = piramide.calcular_superficie()
            
            self.label_volumen.config(text=f"Volumen: {volumen:.2f} cm³")
            self.label_superficie.config(text=f"Superficie: {superficie:.2f} cm²")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")



class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora de Figuras Geométricas")
        self.ventana.geometry("800x600")
        self.ventana.configure(bg="#33e994")
        self.ventana.resizable(False, False)
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        
        titulo = tk.Label(self.ventana, 
                         text="CALCULADORA DE FIGURAS GEOMÉTRICAS",
                         font=("Arial", 16, "bold"),
                         bg="#1ed69f",
                         fg='#333333',
                         pady=20)
        titulo.pack()
        
        
        subtitulo = tk.Label(self.ventana,
                           text="Seleccione una figura para calcular su volumen y superficie",
                           font=("Arial", 11),
                           bg='#1ed69f',
                           fg='#666666')
        subtitulo.pack(pady=5)
        
        
        frame_botones = tk.Frame(self.ventana, bg='#1ed69f')
        frame_botones.pack(pady=30)
        
        
        boton_cilindro = tk.Button(frame_botones,
                                  text="CILINDRO",
                                  font=("Arial", 12, "bold"),
                                  command=self.abrir_ventana_cilindro,
                                  bg="#7AAF4C",
                                  fg='white',
                                  width=15,
                                  height=4,
                                  relief='raised',
                                  bd=3)
        boton_cilindro.grid(row=0, column=0, padx=15, pady=10)
        
        
        boton_esfera = tk.Button(frame_botones,
                                text="ESFERA",
                                font=("Arial", 12, "bold"),
                                command=self.abrir_ventana_esfera,
                                bg="#47A3EE",
                                fg='white',
                                width=15,
                                height=4,
                                relief='raised',
                                bd=3)
        boton_esfera.grid(row=0, column=1, padx=15, pady=10)
        
       
        boton_piramide = tk.Button(frame_botones,
                                  text="PIRÁMIDE",
                                  font=("Arial", 12, "bold"),
                                  command=self.abrir_ventana_piramide,
                                  bg="#F2AF4C",
                                  fg='white',
                                  width=15,
                                  height=4,
                                  relief='raised',
                                  bd=3)
        boton_piramide.grid(row=0, column=2, padx=15, pady=10)
        
        
        info = tk.Label(self.ventana,
                       text="Recuerde ingresar valores positivos y en centímetros.",
                       font=("Arial", 10, "italic"),
                       bg='#1ed69f',
                       fg='#888888',
                       pady=20)
        info.pack(side='bottom')
    
    
    def abrir_ventana_cilindro(self):
        VentanaCilindro()
    
    def abrir_ventana_esfera(self):
        VentanaEsfera()
    
    def abrir_ventana_piramide(self):
        VentanaPiramide()
    
    def ejecutar(self):
        self.ventana.mainloop()




app = VentanaPrincipal()
app.ejecutar()