# from tkinter import *
# from PIL import Image, ImageTk
# from productos import productos


# class sistema(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Sistema de Caja para Supermercado")
#         self.geometry("600x400")
#         self.configure(bg="#052d55")
#         self.iconbitmap("icono.ico")  # Asegúrate de tener un icono en el mismo directorio
#         self.resizable(False, False)
#         # Crear los frames y guardarlos en el diccionario
#         self.frames = {}
#         for F in (PantallaPrincipal, PantallaCobro, PantallaListaProductos):
#             frame = F(self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.mostrar_frame(PantallaPrincipal)

#     def mostrar_frame(self, contenedor):
#         frame = self.frames[contenedor]
#         frame.tkraise()


# class PantallaPrincipal(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.lista_productos = []
#         self.total = 0

#         # Configurar el peso de las columnas para centrar
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo = Label(self, text="Bienvenido al Sistema de Caja", font=("Arial", 16), bg="#b5daff")
#         label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame(PantallaCobro), bg="#b5f5ff", padx=40, pady=5)
#         cobrarBoton.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame(PantallaListaProductos), bg="#b5f5ff", padx=40, pady=5)
#         listaProductosBoton.grid(row=2, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Cargar la imagen
#         imagen_pil = Image.open("supermecado.jpg")
#         imagen_pil = imagen_pil.resize((200, 200))
#         self.imagen = ImageTk.PhotoImage(imagen_pil)

#         label_imagen = Label(self, image=self.imagen)
#         label_imagen.grid(row=3, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")


# class PantallaCobro(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.lista_productos = productos
#         self.master = master
#         self.total = 0

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_cobro = Label(self, text="Pantalla de Cobro", font=("Arial", 16), bg="#b5daff")
#         label_titulo_cobro.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=1, column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")
#         # Aquí puedes agregar widgets para la pantalla de cobro


# class PantallaListaProductos(Frame):
#     '''Pantalla para mostrar la lista de productos disponibles'''
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.master = master

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_lista = Label(self, text="Lista de Productos", font=("Arial", 16), bg="#b5daff")
#         label_titulo_lista.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")
        
#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")
#         # Aquí puedes agregar widgets para la lista de productos





# # Ejecucion del sistema 

# app = sistema()
# app.mainloop()

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk

# try:
#     from productos import productos
# except ImportError:
#     productos = [
#         {"nombre": "Ejemplo", "precio": 10.0}
#     ]  # Lista de ejemplo si no existe productos.py

# class sistema(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Sistema de Caja para Supermercado")
#         self.geometry("600x400")
#         self.configure(bg="#052d55")
#         # self.iconbitmap("icono.ico")  # Descomenta si tienes el archivo icono.ico
#         self.resizable(False, False)
#         self.frames = {}
#         for F in (PantallaPrincipal, PantallaCobro, PantallaListaProductos):
#             frame = F(self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.mostrar_frame(PantallaPrincipal)

#     def mostrar_frame(self, contenedor):
#         frame = self.frames[contenedor]
#         frame.tkraise()

# class PantallaPrincipal(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo = Label(self, text="Bienvenido al Sistema de Caja", font=("Arial", 16), bg="#b5daff")
#         label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame(PantallaCobro), bg="#b5f5ff", padx=40, pady=5)
#         cobrarBoton.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame(PantallaListaProductos), bg="#b5f5ff", padx=40, pady=5)
#         listaProductosBoton.grid(row=2, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Cargar la imagen con manejo de error
#         try:
#             imagen_pil = Image.open("supermecado.jpg")
#             imagen_pil = imagen_pil.resize((200, 200))
#             self.imagen = ImageTk.PhotoImage(imagen_pil)
#             label_imagen = Label(self, image=self.imagen)
#         except Exception as e:
#             label_imagen = Label(self, text="Imagen no encontrada", bg="#b5daff")
#         label_imagen.grid(row=3, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

# class PantallaCobro(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.lista_productos = productos
#         self.master = master
#         self.total = 0

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_cobro = Label(self, text="Pantalla de Cobro", font=("Arial", 16), bg="#b5daff")
#         label_titulo_cobro.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=1, column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")
#         # Aquí puedes agregar widgets para la pantalla de cobro

# class PantallaListaProductos(Frame):
#     '''Pantalla para mostrar la lista de productos disponibles'''
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.master = master

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_lista = Label(self, text="Lista de Productos", font=("Arial", 16), bg="#b5daff")
#         label_titulo_lista.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")
        
#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Mostrar productos
#         for idx, prod in enumerate(productos):
#             nombre = prod.get("nombre", "Sin nombre")
#             precio = prod.get("precio", 0)
#             label_prod = Label(self, text=f"{nombre} - ${precio:.2f}", bg="#b5daff")
#             label_prod.grid(row=2+idx, column=0, columnspan=2, padx=10, pady=2, sticky="ew")

# # Ejecución del sistema 
# if __name__ == "__main__":
#     app = sistema()
# #     app.mainloop()

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk

# # Lista de productos de ejemplo
# productos = [
#     {"nombre": "Pan", "precio": 1.50},
#     {"nombre": "Leche", "precio": 2.00},
#     {"nombre": "Huevos", "precio": 3.20},
#     {"nombre": "Queso", "precio": 4.50},
#     {"nombre": "Arroz", "precio": 2.30}
# ]

# class sistema(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Sistema de Caja para Supermercado")
#         self.geometry("600x400")
#         self.configure(bg="#052d55")
#         # self.iconbitmap("icono.ico")  # Descomenta si tienes el archivo icono.ico
#         self.resizable(False, False)
#         self.frames = {}
#         for F in (PantallaPrincipal, PantallaCobro, PantallaListaProductos):
#             frame = F(self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.mostrar_frame(PantallaPrincipal)

#     def mostrar_frame(self, contenedor):
#         frame = self.frames[contenedor]
#         frame.tkraise()

# class PantallaPrincipal(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo = Label(self, text="Bienvenido al Sistema de Caja", font=("Arial", 16), bg="#b5daff")
#         label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame(PantallaCobro), bg="#b5f5ff", padx=40, pady=5)
#         cobrarBoton.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame(PantallaListaProductos), bg="#b5f5ff", padx=40, pady=5)
#         listaProductosBoton.grid(row=2, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Cargar la imagen con manejo de error
#         try:
#             imagen_pil = Image.open("supermecado.jpg")
#             imagen_pil = imagen_pil.resize((200, 200))
#             self.imagen = ImageTk.PhotoImage(imagen_pil)
#             label_imagen = Label(self, image=self.imagen)
#         except Exception as e:
#             label_imagen = Label(self, text="Imagen no encontrada", bg="#b5daff")
#         label_imagen.grid(row=3, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

# class PantallaCobro(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.lista_productos = productos
#         self.master = master
#         self.total = 0

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_cobro = Label(self, text="Pantalla de Cobro", font=("Arial", 16), bg="#b5daff")
#         label_titulo_cobro.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=1, column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")
#         # Aquí puedes agregar widgets para la pantalla de cobro

# class PantallaListaProductos(Frame):
#     '''Pantalla para mostrar la lista de productos disponibles'''
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.master = master

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_lista = Label(self, text="Lista de Productos", font=("Arial", 16), bg="#b5daff")
#         label_titulo_lista.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")
        
#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Mostrar productos
#         for idx, prod in enumerate(productos):
#             nombre = prod.get("nombre", "Sin nombre")
#             precio = prod.get("precio", 0)
#             label_prod = Label(self, text=f"{nombre} - ${precio:.2f}", bg="#b5daff")
#             label_prod.grid(row=2+idx, column=0, columnspan=2, padx=10, pady=2, sticky="ew")

