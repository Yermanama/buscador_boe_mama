import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


archivo_ejecutado = os.path.basename(__file__)


def buscar_huelva(driver: webdriver, nombre_archivo):
    driver = webdriver.Chrome()
    driver.get('https://sede.diphuelva.es/opencms/opencms/system/modules/gsede/elements/contenedores/BOP.html')
    driver.find_element(by=By.ID, value='minusbusqueda').click()
    driver.find_elements(by=By.CLASS_NAME, value='elemento_submenu')[2].click()
    sleep(20)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'pclave'))).send_keys('ingeniero/a de caminos')

    sleep(2)

    driver.find_element(by=By.ID, value='btnBuscar').click()
    sleep(2)


if __name__ == '__main__':
    buscar_huelva(driver=webdriver.Chrome(), nombre_archivo='pruebaHuelva.txt')
