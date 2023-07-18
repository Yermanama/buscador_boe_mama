import os
from datetime import datetime
import traceback
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.common.by import By

from .escribir_txt import append_texto

archivo_ejecutado = os.path.basename(__file__)
fecha_hoy = datetime.now()
fecha_hace_mes = fecha_hoy - relativedelta(months=1)
fecha_hoy = fecha_hoy.strftime('%d-%m-%Y')
fecha_hace_mes = fecha_hace_mes.strftime('%d-%m-%Y')


def buscar_cordoba(driver: webdriver, nombre_archivo):
    try:
        driver = driver
        driver.get('https://bop.dipucordoba.es/')
        driver.find_element(by=By.CLASS_NAME, value='link').find_element(by=By.TAG_NAME, value='a').click()
        driver.find_element(by=By.ID, value='query').send_keys('ingeniero de caminos')
        driver.find_element(by=By.ID, value='date_down').send_keys(fecha_hace_mes)
        driver.find_element(by=By.ID, value='date_up').send_keys(fecha_hoy)
        driver.find_element(by=By.ID, value='commit').click()
        driver.implicitly_wait(5)
        resultado = driver.find_element(by=By.CLASS_NAME, value='record')
        fecha = resultado.find_element(by=By.CLASS_NAME, value='date').text
        titulo_boletin = resultado.find_element(by=By.TAG_NAME, value='a').text
        resultado.find_element(by=By.TAG_NAME, value='a').click()
        enlace = driver.find_element(By.CSS_SELECTOR, '.links ul li:nth-child(2) a').get_attribute('href')
        append_texto(nombre_archivo=nombre_archivo, enlace=enlace, fecha=fecha, texto=titulo_boletin,
                     nombre_boletin_may='BOLETIN DE CORDOBA')


    except Exception as error:
        print(f'Hay un error del tipo {error} en el archivo {archivo_ejecutado}')
        traceback.print_exc()


if __name__ == '__main__':
    buscar_cordoba(nombre_archivo='cordoba.txt', driver=webdriver.Chrome())
