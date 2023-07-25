from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# from .escribir_txt import append_texto
from .escribir_txt import append_texto

nombre_ejecutado = os.path.basename(__file__)


def buscar_almeria(driver, nombre_archivo, parametro_busqueda):
    try:
        driver.get('https://www.dipalme.org/Servicios/cmsdipro/index.nsf/bop_view.xsp?p=dipalme')
        driver.find_element(by=By.CSS_SELECTOR,
                            value='button.registerbtn.rechazarbtn.cerrar_ventana_cookies_rechazar').click()
        driver.find_element(by=By.ID, value='search-button-bop-show').click()
        driver.implicitly_wait(5)
        driver.find_element(by=By.ID, value='view:form_texto').send_keys(parametro_busqueda)
        driver.find_element(by=By.ID, value='sf_submit').click()
        driver.implicitly_wait(10)
        driver.find_element(by=By.CSS_SELECTOR,
                            value='button.registerbtn.rechazarbtn.cerrar_ventana_cookies_rechazar').click()
        driver.implicitly_wait(5)
        div = driver.find_element(by=By.ID, value='view:_id6:repeat1').find_element(by=By.CSS_SELECTOR, value='div.right')
        # Me falta obtener el párrafo y la información que hay en él
        parrafo = div.find_element(by=By.TAG_NAME, value='p')
        fecha = parrafo.text[0:30]
        html = parrafo.get_attribute('innerHTML')
        parts = html.split('<br>')
        if len(parts) >= 4:
            texto = parts[3]
        else:
            texto = "No se encontró el cuarto segmento del texto"
        enlace = parrafo.find_element(by=By.TAG_NAME, value='a').get_attribute('href')

        append_texto(nombre_archivo=nombre_archivo, fecha=fecha, enlace=enlace, texto=texto,
                     nombre_boletin_may='BOLETIN PROVINCIAL ALMERÍA')
    except Exception as error:
        print(f'Ha habido un error del tipo {type(error)} en el fichero {nombre_ejecutado}')


if __name__ == "__main__":
    buscar_almeria(driver=webdriver.Chrome(), nombre_archivo='prueba.txt')
