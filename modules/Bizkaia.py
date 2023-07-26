import os
from traceback import print_exc

from selenium import webdriver
from selenium.webdriver.common.by import By

from .escribir_txt import append_texto

archivo_ejecutado = os.path.basename(__file__)


def buscar_bizkaia(driver: webdriver, nombre_archivo, parametro_busqueda):
    try:
        driver = driver
        driver.get("https://www.bizkaia.eus/es/bob")
        driver.find_element(by=By.ID, value="lTMCookies1").click()
        driver.find_element(by=By.ID, value="_IYBIWBCC_text").send_keys(
            parametro_busqueda
        )
        driver.find_element(by=By.ID, value="_IYBIWBCC_buscar").click()
        fecha = (
            driver.find_elements(by=By.CSS_SELECTOR, value="div.col-12.col-sm-2")[0]
            .find_elements(by=By.TAG_NAME, value="p")[1]
            .text
        )
        texto = driver.find_elements(by=By.CSS_SELECTOR, value="div.col-9.col-sm-7")[
            0
        ].text
        enlace = driver.find_element(
            by=By.CSS_SELECTOR, value="a.btn_bobresult"
        ).get_attribute("href")

        append_texto(
            nombre_archivo=nombre_archivo,
            nombre_boletin_may="BOLETIN DE BIZKAIA",
            texto=texto,
            enlace=enlace,
            fecha=fecha,
        )

    except Exception as e:
        print(f"Ha habido un error del tipo {e} en el archivo {archivo_ejecutado}")
        print_exc()


if __name__ == "__main__":
    buscar_bizkaia(webdriver.Chrome(), "prueba_bizkaia.txt", "ingeniero/a de caminos")
