def append_texto(
    nombre_archivo,
    nombre_boletin_may,
    fecha="No he conseguido la fecha",
    enlace="No he conseguido el enlace",
    texto="No he conseguido el texto",
):
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(nombre_boletin_may.center(100, "-"))
        archivo.write('\n')
        archivo.write(f"Fecha del boletín: {fecha}\n")
        archivo.write(f"Enlace al boletín : {enlace}\n")
        archivo.write(f"Texto del boletín: {texto}\n")
        archivo.write('\n\n\n')

if __name__ == "__main__":
    append_texto()