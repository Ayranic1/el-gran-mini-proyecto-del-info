from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

import gestor_productos # Fuciones para gestionar los productos en json

from ModuloCobro import PantallaCobro
from ModuloLista import PantallaListaProductos

class sistema(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Caja para Supermercado")
        self.geometry("900x450")
        self.configure(bg="#f5f5f6")
        self.resizable(False, False)

        # Icono de la ventana
        try:
            self.iconbitmap("Images/icono.ico")
        except Exception as e:
            print(f"Advertencia: No se pudo cargar el icono: {e}")

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

        

        try:
            bg_img = Image.open("Images/main.png")  # Cambia aquí el nombre si tu imagen se llama diferente 
            bg_img = bg_img.resize((900, 450), Image.Resampling.LANCZOS) # Usar LANCZOS para mejor calidad
            self.bg_imgtk = ImageTk.PhotoImage(bg_img)
            self.bg_label = Label(self, image=self.bg_imgtk)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        except Exception as e: # Captura la excepción para debug
            print(f"Advertencia: No se pudo cargar la imagen de fondo: {e}")
            self.bg_label = Label(self, bg="#f5f5f6")
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

         # - - - Barra superior
        top_frame = Frame(self, bg="#0000ff", bd=2, relief="groove")
        top_frame.pack(side="top", fill="both")
        top_frame.config(bg="#f5f5f6", border=0, height=40)

        # titulo    
        label_titulo = Label(top_frame, text="¡Bienvenido al Sistema de Caja!", font=("Arial", 16), bg="#f5f5f6", fg="#000000")
        label_titulo.place(x=0, y=0, width=400, height=40)

        # botones
        cobrarBoton = Button(self, text="Cobrar", command=lambda: master.mostrar_frame("PantallaCobro"), bg="#3a2d97", fg="#FFFFFF")
        cobrarBoton.place(x=10, y=400, width=200, height=40)

        listaProductosBoton = Button(self, text="Lista de Productos", command=lambda: master.mostrar_frame("PantallaListaProductos"), bg="#adadc2")
        listaProductosBoton.place(x=220, y=400, width=200, height=40)


if __name__ == "__main__":
    app = sistema()
    app.mainloop()