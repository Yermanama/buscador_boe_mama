from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

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

# Después recupero todos los elementos a en el listado
a_elementos = listado_resultados.find_elements(by=By.TAG_NAME, value='a')

# Obtener texto del anuncio
textos_anuncios = [texto.text for texto in a_elementos]

# Obtener el boletín de donde ha salido

# Obtengo los enlaces de cada elemento 
enlaces = [elemento.get_attribute('href') for elemento in a_elementos]

with open('enlacesBOJA.txt', 'w') as file:
    for enlace in enlaces:
        file.write(enlace + '\n')

# Revisar si los resutlados están bien, en el orden correcto
# Asignar correctamente los enlaces, los textos y los boletines a cada elemento de la lista