# # Ejecución del sistema 
# if __name__ == "__main__":
#     app = sistema()
#     app.mainloop()

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk

# # Lista de productos de ejemplo
# productos = [
#     {"nombre": "Pan", "precio": 1.50},
#     {"nombre": "Leche", "precio": 2.00},
#     {"nombre": "Huevos", "precio": 3.20},
#     {"nombre": "Queso", "precio": 4.50},
#     {"nombre": "Arroz", "precio": 2.30}
# ]

# class sistema(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Sistema de Caja para Supermercado")
#         self.geometry("600x400")
#         self.configure(bg="#052d55")
#         # self.iconbitmap("icono.ico")  # Descomenta si tienes el archivo icono.ico
#         self.resizable(False, False)
#         self.frames = {}
#         for F in (PantallaPrincipal, PantallaCobro, PantallaListaProductos):
#             frame = F(self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.mostrar_frame(PantallaPrincipal)

#     def mostrar_frame(self, contenedor):
#         frame = self.frames[contenedor]
#         frame.tkraise()

# class PantallaPrincipal(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo = Label(self, text="Bienvenido al Sistema de Caja", font=("Arial", 16), bg="#b5daff")
#         label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame(PantallaCobro), bg="#b5f5ff", padx=40, pady=5)
#         cobrarBoton.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame(PantallaListaProductos), bg="#b5f5ff", padx=40, pady=5)
#         listaProductosBoton.grid(row=2, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Cargar la imagen con manejo de error
#         try:
#             imagen_pil = Image.open("supermecado.jpg")
#             imagen_pil = imagen_pil.resize((200, 200))
#             self.imagen = ImageTk.PhotoImage(imagen_pil)
#             label_imagen = Label(self, image=self.imagen)
#         except Exception as e:
#             label_imagen = Label(self, text="Imagen no encontrada", bg="#b5daff")
#         label_imagen.grid(row=3, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

# class PantallaCobro(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.master = master
#         self.total = 0

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_cobro = Label(self, text="Pantalla de Cobro", font=("Arial", 16), bg="#b5daff")
#         label_titulo_cobro.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Checkboxes para seleccionar productos
#         self.vars = []
#         for idx, prod in enumerate(productos):
#             var = IntVar()
#             chk = Checkbutton(self, text=f"{prod['nombre']} - ${prod['precio']:.2f}", variable=var, bg="#b5daff")
#             chk.grid(row=2+idx, column=0, columnspan=2, sticky="w", padx=20)
#             self.vars.append((var, prod["precio"]))

#         self.label_total = Label(self, text="Total: $0.00", font=("Arial", 14), bg="#b5daff")
#         self.label_total.grid(row=2+len(productos), column=0, columnspan=2, pady=(10,0), sticky="ew")

#         boton_calcular = Button(self, text="Calcular Total", command=self.calcular_total, bg="#b5f5ff", padx=40, pady=5)
#         boton_calcular.grid(row=3+len(productos), column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=4+len(productos), column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")

#     def calcular_total(self):
#         total = 0
#         for var, precio in self.vars:
#             if var.get():
#                 total += precio
#         self.label_total.config(text=f"El total de su compra es: ${total:.2f}")

# class PantallaListaProductos(Frame):
#     '''Pantalla para mostrar la lista de productos disponibles'''
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.master = master

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_lista = Label(self, text="Lista de Productos", font=("Arial", 16), bg="#b5daff")
#         label_titulo_lista.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")
        
#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Mostrar productos
#         for idx, prod in enumerate(productos):
#             nombre = prod.get("nombre", "Sin nombre")
#             precio = prod.get("precio", 0)
#             label_prod = Label(self, text=f"{nombre} - ${precio:.2f}", bg="#b5daff")
#             label_prod.grid(row=2+idx, column=0, columnspan=2, padx=10, pady=2, sticky="ew")

# # Ejecución del sistema 
# if __name__ == "__main__":
#     app = sistema()
#     app.mainloop()

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk

# # Lista de productos de ejemplo
# productos = [
#     {"nombre": "Pan", "precio": 1.50},
#     {"nombre": "Leche", "precio": 2.00},
#     {"nombre": "Huevos", "precio": 3.20},
#     {"nombre": "Queso", "precio": 4.50},
#     {"nombre": "Arroz", "precio": 2.30}
# ]

# class sistema(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Sistema de Caja para Supermercado")
#         self.geometry("600x400")
#         self.configure(bg="#052d55")
#         # self.iconbitmap("icono.ico")  # Descomenta si tienes el archivo icono.ico
#         self.resizable(False, False)
#         self.frames = {}
#         for F in (PantallaPrincipal, PantallaCobro, PantallaListaProductos):
#             frame = F(self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.mostrar_frame(PantallaPrincipal)

#     def mostrar_frame(self, contenedor):
#         frame = self.frames[contenedor]
#         if hasattr(frame, "actualizar_lista"):
#             frame.actualizar_lista()
#         frame.tkraise()

# class PantallaPrincipal(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo = Label(self, text="Bienvenido al Sistema de Caja", font=("Arial", 16), bg="#b5daff")
#         label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame(PantallaCobro), bg="#b5f5ff", padx=40, pady=5)
#         cobrarBoton.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame(PantallaListaProductos), bg="#b5f5ff", padx=40, pady=5)
#         listaProductosBoton.grid(row=2, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Cargar la imagen con manejo de error
#         try:
#             imagen_pil = Image.open("supermecado.jpg")
#             imagen_pil = imagen_pil.resize((200, 200))
#             self.imagen = ImageTk.PhotoImage(imagen_pil)
#             label_imagen = Label(self, image=self.imagen)
#         except Exception as e:
#             label_imagen = Label(self, text="Imagen no encontrada", bg="#b5daff")
#         label_imagen.grid(row=3, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

# class PantallaCobro(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.master = master
#         self.total = 0

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_cobro = Label(self, text="Pantalla de Cobro", font=("Arial", 16), bg="#b5daff")
#         label_titulo_cobro.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         self.vars = []
#         self.checks = []
#         self.label_total = Label(self, text="Total: $0.00", font=("Arial", 14), bg="#b5daff")
#         self.label_total.grid(row=100, column=0, columnspan=2, pady=(10,0), sticky="ew")

#         boton_calcular = Button(self, text="Calcular Total", command=self.calcular_total, bg="#b5f5ff", padx=40, pady=5)
#         boton_calcular.grid(row=101, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=102, column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")

#         self.actualizar_lista()

#     def actualizar_lista(self):
#         # Eliminar checkboxes anteriores
#         for chk in getattr(self, "checks", []):
#             chk.destroy()
#         self.vars = []
#         self.checks = []
#         for idx, prod in enumerate(productos):
#             var = IntVar()
#             chk = Checkbutton(self, text=f"{prod['nombre']} - ${prod['precio']:.2f}", variable=var, bg="#b5daff")
#             chk.grid(row=2+idx, column=0, columnspan=2, sticky="w", padx=20)
#             self.vars.append((var, prod["precio"]))
#             self.checks.append(chk)
#         self.label_total.config(text="Total: $0.00")

#     def calcular_total(self):
#         total = 0
#         for var, precio in self.vars:
#             if var.get():
#                 total += precio
#         self.label_total.config(text=f"El total de su compra es: ${total:.2f}")

