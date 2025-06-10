from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Productos import productos
from ModuloCobro import PantallaCobro

class sistema(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Caja para Supermercado")
        self.geometry("900x450")
        self.configure(bg="#052d55")
        self.resizable(False, False)
        self.frames = {}
        for F in (PantallaPrincipal, PantallaCobro, PantallaListaProductos):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.mostrar_frame(PantallaPrincipal)

    def mostrar_frame(self, contenedor):
        frame = self.frames[contenedor]
        if hasattr(frame, "actualizar_lista"):
            frame.actualizar_lista()
        frame.tkraise()

class PantallaPrincipal(Frame):
    def __init__(self, master):
        super().__init__(master, width=900, height=450)
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Fondo con imagen lam.jpg 
        try:
            bg_img = Image.open("super.png")  # Cambia aquí el nombre si tu imagen se llama diferente 
            bg_img = bg_img.resize((900, 450))
            self.bg_imgtk = ImageTk.PhotoImage(bg_img)
            self.bg_label = Label(self, image=self.bg_imgtk)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception:
            self.bg_label = Label(self, bg="#052d55")
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Widgets principales (encima del fondo) 
        label_titulo = Label(self, text="Bienvenido al Sistema de Caja", font=("Arial", 16), bg="#032241", fg="white")
        label_titulo.place(x=250, y=30, width=400, height=40)

        cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame(PantallaCobro), bg="#b5f5ff")
        cobrarBoton.place(x=350, y=100, width=200, height=40)

        listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame(PantallaListaProductos), bg="#b5f5ff")
        listaProductosBoton.place(x=350, y=160, width=200, height=40)


class PantallaListaProductos(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#052d55", width=900, height=450)
        self.grid_propagate(False)
        self.master = master

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        label_titulo_lista = Label(self, text="Lista de Productos", font=("Arial", 16), bg="#b5daff")
        label_titulo_lista.grid(row=0, column=0, columnspan=3, padx=10, pady=(10,10), sticky="ew")
        
        boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff")
        boton_volver.grid(row=1, column=0, columnspan=3, padx=10, pady=(10,10), sticky="ew")

        boton_agregar = Button(self, text="AGREGAR PRODUCTO", command=self.ventana_agregar_producto, bg="#b5ffb5")
        boton_agregar.grid(row=2, column=0, columnspan=3, padx=10, pady=(10,10), sticky="ew")

        self.labels_productos = []
        self.botones_editar = []
        self.botones_eliminar = []
        self.actualizar_lista()

    def actualizar_lista(self):
        for lbl in getattr(self, "labels_productos", []):
            lbl.destroy()
        for btn in getattr(self, "botones_editar", []):
            btn.destroy()
        for btn in getattr(self, "botones_eliminar", []):
            btn.destroy()
        self.labels_productos = []
        self.botones_editar = []
        self.botones_eliminar = []
        for idx, prod in enumerate(productos):
            nombre = prod.get("nombre", "Sin nombre")
            precio = prod.get("precio", 0)
            label_prod = Label(self, text=f"{nombre} - ${precio:.2f}", bg="#b5daff")
            label_prod.grid(row=3+idx, column=0, padx=10, pady=2, sticky="ew")
            self.labels_productos.append(label_prod)

            btn_editar = Button(self, text="Editar", command=lambda i=idx: self.ventana_editar_producto(i), bg="#fff5b5")
            btn_editar.grid(row=3+idx, column=1, padx=5, pady=2)
            self.botones_editar.append(btn_editar)

            btn_eliminar = Button(self, text="Eliminar", command=lambda i=idx: self.eliminar_producto(i), bg="#ffb5b5")
            btn_eliminar.grid(row=3+idx, column=2, padx=5, pady=2)
            self.botones_eliminar.append(btn_eliminar)

    def ventana_agregar_producto(self):
        ventana = Toplevel(self)
        ventana.title("Agregar Producto")
        ventana.geometry("300x150")
        ventana.configure(bg="#b5daff")

        Label(ventana, text="Nombre del producto:", bg="#b5daff").pack(pady=(10,0))
        entry_nombre = Entry(ventana)
        entry_nombre.pack(pady=5)

        Label(ventana, text="Precio:", bg="#b5daff").pack()
        entry_precio = Entry(ventana)
        entry_precio.pack(pady=5)

        def agregar():
            nombre = entry_nombre.get().strip()
            try:
                precio = float(entry_precio.get())
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número.")
                return
            if not nombre:
                messagebox.showerror("Error", "El nombre no puede estar vacío.")
                return
            productos.append({"nombre": nombre, "precio": precio})
            self.actualizar_lista()
            if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
                self.master.frames[PantallaCobro].actualizar_lista()
            ventana.destroy()

        Button(ventana, text="Agregar", command=agregar, bg="#b5f5ff").pack(pady=10)

    def ventana_editar_producto(self, idx):
        producto = productos[idx]
        ventana = Toplevel(self)
        ventana.title("Editar Producto")
        ventana.geometry("300x150")
        ventana.configure(bg="#b5daff")

        Label(ventana, text="Nombre del producto:", bg="#b5daff").pack(pady=(10,0))
        entry_nombre = Entry(ventana)
        entry_nombre.insert(0, producto["nombre"])
        entry_nombre.pack(pady=5)

        Label(ventana, text="Precio:", bg="#b5daff").pack()
        entry_precio = Entry(ventana)
        entry_precio.insert(0, str(producto["precio"]))
        entry_precio.pack(pady=5)

        def guardar():
            nombre = entry_nombre.get().strip()
            try:
                precio = float(entry_precio.get())
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número.")
                return
            if not nombre:
                messagebox.showerror("Error", "El nombre no puede estar vacío.")
                return
            productos[idx] = {"nombre": nombre, "precio": precio}
            self.actualizar_lista()
            if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
                self.master.frames[PantallaCobro].actualizar_lista()
            ventana.destroy()

        Button(ventana, text="Guardar", command=guardar, bg="#b5f5ff").pack(pady=10)

    def eliminar_producto(self, idx):
        if messagebox.askyesno("Eliminar", "¿Seguro que desea eliminar este producto?"):
            productos.pop(idx)
            self.actualizar_lista()
            if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
                self.master.frames[PantallaCobro].actualizar_lista()

if __name__ == "__main__":
    app = sistema()
    app.mainloop()