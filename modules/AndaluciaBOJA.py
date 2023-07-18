from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os

from .escribir_txt import append_texto

nombre_ejecutado = os.path.basename(__file__)

def buscarBOJA(driver, nombre_archivo):
    try:
        driver.get('https://www.juntadeandalucia.es/eboja/buscador/')
        driver.implicitly_wait(5)
        driver.find_element(by=By.ID, value='q').send_keys('ingeniero/a de caminos')
        driver.implicitly_wait(5)
        driver.find_element(by=By.CLASS_NAME, value='pl-0').click()
        Select(driver.find_element(by=By.ID, value='ordenacion')).select_by_value('bojaDateNormalized')
        driver.find_element(by=By.ID, value='sentido_ordenacion-descendente').click()
        driver.find_element(by=By.CSS_SELECTOR, value='.btn.btn-primary.btn-lg').click()
        li_elementos = driver.find_element(by=By.CLASS_NAME, value='listado_resultados.list-unstyled').find_elements(
            by=By.TAG_NAME, value='li')
        textos_anuncios = [texto.text for texto in li_elementos]
        enlaces = [elemento.find_element(by=By.TAG_NAME, value='a').get_attribute('href') for elemento in li_elementos]
        lista_combinada = list(zip(textos_anuncios, enlaces))
        for elemento in lista_combinada:
            append_texto(nombre_archivo, 'INFORMACIÓN DEL BOJA', texto=elemento[0], enlace=elemento[1])
    except Exception as error:
        print(f'Ha habido un error del tipo {error} en el fichero {nombre_ejecutado}')
