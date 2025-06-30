from tkinter import Frame, Label, Button, messagebox, Entry, Listbox, END, Scrollbar
from PIL import Image, ImageTk
import gestor_productos #  módulo de gestion de productos

class PantallaCobro(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f5f5f6", width=900, height=450)
        self.grid_propagate(False)
        self.master = master
        

        # Configuración de la cuadrícula: permite que las columnas se expandan
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

         # - - - Barra superior
        top_frame = Frame(self, bg="lightblue", bd=2, relief="groove")
        top_frame.pack(side="top", fill="both", pady=10)
        top_frame.config(bg="#f5f5f6", border=0)

        # texto de título
        label_titulo_cobro = Label(top_frame, text="Cobro", font=("Arial", 16), bg="#f5f5f6")
        label_titulo_cobro.pack(side="left", padx=20)

        # texto de código del producto
        label_codigo = Label(top_frame, text="Código del producto", font=("Arial", 11), bg="#f5f5f6", fg="black")
        label_codigo.pack(side="left", padx=(210, 10))
        
        

        # - - - Area de contenido principal
        contenido_Principal = Frame(self, padx=10, pady=10, bg="#f5f5f6")
        contenido_Principal.pack(fill="both", expand=True)
        # Se expande
        contenido_Principal.grid_columnconfigure(0, weight=1)  
        contenido_Principal.grid_columnconfigure(1, weight=3)  
        contenido_Principal.grid_rowconfigure(0, weight=1)    
        contenido_Principal.grid_rowconfigure(1, weight=0)    
        contenido_Principal.grid_rowconfigure(2, weight=0)    


        # - - Panel izquierdo
        panel_izquierdo = Frame(contenido_Principal, bg="#f5f5f6")
        panel_izquierdo.grid(row=0, column=0, rowspan=4, columnspan=1, sticky="nsew", padx=5, pady=5)  # Ocupa varias filas
        panel_izquierdo.config(border=0)


        # imagen
        # prueba si la imagen se carga correctamente
        # Si no se carga, muestra un texto de marcador de posición
        try:
            img = Image.open("Images/modCobro.png")
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            imgtk = ImageTk.PhotoImage(img)
            image_label = Label(panel_izquierdo, image=imgtk, bg="#f5f5f6")
            image_label.image = imgtk  # Mantener una referencia
            image_label.pack(pady=10, padx=10, fill="x")

        except Exception as e:
            print(f"No se pudo cargar la imagen: {e}")
            placeholder_label = Label(panel_izquierdo, text="[Imagen Aquí]", font=("Arial", 12), bg="#f5f5f6")
            placeholder_label.pack(pady=10, padx=10, fill="x")
                
        # Botón agregar
        self.boton_agregar = Button(panel_izquierdo, text="Agregar", command=self.agregar_producto, bg="#adadc2", font=("Arial", 14))
        self.boton_agregar.pack(fill="x", pady=5, padx=10)
        
        # Boton eliminar ultimo producto registrado
        # ¡AQUÍ ESTÁ EL CAMBIO! Ahora llama a un nuevo método `eliminar_ultimo_producto_en_cobro`
        self.boton_eliminar = Button(panel_izquierdo, text="Eliminar último producto", command=self.eliminar_ultimo_producto_en_cobro, bg="#adadc2", font=("Arial", 14))
        self.boton_eliminar.pack(fill="x", pady=5, padx=10)

        # Botón volver
        self.boton_volver = Button(panel_izquierdo, text="Volver", command=lambda: master.mostrar_frame("PantallaPrincipal"), bg="#adadc2", font=("Arial", 14))
        self.boton_volver.pack(fill="x", pady=5, padx=10)



        # - - Panel derecho - parte de la lista de productos
        panel_derecho = Frame(contenido_Principal, bg="#f5f5f6")
        panel_derecho.grid(row=0, column=1, sticky="nsew")

        ## Input para código de producto
        self.input_codigo = Entry(panel_derecho, font=("Arial", 15), bg="#d8e1e6", fg="black")
        self.input_codigo.pack(side="top", fill="x", expand=True, padx=10,pady=1)
        self.input_codigo.bind("<Return>", lambda event: self.agregar_producto()) # permite agregar el producto al presionar el boton Enter

        # texto
        nombreLab = Label(panel_derecho, text="Productos Agregados", font=("Arial", 11), bg="#f5f5f6")
        nombreLab.pack(pady=0, padx=(0,400), fill="x")


        # Lista
        self.lista = Listbox(panel_derecho, width=40, bg="#d3d7dd", font=("Arial", 12), selectmode="single")
        self.lista.pack(fill="both", expand=True, padx=10, pady=5)


        # - - Panel derecho Total a pagar
        panel_derecho_total = Frame(contenido_Principal, bg="#d3d7dd")
        panel_derecho_total.grid(row=1, column=1, sticky="nsew", pady=10)

        # Asegúrate de que la fila 1 pueda expandirse
        contenido_Principal.grid_rowconfigure(1, weight=1)

        self.label_total = Label(panel_derecho_total, text="Total: $0.00", font=("Arial", 14), bg="#f5f5f6")
        self.label_total.pack(fill="both", expand=True)

        # - - Panel derecho Boton de pago
        panel_derecho_pago = Frame(contenido_Principal, bg="#f5f5f6")
        panel_derecho_pago.grid(row=3, column=1, columnspan=2, sticky="nsew", pady=(10,20))

        # Asegúrate de que la fila 3 pueda expandirse
        contenido_Principal.grid_rowconfigure(3, weight=1)

        # boton
        self.boton_pagar = Button(panel_derecho_pago, text="Pagar", command=self.finalizar_compra, bg="#3a2d97", fg="white", font=("Arial", 14))
        self.boton_pagar.config(height=2, width=20)
        self.boton_pagar.pack(fill="both", expand=True)


        # Variables de control
        self.lista_productos_en_cobro = [] # Usar un nombre más descriptivo para los productos en la transacción actual
        self.total = 0.0


    def agregar_producto(self):
        codigo = self.input_codigo.get().strip() # .strip() para eliminar espacios en blanco
        if not codigo: # Validar que el campo no esté vacío
            messagebox.showwarning("Entrada Vacía", "Por favor, ingrese un código de producto.")
            return

        # Obtenemos el producto del gestor, que leerá del JSON
        producto_encontrado = gestor_productos.buscar_producto_por_codigo(codigo)
        
        if producto_encontrado:
            nombre = producto_encontrado['nombre']
            precio = producto_encontrado['precio']
            # Guarda el nombre y precio en la lista interna
            self.lista_productos_en_cobro.append((nombre, precio)) 
            self.lista.insert(END, f"{nombre} - ${precio:.2f}")
            self.total += precio
            self.label_total.config(text=f"Total: ${self.total:.2f}")
            self.input_codigo.delete(0, END)
        else:
            messagebox.showwarning("Código inválido", f"El producto con código '{codigo}' no existe.")

    def eliminar_ultimo_producto_en_cobro(self):
        """
        Elimina el último producto de la lista visual y descuenta su precio del total.
        """
        if self.lista_productos_en_cobro: # Asegura de que haya productos para eliminar
            # Elimina el último elemento de la lista interna
            nombre_producto_eliminado, precio_producto_eliminado = self.lista_productos_en_cobro.pop()
            
            # Elimina el último elemento de la Listbox visual
            self.lista.delete(END)
            
            # Descuenta el precio del total
            self.total -= precio_producto_eliminado
            self.label_total.config(text=f"Total: ${self.total:.2f}")
            messagebox.showinfo("Producto Eliminado", f"Se eliminó '{nombre_producto_eliminado}' de la lista de cobro.")
        else:
            messagebox.showwarning("Atención", "No hay productos en la lista para eliminar.")


    def finalizar_compra(self):
        if not self.lista_productos_en_cobro:
            messagebox.showwarning("Atención", "Debe agregar al menos un producto.")
            return
        messagebox.showinfo("Compra finalizada", f"Compra realizada por ${self.total:.2f}.")
        self.lista.delete(0, END)
        self.lista_productos_en_cobro.clear()
        self.total = 0.0
        self.label_total.config(text="Total: $0.00")