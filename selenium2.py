
# Siempre en los programas de selenium
import time
from selenium import webdriver # es el navegador
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service # Para quitar el problema con el executable_pa

driver_service = Service(executable_path='./drivers/chromedriver.exe')

# PASOS
    # Configurar el driver
#options = Options()
#options.headless = True  # hace odo el trabajo sin mostrar fisicamente la pantalla del navegador
navegador = webdriver.Chrome(service=driver_service)
# navegador = webdriver.Chrome(executable_path='./drivers/chromedriver.exe') Aqui es donde nos da un deprecationwarning
        #Ponemos tamaño al navegador:
navegador.set_window_position(0,0)
navegador.set_window_size(1200,1200)

    # Abrir un navegador en una ruta
navegador.get('https://testing-ground.webscraping.pro/login')

    # Identificaremos elementos y actuaremos sobre ellos
navegador.find_element_by_xpath("//input[@id='usr']").send_keys(admin)
navegador.find_element_by_xpath("//input[@id='pwd']").send_keys(12345)

    # Capturas de pantalla
navegador.save_screenshot("capturas/captura_antes_borde.png")
borde_anterior = remarcar_elemento(navegador, "//form")
navegador.save_screenshot("capturas/captura_despues_borde.png")
sacar_foto_elemento(navegador, "//form", 'capturas/formulario.png')
remarcar_elemento(navegador,"//form", borde_anterior)
    # Cerrar el navegador
navegador.quit()

