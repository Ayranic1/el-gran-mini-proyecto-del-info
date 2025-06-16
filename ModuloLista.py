from tkinter import Frame, Label, Button, Entry, Toplevel, messagebox, Listbox, END
import gestor_productos # Cambiado de 'Productos' a 'gestor_productos'

class PantallaListaProductos(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#3a2d97", width=900, height=450)
        self.grid_propagate(False)
        self.master = master
        

        # Configuración de la cuadrícula: permite que las columnas se expandan
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)  
        self.grid_rowconfigure(2, weight=1)  

        # encabezado de la pantalla
        encabezado = Frame(self, bg="#f5f5f6", height=50)
        encabezado.pack(fill="x")
        encabezado.grid(row=0, column=0, columnspan=3, sticky="ew")


        texto_titulo = Label(encabezado, text="Lista de Productos", font=("Arial", 16), bg="#f5f5f6")
        texto_titulo.pack(side="left", padx=10, pady=10)


        # Parte principal de la pantalla - LISTA DE PRODUCTOS

        contenido_principal = Frame(self, bg="#f5f5f6")
        contenido_principal.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

        self.lista = Listbox(contenido_principal, height= 15, font=("Arial", 12))
        self.lista.pack(side="top", fill="both", expand=True)
        

        self.actualizar_lista() # Llama a la función para llenar la lista con los productos actuales
        
        # - - PIE DE PANTALLA
        pie = Frame(self, bg="#f5f5f6", height=100) # Cambiado el color a algo que combine más
        pie.grid(row=2, column=0, columnspan=3, rowspan=2, sticky="nsew")


        boton_agregar = Button(pie, text="Agregar", command=self.agregar, bg="#3a2d97", fg="white")
        boton_agregar.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        colorBoton = "#adadc2"

        boton_editar = Button(pie, text="Editar", command=self.iniciar_edicion, bg=colorBoton) 
        boton_editar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        boton_eliminar = Button(pie, text="Eliminar", command=self.eliminar, bg=colorBoton)
        boton_eliminar.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        boton_volver = Button(pie, text="Volver", command=lambda: master.mostrar_frame("PantallaPrincipal"), bg=colorBoton)
        boton_volver.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

        # Configurar la expansión de columnas en el pie
        pie.grid_columnconfigure(0, weight=1)
        pie.grid_columnconfigure(1, weight=1)
        pie.grid_columnconfigure(2, weight=1)
        pie.grid_columnconfigure(3, weight=1)


    def agregar(self):
        ventana = Toplevel(self)
        ventana.title("Agregar Producto")
        ventana.geometry("300x200") # Aumentado el tamaño para el código
        ventana.configure(bg="#f5f5f6")

        # Icono de la ventana
        try:
            ventana.iconbitmap("Images/icono.ico")
        except Exception as e:
            print(f"Advertencia: No se pudo cargar el icono: {e}")

        Label(ventana, text="Código del producto:", bg="#f5f5f6").pack(pady=(10,0))
        entry_codigo = Entry(ventana, bg="#d8e1e6")
        entry_codigo.pack(pady=5)

        Label(ventana, text="Nombre del producto:", bg="#f5f5f6").pack()
        entry_nombre = Entry(ventana, bg="#d8e1e6")
        entry_nombre.pack(pady=5)

        Label(ventana, text="Precio:", bg="#f5f5f6").pack()
        entry_precio = Entry(ventana, bg="#d8e1e6")
        entry_precio.pack(pady=5)

        def agregarProducto():
            codigo = entry_codigo.get().strip()
            nombre = entry_nombre.get().strip()
            try:
                precio = float(entry_precio.get())
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número válido.")
                return
            
            if not codigo or not nombre:
                messagebox.showerror("Error", "Código y nombre no pueden estar vacíos.")
                return

            # Usar la función del gestor de productos
            exito, mensaje = gestor_productos.agregar_producto(codigo, nombre, precio)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
            else:
                messagebox.showerror("Error", mensaje)
            ventana.destroy()

        Button(ventana, text="Agregar", command=agregarProducto, bg="#3a2d97", fg="white").pack(pady=10)


    def eliminar(self):
        seleccion = self.lista.curselection()
        if seleccion:
            idx = seleccion[0]
            # Obtener el producto de la lista visual para extraer el código
            # Asumiendo que el formato es "Código - Nombre - $Precio"
            item_texto = self.lista.get(idx)
            try:
                codigo = item_texto.split(' ')[0] # se divide la cadena (split) y se toma el primer elemento de la lista

                # Confirmación antes de eliminar
                confirmar = messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro que desea eliminar el producto con código {codigo}?")
                if confirmar:
                    exito, mensaje = gestor_productos.eliminar_producto(codigo)
                    if exito:
                        messagebox.showinfo("Éxito", mensaje)
                        self.actualizar_lista()
                    else:
                        messagebox.showerror("Error", mensaje)
            except Exception:
                messagebox.showerror("Error", "No se pudo obtener el código del producto para eliminar.")
        else:
            messagebox.showwarning("Atención", "Debe seleccionar un producto para eliminar.")

    def iniciar_edicion(self):
        seleccion = self.lista.curselection()
        if seleccion:
            idx = seleccion[0] # indice del elemento seleccionado
            item_texto = self.lista.get(idx)
            try:
                codigo = item_texto.split(' ')[0] # Asume que el código es la primera palabra
                self.ventana_editar_producto(codigo) # Pasamos el código directamente
            except Exception:
                messagebox.showerror("Error", "No se pudo obtener el código del producto para editar.")
        else:
            messagebox.showwarning("Atención", "Debe seleccionar un producto para editar.")

    def actualizar_lista(self):
        self.lista.delete(0, END) # Limpia la lista actual
        # Obtiene la lista más reciente del gestor de productos
        productos_actuales = gestor_productos.obtener_todos_los_productos()
        
        # Vuelve a llenar la lista con los productos actuales
        for producto in productos_actuales:
            self.lista.insert(END, f"{producto['codigoProd']} - {producto['nombre']} - ${producto['precio']:.2f}")


    def ventana_editar_producto(self, codigo_producto):
        producto = gestor_productos.buscar_producto_por_codigo(codigo_producto)
        if not producto:
            messagebox.showerror("Error", "Producto no encontrado para editar.")
            return

        ventana = Toplevel(self)
        ventana.title(f"Editar Producto: {producto['nombre']}")
        ventana.geometry("300x150")
        ventana.configure(bg="#f5f5f6") 

        # carga de icono
        try:
            ventana.iconbitmap("Images/icono.ico")
        except Exception as e:
            print(f"Advertencia: No se pudo cargar el icono: {e}")


        Label(ventana, text="Nombre:", bg="#f5f5f6").pack(pady=(10,0))
        entry_nombre = Entry(ventana, bg="#d8e1e6")
        entry_nombre.insert(0, producto["nombre"])
        entry_nombre.pack(pady=5)

        Label(ventana, text="Precio:", bg="#f5f5f6").pack()
        entry_precio = Entry(ventana, bg="#d8e1e6")
        entry_precio.insert(0, str(producto["precio"]))
        entry_precio.pack(pady=5)

        def guardar_cambios():
            nuevo_nombre = entry_nombre.get().strip()
            try:
                nuevo_precio = float(entry_precio.get())
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número válido.")
                return
            
            if not nuevo_nombre:
                messagebox.showerror("Error", "El nombre no puede estar vacío.")
                return

            # Usar la función del gestor de productos para modificar
            exito, mensaje = gestor_productos.modificar_producto(codigo_producto, nuevo_nombre, nuevo_precio)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self.actualizar_lista() # Refresca la lista visual
            else:
                messagebox.showerror("Error", mensaje)
            ventana.destroy()

        Button(ventana, text="Guardar", command=guardar_cambios, bg="#3a2d97", fg="white").pack(pady=10)