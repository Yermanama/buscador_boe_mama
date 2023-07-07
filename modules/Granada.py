from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def BOPGranada(nombre_archivo):
    driver = webdriver.Chrome()
    driver.get('https://bop2.dipgra.es/opencms/')
    driver.find_element(by=By.ID, value='textoLibre').send_keys('ingeniero de caminos')
    driver.find_element(by=By.CSS_SELECTOR, value='input.boton[value="BUSCAR"]').click()
    boletin = driver.find_element(by=By.ID, value = 'cabeceraListado').find_element(by=By.TAG_NAME, value = 'h2').text
    enlacePDF = driver.find_element(by=By.ID, value = 'cabeceraListado').find_element(by=By.TAG_NAME, value = 'a').get_attribute('href')
    
    with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
        archivo.write('BOLETIN PROVINCIAL GRANADA'.center(100, '-'))
        archivo.write(f'Fecha Boletin->{boletin}\nEnlace de boletin -> {enlacePDF}\n')
        archivo.write('\n\n\n')



if __name__ == "__main__":
    BOPGranada('archivoMama.txt')