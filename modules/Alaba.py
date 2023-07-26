import os
from traceback import print_exc

from selenium import webdriver
from selenium.webdriver.common.by import By

from .escribir_txt import append_texto

archivo_ejecutado = os.path.basename(__file__)

def buscar_alaba(driver: webdriver, nombre_archivo, parametro_busqueda):
    try:
        driver = driver
        driver.get('https://www.araba.eus/botha/Busquedas/SGBO5016.aspx')
        driver.find_element(by=By.ID, value='tbAnuncio').send_keys(parametro_busqueda)
        driver.find_element(by=By.ID, value='btnBuscar').click()
        boletin = driver.find_elements(by=By.TAG_NAME, value='tr')[1].find_elements(by=By.TAG_NAME, value='td')
        fecha = boletin[0].text
        texto = boletin[3].text
        enlace = boletin[5].find_element(by=By.TAG_NAME, value='a').get_attribute('href')
        
        append_texto(
            nombre_archivo=nombre_archivo,
            nombre_boletin_may="BOLETIN DE ÁLABA",
            texto=texto,
            enlace=enlace,
            fecha=fecha,
        )

    except Exception as e:
        print(f"Ha habido un error del tipo {e} en el archivo {archivo_ejecutado}")
        print_exc()


if __name__ == "__main__":
    buscar_alaba(webdriver.Chrome(), "prueba_alaba.txt", 'ingeniero/a de caminos')