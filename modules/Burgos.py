import os
from traceback import print_exc
from selenium import webdriver
from selenium.webdriver.common.by import By

from .escribir_txt import append_texto

archivo_ejecutado = os.path.basename(__file__)


def buscar_burgos(driver: webdriver, nombre_archivo, parametro_busqueda):
    try:
        driver = driver
        driver.get("http://bopbur.diputaciondeburgos.es/busqueda")
        driver.find_element(by=By.ID, value="edit-keys").send_keys(parametro_busqueda)
        driver.find_element(by=By.ID, value="edit-submit-search").click()
        boletin = driver.find_element(
            by=By.CSS_SELECTOR,
            value="div.views-row.views-row-1.views-row-odd.views-row-first"
        )
        fecha = boletin.find_element(by=By.CLASS_NAME, value='title-numberdate').text
        texto = boletin.find_element(by=By.CSS_SELECTOR, value='ul.bopbur-categorias-anuncios').find_elements(by=By.TAG_NAME, value='p')[0].text
        enlace =  boletin.find_element(by=By.CSS_SELECTOR, value='ul.bopbur-categorias-anuncios').find_elements(by=By.TAG_NAME, value='p')[-1].find_element(by=By.TAG_NAME, value='a').get_attribute('href')

        append_texto(
            nombre_archivo=nombre_archivo,
            nombre_boletin_may="BOLETIN DE BURGOS",
            texto=texto,
            enlace=enlace,
            fecha=fecha,
        )
    
    except Exception as e:
        print(f"Ha habido un error del tipo {e} en el archivo {archivo_ejecutado}")
        print_exc()


if __name__ == "__main__":
    buscar_burgos(webdriver.Chrome(), "prueba_burgos.txt", "ingeniero/a de caminos")
