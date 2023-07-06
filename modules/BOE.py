from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

# Primero vamos a iniciar sesión
driver = webdriver.Chrome()

# Después nos vamos a la página web que deseamos, en esta caso el BOE
driver.get('https://boe.es/buscar/boe.php')

# Nos vamos a la caja de texto donde introducimos el texto que queremos e introducimos texto
caja_texto = driver.find_element(by=By.ID, value = 'DOC').send_keys('ingeniero/a de caminos')

# Pulsamos en enviar ya que aquí ya está todo bien por predeterminado
buscar_boton = driver.find_element(by= By.NAME, value='accion')
buscar_boton.click()

# Ahora buscamos el contenedor ul donde están todos los resultados
contenedor_ul = driver.find_element(by=By.TAG_NAME, value= 'ul')
print(contenedor_ul)
