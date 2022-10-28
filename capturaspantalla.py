from selenium import webdriver

''' Instalamos pillow '''
from PIL import Image
from io import BytesIO

driver = webdriver.Chrome()
driver.get('http://google.com/')

# Buscamos el logotipo de Google
element = driver.find_element_by_id('hplogo')
image_location = element.location
size = element.size

png = driver.get_screenshot_as_png()

''' La captura es correcta, por lo que salimos del navegador '''
driver.quit()

''' Abrimos la imagen con la librería de PIL '''
crop_image = Image.open(BytesIO(png))

''' Extraemos las coordenadas (x,y) '''

left = image_location['x']
top = image_location['y']
right = image_location['x'] + size['width']
bottom = image_location['y'] + size['height']

crop_image = crop_image.crop((left, top, right, bottom))
crop_image.save('captura-logotipo.png')