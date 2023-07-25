import tkinter as tk
from tkinter import ttk, messagebox
from modules.GUI.Componentes import Etiqueta, Boton_busqueda, Entrada
import sys

class Ventana(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self._centrar_ventana()
        self.resizable(0, 0)
        self.title("Buscador de boletines")
        # Creo un frame en donde estarán los componentes centrados
        self._crear_frame()
        self._crear_componentes()

    def _centrar_ventana(self):
        # Obtengo información de la pantalla (Alto y ancho)
        alto = self.winfo_screenheight()
        ancho = self.winfo_screenwidth()

        # Obtengo ahora las coordenadas para centrar la app en la pantalla
        x = alto // 2
        y = ancho // 2

        # Configuramos la geometría
        self.geometry(f"500x300+{x}+{y}")

    def _crear_frame(self):
        self.frame = ttk.Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

    def main(self):
        from main import main
        parametro = self.entrada.get()
        main(parametro_busqueda=parametro)
        messagebox.showinfo('Tarea finalizada', 'El archivo se ha creado satisfactoriamente')
        self.quit()
        self.destroy()
        sys.exit()
        

    def _crear_componentes(self):
        self.etiqueta = Etiqueta(self.frame)
        self.entrada = Entrada(self.frame)
        self.boton_guardar = Boton_busqueda(self.frame, command=self.main)
        self.etiqueta.grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)
        self.entrada.grid(row=1, column=1, padx=10, pady=10)
        self.boton_guardar.grid(row=2, column=1, sticky="NSWE", padx=10, pady=10)

    
    

if __name__ == "__main__":
    ventana = Ventana()
    ventana.mainloop()
    