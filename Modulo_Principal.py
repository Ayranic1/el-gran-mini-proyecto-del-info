from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Productos import productos
from ModuloCobro import PantallaCobro
from ModuloLista import PantallaListaProductos
class sistema(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Caja para Supermercado")
        self.geometry("900x450")
        self.configure(bg="#052d55")
        self.resizable(True, True)
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

        cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame("PantallaCobro"), bg="#b5f5ff")
        cobrarBoton.place(x=350, y=100, width=200, height=40)

        listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame("PantallaListaProductos"), bg="#b5f5ff")
        listaProductosBoton.place(x=350, y=160, width=200, height=40)


if __name__ == "__main__":
    app = sistema()
    app.mainloop() 