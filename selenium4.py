
# Cerrar pestañas del navegador, cambiando el foco de una a otra
# + Scroll en la pagina

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')
# Abrimos una nueva pestaña
driver.execute_script("window.open('');")
time.sleep(5)
# Cambiamos el foco a la nueva pestaña
driver.switch_to.window(driver.window_handles[1])
driver.get("https://qalovers.com")
time.sleep(5)
# Ahora, cerramos la pestaña actual
driver.close()
time.sleep(5)
# Volvemos a cambiar el foco a la primera pestaña
driver.switch_to.window(driver.window_handles[0])
driver.get("https://www.youtube.com")
time.sleep(5)
# Cerramos la última pestaña, y por lo tanto, cerraremos el navegador.
#driver.close()

# Hacemos scroll complete en toda la página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)

driver.quit()