# class PantallaListaProductos(Frame):
#     '''Pantalla para mostrar la lista de productos disponibles'''
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.master = master

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_lista = Label(self, text="Lista de Productos", font=("Arial", 16), bg="#b5daff")
#         label_titulo_lista.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")
        
#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         boton_agregar = Button(self, text="AGREGAR PRODUCTO", command=self.ventana_agregar_producto, bg="#b5ffb5", padx=40, pady=5)
#         boton_agregar.grid(row=2, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         self.labels_productos = []
#         self.actualizar_lista()

#     def actualizar_lista(self):
#         # Eliminar labels anteriores
#         for lbl in getattr(self, "labels_productos", []):
#             lbl.destroy()
#         self.labels_productos = []
#         for idx, prod in enumerate(productos):
#             nombre = prod.get("nombre", "Sin nombre")
#             precio = prod.get("precio", 0)
#             label_prod = Label(self, text=f"{nombre} - ${precio:.2f}", bg="#b5daff")
#             label_prod.grid(row=3+idx, column=0, columnspan=2, padx=10, pady=2, sticky="ew")
#             self.labels_productos.append(label_prod)

#     def ventana_agregar_producto(self):
#         ventana = Toplevel(self)
#         ventana.title("Agregar Producto")
#         ventana.geometry("300x150")
#         ventana.configure(bg="#b5daff")

#         Label(ventana, text="Nombre del producto:", bg="#b5daff").pack(pady=(10,0))
#         entry_nombre = Entry(ventana)
#         entry_nombre.pack(pady=5)

#         Label(ventana, text="Precio:", bg="#b5daff").pack()
#         entry_precio = Entry(ventana)
#         entry_precio.pack(pady=5)

#         def agregar():
#             nombre = entry_nombre.get().strip()
#             try:
#                 precio = float(entry_precio.get())
#             except ValueError:
#                 messagebox.showerror("Error", "El precio debe ser un número.")
#                 return
#             if not nombre:
#                 messagebox.showerror("Error", "El nombre no puede estar vacío.")
#                 return
#             productos.append({"nombre": nombre, "precio": precio})
#             self.actualizar_lista()
#             # Actualizar la pantalla de cobro si está abierta
#             if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
#                 self.master.frames[PantallaCobro].actualizar_lista()
#             ventana.destroy()

#         Button(ventana, text="Agregar", command=agregar, bg="#b5f5ff").pack(pady=10)

# # Ejecución del sistema 
# if __name__ == "__main__":
#     app = sistema()
#     app.mainloop()

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk

# # Lista de productos de ejemplo
# productos = [
#     {"nombre": "Pan", "precio": 1.50},
#     {"nombre": "Leche", "precio": 2.00},
#     {"nombre": "Huevos", "precio": 3.20},
#     {"nombre": "Queso", "precio": 4.50},
#     {"nombre": "Arroz", "precio": 2.30}
# ]

# class sistema(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Sistema de Caja para Supermercado")
#         self.geometry("600x400")
#         self.configure(bg="#052d55")
#         # self.iconbitmap("icono.ico")  # Descomenta si tienes el archivo icono.ico
#         self.resizable(False, False)
#         self.frames = {}
#         for F in (PantallaPrincipal, PantallaCobro, PantallaListaProductos):
#             frame = F(self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.mostrar_frame(PantallaPrincipal)

#     def mostrar_frame(self, contenedor):
#         frame = self.frames[contenedor]
#         if hasattr(frame, "actualizar_lista"):
#             frame.actualizar_lista()
#         frame.tkraise()

# class PantallaPrincipal(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo = Label(self, text="Bienvenido al Sistema de Caja", font=("Arial", 16), bg="#b5daff")
#         label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame(PantallaCobro), bg="#b5f5ff", padx=40, pady=5)
#         cobrarBoton.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame(PantallaListaProductos), bg="#b5f5ff", padx=40, pady=5)
#         listaProductosBoton.grid(row=2, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Cargar la imagen con manejo de error
#         try:
#             imagen_pil = Image.open("supermecado.jpg")
#             imagen_pil = imagen_pil.resize((200, 200))
#             self.imagen = ImageTk.PhotoImage(imagen_pil)
#             label_imagen = Label(self, image=self.imagen)
#         except Exception as e:
#             label_imagen = Label(self, text="Imagen no encontrada", bg="#b5daff")
#         label_imagen.grid(row=3, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

# class PantallaCobro(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.master = master
#         self.total = 0

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_cobro = Label(self, text="Pantalla de Cobro", font=("Arial", 16), bg="#b5daff")
#         label_titulo_cobro.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         self.vars = []
#         self.checks = []
#         self.label_total = Label(self, text="Total: $0.00", font=("Arial", 14), bg="#b5daff")
#         self.label_total.grid(row=100, column=0, columnspan=2, pady=(10,0), sticky="ew")

#         boton_calcular = Button(self, text="Calcular Total", command=self.calcular_total, bg="#b5f5ff", padx=40, pady=5)
#         boton_calcular.grid(row=101, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=102, column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")

#         self.actualizar_lista()

#     def actualizar_lista(self):
#         # Eliminar checkboxes anteriores
#         for chk in getattr(self, "checks", []):
#             chk.destroy()
#         self.vars = []
#         self.checks = []
#         for idx, prod in enumerate(productos):
#             var = IntVar()
#             chk = Checkbutton(self, text=f"{prod['nombre']} - ${prod['precio']:.2f}", variable=var, bg="#b5daff")
#             chk.grid(row=2+idx, column=0, columnspan=2, sticky="w", padx=20)
#             self.vars.append((var, prod["precio"]))
#             self.checks.append(chk)
#         self.label_total.config(text="Total: $0.00")

#     def calcular_total(self):
#         total = 0
#         for var, precio in self.vars:
#             if var.get():
#                 total += precio
#         self.label_total.config(text=f"El total de su compra es: ${total:.2f}")

# class PantallaListaProductos(Frame):
#     '''Pantalla para mostrar la lista de productos disponibles'''
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.master = master

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_lista = Label(self, text="Lista de Productos", font=("Arial", 16), bg="#b5daff")
#         label_titulo_lista.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")
        
#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         boton_agregar = Button(self, text="AGREGAR PRODUCTO", command=self.ventana_agregar_producto, bg="#b5ffb5", padx=40, pady=5)
#         boton_agregar.grid(row=2, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         self.labels_productos = []
#         self.actualizar_lista()

#     def actualizar_lista(self):
#         # Eliminar labels anteriores
#         for lbl in getattr(self, "labels_productos", []):
#             lbl.destroy()
#         self.labels_productos = []
#         for idx, prod in enumerate(productos):
#             nombre = prod.get("nombre", "Sin nombre")
#             precio = prod.get("precio", 0)
#             label_prod = Label(self, text=f"{nombre} - ${precio:.2f}", bg="#b5daff")
#             label_prod.grid(row=3+idx, column=0, columnspan=2, padx=10, pady=2, sticky="ew")
#             self.labels_productos.append(label_prod)

#     def ventana_agregar_producto(self):
#         ventana = Toplevel(self)
#         ventana.title("Agregar Producto")
#         ventana.geometry("300x150")
#         ventana.configure(bg="#b5daff")

#         Label(ventana, text="Nombre del producto:", bg="#b5daff").pack(pady=(10,0))
#         entry_nombre = Entry(ventana)
#         entry_nombre.pack(pady=5)

#         Label(ventana, text="Precio:", bg="#b5daff").pack()
#         entry_precio = Entry(ventana)
#         entry_precio.pack(pady=5)

