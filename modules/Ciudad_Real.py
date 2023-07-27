import os
from traceback import print_exc
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from .escribir_txt import append_texto

archivo_ejecutado = os.path.basename(__file__)

def buscar_ciudad_real(driver: webdriver, nombre_archivo, parametro_busqueda):
    try:
        driver = webdriver.Chrome()
        driver.get('https://bop.dipucr.es/buscador')
        driver.find_element(by=By.CSS_SELECTOR, value='input.largo').send_keys(parametro_busqueda)
        driver.find_element(by=By.CLASS_NAME, value='line_botones').find_elements(by=By.TAG_NAME, value='input')[0].click()
        boletin = driver.find_element(by=By.ID, value='cuadro_resultados').find_elements(by=By.TAG_NAME, value='li')[0]
        texto = boletin.find_element(by=By.TAG_NAME, value='div').text
        fecha = boletin.find_element(by=By.TAG_NAME, value='p').text
        enlace = boletin.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
        
        append_texto(
            nombre_archivo=nombre_archivo,
            nombre_boletin_may="BOLETIN DE CIUDAD REAL",
            texto=texto,
            enlace=enlace,
            fecha=fecha,
        )

    except Exception as e:
        print(f"Ha habido un error del tipo {e} en el archivo {archivo_ejecutado}")
        print_exc()


if __name__ == "__main__":
    buscar_ciudad_real(webdriver.Chrome(), "prueba_ciudad_real.txt", "ingeniero/a de caminos")
