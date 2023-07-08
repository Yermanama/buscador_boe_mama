from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#from .escribir_txt import append_texto
from .escribir_txt import append_texto

def buscar_almeria(driver, nombre_archivo):
    # Esto hay que quitarlo cuando se termine
    driver = webdriver.Chrome()

    driver.get('https://www.dipalme.org/Servicios/cmsdipro/index.nsf/bop_view.xsp?p=dipalme')
    driver.find_element(by=By.CSS_SELECTOR, value='button.registerbtn.rechazarbtn.cerrar_ventana_cookies_rechazar').click()
    driver.find_element(by=By.ID, value='search-button-bop-show').click()
    driver.implicitly_wait(5)
    driver.find_element(by=By.ID, value= 'view:form_texto').send_keys('ingeniero de caminos')
    driver.find_element(by=By.ID, value='sf_submit').click()
    driver.find_element(by=By.CSS_SELECTOR, value='button.registerbtn.rechazarbtn.cerrar_ventana_cookies_rechazar').click()
    driver.find_element(by=By.ID, value='view:_id6:repeat1').find_element(by=By.CSS_SELECTOR, value ='div.right')
    # Me falta obtener el párrafo y la información que hay en el

if __name__ == "__main__":
    buscar_almeria('prueba.txt')
