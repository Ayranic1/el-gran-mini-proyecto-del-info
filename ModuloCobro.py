from tkinter import Frame, Label, Button, Checkbutton, IntVar, messagebox
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

        self.vars = []
        self.checks = []
        self.label_total = Label(self, text="Total: $0.00", font=("Arial", 14), bg="#b5daff")
        self.label_total.grid(row=100, column=0, columnspan=2, pady=(10,0), sticky="ew")

        self.boton_calcular = Button(self, text="Calcular Total", command=self.calcular_total, bg="#b5f5ff")
        self.boton_calcular.grid(row=101, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

        self.boton_efectivo = Button(self, text="Efectivo", command=lambda: self.finalizar_compra("efectivo"), bg="#b5ffb5")
        self.boton_credito = Button(self, text="Tarjeta de Crédito", command=lambda: self.finalizar_compra("credito"), bg="#b5b5ff")
        self.boton_debito = Button(self, text="Tarjeta de Débito", command=lambda: self.finalizar_compra("debito"), bg="#ffd6b5")

        self.label_acumulados = Label(self, text="", font=("Arial", 12), bg="#b5daff", anchor="w", justify="left")
        self.label_acumulados.grid(row=110, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

        # Cambia aquí: usa string en mostrar_frame
        self.boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame("PantallaPrincipal"), bg="#b5f5ff")
        self.boton_volver.grid(row=120, column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")

        self.monto_actual = 0.0
        self.total_compras = 0.0
        self.total_efectivo = 0.0
        self.total_credito = 0.0
        self.total_debito = 0.0

        self.actualizar_lista()

    def actualizar_lista(self):
        # Aquí va tu lógica para actualizar la lista de productos y los widgets
        self.limpiar_checks()
        self.vars = []
        self.checks = []
        for idx, prod in enumerate(productos):
            var = IntVar()
            check = Checkbutton(self, text=f"{prod['nombre']} - ${prod['precio']:.2f}", variable=var, bg="#b5daff")
            check.grid(row=1+idx, column=0, columnspan=2, sticky="w", padx=20)
            self.vars.append(var)
            self.checks.append(check)
        self.label_total.config(text="Total: $0.00")
        self.monto_actual = 0.0
        self.actualizar_acumulados()

    def limpiar_checks(self):
        for check in getattr(self, "checks", []):
            check.destroy()

    def calcular_total(self):
        total = 0.0
        for var, prod in zip(self.vars, productos):
            if var.get():
                total += prod["precio"]
        self.monto_actual = total
        self.label_total.config(text=f"Total: ${total:.2f}")

        # Muestra los botones de pago solo si hay monto
        if total > 0:
            self.boton_efectivo.grid(row=102, column=0, padx=10, pady=(5,5), sticky="ew")
            self.boton_credito.grid(row=102, column=1, padx=10, pady=(5,5), sticky="ew")
            self.boton_debito.grid(row=103, column=0, columnspan=2, padx=10, pady=(5,10), sticky="ew")
        else:
            self.boton_efectivo.grid_remove()
            self.boton_credito.grid_remove()
            self.boton_debito.grid_remove()

    def finalizar_compra(self, metodo):
        if self.monto_actual == 0:
            messagebox.showwarning("Atención", "Debe seleccionar al menos un producto.")
            return
        self.total_compras += self.monto_actual
        if metodo == "efectivo":
            self.total_efectivo += self.monto_actual
        elif metodo == "credito":
            self.total_credito += self.monto_actual
        elif metodo == "debito":
            self.total_debito += self.monto_actual
        messagebox.showinfo("Compra finalizada", f"Compra realizada por ${self.monto_actual:.2f} con {metodo}.")
        self.actualizar_lista()

    def actualizar_acumulados(self):
        texto = (
            f"Total ventas: ${self.total_compras:.2f}\n"
            f"Total efectivo: ${self.total_efectivo:.2f}\n"
            f"Total crédito: ${self.total_credito:.2f}\n"
            f"Total débito: ${self.total_debito:.2f}"
        )
        self.label_acumulados.config(text=texto)