# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# from Productos import productos
# from ModuloCobro import PantallaCobro
# from ModuloLista import PantallaListaProductos
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
#             self.frames[F.__name__] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#         self.mostrar_frame("PantallaPrincipal")

#     def mostrar_frame(self, contenedor):
#         frame = self.frames[contenedor]  # contenedor es un string
#         if hasattr(frame, "actualizar_lista"):
#             frame.actualizar_lista()
#         frame.tkraise()

# class PantallaPrincipal(Frame):
#     def __init__(self, master):
#         super().__init__(master, width=900, height=450)
#         self.grid_propagate(False)
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         # Canvas para fondo
#         self.canvas = Canvas(self, width=900, height=450, highlightthickness=0)
#         self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

#         try:
#             self.bg_img = Image.open("super.png")
#             self.bg_img = self.bg_img.resize((900, 450))
#             self.bg_imgtk = ImageTk.PhotoImage(self.bg_img)
#             self.canvas.create_image(0, 0, anchor="nw", image=self.bg_imgtk)
#         except Exception as e:
#             print(f"Error cargando imagen de fondo: {e}")
#             self.canvas.create_rectangle(0, 0, 900, 450, fill="#052d55", outline="")

#         # Widgets principales (encima del fondo)
#         label_titulo = Label(self, text="Bienvenido al Sistema de Caja", font=("Arial", 16), bg="#032241", fg="white")
#         label_titulo.place(x=250, y=30, width=400, height=40)

#         cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame("PantallaCobro"), bg="#b5f5ff")
#         cobrarBoton.place(x=350, y=100, width=200, height=40)

#         listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame("PantallaListaProductos"), bg="#b5f5ff")
#         listaProductosBoton.place(x=350, y=160, width=200, height=40)
        

# if __name__ == "__main__":
#     app = sistema()
#     app.mainloop()

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
from Productos import productos
from ModuloCobro import PantallaCobro
from ModuloLista import PantallaListaProductos

class sistema(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Caja para Supermercado")
        self.geometry("900x450")
        # self.configure(bg="#052d55")  # Eliminado para mostrar solo la imagen de fondo
        self.resizable(False, False)
        self.frames = {}
        for F in (PantallaPrincipal, PantallaCobro, PantallaListaProductos):
            frame = F(self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.mostrar_frame("PantallaPrincipal")

    def mostrar_frame(self, contenedor):
        frame = self.frames[contenedor]  # contenedor es un string
        if hasattr(frame, "actualizar_lista"):
            frame.actualizar_lista()
        frame.tkraise()

class PantallaPrincipal(Frame):
    def __init__(self, master):
        super().__init__(master, width=900, height=450)
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Canvas para fondo
        self.canvas = Canvas(self, width=900, height=450, highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        #Cargar y mostrar la imagen
        self.bg_img = Image.open("fondo.jpg")
        self.bg_img = self.bg_img.resize((900, 450))
        self.bg_imgtk = ImageTk.PhotoImage(self.bg_img)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_imgtk)


        # Widgets principales (encima del fondo)
        label_titulo = Label(self, text="Bienvenido al Sistema de Caja", font=("Arial", 16), bg="#032241", fg="white")
        label_titulo.place(x=250, y=30, width=400, height=40)

        # Reloj digital
        self.label_reloj = Label(self, font=("Arial", 14), bg="#032241", fg="white")
        self.label_reloj.place(x=700, y=30, width=180, height=40)
        self.actualizar_reloj()

        cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame("PantallaCobro"), bg="#b5f5ff")
        cobrarBoton.place(x=350, y=100, width=200, height=40)

        listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame("PantallaListaProductos"), bg="#b5f5ff")
        listaProductosBoton.place(x=350, y=160, width=200, height=40)

    def actualizar_reloj(self):
        hora_actual = datetime.now().strftime("%H:%M:%S")
        self.label_reloj.config(text=hora_actual)
        self.after(1000, self.actualizar_reloj)

if __name__ == "__main__":
    app = sistema()
    app.mainloop()