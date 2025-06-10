from tkinter import Frame, Label, Button, messagebox, Entry, Listbox, END
from Productos import productos

class PantallaCobro(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#052d55", width=900, height=450)
        self.grid_propagate(False)
        self.master = master

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        label_titulo_cobro = Label(self, text="Pantalla de Cobro", font=("Arial", 16), bg="#b5daff")
        label_titulo_cobro.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

        # Input para código
        self.input_codigo = Entry(self)
        self.input_codigo.grid(row=1, column=0, padx=10, pady=5)

        # Botón agregar
        self.boton_agregar = Button(self, text="Agregar", command=self.agregar_producto, bg="#b5f5ff")
        self.boton_agregar.grid(row=1, column=1, padx=10, pady=5)

        # Lista visual
        self.lista = Listbox(self, width=40)
        self.lista.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Total a pagar
        self.label_total = Label(self, text="Total: $0.00", font=("Arial", 14), bg="#b5daff")
        self.label_total.grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")

        # Botones de pago
        self.boton_efectivo = Button(self, text="Efectivo", command=lambda: self.finalizar_compra("efectivo"), bg="#b5ffb5")
        self.boton_credito = Button(self, text="Tarjeta de Crédito", command=lambda: self.finalizar_compra("credito"), bg="#b5b5ff")
        self.boton_debito = Button(self, text="Tarjeta de Débito", command=lambda: self.finalizar_compra("debito"), bg="#ffd6b5")
        self.boton_efectivo.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        self.boton_credito.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        self.boton_debito.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        self.boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame("PantallaPrincipal"), bg="#b5f5ff")
        self.boton_volver.grid(row=6, column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")

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

    def finalizar_compra(self, metodo):
        if not self.lista_productos:
            messagebox.showwarning("Atención", "Debe agregar al menos un producto.")
            return
        messagebox.showinfo("Compra finalizada", f"Compra realizada por ${self.total:.2f} con {metodo}.")
        self.lista.delete(0, END)
        self.lista_productos.clear()
        self.total = 0.0
        self.label_total.config(text="Total: $0.00")