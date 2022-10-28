
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# PASOS
def hacer_login(usuario, password, nombre_prueba, carpeta):

        # Configurar el driver
    opciones = Options()
    opciones.headless = True
    navegador = webdriver.Chrome()
            #Ponemos tamaño al navegador:
    navegador.set_window_size(1000, 500)
    #navegador.maximize_window()

        # Abrir un navegador en una ruta
    navegador.get('https://google.es')

        # Aceptamos dialogo de cookies
    ActionChains(navegador).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    ActionChains(navegador).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    ActionChains(navegador).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    ActionChains(navegador).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    ActionChains(navegador).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(navegador).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

        # Identificaremos elementos y actuaremos sobre ellos

    #Encuentra la barra de busqueda, escribe y le da a enter
    navegador.find_element(By.NAME,'q').send_keys('testing_ground.scraping.pro/login'+ Keys.ENTER)
    #navegador.find_element_by_xpath("//h3[normalize-space()='Web Scraper Testing Ground'])[1]").click()

    navegador.find_element(By.NAME,'usr').send_keys(usuario) #ahora funciona como argumento usuario
    navegador.find_element(By.NAME,'pwd').send_keys(password)

    # Crear carpeta para las fotos
    directorio = carpeta + '/capturas/' + nombre_prueba
    try:
        os.stat(directorio)
    except:
        os.makedirs(directorio)

    # Pedir foto con los datos rellenos
    # Esto hace scroll y busca el elemento que nos interesa sacar
    ubicacion= navegador.find_element(By.NAME, 'usr').location_once_scrolled_into_view
    # Poner borde alrededor del formulario
    remarcar_elemento(navegador, "//form")

    navegador.save_screenshot(directorio + '/antes_del_login.png')
    # Hacemos click para probar el login
    navegador.find_element_by_xpath("//input[@type='submit']").click()

    resultado_login = navegador.find_element_by_xpath("//h3[@class='success' or @class='error']").text
    ubicacion = navegador.find_element_by_xpath("//h3[@class='success' or @class='error']").location_once_scrolled_into_view
    # HAcer borde alrededor del texto
    borde_original = remarcar_elemento(navegador,"//h3[@class='success' or @class='error']")
    navegador.save_screenshot(directorio + '/despues_del_login_con_borde.png')

    remarcar_elemento(navegador, "//h3[@class='success' or @class='error']", borde_original)
    navegador.save_screenshot(directorio + '/despues_del_login.png')

    # Cerrar el navegador
    navegador.quit()
    return resultado_login


def remarcar_elemento(navegador, xpath, estilo= '4px solid red'):
    # Buscamos el elemento
    elemento = navegador.find_element_by_xpath(xpath)
    # Recuperamos el borde que tenia
    original = navegador.execute_script("return arguments[0].style.border;", elemento)
    # Ponemos el nuevo borde
    navegador.execute_script("argumento[0].style.border = '" + estilo + "';", elemento)
    return original
