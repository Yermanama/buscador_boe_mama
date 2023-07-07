from selenium import webdriver
from selenium.webdriver.common.by import By
from .escribir_txt import append_texto


def BOPGranada(nombre_archivo):
    driver = webdriver.Chrome()
    driver.get('https://bop2.dipgra.es/opencms/')
    driver.find_element(by=By.ID, value='textoLibre').send_keys('ingeniero de caminos')
    driver.find_element(by=By.CSS_SELECTOR, value='input.boton[value="BUSCAR"]').click()
    boletin = driver.find_element(by=By.ID, value = 'cabeceraListado').find_element(by=By.TAG_NAME, value = 'h2').text
    enlacePDF = driver.find_element(by=By.ID, value = 'cabeceraListado').find_element(by=By.TAG_NAME, value = 'a').get_attribute('href')
    
    append_texto(nombre_archivo = nombre_archivo, nombre_boletin_may='BOLETIN DE GRANADA', enlace=enlacePDF, texto=boletin)


if __name__ == "__main__":
    BOPGranada('archivoMama.txt')