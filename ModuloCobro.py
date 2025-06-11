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

         # --- Barra superior ---
        top_frame = Frame(self, bg="lightblue", bd=2, relief="groove")
        top_frame.pack(side="top", fill="x", pady=10, padx=10)

        label_titulo_cobro = Label(top_frame, text="Pantalla de Cobro", font=("Arial", 16), bg="#b5daff")
        label_titulo_cobro.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

        # Input para código
        self.input_codigo = Entry(self)
        self.input_codigo.grid(row=1, column=0, padx=10, pady=5)

        # Botón agregar
        self.boton_agregar = Button(self, text="Agregar", command=self.agregar_producto, bg="#b5f5ff")
        self.boton_agregar.grid(row=1, column=1, padx=10, pady=5)

        # Lista visual
        self.lista = Listbox(self, width=40)
        self.lista.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

        # Botón volver
        self.boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame("PantallaPrincipal"), bg="#b5f5ff")
        self.boton_volver.grid(row=2, column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")

        # Boton eliminar ultimo producto registrado
        self.boton_eliminar = Button(self, text="Eliminar último producto", command=lambda: self.lista.delete(END), bg="#ffb5b5")
        self.boton_eliminar.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

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