from tkinter import Frame, Label, Button, messagebox, Entry, Listbox, END
from Productos import productos

class PantallaCobro(Frame):
    def __init__(self, master):
        # 1024x768
        super().__init__(master, bg="#052d55", width=1024, height=768)
        self.grid_propagate(False)
        self.master = master
        


        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

         # - - - Barra superior
        top_frame = Frame(self, bg="lightblue", bd=2, relief="groove")
        top_frame.pack(side="top", fill="both")
        top_frame.config(bg="#f5f5f6", border=0)


        
        label_titulo_cobro = Label(top_frame, text="Cobro", font=("Arial", 16), bg="#f5f5f6")
        label_titulo_cobro.pack(side="left", padx=20)

        # Input para código
        label_codigo = Label(top_frame, text="Código del producto", font=("Arial", 11), bg="#f5f5f6", fg="black")
        label_codigo.pack(side="left", padx=20)
        
        self.input_codigo = Entry(top_frame, font=("Arial", 14), width=30)
        self.input_codigo.pack(side="left", fill="x", expand=True, padx=20)

        # - - - Area de contenido principal
        contenido_Principal = Frame(self, padx=10, pady=10, bg="#f5f5f6")
        contenido_Principal.pack(fill="both", expand=True)
        contenido_Principal.grid_columnconfigure(0, weight=1)  # Columna izquierda se expande al cambiar el tamaño de la ventana
        contenido_Principal.grid_columnconfigure(1, weight=3)  # Columna derecha se expande
        contenido_Principal.grid_rowconfigure(0, weight=1)    # Fila superior se expande
        contenido_Principal.grid_rowconfigure(1, weight=0)    # Fila central (total) es fija
        contenido_Principal.grid_rowconfigure(2, weight=0)    # Fila inferior (pagar) es fija

        # - - Panel izquierdo
        panel_izquierdo = Frame(contenido_Principal, bg="#f5f5f6")
        panel_izquierdo.grid(row=0, column=0, rowspan=3, sticky="nsew")

        # imagen
        # prueba si la imagen se carga correctamente
        # Si no se carga, muestra un texto de marcador de posición
        try:
            from PIL import Image, ImageTk
            img = Image.open("images/modCobro.png")
            image_label = Label(panel_izquierdo, image=ImageTk.PhotoImage(img))
            image_label.image = ImageTk.PhotoImage(img)  # Mantener una referencia
            image_label.pack(pady=10, padx=10, fill="x")
        except Exception as e:
            print(f"No se pudo cargar la imagen: {e}")
            placeholder_label = Label(panel_izquierdo, text="[Imagen Aquí]", font=("Arial", 12), bg="#f5f5f6")
            placeholder_label.pack(pady=10, padx=10, fill="x")
                
        # Botón agregar
        self.boton_agregar = Button(self, text="Agregar", command=self.agregar_producto, bg="#b5f5ff", font=("Arial", 14))
        self.boton_agregar.pack(fill="x", pady=5, padx=10)
        
        # Boton eliminar ultimo producto registrado
        self.boton_eliminar = Button(self, text="Eliminar último producto", command=lambda: self.lista.delete(END), bg="#ffb5b5", font=("Arial", 14))
        self.boton_eliminar.pack(fill="x", pady=5, padx=10)

        # Botón volver
        self.boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame("PantallaPrincipal"), bg="#b5f5ff", font=("Arial", 14))
        self.boton_volver.pack(fill="x", pady=5, padx=10)




        # - - Panel derecho - parte de la lista de productos
        panel_derecho = Frame(contenido_Principal, bg="#f5f5f6")
        panel_derecho.grid(row=0, column=1, sticky="nsew")

        nombreLab = Label(panel_derecho, text="Productos Agregados", font=("Arial", 14), bg="#f5f5f6")
        nombreLab.pack(pady=10, padx=10, fill="x")

        # Lista
        self.lista = Listbox(panel_derecho, width=40)
        self.lista.pack(padx=10, pady=5)



        # Total a pagar
        self.label_total = Label(self, text="Total: $0.00", font=("Arial", 14), bg="#b5daff")
        self.label_total.grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")

        # Boton de pago
        self.boton_pagar = Button(self, text="Pagar", command=self.finalizar_compra, bg="#b5ffb5")
        self.boton_pagar.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        

        

        # Variables de control
        self.lista_productos = []
        self.total = 0.0

        # Diccionario de productos por códigoProd
        self.precios = {str(prod["codigoProd"]): (prod["nombre"], prod["precio"]) for prod in productos}

    def agregar_producto(self):
        codigo = self.input_codigo.get()
        if codigo in self.precios:
            nombre, precio = self.precios[codigo]
            self.lista_productos.append((nombre, precio))
            self.lista.insert(END, f"{nombre} - ${precio:.2f}")
            self.total += precio
            self.label_total.config(text=f"Total: ${self.total:.2f}")
            self.input_codigo.delete(0, END)
        else:
            messagebox.showwarning("Código inválido", "El código no existe.")

    def finalizar_compra(self):
        if not self.lista_productos:
            messagebox.showwarning("Atención", "Debe agregar al menos un producto.")
            return
        messagebox.showinfo("Compra finalizada", f"Compra realizada por ${self.total:.2f}.")
        self.lista.delete(0, END)
        self.lista_productos.clear()
        self.total = 0.0
        self.label_total.config(text="Total: $0.00")