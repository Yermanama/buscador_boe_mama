from modules.AndaluciaBOJA import buscar_BOJA
from modules.BOE import buscar_BOE
from modules.Granada import BOPGranada
from modules.Cadiz import buscar_cadiz



nombre_archivo = 'archivoMama.txt'

if __name__ == '__main__':
    buscar_BOE(nombre_archivo)
    buscar_BOJA(nombre_archivo)
    buscar_cadiz(nombre_archivo)
    BOPGranada(nombre_archivo)
    