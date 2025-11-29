import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

class Habitacion:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
        self.disponible = True
        self.huesped = None
        self.fecha_ingreso = None
        self.fecha_salida = None
    
    def ocupar(self, huesped, fecha_ingreso):
        self.disponible = False
        self.huesped = huesped
        self.fecha_ingreso = fecha_ingreso
    
    def liberar(self, fecha_salida):
        self.disponible = True
        self.fecha_salida = fecha_salida
        huesped = self.huesped
        self.huesped = None
        return huesped
    
    def calcular_costo(self, fecha_salida):
        if not self.fecha_ingreso:
            return 0
        dias = (fecha_salida - self.fecha_ingreso).days
        return dias * self.precio

class Huesped:
    def __init__(self, nombre, apellido, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento

class Hotel:
    def __init__(self):
        self.habitaciones = []
        self.inicializar_habitaciones()
    
    def inicializar_habitaciones(self):
       
        for i in range(1, 6):
            self.habitaciones.append(Habitacion(i, 120000))
        
        
        for i in range(6, 11):
            self.habitaciones.append(Habitacion(i, 160000))
    
    def obtener_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                return habitacion
        return None
    
    def habitaciones_disponibles(self):
        return [h for h in self.habitaciones if h.disponible]
    
    def habitaciones_ocupadas(self):
        return [h for h in self.habitaciones if not h.disponible]

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión Hotelera")
        self.root.geometry("700x550")
        self.root.configure(bg='#2C3E50')
        
        
        self.configurar_estilos()
        
        self.hotel = Hotel()
        
        self.crear_menu_principal()
    
    def configurar_estilos(self):
        style = ttk.Style()
        
        
        style.theme_use('clam')
        
        
        self.color_primario = '#3498DB'
        self.color_secundario = '#2980B9'
        self.color_exito = '#27AE60'
        self.color_peligro = '#E74C3C'
        self.color_advertencia = '#F39C12'
        self.color_fondo = '#2C3E50'
        self.color_fondo_claro = '#34495E'
        self.color_texto = '#ECF0F1'
        
        
        style.configure('Primary.TButton',
                       background=self.color_primario,
                       foreground='white',
                       padding=(20, 10),
                       font=('Arial', 10, 'bold'),
                       borderwidth=0,
                       focuscolor='none')
        
        style.configure('Success.TButton',
                       background=self.color_exito,
                       foreground='white',
                       padding=(20, 10),
                       font=('Arial', 10, 'bold'),
                       borderwidth=0)
        
        style.configure('Danger.TButton',
                       background=self.color_peligro,
                       foreground='white',
                       padding=(20, 10),
                       font=('Arial', 10, 'bold'),
                       borderwidth=0)
        
        style.configure('Warning.TButton',
                       background=self.color_advertencia,
                       foreground='white',
                       padding=(20, 10),
                       font=('Arial', 10, 'bold'),
                       borderwidth=0)
        
       
        style.configure('Card.TFrame',
                       background=self.color_fondo_claro,
                       relief='raised',
                       borderwidth=1)
        
        style.configure('Titulo.TLabel',
                       background=self.color_fondo,
                       foreground=self.color_texto,
                       font=('Arial', 18, 'bold'))
        
        style.configure('Subtitulo.TLabel',
                       background=self.color_fondo_claro,
                       foreground=self.color_texto,
                       font=('Arial', 12, 'bold'))
        
        style.configure('Normal.TLabel',
                       background=self.color_fondo_claro,
                       foreground=self.color_texto,
                       font=('Arial', 10))
    
    def crear_frame_principal(self, window, padding="20"):
        frame = ttk.Frame(window, style='Card.TFrame', padding=padding)
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        return frame
    
    def crear_titulo(self, parent, texto):
        label = ttk.Label(parent, text=texto, style='Titulo.TLabel')
        return label
    
    def crear_subtitulo(self, parent, texto):
        label = ttk.Label(parent, text=texto, style='Subtitulo.TLabel')
        return label
    
    def crear_menu_principal(self):
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        
        main_frame = self.crear_frame_principal(self.root, "30")
        main_frame.configure(style='Card.TFrame')
        
        
        titulo = self.crear_titulo(main_frame, "Sistema de Gestión Hotelera")
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        
        botones_frame = ttk.Frame(main_frame, style='Card.TFrame', padding="20")
        botones_frame.grid(row=1, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))
        
        
        btn_consultar = ttk.Button(botones_frame, 
                                  text="Consultar Habitaciones", 
                                  command=self.consultar_habitaciones,
                                  style='Primary.TButton',
                                  width=25)
        btn_consultar.grid(row=0, column=0, pady=15, padx=10)
        
        btn_salida = ttk.Button(botones_frame, 
                               text="Salida de Huéspedes", 
                               command=self.salida_huespedes,
                               style='Warning.TButton',
                               width=25)
        btn_salida.grid(row=0, column=1, pady=15, padx=10)
        
        
        info_frame = ttk.Frame(main_frame, style='Card.TFrame', padding="15")
        info_frame.grid(row=2, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))
        
        info_text = "Información del Hotel:\n• Habitaciones 1-5: $120,000 por día\n• Habitaciones 6-10: $160,000 por día\n• Total habitaciones: 10"
        
        info_label = ttk.Label(info_frame, text=info_text, style='Normal.TLabel', justify=tk.LEFT)
        info_label.grid(row=0, column=0, sticky=tk.W)
        
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        botones_frame.columnconfigure(0, weight=1)
        botones_frame.columnconfigure(1, weight=1)
    
    def consultar_habitaciones(self):
        
        consulta_window = tk.Toplevel(self.root)
        consulta_window.title("Estado de Habitaciones")
        consulta_window.geometry("800x600")
        consulta_window.configure(bg=self.color_fondo)
        consulta_window.transient(self.root)
        consulta_window.grab_set()
        
        
        main_frame = self.crear_frame_principal(consulta_window, "20")
        
      
        titulo = self.crear_titulo(main_frame, "Estado de Habitaciones")
        titulo.grid(row=0, column=0, columnspan=4, pady=(0, 20))
        
       
        encabezados = ["Habitación", "Precio/día", "Estado", "Tipo"]
        for i, texto in enumerate(encabezados):
            label = ttk.Label(main_frame, text=texto, style='Subtitulo.TLabel')
            label.grid(row=1, column=i, padx=8, pady=10, sticky=tk.W)
        
        
        for i, habitacion in enumerate(self.hotel.habitaciones, start=2):
           
            ttk.Label(main_frame, text=f"Habitación {habitacion.numero}", 
                     style='Normal.TLabel').grid(row=i, column=0, padx=8, pady=6, sticky=tk.W)
            
            
            ttk.Label(main_frame, text=f"${habitacion.precio:,}", 
                     style='Normal.TLabel').grid(row=i, column=1, padx=8, pady=6, sticky=tk.W)
            
            
            estado = "Disponible" if habitacion.disponible else "Ocupada"
            color_estado = "#27AE60" if habitacion.disponible else "#E74C3C"
            estado_label = tk.Label(main_frame, text=estado, 
                                   bg=self.color_fondo_claro, fg=color_estado,
                                   font=('Arial', 9, 'bold'), padx=8, pady=2)
            estado_label.grid(row=i, column=2, padx=8, pady=6, sticky=tk.W)
            
            
            tipo = "Estándar" if habitacion.numero <= 5 else "Lujo"
            ttk.Label(main_frame, text=tipo, 
                     style='Normal.TLabel').grid(row=i, column=3, padx=8, pady=6, sticky=tk.W)
        
        seleccion_frame = ttk.Frame(main_frame, style='Card.TFrame', padding="15")
        seleccion_frame.grid(row=13, column=0, columnspan=4, pady=20, sticky=(tk.W, tk.E))
        
        ttk.Label(seleccion_frame, text="Seleccionar habitación a ocupar:",
                 style='Subtitulo.TLabel').grid(row=0, column=0, padx=5, pady=5)
        
        self.habitacion_var = tk.StringVar()
        habitaciones_disponibles = [str(h.numero) for h in self.hotel.habitaciones_disponibles()]
        habitacion_combo = ttk.Combobox(seleccion_frame, textvariable=self.habitacion_var, 
                                       values=habitaciones_disponibles,
                                       state="readonly", width=12,
                                       font=('Arial', 10))
        habitacion_combo.grid(row=0, column=1, padx=10, pady=5)
        
        btn_ocupar = ttk.Button(seleccion_frame, text="Ocupar Habitación", 
                               command=self.ocupar_habitacion,
                               style='Success.TButton')
        btn_ocupar.grid(row=0, column=2, padx=10, pady=5)
        
        btn_volver = ttk.Button(main_frame, text="Volver al Menú", 
                               command=consulta_window.destroy,
                               style='Primary.TButton')
        btn_volver.grid(row=14, column=0, columnspan=4, pady=15)
        
        
        consulta_window.columnconfigure(0, weight=1)
        consulta_window.rowconfigure(0, weight=1)
        for i in range(4):
            main_frame.columnconfigure(i, weight=1)
    
    def ocupar_habitacion(self):
        try:
            num_habitacion = int(self.habitacion_var.get())
            habitacion = self.hotel.obtener_habitacion(num_habitacion)
            
            if not habitacion or not habitacion.disponible:
                messagebox.showerror("Error", "Habitación no disponible o no existe")
                return
            
            self.mostrar_formulario_registro(habitacion)
            
        except ValueError:
            messagebox.showerror("Error", "Seleccione una habitación válida")
    
    def mostrar_formulario_registro(self, habitacion):
        registro_window = tk.Toplevel(self.root)
        registro_window.title(f"Registro - Habitación {habitacion.numero}")
        registro_window.geometry("450x400")
        registro_window.configure(bg=self.color_fondo)
        registro_window.transient(self.root)
        registro_window.grab_set()
        
        
        main_frame = self.crear_frame_principal(registro_window, "25")
        
        titulo = self.crear_titulo(main_frame, f"Registro Habitación {habitacion.numero}")
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        
        info_frame = ttk.Frame(main_frame, style='Card.TFrame', padding="10")
        info_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        tipo = "Estándar" if habitacion.numero <= 5 else "Superior"
        precio = "$120,000/día" if habitacion.numero <= 5 else "$160,000/día"
        
        info_text = f"Información de la habitación:\n• Número: {habitacion.numero}\n• Tipo: {tipo}\n• Precio: {precio}"
        
        ttk.Label(info_frame, text=info_text, style='Normal.TLabel', 
                 justify=tk.LEFT).grid(row=0, column=0, sticky=tk.W)
        
        
        campos = [
            ("Fecha de Ingreso (DD/MM/AAAA):", "fecha_ingreso"),
            ("Nombre:", "nombre"),
            ("Apellido:", "apellido"), 
            ("Documento:", "documento")
        ]
        
        self.campos_vars = {}
        for i, (label_text, campo) in enumerate(campos, start=2):
            ttk.Label(main_frame, text=label_text, style='Normal.TLabel').grid(
                row=i, column=0, sticky=tk.W, pady=8)
            
            var = tk.StringVar()
            if campo == "fecha_ingreso":
                var.set(datetime.now().strftime("%d/%m/%Y"))
            
            entry = ttk.Entry(main_frame, textvariable=var, width=25, font=('Arial', 10))
            entry.grid(row=i, column=1, pady=8, padx=10, sticky=tk.W)
            self.campos_vars[campo] = var
        
        
        btn_frame = ttk.Frame(main_frame, style='Card.TFrame', padding="10")
        btn_frame.grid(row=6, column=0, columnspan=2, pady=20)
        
        btn_registrar = ttk.Button(btn_frame, text="Registrar Huésped", 
                                  command=lambda: self.registrar_huesped(habitacion, registro_window),
                                  style='Success.TButton')
        btn_registrar.grid(row=0, column=0, padx=10)
        
        btn_cancelar = ttk.Button(btn_frame, text="Cancelar", 
                                 command=registro_window.destroy,
                                 style='Danger.TButton')
        btn_cancelar.grid(row=0, column=1, padx=10)
        
        
        registro_window.columnconfigure(0, weight=1)
        registro_window.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
    
    def registrar_huesped(self, habitacion, window):
        
        campos_requeridos = ['fecha_ingreso', 'nombre', 'apellido', 'documento']
        for campo in campos_requeridos:
            if not self.campos_vars[campo].get():
                messagebox.showerror("Error", f"El campo {campo.replace('_', ' ').title()} es obligatorio")
                return
        
        
        try:
            fecha_ingreso = datetime.strptime(self.campos_vars['fecha_ingreso'].get(), "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Use DD/MM/AAAA")
            return
        
        
        huesped = Huesped(self.campos_vars['nombre'].get(), 
                         self.campos_vars['apellido'].get(), 
                         self.campos_vars['documento'].get())
        habitacion.ocupar(huesped, fecha_ingreso)
        
        messagebox.showinfo("Éxito", f"Habitación {habitacion.numero} ocupada exitosamente")
        window.destroy()
    
    def salida_huespedes(self):
        salida_window = tk.Toplevel(self.root)
        salida_window.title("Salida de Huéspedes")
        salida_window.geometry("500x300")
        salida_window.configure(bg=self.color_fondo)
        salida_window.transient(self.root)
        salida_window.grab_set()
        
    
        main_frame = self.crear_frame_principal(salida_window, "25")
        
        
        titulo = self.crear_titulo(main_frame, "Salida de Huéspedes")
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        
        seleccion_frame = ttk.Frame(main_frame, style='Card.TFrame', padding="20")
        seleccion_frame.grid(row=1, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))
        
        ttk.Label(seleccion_frame, text="Seleccione la habitación a entregar:",
                 style='Subtitulo.TLabel').grid(row=0, column=0, columnspan=2, pady=10)
        
        self.habitacion_salida_var = tk.StringVar()
        habitaciones_ocupadas = [str(h.numero) for h in self.hotel.habitaciones_ocupadas()]
        
        if not habitaciones_ocupadas:
            ttk.Label(seleccion_frame, text="¡Todas las habitaciones están disponibles!",
                     style='Normal.TLabel').grid(row=1, column=0, columnspan=2, pady=10)
        else:
            habitacion_combo = ttk.Combobox(seleccion_frame, textvariable=self.habitacion_salida_var, 
                                           values=habitaciones_ocupadas, 
                                           state="readonly", width=15,
                                           font=('Arial', 11))
            habitacion_combo.grid(row=1, column=0, pady=15, padx=10)
            
            btn_continuar = ttk.Button(seleccion_frame, text="Continuar", 
                                      command=self.procesar_salida,
                                      style='Primary.TButton')
            btn_continuar.grid(row=1, column=1, pady=15, padx=10)
        
        
        btn_volver = ttk.Button(main_frame, text="Volver al Menú", 
                               command=salida_window.destroy,
                               style='Primary.TButton')
        btn_volver.grid(row=2, column=0, columnspan=2, pady=10)
        

        salida_window.columnconfigure(0, weight=1)
        salida_window.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        seleccion_frame.columnconfigure(0, weight=1)
        seleccion_frame.columnconfigure(1, weight=1)
    
    def procesar_salida(self):
        try:
            num_habitacion = int(self.habitacion_salida_var.get())
            habitacion = self.hotel.obtener_habitacion(num_habitacion)
            
            if not habitacion or habitacion.disponible:
                messagebox.showerror("Error", "Habitación no ocupada o no existe")
                return
            
            self.mostrar_calculo_pago(habitacion)
            
        except ValueError:
            messagebox.showerror("Error", "Seleccione una habitación válida")
    
    def mostrar_calculo_pago(self, habitacion):
        pago_window = tk.Toplevel(self.root)
        pago_window.title(f"Salida - Habitación {habitacion.numero}")
        pago_window.geometry("550x500")
        pago_window.configure(bg=self.color_fondo)
        pago_window.transient(self.root)
        pago_window.grab_set()
        
        
        main_frame = self.crear_frame_principal(pago_window, "20")
        
        
        titulo = self.crear_titulo(main_frame, f"Salida Habitación {habitacion.numero}")
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        
        info_frame = ttk.LabelFrame(main_frame, text="Información del Huésped", 
                                   style='Card.TFrame', padding="15")
        info_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=15)
        
        info_text = f"""• Habitación: {habitacion.numero}
• Nombre: {habitacion.huesped.nombre} {habitacion.huesped.apellido}
• Documento: {habitacion.huesped.documento}
• Fecha ingreso: {habitacion.fecha_ingreso.strftime('%d/%m/%Y')}
• Precio/día: ${habitacion.precio:,}"""
        
        ttk.Label(info_frame, text=info_text, style='Normal.TLabel', 
                 justify=tk.LEFT).grid(row=0, column=0, sticky=tk.W)
        
        
        ttk.Label(main_frame, text="Fecha de Salida (DD/MM/AAAA):", 
                 style='Subtitulo.TLabel').grid(row=2, column=0, sticky=tk.W, pady=15)
        
        self.fecha_salida_var = tk.StringVar(value=datetime.now().strftime("%d/%m/%Y"))
        entry_fecha_salida = ttk.Entry(main_frame, textvariable=self.fecha_salida_var, 
                                      width=20, font=('Arial', 10))
        entry_fecha_salida.grid(row=2, column=1, pady=15, padx=10, sticky=tk.W)
        
        
        btn_calcular = ttk.Button(main_frame, text="Calcular Total", 
                                 command=lambda: self.calcular_total(habitacion, resultado_label),
                                 style='Primary.TButton')
        btn_calcular.grid(row=3, column=0, columnspan=2, pady=15)
        
        
        resultado_frame = ttk.Frame(main_frame, style='Card.TFrame', padding="15")
        resultado_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        resultado_label = ttk.Label(resultado_frame, text="Esperando cálculo...", 
                                   style='Normal.TLabel', font=('Arial', 10))
        resultado_label.grid(row=0, column=0, sticky=tk.W)
        
        
        self.btn_registrar_salida = ttk.Button(main_frame, text="Registrar Salida", 
                                              command=lambda: self.registrar_salida(habitacion, pago_window),
                                              style='Success.TButton',
                                              state="disabled")
        self.btn_registrar_salida.grid(row=5, column=0, columnspan=2, pady=15)
        
        btn_volver = ttk.Button(main_frame, text="Volver", 
                               command=pago_window.destroy,
                               style='Primary.TButton')
        btn_volver.grid(row=6, column=0, columnspan=2, pady=10)
        
        
        pago_window.columnconfigure(0, weight=1)
        pago_window.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
    
    def calcular_total(self, habitacion, resultado_label):
        try:
            fecha_salida = datetime.strptime(self.fecha_salida_var.get(), "%d/%m/%Y")
            
            if fecha_salida <= habitacion.fecha_ingreso:
                messagebox.showerror("Error", "La fecha de salida debe ser mayor a la fecha de ingreso")
                return
            
            total_dias = (fecha_salida - habitacion.fecha_ingreso).days
            total_pago = habitacion.calcular_costo(fecha_salida)
            
            resultado_text = f"""RESUMEN DE PAGO:
• Días de alojamiento: {total_dias}
• Precio por día: ${habitacion.precio:,}
• Total a pagar: ${total_pago:,}"""
            
            resultado_label.config(text=resultado_text)
            
            
            self.btn_registrar_salida.config(state="normal")
            
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Use DD/MM/AAAA")
    
    def registrar_salida(self, habitacion, window):
        try:
            fecha_salida = datetime.strptime(self.fecha_salida_var.get(), "%d/%m/%Y")
            huesped = habitacion.liberar(fecha_salida)
            
            messagebox.showinfo("Éxito", 
                              f"Salida registrada exitosamente para:\n{huesped.nombre} {huesped.apellido}\n\nHabitación {habitacion.numero} ahora está disponible")
            window.destroy()
            
        except ValueError:
            messagebox.showerror("Error", "Error al registrar la salida")

def main():
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()