#         def agregar():
#             nombre = entry_nombre.get().strip()
#             try:
#                 precio = float(entry_precio.get())
#             except ValueError:
#                 messagebox.showerror("Error", "El precio debe ser un número.")
#                 return
#             if not nombre:
#                 messagebox.showerror("Error", "El nombre no puede estar vacío.")
#                 return
#             productos.append({"nombre": nombre, "precio": precio})
#             self.actualizar_lista()
#             # Actualizar la pantalla de cobro si está abierta
#             if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
#                 self.master.frames[PantallaCobro].actualizar_lista()
#             ventana.destroy()

#         Button(ventana, text="Agregar", command=agregar, bg="#b5f5ff").pack(pady=10)

# # Ejecución del sistema 
# if __name__ == "__main__":
#     app = sistema()
#     app.mainloop()

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk

# # Lista de productos de ejemplo
# productos = [
#     {"nombre": "Pan", "precio": 1.50},
#     {"nombre": "Leche", "precio": 2.00},
#     {"nombre": "Huevos", "precio": 3.20},
#     {"nombre": "Queso", "precio": 4.50},
#     {"nombre": "Arroz", "precio": 2.30}
# ]

# class sistema(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Sistema de Caja para Supermercado")
#         self.geometry("600x400")
#         self.configure(bg="#052d55")
#         # self.iconbitmap("icono.ico")  # Descomenta si tienes el archivo icono.ico
#         self.resizable(False, False)
#         self.frames = {}
#         for F in (PantallaPrincipal, PantallaCobro, PantallaListaProductos):
#             frame = F(self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.mostrar_frame(PantallaPrincipal)

#     def mostrar_frame(self, contenedor):
#         frame = self.frames[contenedor]
#         if hasattr(frame, "actualizar_lista"):
#             frame.actualizar_lista()
#         frame.tkraise()

# class PantallaPrincipal(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo = Label(self, text="Bienvenido al Sistema de Caja", font=("Arial", 16), bg="#b5daff")
#         label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame(PantallaCobro), bg="#b5f5ff", padx=40, pady=5)
#         cobrarBoton.grid(row=1, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame(PantallaListaProductos), bg="#b5f5ff", padx=40, pady=5)
#         listaProductosBoton.grid(row=2, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Cargar la imagen con manejo de error
#         try:
#             imagen_pil = Image.open("supermecado.jpg")
#             imagen_pil = imagen_pil.resize((200, 200))
#             self.imagen = ImageTk.PhotoImage(imagen_pil)
#             label_imagen = Label(self, image=self.imagen)
#         except Exception as e:
#             label_imagen = Label(self, text="Imagen no encontrada", bg="#b5daff")
#         label_imagen.grid(row=3, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

# class PantallaCobro(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.master = master
#         self.total = 0

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_cobro = Label(self, text="Pantalla de Cobro", font=("Arial", 16), bg="#b5daff")
#         label_titulo_cobro.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         self.vars = []
#         self.checks = []
#         self.label_total = Label(self, text="Total: $0.00", font=("Arial", 14), bg="#b5daff")
#         self.label_total.grid(row=100, column=0, columnspan=2, pady=(10,0), sticky="ew")

#         boton_calcular = Button(self, text="Calcular Total", command=self.calcular_total, bg="#b5f5ff", padx=40, pady=5)
#         boton_calcular.grid(row=101, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=102, column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")

#         self.actualizar_lista()

#     def actualizar_lista(self):
#         # Eliminar checkboxes anteriores
#         for chk in getattr(self, "checks", []):
#             chk.destroy()
#         self.vars = []
#         self.checks = []
#         for idx, prod in enumerate(productos):
#             var = IntVar()
#             chk = Checkbutton(self, text=f"{prod['nombre']} - ${prod['precio']:.2f}", variable=var, bg="#b5daff")
#             chk.grid(row=2+idx, column=0, columnspan=2, sticky="w", padx=20)
#             self.vars.append((var, prod["precio"]))
#             self.checks.append(chk)
#         self.label_total.config(text="Total: $0.00")

#     def calcular_total(self):
#         total = 0
#         for var, precio in self.vars:
#             if var.get():
#                 total += precio
#         self.label_total.config(text=f"El total de su compra es: ${total:.2f}")

# class PantallaListaProductos(Frame):
#     '''Pantalla para mostrar la lista de productos disponibles'''
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.master = master

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_columnconfigure(2, weight=1)

#         label_titulo_lista = Label(self, text="Lista de Productos", font=("Arial", 16), bg="#b5daff")
#         label_titulo_lista.grid(row=0, column=0, columnspan=3, padx=10, pady=(10,10), sticky="ew")
        
#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=1, column=0, columnspan=3, padx=10, pady=(10,10), sticky="ew")

#         boton_agregar = Button(self, text="AGREGAR PRODUCTO", command=self.ventana_agregar_producto, bg="#b5ffb5", padx=40, pady=5)
#         boton_agregar.grid(row=2, column=0, columnspan=3, padx=10, pady=(10,10), sticky="ew")

#         self.labels_productos = []
#         self.botones_editar = []
#         self.botones_eliminar = []
#         self.actualizar_lista()

#     def actualizar_lista(self):
#         # Eliminar widgets anteriores
#         for lbl in getattr(self, "labels_productos", []):
#             lbl.destroy()
#         for btn in getattr(self, "botones_editar", []):
#             btn.destroy()
#         for btn in getattr(self, "botones_eliminar", []):
#             btn.destroy()
#         self.labels_productos = []
#         self.botones_editar = []
#         self.botones_eliminar = []
#         for idx, prod in enumerate(productos):
#             nombre = prod.get("nombre", "Sin nombre")
#             precio = prod.get("precio", 0)
#             label_prod = Label(self, text=f"{nombre} - ${precio:.2f}", bg="#b5daff")
#             label_prod.grid(row=3+idx, column=0, padx=10, pady=2, sticky="ew")
#             self.labels_productos.append(label_prod)

#             btn_editar = Button(self, text="Editar", command=lambda i=idx: self.ventana_editar_producto(i), bg="#fff5b5")
#             btn_editar.grid(row=3+idx, column=1, padx=5, pady=2)
#             self.botones_editar.append(btn_editar)

#             btn_eliminar = Button(self, text="Eliminar", command=lambda i=idx: self.eliminar_producto(i), bg="#ffb5b5")
#             btn_eliminar.grid(row=3+idx, column=2, padx=5, pady=2)
#             self.botones_eliminar.append(btn_eliminar)

#     def ventana_agregar_producto(self):
#         ventana = Toplevel(self)
#         ventana.title("Agregar Producto")
#         ventana.geometry("300x150")
#         ventana.configure(bg="#b5daff")

#         Label(ventana, text="Nombre del producto:", bg="#b5daff").pack(pady=(10,0))
#         entry_nombre = Entry(ventana)
#         entry_nombre.pack(pady=5)

#         Label(ventana, text="Precio:", bg="#b5daff").pack()
#         entry_precio = Entry(ventana)
#         entry_precio.pack(pady=5)

#         def agregar():
#             nombre = entry_nombre.get().strip()
#             try:
#                 precio = float(entry_precio.get())
#             except ValueError:
#                 messagebox.showerror("Error", "El precio debe ser un número.")
#                 return
#             if not nombre:
#                 messagebox.showerror("Error", "El nombre no puede estar vacío.")
#                 return
#             productos.append({"nombre": nombre, "precio": precio})
#             self.actualizar_lista()
#             # Actualizar la pantalla de cobro si está abierta
#             if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
#                 self.master.frames[PantallaCobro].actualizar_lista()
#             ventana.destroy()

