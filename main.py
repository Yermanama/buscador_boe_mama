import modules.AndaluciaBOJA as BOJA
import modules.BOE as BOE
import modules.Granada as granada

nombre_archivo = 'archivoMama.txt'

BOE.buscar_BOE(nombre_archivo)
BOJA.buscar_BOJA(nombre_archivo)
granada.BOPGranada(nombre_archivo)