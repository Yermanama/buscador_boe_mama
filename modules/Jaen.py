import os
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from .escribir_txt import append_texto

archivo_ejecutado = os.path.basename(__file__)


def buscar_jaen(driver: webdriver, nombre_archivo):
    try:
        driver = driver
        driver.get('https://bop.dipujaen.es/busquedas')
        driver.find_element(by=By.ID, value='txtEdicto').send_keys('ingeniero/a de caminos')
        driver.find_element(by=By.XPATH, value='//input[@aria-label="Buscar edictos"]').click()
        parrafo = driver.find_element(by=By.ID, value='resultados').find_element(by=By.TAG_NAME, value='p')
        enlace = parrafo.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
        fecha = parrafo.find_element(by=By.CLASS_NAME, value='verdeCursiva').text
        texto = parrafo.find_element(by=By.CLASS_NAME, value='textoGris').text

        append_texto(texto=texto, enlace=enlace, fecha=fecha, nombre_archivo=nombre_archivo,
                     nombre_boletin_may='BOLETIN JAEN')

    except Exception as e:
        print(f'Ha ocurrido un error del tipo {e} en el archivo {archivo_ejecutado}')
        traceback.print_exc()


if __name__ == '__main__':
    buscar_jaen(webdriver.Chrome(), 'prueba_jaen.txt')
