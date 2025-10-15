import tkinter as tk
from tkinter import ttk, messagebox
import math

class Estadisticas:
    def __init__(self):
        self.notas = []
    
    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)
    
    def calcular_desviacion_estandar(self):
        promedio = self.calcular_promedio()
        suma_cuadrados = sum((nota - promedio) ** 2 for nota in self.notas)
        varianza = suma_cuadrados / len(self.notas)
        return math.sqrt(varianza)
    
    def obtener_mayor_nota(self):
        return max(self.notas)
    
    def obtener_menor_nota(self):
        return min(self.notas)

class ValidadorNotas:
    def validar_notas(self, entradas_notas):
        notas = []
        
        for i, entrada in enumerate(entradas_notas):
            valor = entrada.get().strip()
            
            if not valor:
                messagebox.showerror("Error", f"La nota {i+1} está vacía")
                return False, []
            
            try:
                nota = float(valor)
                if nota < 0 or nota > 5:
                    messagebox.showerror("Error", f"La nota {i+1} debe estar entre 0 y 5")
                    return False, []
                notas.append(nota)
            except ValueError:
                messagebox.showerror("Error", f"La nota {i+1} no es un número válido")
                return False, []
        
        return True, notas

class CalculadoraNotas:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora de Notas del Estudiante")
        self.ventana.geometry("800x600")
        self.ventana.resizable(True, True)
        self.ventana.configure(bg="#2c528c")  
        
        self.estadisticas = Estadisticas()
        self.validador = ValidadorNotas()
        
        self.crear_contenedores()
    
    def crear_contenedores(self):
        titulo = tk.Label(self.ventana, 
                         text=" Calculadora de Notas del Estudiante", 
                         font=("Arial", 14, "bold"),
                         bg="#892222",        
                         fg='white',          
                         pady=10)
        titulo.pack(fill="x", padx=10, pady=10)
        
        contenedor_entradas = tk.Frame(self.ventana, bg='#E3F2FD', relief="raised", bd=2)
        contenedor_entradas.pack(pady=10, padx=20, fill="x")
        
        casilla_titulo_entradas = tk.Label(contenedor_entradas, 
                                      text="Ingrese las 5 notas (0-5):",
                                      font=("Arial", 10, "bold"),
                                      bg='#E3F2FD',
                                      fg='#1565C0')
        casilla_titulo_entradas.pack(pady=5)
        
        self.entradas_notas = []
        for i in range(5):
            subcontenedor = tk.Frame(contenedor_entradas, bg='#E3F2FD')
            subcontenedor.pack(pady=3)
            
            casilla = tk.Label(subcontenedor, 
                            text=f"Nota {i+1}:", 
                            font=("Arial", 9),
                            bg='#E3F2FD',
                            fg='#0D47A1',
                            width=8,
                            anchor="e")
            casilla.pack(side="left", padx=5)
            
            entrada = tk.Entry(subcontenedor, 
                              width=8,
                              font=("Arial", 9),
                              justify="center",
                              bg='#FFFFFF',
                              fg='#333333',
                              relief="solid",
                              bd=1)
            entrada.pack(side="left", padx=5)
            self.entradas_notas.append(entrada)
        
        contenedor_botones = tk.Frame(self.ventana, bg="#2c528c")
        contenedor_botones.pack(pady=15)
        
        boton_calcular = tk.Button(contenedor_botones, 
                                text="Calcular", 
                                font=("Arial", 10, "bold"),
                                command=self.calcular_estadisticas,
                                bg="#04A2EC",      
                                fg='white',       
                                activebackground="#8E948E",  
                                activeforeground='white',
                                relief="raised",
                                bd=2,
                                padx=15,
                                pady=5)
        boton_calcular.grid(row=0, column=0, padx=10)
        
        boton_limpiar = tk.Button(contenedor_botones, 
                               text=" Limpiar", 
                               font=("Arial", 10),
                               command=self.limpiar_campos,
                               bg="#00A2FF",       
                               fg='white',
                               activebackground="#00C8F5",
                               activeforeground='white',
                                relief="raised",
                                bd=2,
                                padx=15,
                                pady=5)
        boton_limpiar.grid(row=0, column=1, padx=10)
        
        contenedor_resultados = tk.LabelFrame(self.ventana, 
                                        text="  Estadísticas Calculadas  ",
                                        font=("Arial", 11, "bold"),
                                        bg='#2196F3',
                                        fg='white',
                                        bd=3)
        contenedor_resultados.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.casilla_promedio = self.crear_casilla_resultado(contenedor_resultados, "Promedio: ")
        self.casilla_desviacion = self.crear_casilla_resultado(contenedor_resultados, "Desviación Estándar: ")
        self.casilla_mayor = self.crear_casilla_resultado(contenedor_resultados, "Mayor Nota: ")
        self.casilla_menor = self.crear_casilla_resultado(contenedor_resultados, "Menor Nota: ")
    
    def crear_casilla_resultado(self, parent, texto):
        casilla = tk.Label(parent,
                        text=texto,
                        font=("Arial", 10, "bold"),
                        bg='#E3F2FD',      
                        fg='#0D47A1',      
                        anchor="w",
                        relief="flat",
                        padx=10,
                        pady=8)
        casilla.pack(fill="x", padx=5, pady=2)
        return casilla
    
    def calcular_estadisticas(self):
        es_valido, notas = self.validador.validar_notas(self.entradas_notas)
        
        if not es_valido:
            return
        
        self.estadisticas.notas = notas
        
        promedio = self.estadisticas.calcular_promedio()
        desviacion = self.estadisticas.calcular_desviacion_estandar()
        mayor_nota = self.estadisticas.obtener_mayor_nota()
        menor_nota = self.estadisticas.obtener_menor_nota()
        
        self.casilla_promedio.config(text=f" Promedio: {promedio:.2f}")
        self.casilla_desviacion.config(text=f" Desviación Estándar: {desviacion:.2f}")
        self.casilla_mayor.config(text=f" Mayor Nota: {mayor_nota:.2f}")
        self.casilla_menor.config(text=f" Menor Nota: {menor_nota:.2f}")
    
    def limpiar_campos(self):
        for entrada in self.entradas_notas:
            entrada.delete(0, tk.END)
        
        self.casilla_promedio.config(text="Promedio: ", bg='#E3F2FD')
        self.casilla_desviacion.config(text="Desviación Estándar: ", bg='#E3F2FD')
        self.casilla_mayor.config(text="Mayor Nota: ", bg='#E3F2FD')
        self.casilla_menor.config(text="Menor Nota: ", bg='#E3F2FD')
        
        self.estadisticas.notas = []
    
    def ejecutar(self):
        self.ventana.mainloop()


app = CalculadoraNotas()
app.ejecutar()