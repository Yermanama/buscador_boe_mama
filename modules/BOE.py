from selenium import webdriver
from selenium.webdriver.common.by import By
from .escribir_txt import append_texto
import os

nombre_ejecutado = os.path.basename(__file__)


def buscar_BOE(driver: webdriver, nombre_archivo, parametro_busqueda):
    try:
        driver = driver
        driver.get('https://boe.es/buscar/boe.php')
        driver.find_element(by=By.ID, value = 'DOC').send_keys(parametro_busqueda)
        driver.find_element(by= By.NAME, value='accion').click()
        elementos_li = driver.find_element(by=By.CLASS_NAME, value= 'listadoResult').find_elements(by=By.CLASS_NAME, value = 'resultado-busqueda')
        for elemento in elementos_li[0:10]:
            boletin = elemento.find_element(by=By.TAG_NAME, value='h4').text
            parrafo = elemento.find_element(by=By.TAG_NAME, value='p').text
            enlace = elemento.find_element(by=By.TAG_NAME, value='a').get_attribute('href')

            append_texto(nombre_archivo, 'INFORMACIÓN DEL BOE', texto=boletin, enlace=enlace, fecha=parrafo)
    except Exception as error:
        print(f'Ha habido un error del tipo {error} en el archivo {nombre_ejecutado}')