#         Button(ventana, text="Agregar", command=agregar, bg="#b5f5ff").pack(pady=10)

#     def ventana_editar_producto(self, idx):
#         producto = productos[idx]
#         ventana = Toplevel(self)
#         ventana.title("Editar Producto")
#         ventana.geometry("300x150")
#         ventana.configure(bg="#b5daff")

#         Label(ventana, text="Nombre del producto:", bg="#b5daff").pack(pady=(10,0))
#         entry_nombre = Entry(ventana)
#         entry_nombre.insert(0, producto["nombre"])
#         entry_nombre.pack(pady=5)

#         Label(ventana, text="Precio:", bg="#b5daff").pack()
#         entry_precio = Entry(ventana)
#         entry_precio.insert(0, str(producto["precio"]))
#         entry_precio.pack(pady=5)

#         def guardar():
#             nombre = entry_nombre.get().strip()
#             try:
#                 precio = float(entry_precio.get())
#             except ValueError:
#                 messagebox.showerror("Error", "El precio debe ser un número.")
#                 return
#             if not nombre:
#                 messagebox.showerror("Error", "El nombre no puede estar vacío.")
#                 return
#             productos[idx] = {"nombre": nombre, "precio": precio}
#             self.actualizar_lista()
#             if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
#                 self.master.frames[PantallaCobro].actualizar_lista()
#             ventana.destroy()

#         Button(ventana, text="Guardar", command=guardar, bg="#b5f5ff").pack(pady=10)

#     def eliminar_producto(self, idx):
#         if messagebox.askyesno("Eliminar", "¿Seguro que desea eliminar este producto?"):
#             productos.pop(idx)
#             self.actualizar_lista()
#             if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
#                 self.master.frames[PantallaCobro].actualizar_lista()

# # Ejecución del sistema 
# if __name__ == "__main__":
#     app = sistema()
#     app.mainloop()

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk

# # Lista de productos de ejemplo
# productos = [
#     {"nombre": "Pan", "precio": 2000.00},
#     {"nombre": "Leche", "precio": 1800.00},
#     {"nombre": "Huevos", "precio": 4000.00},
#     {"nombre": "Queso los 100g", "precio": 800.00},
#     {"nombre": "Arroz", "precio": 2200.00}
# ]

# # Variables globales para acumulados
# compras_acumuladas = []
# total_efectivo = 0.0
# total_tarjeta = 0.0

# class sistema(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Sistema de Caja para Supermercado")
#         self.geometry("900x450")
#         self.configure(bg="#052d55")
#         self.resizable(False, False)
#         self.frames = {}
#         for F in (PantallaPrincipal, PantallaCobro, PantallaListaProductos):
#             frame = F(self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.mostrar_frame(PantallaPrincipal)

#     def mostrar_frame(self, contenedor):
#         frame = self.frames[contenedor]
#         if hasattr(frame, "actualizar_lista"):
#             frame.actualizar_lista()
#         if hasattr(frame, "actualizar_historial"):
#             frame.actualizar_historial()
#         frame.tkraise()

# class PantallaPrincipal(Frame):
#     def __init__(self, master):
#         super().__init__(master, width=900, height=450)
#         self.grid_propagate(False)
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         # Fondo con supermercado.jpg
#         try:
#             bg_img = Image.open("supermercado.jpg")
#             bg_img = bg_img.resize((900, 450))
#             self.bg_imgtk = ImageTk.PhotoImage(bg_img)
#             self.bg_label = Label(self, image=self.bg_imgtk)
#             self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#         except Exception as e:
#             self.bg_label = Label(self, bg="#052d55")
#             self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#         # Widgets principales (colocados encima del fondo)
#         label_titulo = Label(self, text="Bienvenido al Sistema de Caja", font=("Arial", 16), bg="#b5daff")
#         label_titulo.place(x=250, y=30, width=400, height=40)

#         cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame(PantallaCobro), bg="#b5f5ff", padx=40, pady=5)
#         cobrarBoton.place(x=350, y=100, width=200, height=40)

#         listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame(PantallaListaProductos), bg="#b5f5ff", padx=40, pady=5)
#         listaProductosBoton.place(x=350, y=160, width=200, height=40)

#         # Cargar la imagen con manejo de error
#         try:
#             imagen_pil = Image.open("supermecado.jpg")
#             imagen_pil = imagen_pil.resize((200, 200))
#             self.imagen = ImageTk.PhotoImage(imagen_pil)
#             label_imagen = Label(self, image=self.imagen)
#         except Exception as e:
#             label_imagen = Label(self, text="Imagen no encontrada", bg="#b5daff")
#         label_imagen.grid(row=3, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

# class PantallaCobro(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=600, height=400)
#         self.grid_propagate(False)
#         self.master = master

#         # Acumuladores globales
#         self.total_compras = 0.0
#         self.total_efectivo = 0.0
#         self.total_credito = 0.0
#         self.total_debito = 0.0

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_cobro = Label(self, text="Pantalla de Cobro", font=("Arial", 16), bg="#b5daff")
#         label_titulo_cobro.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Checkboxes para seleccionar productos
#         self.vars = []
#         self.checks = []
#         for idx, prod in enumerate(productos):
#             var = IntVar()
#             chk = Checkbutton(self, text=f"{prod['nombre']} - ${prod['precio']:.2f}", variable=var, bg="#b5daff")
#             chk.grid(row=2+idx, column=0, columnspan=2, sticky="w", padx=20)
#             self.vars.append((var, prod["precio"]))
#             self.checks.append(chk)

#         self.label_total = Label(self, text="Total: $0.00", font=("Arial", 14), bg="#b5daff")
#         self.label_total.grid(row=2+len(productos), column=0, columnspan=2, pady=(10,0), sticky="ew")

#         self.boton_calcular = Button(self, text="Calcular Total", command=self.calcular_total, bg="#b5f5ff", padx=40, pady=5)
#         self.boton_calcular.grid(row=3+len(productos), column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         # Botones de pago (se muestran después de calcular)
#         self.boton_efectivo = Button(self, text="Efectivo", command=lambda: self.finalizar_compra("efectivo"), bg="#b5ffb5", padx=20, pady=5)
#         self.boton_credito = Button(self, text="Tarjeta de Crédito", command=lambda: self.finalizar_compra("credito"), bg="#b5b5ff", padx=20, pady=5)
#         self.boton_debito = Button(self, text="Tarjeta de Débito", command=lambda: self.finalizar_compra("debito"), bg="#ffd6b5", padx=20, pady=5)

#         self.label_acumulados = Label(self, text="", font=("Arial", 12), bg="#b5daff", anchor="w", justify="left")
#         self.label_acumulados.grid(row=7+len(productos), column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         self.boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         self.boton_volver.grid(row=8+len(productos), column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")

#         self.monto_actual = 0.0
#         self.actualizar_acumulados()

#     def calcular_total(self):
#         total = 0
#         for var, precio in self.vars:
#             if var.get():
#                 total += precio
#         self.monto_actual = total
#         self.label_total.config(text=f"El total de su compra es: ${total:.2f}")

