from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def buscar_BOJA():
    # Iniciamos sesión
    driver = webdriver.Chrome()

    # Actuamos sobre el navegador
    driver.get('https://www.juntadeandalucia.es/eboja/buscador/')

    # Le damos un par de segundos para que se cargue bien la página
    driver.implicitly_wait(5)

    # Buscamos el elemento barra de búsqueda
    barra_busqueda = driver.find_element(by= By.ID, value= 'q')

    # Primero nos aseguramos que la barra no tenga nada escrito sobre ella, la limpiamos
    barra_busqueda.clear()

    # Ahora introducimos lo que queremos que lleve
    barra_busqueda.send_keys('ingeniero/a de caminos')

    driver.implicitly_wait(5)

    # Busco el botón de búsqueda avanzada
    boton_busqueda = driver.find_element(by=By.CLASS_NAME, value='pl-0')

    boton_busqueda.click()

    # Pulso botón de ordenar por: (Tengo que crear una clase para ello)
    ordenar_por = driver.find_element(by=By.ID, value='ordenacion')
    seleccionar = Select(ordenar_por)
    seleccionar.select_by_value('bojaDateNormalized')


    # Selecciono orden descendente
    sentido_descendente = driver.find_element(by=By.ID, value='sentido_ordenacion-descendente')
    sentido_descendente.click()

    # Le doy al botón de buscar
    buscar = driver.find_element(by=By.CSS_SELECTOR, value='.btn.btn-primary.btn-lg')
    buscar.click()

    # Recopilo los últimos 10 boja en donde se ha mencionado la búsqueda
    #Primero encuentro el lugar donde está el listado
    listado_resultados = driver.find_element(by=By.CLASS_NAME, value= 'listado_resultados.list-unstyled')

    # Después recupero todos los elementos li en el listado
    li_elementos = listado_resultados.find_elements(by=By.TAG_NAME, value='li')

    # Obtener texto del anuncio
    textos_anuncios = [texto.text for texto in li_elementos]

    # Obtengo los enlaces de cada elemento, pero primero tengo que obtener los elementos a
    enlaces = [elemento.find_element(by=By.TAG_NAME, value='a').get_attribute('href') for elemento in li_elementos]

    # Junto las dos listas, por su índice, a ver si coinciden, que se supone que si
    lista_combinada = list(zip(textos_anuncios, enlaces))

    with open('enlacesBOJA.txt', 'w',encoding='utf-8') as archivo:
        for elemento in lista_combinada:
            archivo.write(f'''Texto del boletín: {elemento[0]}\nEnlace al boletín: {elemento[1]}\n\n''')

if __name__ == "__main__":
    buscar_BOJA()