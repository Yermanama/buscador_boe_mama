import tkinter as tk

class Entrada(tk.Tk):

    def __init__(self, parent):
        super.__init__(parent, width=30, font=('Roboto', 12))


class Etiqueta(tk.Tk):
    def __init__(self, parent):
        super().__init__(parent, text='Inserta criterio de búsqueda', font=('Roboto', 14))
        

class Boton_busqueda(tk.Tk):
    def __init__(self, parent, command):
        super.__init__(parent, text='Buscar', command=command, width=20)