#         # Mostrar botones de pago solo si hay algo seleccionado
#         if total > 0:
#             self.boton_efectivo.grid(row=4+len(productos), column=0, padx=10, pady=(5,5), sticky="ew")
#             self.boton_credito.grid(row=4+len(productos), column=1, padx=10, pady=(5,5), sticky="ew")
#             self.boton_debito.grid(row=5+len(productos), column=0, columnspan=2, padx=10, pady=(5,5), sticky="ew")
#         else:
#             self.boton_efectivo.grid_remove()
#             self.boton_credito.grid_remove()
#             self.boton_debito.grid_remove()

#     def finalizar_compra(self, metodo):
#         if self.monto_actual == 0:
#             messagebox.showwarning("Sin selección", "Seleccione productos y calcule el total antes de pagar.")
#             return

#         self.total_compras += self.monto_actual
#         if metodo == "efectivo":
#             self.total_efectivo += self.monto_actual
#         elif metodo == "credito":
#             self.total_credito += self.monto_actual
#         elif metodo == "debito":
#             self.total_debito += self.monto_actual

#         messagebox.showinfo("Compra realizada", f"Compra registrada por ${self.monto_actual:.2f} con {metodo.capitalize()}.")

#         # Limpiar selección y total
#         for var, _ in self.vars:
#             var.set(0)
#         self.label_total.config(text="Total: $0.00")
#         self.monto_actual = 0.0

#         # Ocultar botones de pago
#         self.boton_efectivo.grid_remove()
#         self.boton_credito.grid_remove()
#         self.boton_debito.grid_remove()

#         self.actualizar_acumulados()

#     def actualizar_acumulados(self):
#         self.label_acumulados.config(
#             text=f"Total acumulado de ventas: ${self.total_compras:.2f}\n"
#                  f"Total en efectivo: ${self.total_efectivo:.2f}\n"
#                  f"Total en tarjeta de crédito: ${self.total_credito:.2f}\n"
#                  f"Total en tarjeta de débito: ${self.total_debito:.2f}"
#         )
# class PantallaListaProductos(Frame):
#     '''Pantalla para mostrar la lista de productos disponibles'''
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=900, height=450)
#         self.grid_propagate(False)
#         self.master = master

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_columnconfigure(2, weight=1)

#         label_titulo_lista = Label(self, text="Lista de Productos", font=("Arial", 16), bg="#b5daff")
#         label_titulo_lista.grid(row=0, column=0, columnspan=3, padx=10, pady=(10,10), sticky="ew")
        
#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff", padx=40, pady=5)
#         boton_volver.grid(row=1, column=0, columnspan=3, padx=10, pady=(10,10), sticky="ew")

#         boton_agregar = Button(self, text="AGREGAR PRODUCTO", command=self.ventana_agregar_producto, bg="#b5ffb5", padx=40, pady=5)
#         boton_agregar.grid(row=2, column=0, columnspan=3, padx=10, pady=(10,10), sticky="ew")

#         self.labels_productos = []
#         self.botones_editar = []
#         self.botones_eliminar = []
#         self.actualizar_lista()

#     def actualizar_lista(self):
#         for lbl in getattr(self, "labels_productos", []):
#             lbl.destroy()
#         for btn in getattr(self, "botones_editar", []):
#             btn.destroy()
#         for btn in getattr(self, "botones_eliminar", []):
#             btn.destroy()
#         self.labels_productos = []
#         self.botones_editar = []
#         self.botones_eliminar = []
#         for idx, prod in enumerate(productos):
#             nombre = prod.get("nombre", "Sin nombre")
#             precio = prod.get("precio", 0)
#             label_prod = Label(self, text=f"{nombre} - ${precio:.2f}", bg="#b5daff")
#             label_prod.grid(row=3+idx, column=0, padx=10, pady=2, sticky="ew")
#             self.labels_productos.append(label_prod)

#             btn_editar = Button(self, text="Editar", command=lambda i=idx: self.ventana_editar_producto(i), bg="#fff5b5")
#             btn_editar.grid(row=3+idx, column=1, padx=5, pady=2)
#             self.botones_editar.append(btn_editar)

#             btn_eliminar = Button(self, text="Eliminar", command=lambda i=idx: self.eliminar_producto(i), bg="#ffb5b5")
#             btn_eliminar.grid(row=3+idx, column=2, padx=5, pady=2)
#             self.botones_eliminar.append(btn_eliminar)

#     def ventana_agregar_producto(self):
#         ventana = Toplevel(self)
#         ventana.title("Agregar Producto")
#         ventana.geometry("300x150")
#         ventana.configure(bg="#b5daff")

#         Label(ventana, text="Nombre del producto:", bg="#b5daff").pack(pady=(10,0))
#         entry_nombre = Entry(ventana)
#         entry_nombre.pack(pady=5)

#         Label(ventana, text="Precio:", bg="#b5daff").pack()
#         entry_precio = Entry(ventana)
#         entry_precio.pack(pady=5)

#         def agregar():
#             nombre = entry_nombre.get().strip()
#             try:
#                 precio = float(entry_precio.get())
#             except ValueError:
#                 messagebox.showerror("Error", "El precio debe ser un número.")
#                 return
#             if not nombre:
#                 messagebox.showerror("Error", "El nombre no puede estar vacío.")
#                 return
#             productos.append({"nombre": nombre, "precio": precio})
#             self.actualizar_lista()
#             if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
#                 self.master.frames[PantallaCobro].actualizar_lista()
#             ventana.destroy()

#         Button(ventana, text="Agregar", command=agregar, bg="#b5f5ff").pack(pady=10)

#     def ventana_editar_producto(self, idx):
#         producto = productos[idx]
#         ventana = Toplevel(self)
#         ventana.title("Editar Producto")
#         ventana.geometry("300x150")
#         ventana.configure(bg="#b5daff")

#         Label(ventana, text="Nombre del producto:", bg="#b5daff").pack(pady=(10,0))
#         entry_nombre = Entry(ventana)
#         entry_nombre.insert(0, producto["nombre"])
#         entry_nombre.pack(pady=5)

#         Label(ventana, text="Precio:", bg="#b5daff").pack()
#         entry_precio = Entry(ventana)
#         entry_precio.insert(0, str(producto["precio"]))
#         entry_precio.pack(pady=5)

#         def guardar():
#             nombre = entry_nombre.get().strip()
#             try:
#                 precio = float(entry_precio.get())
#             except ValueError:
#                 messagebox.showerror("Error", "El precio debe ser un número.")
#                 return
#             if not nombre:
#                 messagebox.showerror("Error", "El nombre no puede estar vacío.")
#                 return
#             productos[idx] = {"nombre": nombre, "precio": precio}
#             self.actualizar_lista()
#             if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
#                 self.master.frames[PantallaCobro].actualizar_lista()
#             ventana.destroy()

#         Button(ventana, text="Guardar", command=guardar, bg="#b5f5ff").pack(pady=10)

#     def eliminar_producto(self, idx):
#         if messagebox.askyesno("Eliminar", "¿Seguro que desea eliminar este producto?"):
#             productos.pop(idx)
#             self.actualizar_lista()
#             if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
#                 self.master.frames[PantallaCobro].actualizar_lista()

# if __name__ == "__main__":
#     app = sistema()
#     app.mainloop()

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk

# # Lista de productos de ejemplo
# productos = [
#     {"nombre": "Pan", "precio": 2000.00},
#     {"nombre": "Leche", "precio": 1800.00},
#     {"nombre": "Huevos", "precio": 4000.00},
#     {"nombre": "Queso los 100g", "precio": 800.00},
#     {"nombre": "Arroz", "precio": 2200.00}
# ]

