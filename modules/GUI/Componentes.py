from tkinter import ttk

class Entrada(ttk.Entry):

    def __init__(self, parent):
        super().__init__(parent, width=30, font=('Roboto', 12))


class Etiqueta(ttk.Label):
    def __init__(self, parent):
        super().__init__(parent, text='Inserta criterio de búsqueda', font=('Roboto', 14))
        

class Boton_busqueda(ttk.Button):
    def __init__(self, parent, command=None):
        super().__init__(parent, text='Buscar', command=command, width=20)