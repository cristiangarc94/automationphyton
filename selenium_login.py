
# Siempre en los programas de selenium
import time
from selenium import webdriver # es el navegador
from selenium.webdriver import ActionChains
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
#navegador.set_window_size(1000,800)
navegador.maximize_window()

    # Abrir un navegador en una ruta
navegador.get('https://google.es')
#print(navegador.page_source) #Esto muestra el script de la pagina
#time.sleep(3)

ActionChains(navegador).key_down(Keys.TAB).key_up(Keys.TAB).perform()
ActionChains(navegador).key_down(Keys.TAB).key_up(Keys.TAB).perform()
ActionChains(navegador).key_down(Keys.TAB).key_up(Keys.TAB).perform()
ActionChains(navegador).key_down(Keys.TAB).key_up(Keys.TAB).perform()
ActionChains(navegador).key_down(Keys.TAB).key_up(Keys.TAB).perform()
time.sleep(1)
ActionChains(navegador).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


    # Identificaremos elementos y actuaremos sobre ellos
#navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#time.sleep(3)


#navegador.find_element_by_xpath("//input[id='L2AGLb']").click()
#navegador.find_element_by_link_text('Aceptar odo')
#navegador.send_keys(Keys.ENTER)
#time.sleep(3)

#Encuentra la barra de busqueda, escribe y le da a enter
navegador.find_element(By.NAME,'q').send_keys('Sevilla' + Keys.ENTER)
#time.sleep(1)
#navegador.send_keys(Keys.SPACE)
#navegador.find_element(By.NAME,'btnK').send_keys(Keys.ENTER)
time.sleep(3) # Espera 2 segundos

#Otra forma:
#navegador.find_element_by_xpath("//input[@name='q']").click()
#navegador.send_keys("Sevilla" + Keys.ENTER)

#time.sleep(3) # Espera 3 segundos
estadisticas=navegador.find_element_by_xpath("//div[@id='result-stats']").text
print(estadisticas)

    # Cerrar el navegador
navegador.quit()

