from selenium import webdriver
from selenium.webdriver.common.by import By
from .escribir_txt import append_texto


URL = 'https://bop2.dipgra.es/opencms/'
SEARCH_KEYWORD = 'ingeniero de caminos'
FILENAME = 'archivoMama.txt'

def get_boletin(driver):
    """Extrae el texto del boletín de la página web."""
    return driver.find_element(by=By.ID, value='cabeceraListado').find_element(by=By.TAG_NAME, value='h2').text

def get_pdf_link(driver):
    """Extrae el enlace del PDF de la página web."""
    return driver.find_element(by=By.ID, value='cabeceraListado').find_element(by=By.TAG_NAME, value='a').get_attribute('href')

def BOPGranada(driver, nombre_archivo):
        driver.get(URL)
        driver.find_element(by=By.ID, value='textoLibre').send_keys(SEARCH_KEYWORD)
        driver.find_element(by=By.CSS_SELECTOR, value='input.boton[value="BUSCAR"]').click()

        try:
            boletin = get_boletin(driver)
            enlacePDF = get_pdf_link(driver)
        except Exception as e:
            print(f'Error al extraer información: {e}')
            return

        append_texto(nombre_archivo = nombre_archivo, nombre_boletin_may='BOLETIN DE GRANADA', enlace=enlacePDF, texto=boletin)

if __name__ == "__main__":
    BOPGranada(driver= webdriver.Chrome(), nombre_archivo= FILENAME)