# class sistema(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Sistema de Caja para Supermercado")
#         self.geometry("900x450")
#         self.configure(bg="#052d55")
#         self.resizable(False, False)
#         self.frames = {}
#         for F in (PantallaPrincipal, PantallaCobro, PantallaListaProductos):
#             frame = F(self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.mostrar_frame(PantallaPrincipal)

#     def mostrar_frame(self, contenedor):
#         frame = self.frames[contenedor]
#         if hasattr(frame, "actualizar_lista"):
#             frame.actualizar_lista()
#         frame.tkraise()

# class PantallaPrincipal(Frame):
#     def __init__(self, master):
#         super().__init__(master, width=900, height=450)
#         self.grid_propagate(False)
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         # Fondo con imagen (opcional)
#         try:
#             bg_img = Image.open("super.png")
#             bg_img = bg_img.resize((900, 450))
#             self.bg_imgtk = ImageTk.PhotoImage(bg_img)
#             self.bg_label = Label(self, image=self.bg_imgtk)
#             self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#         except Exception:
#             self.bg_label = Label(self, bg="#052d55")
#             self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#         # Widgets principales
#         label_titulo = Label(self, text="Bienvenido al Sistema de Caja", font=("Arial", 16), bg="#032241", fg="white")
#         label_titulo.place(x=250, y=30, width=400, height=40)

#         cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame(PantallaCobro), bg="#b5f5ff")
#         cobrarBoton.place(x=350, y=100, width=200, height=40)

#         listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame(PantallaListaProductos), bg="#b5f5ff")
#         listaProductosBoton.place(x=350, y=160, width=200, height=40)

# class PantallaCobro(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=900, height=450)
#         self.grid_propagate(False)
#         self.master = master

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         label_titulo_cobro = Label(self, text="Pantalla de Cobro", font=("Arial", 16), bg="#b5daff")
#         label_titulo_cobro.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         self.vars = []
#         self.checks = []
#         self.label_total = Label(self, text="Total: $0.00", font=("Arial", 14), bg="#b5daff")
#         self.label_total.grid(row=100, column=0, columnspan=2, pady=(10,0), sticky="ew")

#         self.boton_calcular = Button(self, text="Calcular Total", command=self.calcular_total, bg="#b5f5ff")
#         self.boton_calcular.grid(row=101, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         self.boton_efectivo = Button(self, text="Efectivo", command=lambda: self.finalizar_compra("efectivo"), bg="#b5ffb5")
#         self.boton_credito = Button(self, text="Tarjeta de Crédito", command=lambda: self.finalizar_compra("credito"), bg="#b5b5ff")
#         self.boton_debito = Button(self, text="Tarjeta de Débito", command=lambda: self.finalizar_compra("debito"), bg="#ffd6b5")

#         self.label_acumulados = Label(self, text="", font=("Arial", 12), bg="#b5daff", anchor="w", justify="left")
#         self.label_acumulados.grid(row=110, column=0, columnspan=2, padx=10, pady=(10,10), sticky="ew")

#         self.boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff")
#         self.boton_volver.grid(row=120, column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")

#         self.monto_actual = 0.0
#         self.total_compras = 0.0
#         self.total_efectivo = 0.0
#         self.total_credito = 0.0
#         self.total_debito = 0.0

#         self.actualizar_lista()

#     def actualizar_lista(self):
#         # Eliminar checkboxes anteriores
#         for chk in getattr(self, "checks", []):
#             chk.destroy()
#         self.vars = []
#         self.checks = []
#         for idx, prod in enumerate(productos):
#             var = IntVar()
#             chk = Checkbutton(self, text=f"{prod['nombre']} - ${prod['precio']:.2f}", variable=var, bg="#b5daff")
#             chk.grid(row=2+idx, column=0, columnspan=2, sticky="w", padx=20)
#             self.vars.append((var, prod["precio"]))
#             self.checks.append(chk)
#         self.label_total.config(text="Total: $0.00")
#         self.monto_actual = 0.0
#         self.boton_efectivo.grid_remove()
#         self.boton_credito.grid_remove()
#         self.boton_debito.grid_remove()
#         self.actualizar_acumulados()

#     def calcular_total(self):
#         total = 0
#         for var, precio in self.vars:
#             if var.get():
#                 total += precio
#         self.monto_actual = total
#         self.label_total.config(text=f"El total de su compra es: ${total:.2f}")

#         if total > 0:
#             self.boton_efectivo.grid(row=102, column=0, padx=10, pady=(5,5), sticky="ew")
#             self.boton_credito.grid(row=102, column=1, padx=10, pady=(5,5), sticky="ew")
#             self.boton_debito.grid(row=103, column=0, columnspan=2, padx=10, pady=(5,5), sticky="ew")
#         else:
#             self.boton_efectivo.grid_remove()
#             self.boton_credito.grid_remove()
#             self.boton_debito.grid_remove()

#     def finalizar_compra(self, metodo):
#         if self.monto_actual == 0:
#             messagebox.showwarning("Sin selección", "Seleccione productos y calcule el total antes de pagar.")
#             return

#         self.total_compras += self.monto_actual
#         if metodo == "efectivo":
#             self.total_efectivo += self.monto_actual
#         elif metodo == "credito":
#             self.total_credito += self.monto_actual
#         elif metodo == "debito":
#             self.total_debito += self.monto_actual

#         messagebox.showinfo("Compra realizada", f"Compra registrada por ${self.monto_actual:.2f} con {metodo.capitalize()}.")

#         for var, _ in self.vars:
#             var.set(0)
#         self.label_total.config(text="Total: $0.00")
#         self.monto_actual = 0.0

#         self.boton_efectivo.grid_remove()
#         self.boton_credito.grid_remove()
#         self.boton_debito.grid_remove()

#         self.actualizar_acumulados()

#     def actualizar_acumulados(self):
#         self.label_acumulados.config(
#             text=f"Total acumulado de ventas: ${self.total_compras:.2f}\n"
#                  f"Total en efectivo: ${self.total_efectivo:.2f}\n"
#                  f"Total en tarjeta de crédito: ${self.total_credito:.2f}\n"
#                  f"Total en tarjeta de débito: ${self.total_debito:.2f}"
#         )

# class PantallaListaProductos(Frame):
#     def __init__(self, master):
#         super().__init__(master, bg="#052d55", width=900, height=450)
#         self.grid_propagate(False)
#         self.master = master

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_columnconfigure(2, weight=1)

#         label_titulo_lista = Label(self, text="Lista de Productos", font=("Arial", 16), bg="#b5daff")
#         label_titulo_lista.grid(row=0, column=0, columnspan=3, padx=10, pady=(10,10), sticky="ew")
        
#         boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff")
#         boton_volver.grid(row=1, column=0, columnspan=3, padx=10, pady=(10,10), sticky="ew")

#         boton_agregar = Button(self, text="AGREGAR PRODUCTO", command=self.ventana_agregar_producto, bg="#b5ffb5")
#         boton_agregar.grid(row=2, column=0, columnspan=3, padx=10, pady=(10,10), sticky="ew")

#         self.labels_productos = []
#         self.botones_editar = []
#         self.botones_eliminar = []
#         self.actualizar_lista()

#     def actualizar_lista(self):
#         for lbl in getattr(self, "labels_productos", []):
#             lbl.destroy()
#         for btn in getattr(self, "botones_editar", []):
#             btn.destroy()
#         for btn in getattr(self, "botones_eliminar", []):
#             btn.destroy()
#         self.labels_productos = []
#         self.botones_editar = []
#         self.botones_eliminar = []
#         for idx, prod in enumerate(productos):
#             nombre = prod.get("nombre", "Sin nombre")
#             precio = prod.get("precio", 0)
#             label_prod = Label(self, text=f"{nombre} - ${precio:.2f}", bg="#b5daff")
#             label_prod.grid(row=3+idx, column=0, padx=10, pady=2, sticky="ew")
#             self.labels_productos.append(label_prod)

