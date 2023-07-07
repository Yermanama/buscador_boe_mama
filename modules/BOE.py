from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def buscar_BOE(nombre_archivo):
        
    # Primero vamos a iniciar sesión
    driver = webdriver.Chrome()

    # Después nos vamos a la página web que deseamos, en esta caso el BOE
    driver.get('https://boe.es/buscar/boe.php')

    # Nos vamos a la caja de texto donde introducimos el texto que queremos e introducimos texto
    caja_texto = driver.find_element(by=By.ID, value = 'DOC').send_keys('ingeniero/a de caminos')

    # Pulsamos en enviar ya que aquí ya está todo bien por predeterminado
    buscar_boton = driver.find_element(by= By.NAME, value='accion')
    buscar_boton.click()

    # Ahora buscamos el contenedor ul donde están todos los resultados
    contenedor_div = driver.find_element(by=By.CLASS_NAME, value= 'listadoResult')

    # Ahora tenemos que seleccionar los 10 primeros registros
    elementos_li = contenedor_div.find_elements(by=By.CLASS_NAME, value = 'resultado-busqueda')

    lista_informacion = []
    for elemento in elementos_li[0:10]:
        boletin = elemento.find_element(by=By.TAG_NAME, value= 'h4')
        parrafo = elemento.find_element(by=By.TAG_NAME, value= 'p')
        enlace = elemento.find_element(by=By.TAG_NAME, value = 'a').get_attribute('href')
        informacion = [boletin.text, parrafo.text, enlace]
        lista_informacion.append(informacion)


    # Lo pasamos al documento txt
    with open(nombre_archivo, 'w',encoding='utf-8') as archivo:
            archivo.write('INFORMACIÓN DEL BOE'.center(100,'-') + '\n')
            for elemento in lista_informacion:
                archivo.write(f'''Boletín de donde procede: {elemento[0]}\nTexto del boletín: {elemento[1]}\nEnlace al boletín:{elemento[2]}\n\n''')
                archivo.write('\n\n\n')

