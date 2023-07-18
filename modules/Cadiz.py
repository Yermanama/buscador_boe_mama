from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from .escribir_txt import append_texto
nombre_ejecutado = os.path.basename(__file__)


def buscar_cadiz(driver, nombre_archivo):
    try:
        driver.get('https://www.bopcadiz.es/boletin/')
        driver.find_element(by=By.ID, value='texto').send_keys('ingeniero de caminos')
        driver.find_element(by=By.CSS_SELECTOR, value='div.field.inputField').click()
        driver.implicitly_wait(15)
        contenido = driver.find_element(by=By.CSS_SELECTOR, value='div.listWEntry.noticiaEntry').find_elements(
            by=By.TAG_NAME, value='p')
        fecha = []
        dia_semana_ano = contenido[0].find_elements(by=By.CLASS_NAME, value='dayOfTheWeek')
        dia_semana = dia_semana_ano[0].text
        ano = dia_semana_ano[0].text
        dia_mes = contenido[0].find_element

        texto = driver.find_element(by=By.CSS_SELECTOR, value='div.listData').find_element(by=By.TAG_NAME, value='p').text
        enlace = driver.find_element(by=By.CSS_SELECTOR, value='div.listWEntry.noticiaEntry').find_element(by=By.TAG_NAME,
                                                                                                           value='a').get_attribute(
            'href')

        fecha = driver.find_element(by=By.CSS_SELECTOR, value='div.listWEntry.noticiaEntry').find_element(by=By.TAG_NAME,
                                                                                                          value='p').text

        append_texto(nombre_archivo=nombre_archivo, nombre_boletin_may='BOLETIN DE CADIZ', fecha=fecha, enlace=enlace,
                     texto=texto)
    except Exception as error:
        print(f'Ha habido un error del tipo {error} en el archivo {nombre_ejecutado}')


if __name__ == '__main__':

    buscar_cadiz(driver=webdriver.Chrome(), nombre_archivo='pruebaCadiz.txt')
