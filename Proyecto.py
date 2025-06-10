import tkinter as tk
from tkinter import messagebox

class SistemaCaja:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Caja para Supermercado")
        self.lista_productos = []
        self.total = 0

        # Simulación de precios (por código de producto)
        self.precios = {
            "123": ("Leche", 10),
            "456": ("Pan", 5),
            "789": ("Huevos", 12)
        }

        # Input para código
        self.input_codigo = tk.Entry(root)
        self.input_codigo.grid(row=0, column=0)

        # Botón agregar
        self.boton_agregar = tk.Button(root, text="Agregar", command=self.agregar_producto)
        self.boton_agregar.grid(row=0, column=1)

        # Lista visual
        self.lista = tk.Listbox(root, width=40)
        self.lista.grid(row=1, column=0, columnspan=2)

        # Total a pagar
        self.label_total = tk.Label(root, text="Total: $0", bg="lightgray")
        self.label_total.grid(row=2, column=0, columnspan=2, pady=5)

        # Botón pagar
        self.boton_pagar = tk.Button(root, text="Pagar", command=self.pagar)
        self.boton_pagar.grid(row=3, column=0, columnspan=2)

    def agregar_producto(self):
        codigo = self.input_codigo.get()
        if codigo in self.precios:
            nombre, precio = self.precios[codigo]
            self.lista_productos.append((nombre, precio))
            self.lista.insert(tk.END, f"{nombre} - ${precio}")
            self.total += precio
            self.label_total.config(text=f"Total: ${self.total}")
            self.input_codigo.delete(0, tk.END)
        else:
            messagebox.showwarning("Código inválido", "El código no existe.")

    def pagar(self):
        if self.lista_productos:
            messagebox.showinfo("Pago realizado", f"Total pagado: ${self.total}\nGracias por su compra.")
            self.lista.delete(0, tk.END)
            self.lista_productos.clear()
            self.total = 0
            self.label_total.config(text="Total: $0")
        else:
            messagebox.showwarning("Error", "No hay productos para pagar")

# Ejecutar el sistema
root = tk.Tk()

app = SistemaCaja(root)
root.mainloop()