#             btn_editar = Button(self, text="Editar", command=lambda i=idx: self.ventana_editar_producto(i), bg="#fff5b5")
#             btn_editar.grid(row=3+idx, column=1, padx=5, pady=2)
#             self.botones_editar.append(btn_editar)

#             btn_eliminar = Button(self, text="Eliminar", command=lambda i=idx: self.eliminar_producto(i), bg="#ffb5b5")
#             btn_eliminar.grid(row=3+idx, column=2, padx=5, pady=2)
#             self.botones_eliminar.append(btn_eliminar)

#     def ventana_agregar_producto(self):
#         ventana = Toplevel(self)
#         ventana.title("Agregar Producto")
#         ventana.geometry("300x150")
#         ventana.configure(bg="#b5daff")

#         Label(ventana, text="Nombre del producto:", bg="#b5daff").pack(pady=(10,0))
#         entry_nombre = Entry(ventana)
#         entry_nombre.pack(pady=5)

#         Label(ventana, text="Precio:", bg="#b5daff").pack()
#         entry_precio = Entry(ventana)
#         entry_precio.pack(pady=5)

#         def agregar():
#             nombre = entry_nombre.get().strip()
#             try:
#                 precio = float(entry_precio.get())
#             except ValueError:
#                 messagebox.showerror("Error", "El precio debe ser un número.")
#                 return
#             if not nombre:
#                 messagebox.showerror("Error", "El nombre no puede estar vacío.")
#                 return
#             productos.append({"nombre": nombre, "precio": precio})
#             self.actualizar_lista()
#             if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
#                 self.master.frames[PantallaCobro].actualizar_lista()
#             ventana.destroy()

#         Button(ventana, text="Agregar", command=agregar, bg="#b5f5ff").pack(pady=10)

#     def ventana_editar_producto(self, idx):
#         producto = productos[idx]
#         ventana = Toplevel(self)
#         ventana.title("Editar Producto")
#         ventana.geometry("300x150")
#         ventana.configure(bg="#b5daff")

#         Label(ventana, text="Nombre del producto:", bg="#b5daff").pack(pady=(10,0))
#         entry_nombre = Entry(ventana)
#         entry_nombre.insert(0, producto["nombre"])
#         entry_nombre.pack(pady=5)

#         Label(ventana, text="Precio:", bg="#b5daff").pack()
#         entry_precio = Entry(ventana)
#         entry_precio.insert(0, str(producto["precio"]))
#         entry_precio.pack(pady=5)

#         def guardar():
#             nombre = entry_nombre.get().strip()
#             try:
#                 precio = float(entry_precio.get())
#             except ValueError:
#                 messagebox.showerror("Error", "El precio debe ser un número.")
#                 return
#             if not nombre:
#                 messagebox.showerror("Error", "El nombre no puede estar vacío.")
#                 return
#             productos[idx] = {"nombre": nombre, "precio": precio}
#             self.actualizar_lista()
#             if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
#                 self.master.frames[PantallaCobro].actualizar_lista()
#             ventana.destroy()

#         Button(ventana, text="Guardar", command=guardar, bg="#b5f5ff").pack(pady=10)

#     def eliminar_producto(self, idx):
#         if messagebox.askyesno("Eliminar", "¿Seguro que desea eliminar este producto?"):
#             productos.pop(idx)
#             self.actualizar_lista()
#             if hasattr(self.master.frames[PantallaCobro], "actualizar_lista"):
#                 self.master.frames[PantallaCobro].actualizar_lista()

# if __name__ == "__main__":
#     app = sistema()
#     app.mainloop()

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Lista de productos de ejemplo
productos = [
    {"nombre": "Pan", "precio": 2000.00},
    {"nombre": "Leche", "precio": 1800.00},
    {"nombre": "Huevos", "precio": 4000.00},
    {"nombre": "Queso los 100g", "precio": 800.00},
    {"nombre": "Arroz", "precio": 2200.00}
]

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

        self.boton_volver = Button(self, text="Volver", command=lambda: master.mostrar_frame(PantallaPrincipal), bg="#b5f5ff")
        self.boton_volver.grid(row=120, column=0, columnspan=2, padx=20, pady=(10,10), sticky="ew")

        self.monto_actual = 0.0
        self.total_compras = 0.0
        self.total_efectivo = 0.0
        self.total_credito = 0.0
        self.total_debito = 0.0

        self.actualizar_lista()

    def actualizar_lista(self):
        # Eliminar checkboxes anteriores
        for chk in getattr(self, "checks", []):
            chk.destroy()
        self.vars = []
        self.checks = []
        for idx, prod in enumerate(productos):
            var = IntVar()
            chk = Checkbutton(self, text=f"{prod['nombre']} - ${prod['precio']:.2f}", variable=var, bg="#b5daff")
            chk.grid(row=2+idx, column=0, columnspan=2, sticky="w", padx=20)
            self.vars.append((var, prod["precio"]))
            self.checks.append(chk)
        self.label_total.config(text="Total: $0.00")
        self.monto_actual = 0.0
        self.boton_efectivo.grid_remove()
        self.boton_credito.grid_remove()
        self.boton_debito.grid_remove()
        self.actualizar_acumulados()

    def calcular_total(self):
        total = 0
        for var, precio in self.vars:
            if var.get():
                total += precio
        self.monto_actual = total
        self.label_total.config(text=f"El total de su compra es: ${total:.2f}")

        if total > 0:
            self.boton_efectivo.grid(row=102, column=0, padx=10, pady=(5,5), sticky="ew")
            self.boton_credito.grid(row=102, column=1, padx=10, pady=(5,5), sticky="ew")
            self.boton_debito.grid(row=103, column=0, columnspan=2, padx=10, pady=(5,5), sticky="ew")
        else:
            self.boton_efectivo.grid_remove()
            self.boton_credito.grid_remove()
            self.boton_debito.grid_remove()

    def finalizar_compra(self, metodo):
        if self.monto_actual == 0:
            messagebox.showwarning("Sin selección", "Seleccione productos y calcule el total antes de pagar.")
            return

        self.total_compras += self.monto_actual
        if metodo == "efectivo":
            self.total_efectivo += self.monto_actual
        elif metodo == "credito":
            self.total_credito += self.monto_actual
        elif metodo == "debito":
            self.total_debito += self.monto_actual

        messagebox.showinfo("Compra realizada", f"Compra registrada por ${self.monto_actual:.2f} con {metodo.capitalize()}.")

        for var, _ in self.vars:
            var.set(0)
        self.label_total.config(text="Total: $0.00")
        self.monto_actual = 0.0

        self.boton_efectivo.grid_remove()
        self.boton_credito.grid_remove()
        self.boton_debito.grid_remove()

        self.actualizar_acumulados()

    def actualizar_acumulados(self):
        self.label_acumulados.config(
            text=f"Total acumulado de ventas: ${self.total_compras:.2f}\n"
                 f"Total en efectivo: ${self.total_efectivo:.2f}\n"
                 f"Total en tarjeta de crédito: ${self.total_credito:.2f}\n"
                 f"Total en tarjeta de débito: ${self.total_debito:.2f}"
        )

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