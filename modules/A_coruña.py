import os
from traceback import print_exc

from selenium import webdriver
from selenium.webdriver.common.by import By

from .escribir_txt import append_texto

archivo_ejecutado = os.path.basename(__file__)


def buscar_coruña(driver: webdriver, nombre_archivo, parametro_busqueda):
    try:
        driver = driver
        driver.get("https://bop.dacoruna.gal/bopportal/")
        driver.find_element(by=By.ID, value="idiomaCabeceraCastellano").click()
        driver.find_element(by=By.NAME, value="texto").send_keys(parametro_busqueda)
        driver.find_element(by=By.CSS_SELECTOR, value="i.fa.fa-search").click()
        boletin = driver.find_elements(by=By.CLASS_NAME, value="filaImpar")[0]
        texto = boletin.find_elements(by=By.TAG_NAME, value="td")[3].text
        fecha = boletin.find_elements(by=By.TAG_NAME, value="td")[2].text
        enlace = (
            boletin.find_elements(by=By.TAG_NAME, value="td")[3]
            .find_element(by=By.TAG_NAME, value="a")
            .get_attribute("href")
        )

        append_texto(
            nombre_archivo=nombre_archivo,
            nombre_boletin_may="BOLETIN A CORUÑA",
            fecha=fecha,
            texto=texto,
            enlace=enlace,
        )

    except Exception as e:
        print(f"Ha habido un error del tipo {e} en el archivo {archivo_ejecutado}")
        print_exc()


if __name__ == "__main__":
    buscar_coruña(webdriver.Chrome(), "prueba_coruña.txt", "ingeniero/a de caminos")
