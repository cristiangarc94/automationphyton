
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome() # como ya esta dentro de las variables de enetorno no hace falta poner nada dentro de ()
driver.get("http://www.google.com/")

driver.implicitly_wait(10)

# abrimos la nueva pestaña
driver.execute_script("window.open('https://www.qalovers.com', 'new tab')")
sleep(4)

# para refrescar una pagina
driver.refresh()

sleep(5)
driver.quit()