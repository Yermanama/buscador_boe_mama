from selenium import webdriver
from selenium.webdriver.common.by import By
from .escribir_txt import append_texto

def buscar_cadiz(driver, nombre_archivo):
    driver.get('https://www.bopcadiz.es/boletin/')
    driver.find_element(by=By.ID, value='texto').send_keys('ingeniero de caminos')
    driver.find_element(by=By.CSS_SELECTOR, value='div.field.inputField').click()
    noticia = driver.find_element(by=By.CSS_SELECTOR, value='div.listWEntry.noticiaEntry')
    enlace = noticia.find_element(by=By.TAG_NAME, value= 'a').get_attribute('href')
    fecha = noticia.find_element(by=By.CSS_SELECTOR, value='p.ewDate').text
    parrafo = noticia.find_elements(by=By.TAG_NAME, value='div')[1].find_element(by=By.TAG_NAME, value= 'p').text
    
    append_texto(nombre_archivo=nombre_archivo, nombre_boletin_may='BOLETIN DE CADIZ', fecha=fecha, enlace=enlace, texto=parrafo)

if __name__ == '__main__':
    buscar_cadiz()
