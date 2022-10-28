
# Siempre en los programas de selenium
import time
from selenium import webdriver # es el navegador
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service # Para quitar el problema con el executable_path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver_service = Service(executable_path='./drivers/chromedriver.exe')

# PASOS
    # Configurar el driver
opciones = Options
opciones.headless = True  # hace odo el trabajo sin mostrar fisicamente la pantalla del navegador
navegador = webdriver.Chrome(service=driver_service)
# navegador = webdriver.Chrome(executable_path='./drivers/chromedriver.exe') Aqui es donde nos da un deprecationwarning
        #Ponemos tamaño al navegador:
# navegador.set_window_position(0,0) Si lo vamos hacer modo oculto, no hace falta
navegador.set_window_size(800,500)

    # Abrir un navegador en una ruta
navegador.get('https://google.es')
    # Identificaremos elementos y actuaremos sobre ellos
navegador.find_element_by_xpath("//svg[text()=='Aceptar todo']")
navegador.send_keys(Keys.ENTER)

navegador.find_element(By.NAME,'q')
navegador.send_keys("Sevilla" + Keys.ENTER)
time.sleep(2) # Espera 2 segundos

#navegador.find_element_by_xpath("//input[@name='btnk']").click()
#time.sleep(3) # Espera 3 segundos
#estadisticas=navegador.find_element_by_xpath("//div[@id='result-stats']").text
#print(estadisticas)


    # Cerrar el navegador
navegador.quit()

