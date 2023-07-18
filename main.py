from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from modules.Almeria import buscar_almeria
from modules.AndaluciaBOJA import buscarBOJA
from modules.BOE import buscar_BOE
from modules.Cadiz import buscar_cadiz
from modules.Granada import BOPGranada


def main():
    # Setup chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-usb-keyboard-detect")  # Add this line

    # Set the driver
    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    nombre_archivo = 'boletines.txt'

    buscar_BOE(driver, nombre_archivo)
    buscarBOJA(driver, nombre_archivo)
    buscar_cadiz(driver, nombre_archivo)
    BOPGranada(driver, nombre_archivo)
    buscar_almeria(driver, nombre_archivo)

    driver.quit()


if __name__ == "__main__":
    main()
