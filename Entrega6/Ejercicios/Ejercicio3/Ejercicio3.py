import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class Contacto:
    def __init__(self, nombres, apellidos, fecha_nacimiento, direccion, telefono, email):
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
    
    def to_list(self):
        return [self.nombres, self.apellidos, self.fecha_nacimiento, 
                self.direccion, self.telefono, self.email]

class AgendaContactos:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Contactos - Personal")
        self.root.geometry("700x600")
        self.root.configure(bg="#142C44")  
        
        self.contactos = []
        
        
        self.configurar_estilos()
        self.crear_widgets()
    
    def configurar_estilos(self):
        style = ttk.Style()
        
        
        style.theme_use('clam')
        
        
        color_fondo = "#142C44"
        color_primario = '#3498DB'
        color_secundario = '#2980B9'
        color_exito = '#27AE60'
        color_texto = '#ECF0F1'
        color_cards = '#34495E'
        
        
        style.configure('TFrame', background=color_fondo)
        style.configure('TLabel', background=color_fondo, foreground=color_texto, font=('Arial', 9))
        style.configure('TButton', font=('Arial', 9, 'bold'), padding=6)
        style.configure('Title.TLabel', font=('Arial', 14, 'bold'), foreground='#E74C3C')
        style.configure('Section.TLabel', font=('Arial', 11, 'bold'), foreground='#3498DB')
        
        
        style.configure('Primary.TButton', background=color_primario, foreground='white')
        style.map('Primary.TButton',
                 background=[('active', color_secundario), ('pressed', color_secundario)])
        
        style.configure('Success.TButton', background=color_exito, foreground='white')
        style.map('Success.TButton',
                 background=[('active', '#229954'), ('pressed', '#229954')])
        
        
        style.configure('Custom.TEntry', fieldbackground='white', borderwidth=2, relief='solid')
        
        
        style.configure('Custom.Treeview', 
                       background='white',
                       fieldbackground='white',
                       foreground='black',
                       rowheight=25)
        
        style.configure('Custom.Treeview.Heading',
                       background='#3498DB',
                       foreground='white',
                       font=('Arial', 9, 'bold'))
        
        style.map('Custom.Treeview.Heading',
                 background=[('active', '#2980B9')])
    
    def crear_widgets(self):
        
        main_frame = ttk.Frame(self.root, padding="15", style='TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        
        titulo = ttk.Label(main_frame, text="Agenda de Contactos Personal", 
                          style='Title.TLabel')
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        
        form_frame = tk.Frame(main_frame, bg='#34495E', relief='ridge', bd=2)
        form_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15), padx=5)
        form_frame.columnconfigure(1, weight=1)
        
        
        subtitulo = ttk.Label(form_frame, text="Agregar Nuevo Contacto", 
                             style='Section.TLabel')
        subtitulo.grid(row=0, column=0, columnspan=2, pady=(10, 15))
        
        
        row_offset = 1
        
        
        ttk.Label(form_frame, text="Nombres:", background='#34495E', 
                 foreground='#ECF0F1', font=('Arial', 9, 'bold')).grid(
                 row=row_offset, column=0, sticky=tk.W, pady=8, padx=10)
        self.entry_nombres = ttk.Entry(form_frame, width=30, style='Custom.TEntry', 
                                      font=('Arial', 9))
        self.entry_nombres.grid(row=row_offset, column=1, sticky=(tk.W, tk.E), 
                               pady=8, padx=(0, 10))
        row_offset += 1
        
        
        ttk.Label(form_frame, text="Apellidos:", background='#34495E',
                 foreground='#ECF0F1', font=('Arial', 9, 'bold')).grid(
                 row=row_offset, column=0, sticky=tk.W, pady=8, padx=10)
        self.entry_apellidos = ttk.Entry(form_frame, width=30, style='Custom.TEntry',
                                        font=('Arial', 9))
        self.entry_apellidos.grid(row=row_offset, column=1, sticky=(tk.W, tk.E), 
                                 pady=8, padx=(0, 10))
        row_offset += 1
        
        
        ttk.Label(form_frame, text="Fecha de Nacimiento:", background='#34495E',
                 foreground='#ECF0F1', font=('Arial', 9, 'bold')).grid(
                 row=row_offset, column=0, sticky=tk.W, pady=8, padx=10)
        self.date_picker = DateEntry(form_frame, width=27, background='#E74C3C',
                                   foreground='white', borderwidth=2, 
                                   date_pattern='dd/mm/yyyy',
                                   font=('Arial', 9))
        self.date_picker.grid(row=row_offset, column=1, sticky=tk.W, pady=8, padx=(0, 10))
        row_offset += 1
        

        ttk.Label(form_frame, text="Dirección:", background='#34495E',
                 foreground='#ECF0F1', font=('Arial', 9, 'bold')).grid(
                 row=row_offset, column=0, sticky=tk.W, pady=8, padx=10)
        self.entry_direccion = ttk.Entry(form_frame, width=30, style='Custom.TEntry',
                                        font=('Arial', 9))
        self.entry_direccion.grid(row=row_offset, column=1, sticky=(tk.W, tk.E), 
                                 pady=8, padx=(0, 10))
        row_offset += 1
        
        
        ttk.Label(form_frame, text="Teléfono:", background='#34495E',
                 foreground='#ECF0F1', font=('Arial', 9, 'bold')).grid(
                 row=row_offset, column=0, sticky=tk.W, pady=8, padx=10)
        self.entry_telefono = ttk.Entry(form_frame, width=30, style='Custom.TEntry',
                                       font=('Arial', 9))
        self.entry_telefono.grid(row=row_offset, column=1, sticky=(tk.W, tk.E), 
                                pady=8, padx=(0, 10))
        row_offset += 1
        
        
        ttk.Label(form_frame, text="Email:", background='#34495E',
                 foreground='#ECF0F1', font=('Arial', 9, 'bold')).grid(
                 row=row_offset, column=0, sticky=tk.W, pady=8, padx=10)
        self.entry_email = ttk.Entry(form_frame, width=30, style='Custom.TEntry',
                                    font=('Arial', 9))
        self.entry_email.grid(row=row_offset, column=1, sticky=(tk.W, tk.E), 
                             pady=8, padx=(0, 10))
        row_offset += 1
        
        
        btn_frame = ttk.Frame(form_frame, style='TFrame')
        btn_frame.grid(row=row_offset, column=0, columnspan=2, pady=15)
        
        self.btn_agregar = ttk.Button(btn_frame, text="Agregar Contacto", 
                                     command=self.agregar_contacto, style='Success.TButton')
        self.btn_agregar.pack(pady=5)
        
        
        list_frame = tk.Frame(main_frame, bg='#34495E', relief='ridge', bd=2)
        list_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), 
                       pady=(10, 0), padx=5)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(1, weight=1)
    
        
        lista_titulo = ttk.Label(list_frame, text="Lista de Contactos", 
                               style='Section.TLabel')
        lista_titulo.grid(row=0, column=0, pady=(10, 5))
        
        
        tree_container = ttk.Frame(list_frame)
        tree_container.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=(0, 10))
        tree_container.columnconfigure(0, weight=1)
        tree_container.rowconfigure(0, weight=1)
        
        
        columns = ('nombres', 'apellidos', 'fecha_nac', 'direccion', 'telefono', 'email')
        self.tree = ttk.Treeview(tree_container, columns=columns, show='headings', 
                                height=10, style='Custom.Treeview')
        
        
        self.tree.heading('nombres', text='Nombres')
        self.tree.heading('apellidos', text='Apellidos')
        self.tree.heading('fecha_nac', text='Fecha Nac.')
        self.tree.heading('direccion', text='Dirección')
        self.tree.heading('telefono', text='Teléfono')
        self.tree.heading('email', text='Email')
        
        
        self.tree.column('nombres', width=100, anchor='center')
        self.tree.column('apellidos', width=100, anchor='center')
        self.tree.column('fecha_nac', width=90, anchor='center')
        self.tree.column('direccion', width=120, anchor='center')
        self.tree.column('telefono', width=100, anchor='center')
        self.tree.column('email', width=120, anchor='center')
        
        
        scrollbar = ttk.Scrollbar(tree_container, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        

        main_frame.rowconfigure(2, weight=1)
        list_frame.rowconfigure(1, weight=1)
    
    def agregar_contacto(self):
        
        nombres = self.entry_nombres.get().strip()
        apellidos = self.entry_apellidos.get().strip()
        fecha_nacimiento = self.date_picker.get()
        direccion = self.entry_direccion.get().strip()
        telefono = self.entry_telefono.get().strip()
        email = self.entry_email.get().strip()
        
        
        if not nombres or not apellidos:
            messagebox.showwarning("Advertencia", 
                                 "Los campos Nombres y Apellidos son obligatorios")
            return
        
        
        nuevo_contacto = Contacto(nombres, apellidos, fecha_nacimiento, direccion, telefono, email)
        self.contactos.append(nuevo_contacto)
        
        
        self.tree.insert('', tk.END, values=nuevo_contacto.to_list())
        

        self.limpiar_campos()
        
        messagebox.showinfo("Éxito", "Contacto agregado correctamente")
    
    def limpiar_campos(self):
        self.entry_nombres.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        

def main():
    root = tk.Tk()
    app = AgendaContactos(root)
    root.mainloop()

if __name__ == "__main__":
    main()