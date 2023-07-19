import os
from traceback import print_exc

from selenium import webdriver
from selenium.webdriver.common.by import By

from .escribir_txt import append_texto

archivo_ejecutado = os.path.basename(__file__)


def buscar_malaga(driver: webdriver, nombre_archivo):
    try:
        driver = driver
        driver.get('https://www.bopmalaga.es/buscar.php')
        driver.find_elements(by=By.NAME, value='valor')[1].send_keys('ingeniero/a de caminos')
        driver.find_element(by=By.ID, value='boton').click()
        driver.implicitly_wait(10)
        elemento = driver.find_element(by=By.ID, value='divResultado').find_elements(by=By.TAG_NAME, value='article')[
            0]
        texto = elemento.text
        fecha = elemento.find_element(by=By.CLASS_NAME, value='span_enlaces').find_elements(by=By.TAG_NAME, value='a')[
            0].text
        enlace = elemento.find_element(by=By.CLASS_NAME, value='span_enlaces').find_elements(by=By.TAG_NAME, value='a')[
            1].get_attribute('href')

        append_texto(nombre_archivo=nombre_archivo, nombre_boletin_may='BOLETIN DE MALAGA', texto=texto, enlace=enlace,
                     fecha=fecha)

    except Exception as e:
        print(f'Ha habido un error del tipo {e} en el archivo {archivo_ejecutado}')
        print_exc()


if __name__ == '__main__':
    buscar_malaga(webdriver.Chrome(), 'prueba_malaga.txt')
