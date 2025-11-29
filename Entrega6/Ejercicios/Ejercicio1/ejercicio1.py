
import tkinter as tk
from tkinter import messagebox, ttk
import os

class Empleado:
    def __init__(self, nombre, apellidos, cargo, genero, salario_dia, dias_trabajados, otros_ingresos, pagos_salud, aporte_pensiones):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.genero = genero
        self.salario_dia = salario_dia
        self.dias_trabajados = dias_trabajados
        self.otros_ingresos = otros_ingresos
        self.pagos_salud = pagos_salud
        self.aporte_pensiones = aporte_pensiones
        
    def calcular_sueldo(self):
        return (self.dias_trabajados * self.salario_dia) + self.otros_ingresos - self.pagos_salud - self.aporte_pensiones

class NominaApp:
    def __init__(self):
        self.empleados = []
        
        
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Nómina")
        self.ventana.geometry("500x400")
        
        
        self.crear_botones_principales()
        
    def crear_botones_principales(self):
        self.limpiar_ventana()
        
        tk.Label(self.ventana, text="SISTEMA DE NÓMINA", 
                font=("Arial", 16, "bold")).pack(pady=20)
        
        
        tk.Button(self.ventana, text="Agregar Empleado", 
                 command=self.agregar_empleado, width=20, height=2,
                 bg="lightblue").pack(pady=5)
        
        tk.Button(self.ventana, text="Calcular Nómina", 
                 command=self.calcular_nomina, width=20, height=2,
                 bg="lightgreen").pack(pady=5)
        
        tk.Button(self.ventana, text="Guardar Archivo", 
                 command=self.guardar_archivo, width=20, height=2,
                 bg="yellow").pack(pady=5)
        
        tk.Button(self.ventana, text="Salir", 
                 command=self.ventana.quit, width=20, height=2,
                 bg="red", fg="white").pack(pady=5)
    
    def limpiar_ventana(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
    
    def volver_menu(self):
        self.crear_botones_principales()
    
    def agregar_empleado(self):
        self.limpiar_ventana()
        
        tk.Label(self.ventana, text="AGREGAR EMPLEADO", font=("Arial", 14, "bold")).pack(pady=10)
        
        
        marco = tk.Frame(self.ventana)
        marco.pack(pady=10)
        
        
        tk.Label(marco, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
        entry_nombre = tk.Entry(marco, width=20)
        entry_nombre.grid(row=0, column=1, pady=5)
        
        
        tk.Label(marco, text="Apellidos:").grid(row=1, column=0, sticky="w", pady=5)
        entry_apellidos = tk.Entry(marco, width=20)
        entry_apellidos.grid(row=1, column=1, pady=5)
        
        
        tk.Label(marco, text="Cargo:").grid(row=2, column=0, sticky="w", pady=5)
        combo_cargo = ttk.Combobox(marco, values=["directivo", "estratégico", "operativo"], state="readonly")
        combo_cargo.current(0)
        combo_cargo.grid(row=2, column=1, pady=5)
        
        
        tk.Label(marco, text="Género:").grid(row=3, column=0, sticky="w", pady=5)
        var_genero = tk.StringVar(value="masculino")
        frame_genero = tk.Frame(marco)
        frame_genero.grid(row=3, column=1, pady=5)
        tk.Radiobutton(frame_genero, text="Masculino", variable=var_genero, value="masculino").pack(side="left")
        tk.Radiobutton(frame_genero, text="Femenino", variable=var_genero, value="femenino").pack(side="left")
        
        
        tk.Label(marco, text="Salario por día:").grid(row=4, column=0, sticky="w", pady=5)
        entry_salario = tk.Entry(marco, width=20)
        entry_salario.grid(row=4, column=1, pady=5)
        
        
        tk.Label(marco, text="Días trabajados:").grid(row=5, column=0, sticky="w", pady=5)
        spin_dias = tk.Spinbox(marco, from_=1, to=31, width=18)
        spin_dias.grid(row=5, column=1, pady=5)
        
        
        tk.Label(marco, text="Otros ingresos:").grid(row=6, column=0, sticky="w", pady=5)
        entry_ingresos = tk.Entry(marco, width=20)
        entry_ingresos.grid(row=6, column=1, pady=5)
        entry_ingresos.insert(0, "0")
        
        
        tk.Label(marco, text="Pagos por salud:").grid(row=7, column=0, sticky="w", pady=5)
        entry_salud = tk.Entry(marco, width=20)
        entry_salud.grid(row=7, column=1, pady=5)
        
        
        tk.Label(marco, text="Aporte pensiones:").grid(row=8, column=0, sticky="w", pady=5)
        entry_pension = tk.Entry(marco, width=20)
        entry_pension.grid(row=8, column=1, pady=5)
        
        def guardar():
            try:
                
                if not entry_nombre.get() or not entry_apellidos.get():
                    messagebox.showerror("Error", "Nombre y apellidos son obligatorios")
                    return
                
                
                salario = float(entry_salario.get())
                dias = int(spin_dias.get())
                ingresos = float(entry_ingresos.get())
                salud = float(entry_salud.get())
                pension = float(entry_pension.get())
                
                if salario <= 0:
                    messagebox.showerror("Error", "El salario debe ser mayor a 0")
                    return
                
                
                empleado = Empleado(
                    entry_nombre.get(),
                    entry_apellidos.get(),
                    combo_cargo.get(),
                    var_genero.get(),
                    salario,
                    dias,
                    ingresos,
                    salud,
                    pension
                )
                
                self.empleados.append(empleado)
                messagebox.showinfo("Éxito", "Empleado agregado correctamente")
                self.volver_menu()
                
            except ValueError:
                messagebox.showerror("Error", "Los campos numéricos deben contener números válidos")
        
        
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=20)
        
        tk.Button(frame_botones, text="Guardar", command=guardar, bg="green", fg="white").pack(side="left", padx=10)
        tk.Button(frame_botones, text="Volver", command=self.volver_menu).pack(side="left", padx=10)
    
    def calcular_nomina(self):
        self.limpiar_ventana()
        
        tk.Label(self.ventana, text="CALCULAR NÓMINA", font=("Arial", 14, "bold")).pack(pady=10)
        
        if not self.empleados:
            tk.Label(self.ventana, text="No hay empleados registrados").pack(pady=20)
            tk.Button(self.ventana, text="Volver", command=self.volver_menu).pack(pady=10)
            return
        
        
        frame_tabla = tk.Frame(self.ventana)
        frame_tabla.pack(pady=10)
        
        
        tk.Label(frame_tabla, text="Nombre", borderwidth=1, relief="solid", width=15, bg="lightgray").grid(row=0, column=0)
        tk.Label(frame_tabla, text="Apellidos", borderwidth=1, relief="solid", width=15, bg="lightgray").grid(row=0, column=1)
        tk.Label(frame_tabla, text="Sueldo", borderwidth=1, relief="solid", width=15, bg="lightgray").grid(row=0, column=2)
        
        
        total_nomina = 0
        for i, empleado in enumerate(self.empleados, 1):
            sueldo = empleado.calcular_sueldo()
            total_nomina += sueldo
            
            color_fila = "white" if i % 2 == 0 else "lightyellow"
            
            tk.Label(frame_tabla, text=empleado.nombre, borderwidth=1, relief="solid", width=15, bg=color_fila).grid(row=i, column=0)
            tk.Label(frame_tabla, text=empleado.apellidos, borderwidth=1, relief="solid", width=15, bg=color_fila).grid(row=i, column=1)
            tk.Label(frame_tabla, text=f"${sueldo:.2f}", borderwidth=1, relief="solid", width=15, bg=color_fila).grid(row=i, column=2)
        
        
        tk.Label(self.ventana, text=f"TOTAL NÓMINA: ${total_nomina:.2f}", 
                font=("Arial", 12, "bold"), fg="blue").pack(pady=10)
        
        tk.Button(self.ventana, text="Volver", command=self.volver_menu).pack(pady=10)
    
    def guardar_archivo(self):
        self.limpiar_ventana()
        
        tk.Label(self.ventana, text="GUARDAR ARCHIVO", font=("Arial", 14, "bold")).pack(pady=10)
        
        if not self.empleados:
            tk.Label(self.ventana, text="No hay empleados registrados").pack(pady=20)
            tk.Button(self.ventana, text="Volver", command=self.volver_menu).pack(pady=10)
            return
        
        
        carpeta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(carpeta_actual, "Nómina.txt")
        
        tk.Label(self.ventana, text="Se guardará el archivo 'Nómina.txt' en la misma carpeta del programa").pack(pady=10)
        
        def guardar():
            try:
                with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                    archivo.write("NÓMINA DE EMPLEADOS\n")
                    archivo.write("=" * 40 + "\n\n")
                    
                    total_nomina = 0
                    
                    for i, empleado in enumerate(self.empleados, 1):
                        sueldo = empleado.calcular_sueldo()
                        total_nomina += sueldo
                        
                        archivo.write(f"Empleado {i}:\n")
                        archivo.write(f"  Nombre: {empleado.nombre}\n")
                        archivo.write(f"  Apellidos: {empleado.apellidos}\n")
                        archivo.write(f"  Cargo: {empleado.cargo}\n")
                        archivo.write(f"  Género: {empleado.genero}\n")
                        archivo.write(f"  Salario día: ${empleado.salario_dia:.2f}\n")
                        archivo.write(f"  Días trabajados: {empleado.dias_trabajados}\n")
                        archivo.write(f"  Otros ingresos: ${empleado.otros_ingresos:.2f}\n")
                        archivo.write(f"  Pagos salud: ${empleado.pagos_salud:.2f}\n")
                        archivo.write(f"  Aporte pensiones: ${empleado.aporte_pensiones:.2f}\n")
                        archivo.write(f"  Sueldo mensual: ${sueldo:.2f}\n")
                        archivo.write("-" * 30 + "\n")
                    
                    archivo.write(f"\nTOTAL NÓMINA: ${total_nomina:.2f}\n")
                
                messagebox.showinfo("Éxito", "Archivo 'Nómina.txt' guardado correctamente")
                self.volver_menu()
                
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
        
        tk.Button(self.ventana, text="Guardar Nómina.txt", command=guardar, bg="blue", fg="white").pack(pady=10)
        tk.Button(self.ventana, text="Volver", command=self.volver_menu).pack(pady=10)
    
    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    app = NominaApp()
    app.ejecutar()