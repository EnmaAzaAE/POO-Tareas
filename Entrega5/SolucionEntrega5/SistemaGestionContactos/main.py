# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import json
import re

class GestionContactos:

    def __init__(self):
        # Se obtiene la ruta absoluta del archivo en el mismo directorio del script
        base_ruta = os.path.dirname(os.path.abspath(__file__))
        # Se define la ruta del archivo en funcion
        self.__ruta_archivo=os.path.join(base_ruta, "friendsContacts.txt")
        self._informacion=self.__get_informacion()
   
    # Definimos un metodo para cargar la _informacion
    def __get_informacion(self):
        # Si la carpeta con el archivo no existe entonces se crea
        if not os.path.exists(self.__ruta_archivo):
            with open(self.__ruta_archivo, "w", encoding="utf-8") as f:
                f.write("{}")
            
        # una vez se sabe creada, se carga la _informacion la cual se encuentra en formato json
        with open(self.__ruta_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
        
    # Definimos un metodo para guarda la _informacion
    def __set_information(self, _informacion):
        with open(self.__ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(_informacion, f, ensure_ascii=False, indent=4)
    
    def _crear_contacto(self, nombre: str, telefono: str):
        # validamos que no falte ningun campo por llenar
        if not telefono.strip() or not nombre.strip():
            raise Exception("Campo nombre o telefono vacios")
        # validamos que el nombre cumpla con el formato
        if len(nombre)>22 or not nombre.replace(" ", "").isalnum():
            raise Exception("Nombre de contacto invalido, no cumple con el formato") 
        # validamos que el telefono cumpla con el formato
        if not re.match(r'^\+?\d[\d\s-]{6,14}$', telefono):
            raise Exception("Numero de telefono invalido, no cumple con el formato")        
        # Validamos que la lista con los contactos no este vacia
        if len(self._informacion)>0:
            # revisamos que el contacto no este ya registrado  
            for contacto, info in self._informacion.items():
                if (nombre.replace(" ", "").lower()==info['Nombre'].replace(" ", "").lower() or 
                    telefono.replace(" ", "")==info['Telefono'].replace(" ", "")):
                    raise Exception("El nombre o el telefono ya ha sido registrado")
            # Capturo el ultimo indice y le sumo uno para añadirle un valor nuevo unico de forma dinamica
            nuevo_id = str(max(map(int, self._informacion.keys())) + 1)
            # se actualiza el elemento en la lista de contactos
        else:
            nuevo_id="1"
        self._informacion[nuevo_id]={'Nombre': nombre, 'Telefono': telefono}
        # se guarda en el json
        self.__set_information(self._informacion)

    # Metodo para eliminar el contacto seleccionado
    def _eliminar_contacto(self, contacto):
        del self._informacion[contacto[0]]
        self.__set_information(self._informacion)

    # Metodo para editar contacto
    def _editar_contacto(self, id, nombreNuevo, telefonoNuevo):
        # validamos que no falte ningun campo por llenar
        if not telefonoNuevo.strip() or not nombreNuevo.strip():
            raise Exception("Campo nombre o telefono vacios")
        # validamos que el nombre cumpla con el formato
        if len(nombreNuevo)>22 or not nombreNuevo.replace(" ", "").isalnum():
            raise Exception("Nombre de contacto invalido, no cumple con el formato") 
        # validamos que el telefono cumpla con el formato
        if not re.match(r'^\+?\d[\d\s-]{6,14}$', telefonoNuevo):
            raise Exception("Numero de telefono invalido, no cumple con el formato")        
        # revisamos que el contacto no este ya registrado
        contarReps=0
        for contacto, info in self._informacion.items():
            if (nombreNuevo.replace(" ", "").lower()==info['Nombre'].replace(" ", "").lower() or 
                telefonoNuevo.replace(" ", "")==info['Telefono'].replace(" ", "")):
                contarReps+=1
                if contarReps>1:
                    raise Exception("El nombre o el telefono ya ha sido registrado")
        # Si se cumplen las validaciones se actualiza el contacto seleccionado en cuestion 
        self._informacion[id]={'Nombre': nombreNuevo, 'Telefono': telefonoNuevo}
        # se guarda en el json
        self.__set_information(self._informacion)
    

    

class Interfaz:
    def __init__(self):
        # Estanciamos un objeto de cotnactos a fin de poder acceder a sus metodos e _informacion
        self.__contactos=GestionContactos()
        self.__contacto_seleccionado = None
        self._panel_principal = tk.Tk()
        self._panel_principal.title("Sistema de gestion de contactos")
        # self._panel_principal.geometry("400x380")
        self._panel_principal.resizable(False, False)
        self._panel_principal.configure(bg="#2C3E50")
        
        self.__panel_actual=None

        self._panel_principal.grid_columnconfigure(0, weight=1)
        self._panel_principal.grid_columnconfigure(1, weight=0)
        self._panel_principal.grid_columnconfigure(2, weight=1)
        
        # self.crear_interfaz()
        self.ver_contactos()

    # Método que elimina el panel anterior y crea uno nuevo
    def __limpiarPanel(self):
        if self.__panel_actual:
            self.__panel_actual.destroy()

    # def crear_interfaz(self):
    def ver_contactos(self):
        # limpiamos el contenedor anterios
        self.__limpiarPanel()
        
        # self._panel_principal.geometry("400x380")
        # Definimos un panel con la nueva _informacion
        self.__panel_actual = tk.Frame(self._panel_principal, padx=10, pady=10)

        self.__panel_actual.grid(row=0, column=1, sticky="nsew")
        self.__panel_actual.grid_columnconfigure(0, weight=1)
        self.__panel_actual.grid_columnconfigure(1, weight=0)
        self.__panel_actual.grid_columnconfigure(2, weight=1)
        self.__panel_actual.configure(bg="#2C3E50")

        
        titulo = tk.Label(self.__panel_actual, 
                        text="Listado de contactos", 
                        font=("Arial", 16, "bold"),
                        foreground="#ECF0F1",
                        background="#2C3E50")
        titulo.grid(row=0, column=0, columnspan=3, pady=15)

        
        # Cargamos la _informacion asociada a los contactos
        contactos = [(contacto, info['Nombre'], info['Telefono']) for contacto, info in self.__contactos._informacion.items()]
        
        if len(contactos)>0:
            if len(contactos)<5:
                nregistros=len(contactos)
            else:
                nregistros=5
            # Definimos un contenedor de la tabla
            tabla_frame = tk.Frame(self.__panel_actual, bg="#2C3E50")
            tabla_frame.grid(row=2, column=0, columnspan=3, pady=0)

            # Frame de botones CRUD
            botones_crud = tk.Frame(self.__panel_actual, bg="#2C3E50")
            botones_crud.grid(row=1, column=0, columnspan=1, pady=3, padx=(0,170))

            self.__boton_modificar = tk.Button(botones_crud, 
                                text="Editar", 
                                command=self.__modificar_contacto,  
                                width=8,
                                height=1,
                                font=("Arial", 10, "bold"),
                                bg="#2980B9",
                                fg="white")
            self.__boton_modificar.grid(row=0, column=0, padx=5, pady=5)

            self.__boton_eliminar = tk.Button(botones_crud, 
                                text="Eliminar", 
                                command=self.__eliminar_contacto,
                                width=8,
                                height=1,
                                font=("Arial", 10, "bold"),
                                bg="#C0392B",
                                fg="white")
            self.__boton_eliminar.grid(row=0, column=1, padx=5, pady=5)
        
            
            self.__resultado = tk.Label(self.__panel_actual, 
                                    text="Selecciona un contacto y usa los botones 'Editar' o 'Eliminar'", 
                                    font=("Arial", 11),
                                    bg="#34495E",
                                    fg="#F39C12",
                                    padx=20,
                                    pady=10,
                                    width=43,
                                    anchor="center")
            self.__resultado.grid(row=4, column=0, columnspan=3, pady=5)
            
            scrollbar_y = tk.Scrollbar(tabla_frame, orient="vertical")
            scrollbar_y.pack(side="right", fill="y")

            # Definimos el styl para modificar el estilo del componente de la tabla
            style = ttk.Style()
            # Customizamos el cuerpo de la tabla
            style.configure("Custom.Treeview",
                            background="#2C3E50",      
                            foreground="white",          
                            fieldbackground="#2C3E50",  
                            font=("Arial", 11))
            # Customizamos el encabezado
            style.configure("Custom.Treeview.Heading",
                    background="#34495E",
                    foreground="black",
                    font=("Arial", 11, "bold"))

            style.map("Custom.Treeview",
                    background=[("selected", "#405A74")])  

            self.__tabla_contactos = ttk.Treeview(
                tabla_frame,
                columns=("ID", "Nombre", "Telefono"),
                show="headings",
                height=nregistros,
                yscrollcommand=scrollbar_y.set,
                style="Custom.Treeview" 
            )

            self.__tabla_contactos.heading("ID", text="ID")
            self.__tabla_contactos.heading("Nombre", text="Nombre")
            self.__tabla_contactos.heading("Telefono", text="Teléfono")

            self.__tabla_contactos.column("ID", width=45, anchor="center")
            self.__tabla_contactos.column("Nombre", width=180, anchor="center")
            self.__tabla_contactos.column("Telefono", width=130, anchor="center")

            self.__tabla_contactos.pack(fill="both", expand=True)
            scrollbar_y.config(command=self.__tabla_contactos.yview)


            self.__tabla_contactos.bind("<<TreeviewSelect>>", self.__on_contact_select)

            
            # Recorremos las duplas de contactos y las vamos insertanto en la tabla
            for contacto in contactos:
                
                self.__tabla_contactos.insert("", "end", values=contacto)
        else:
            # Insertamos un mensaje informativo si no hay contactos
            mensaje = tk.Label(self.__panel_actual, 
                        text="No hay contactos registrados", 
                        font=("Arial", 15, "bold"),
                        foreground="#F39C12",
                        background="#2C3E50")
            mensaje.grid(row=2, column=0, columnspan=3, pady=(15, 20), padx=40)
        self.__boton_agregar_contacto = tk.Button(self.__panel_actual, 
                            text="Agregar Contacto", 
                            command=self.añadir_contacto,
                            width=15,
                            height=1,
                            font=("Arial", 10, "bold"),
                            bg="#27AE42",
                            fg="white")
        self.__boton_agregar_contacto.grid(row=3, column=0, pady=15, padx=(0,196))
        
    
    def formulario_editar_contacto(self):
        self.__limpiarPanel()
        
        # Capturamos los nombre
        nombre_var = tk.StringVar()
        telefono_var=tk.StringVar()
        nombre_var.set(self.__contacto_seleccionado[1])
        telefono_var.set(self.__contacto_seleccionado[2])
        

        self.__panel_actual=tk.Frame(self._panel_principal, padx=10, pady=10)

        self.__panel_actual.grid(row=0, column=1, sticky="nsew")
        self.__panel_actual.grid_columnconfigure(0, weight=1)
        self.__panel_actual.grid_columnconfigure(1, weight=0)
        self.__panel_actual.grid_columnconfigure(2, weight=1)
        self.__panel_actual.configure(bg="#2C3E50")

        titulo = tk.Label(self.__panel_actual, 
                         text=f"Editar Contacto\n'{self.__contacto_seleccionado[1]}'", 
                         font=("Arial", 16, "bold"),
                         foreground="#ECF0F1",
                         background="#2C3E50")
        titulo.grid(row=0, column=0, columnspan=3, pady=(10, 0))
        
        
        label_nombre = tk.Label(self.__panel_actual, 
                                text="Nombre Nuevo:", 
                                font=("Arial", 10),
                                foreground="#ECF0F1",
                                background="#2C3E50")
        label_nombre.grid(row=1, column=1, pady=10)
        
        self.____input_nombre_nuevo = tk.Entry(self.__panel_actual, 
                               textvariable=nombre_var,
                               width=20, 
                               font=("Arial", 12),
                               bg="#FFFFFF",
                               justify='center')
        self.____input_nombre_nuevo.grid(row=2, column=1, pady=5)
        self.____input_nombre_nuevo.focus()

        label_telefono = tk.Label(self.__panel_actual, 
                                text="Telefono Nuevo:", 
                                font=("Arial", 10),
                                foreground="#ECF0F1",
                                background="#2C3E50")
        label_telefono.grid(row=3, column=1, pady=10)
        
        self.____input_telefono_nuevo = tk.Entry(self.__panel_actual,
                               textvariable=telefono_var,
                               width=20, 
                               font=("Arial", 12),
                               bg="#FFFFFF",
                               justify='center')
        self.____input_telefono_nuevo.grid(row=4, column=1, pady=5)
        self.____input_telefono_nuevo.focus()
        
        
        botones_frame = tk.Frame(self.__panel_actual, bg="#2C3E50")
        botones_frame.grid(row=5, column=1, pady=15)
        
        self.boton_confirmar_edicion = tk.Button(botones_frame, 
                                  text="Confirmar Edición", 
                                  command=self.__confirmar_edicion,
                                  width=15,
                                  height=1,
                                  font=("Arial", 10, "bold"),
                                  bg="#2980B9",
                                  fg="white")
        self.boton_confirmar_edicion.grid(row=0, column=0, padx=5, pady=5)
        
        self.boton_cancelar_edicion = tk.Button(botones_frame, 
                                   text="Cancelar Edición", 
                                   command=self.__cancelar_edicion,
                                   width=15,
                                   height=1,
                                   font=("Arial", 10, "bold"),
                                   bg="#C0392B",
                                   fg="white")
        self.boton_cancelar_edicion.grid(row=0, column=1, padx=5, pady=5)
        

        
        
        self.__resultado = tk.Label(self.__panel_actual, 
                                 text="Recuerda ingresar valores validos ;)", 
                                 font=("Arial", 11),
                                 bg="#34495E",
                                 fg="#F39C12",
                                 padx=20,
                                 pady=10,
                                 width=35,
                                 anchor="center")
        self.__resultado.grid(row=6, column=1, pady=(5, 10))
        
        
        info_enter = tk.Label(self.__panel_actual, 
                             text="Al presionar 'Enter' se actualizara el contacto", 
                             font=("Arial", 8),
                             foreground="#BDC3C7",
                             background="#2C3E50")
        info_enter.grid(row=7, column=1, pady=5)

        self.____input_nombre_nuevo.bind('<Return>', lambda event: self.__confirmar_edicion())
        self.____input_telefono_nuevo.bind('<Return>', lambda event: self.__confirmar_edicion())
        
    def añadir_contacto(self):
        self.__limpiarPanel()
        self.__contacto_seleccionado=None
        
        # self._panel_principal.geometry("400x380")
        self.__panel_actual=tk.Frame(self._panel_principal, padx=10, pady=10)

        self.__panel_actual.grid(row=0, column=1, sticky="nsew")
        self.__panel_actual.grid_columnconfigure(0, weight=1)
        self.__panel_actual.grid_columnconfigure(1, weight=0)
        self.__panel_actual.grid_columnconfigure(2, weight=1)
        self.__panel_actual.configure(bg="#2C3E50")

        titulo = tk.Label(self.__panel_actual, 
                         text="Añadir contacto", 
                         font=("Arial", 16, "bold"),
                         foreground="#ECF0F1",
                         background="#2C3E50")
        titulo.grid(row=0, column=0, columnspan=3, pady=15)
        
        
        label_nombre = tk.Label(self.__panel_actual, 
                                text="Nombre Contacto:", 
                                font=("Arial", 10),
                                foreground="#ECF0F1",
                                background="#2C3E50")
        label_nombre.grid(row=1, column=1, pady=10)
        
        self.__input_nombre = tk.Entry(self.__panel_actual, 
                               width=20, 
                               font=("Arial", 12),
                               bg="#FFFFFF",
                               justify='center')
        self.__input_nombre.grid(row=2, column=1, pady=5)
        self.__input_nombre.focus()

        label_telefono = tk.Label(self.__panel_actual, 
                                text="Número Telefono:", 
                                font=("Arial", 10),
                                foreground="#ECF0F1",
                                background="#2C3E50")
        label_telefono.grid(row=3, column=1, pady=10)
        
        self.__input_telefono = tk.Entry(self.__panel_actual, 
                               width=20, 
                               font=("Arial", 12),
                               bg="#FFFFFF",
                               justify='center')
        self.__input_telefono.grid(row=4, column=1, pady=5)
        self.__input_telefono.focus()
        
        
        botones_frame = tk.Frame(self.__panel_actual, bg="#2C3E50")
        botones_frame.grid(row=5, column=1, pady=15)
        
        self.boton_crear_contacto = tk.Button(botones_frame, 
                                  text="Crear Contacto", 
                                  command=self.__guardarContacto,
                                  width=13,
                                  height=1,
                                  font=("Arial", 10, "bold"),
                                  bg="#27AE42",
                                  fg="white")
        self.boton_crear_contacto.grid(row=0, column=0, padx=5, pady=5)
        
        self.boton_ver_contactos = tk.Button(botones_frame, 
                                   text="Ver Contactos", 
                                   command=self.ver_contactos,
                                   width=13,
                                   height=1,
                                   font=("Arial", 10, "bold"),
                                   bg="#2980B9",
                                   fg="white")
        self.boton_ver_contactos.grid(row=0, column=1, padx=5, pady=5)
        

        
        
        self.__resultado = tk.Label(self.__panel_actual, 
                                 text="Recuerda ingresar valores validos ;)", 
                                 font=("Arial", 11),
                                 bg="#34495E",
                                 fg="#F39C12",
                                 padx=20,
                                 pady=10,
                                 width=35,
                                 anchor="center")
        self.__resultado.grid(row=6, column=1, pady=(5, 10))
        
        
        info_enter = tk.Label(self.__panel_actual, 
                             text="Al presionar 'Enter' se guardara el contacto", 
                             font=("Arial", 8),
                             foreground="#BDC3C7",
                             background="#2C3E50")
        info_enter.grid(row=7, column=1, pady=5)

        self.__input_nombre.bind('<Return>', lambda event: self.__guardarContacto())
        self.__input_telefono.bind('<Return>', lambda event: self.__guardarContacto())
    
    # Metodo para capturar el registro deleccionado de la tabla
    def __on_contact_select(self, event):
        seleccionado = self.__tabla_contactos.selection()
        if seleccionado:
            valores = self.__tabla_contactos.item(seleccionado[0], "values")
            self.__contacto_seleccionado=valores
            nombre = valores[1]
            self.__resultado.config(text=f"Contacto de '{nombre}' seleccionado", fg="#27AE42")
        else:
            self.__resultado.config(text="Selecciona un contacto y usa los botones 'Editar' o 'Eliminar'")
    
    # Metodo para eliminar el contaco seleccionado
    def __eliminar_contacto(self):
        try:
            if not self.__contacto_seleccionado:
                raise Exception("Aun no se ha seleccionado ningún contacto")
            else:
                respuesta = messagebox.askyesno(
                "Confirmar eliminación",
                f"¿Seguro que deseas eliminar el contacto '{self.__contacto_seleccionado[1]}'?"
            )
                if respuesta:
                    self.__contactos._eliminar_contacto(self.__contacto_seleccionado)
                    messagebox.showinfo("Contacto eliminado", f"El contacto de '{self.__contacto_seleccionado[1]}' ha sido eiminado exitosamente.")   
                    self.__contacto_seleccionado=None
                    self.ver_contactos()
                else:
                    messagebox.showerror("Accion Cancelada", f"La eliminacion del contacto '{self.__contacto_seleccionado[1]}' ha sido cancelada ")
        except Exception as e:
            messagebox.showerror("Error de seleccion", str(e))
    
    def __guardarContacto(self):
        try:
            nombre = str(self.__input_nombre.get())
            telefono = str(self.__input_telefono.get())
            self.__contactos._crear_contacto(nombre, telefono)
            messagebox.showinfo("Contacto guardado", f"El contacto de '{nombre}' ha sido guardado exitosamente.")
            self.ver_contactos() 
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.__resultado.config(text=e, fg="#FF3838")

    def __modificar_contacto(self):
        try:
            if not self.__contacto_seleccionado:
                raise Exception("Aun no se ha seleccionado ningún contacto")
            else:
                self.formulario_editar_contacto()
                
        except Exception as e:
            messagebox.showerror("Error de seleccion", str(e))


    def __confirmar_edicion(self):

        try:
            id=self.__contacto_seleccionado[0]
            nombre_nuevo = str(self.____input_nombre_nuevo.get())
            telefono_nuevo = str(self.____input_telefono_nuevo.get())
            self.__contactos._editar_contacto(id, nombre_nuevo, telefono_nuevo)
            messagebox.showinfo("Actualización exitosa", f"El contacto de '{self.__contacto_seleccionado[1]}' ha sido actualizado exitosamente.")
            self.__contacto_seleccionado=None
            self.ver_contactos()

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.__resultado.config(text=e, fg="#FF3838")

    def __cancelar_edicion(self):
        messagebox.showerror("Edición cancelada", f"La edicion del contacto '{self.__contacto_seleccionado[1]}' ha sido cancelada")
        self.__contacto_seleccionado=None
        self.ver_contactos()

class Main:
    @staticmethod
    def main():
        app = Interfaz()
        app._panel_principal.mainloop()

    
# Condicional para ejecutar el programa prinicipal
if __name__ == "__main__":
    Main.main()