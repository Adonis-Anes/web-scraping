from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import csv

def txt_botones_cookies_a_lista(file_dir):
  """Convertir el archivo txt que contiene los identificadores de las cookies a una lista
  Input: directorio donde se encuentra el archivo txt que queremos leer
  Formato del input: palabras separadas por comas sin espacios
  Output: objeto tipo lista con el contenido del txt
  """
  with open(file_dir) as f:
      line = csv.reader(f, delimiter=",")
      return list(line)[0]

def cargar_ficheros_botones_cookies(cookies_base_dir='cookies/'):
    """Carga el fichero que contiene el texto html que identifica a las cookies
    Input: directorio base donde se encuentran los ficheros de texto que contienen 
    los identificadores de los botones para aceptar las cookies
    Por defecto es '/cookies'
    Output: dos objetos tipo listas que contienen la anterior información
    """
    cookie_button_by_class_dir = cookies_base_dir + "cookie_button_by_class.txt"
    cookie_button_by_id_dir = cookies_base_dir + "cookie_button_by_id.txt"
    button_class = txt_botones_cookies_a_lista(cookie_button_by_class_dir)
    button_id = txt_botones_cookies_a_lista(cookie_button_by_id_dir)
    return button_id, button_class

def aceptar_cookies(url, download_html=False):
  """Pincha en el botón aceptar del cuadro de diálogo que informa sobre la recopilación de cookies
  Input: un enlace de una página web
  Output: nada o si se ha solicitado, el html de la página web
  """
  cookies_button_id, cookies_button_class = cargar_ficheros_botones_cookies()
  # Explicar que es el driver
  driver.get(url)
  driver.minimize_window()
  # Inicializar parámetros
  found_cookie = False
  idx = 0
  atribute_type = ''
  cookies_button_list = cookies_button_id + cookies_button_class
  while not found_cookie and idx<len(cookies_button_list):
    cookie = cookies_button_list[idx]
    try:
      if cookie in cookies_button_id:
        atribute_type = 'id'
        button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, cookie)))
        found_cookie = True
      elif cookie in cookies_button_class:
        atribute_type = 'class'
        button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CLASS_NAME, cookie)))
        found_cookie = True
    except TimeoutException or Exception as e:
      print(f"Buscando botón de cookies con atributo: {atribute_type}={cookie} ({idx+1}/{len(cookies_button_list)})")
      print("Cambiando el tipo de cookies a buscar...")
      idx+= 1
      if idx == len(cookies_button_list):
        print('Búsqueda del botón de cookies finalizada sin éxito')
  if found_cookie:
    try:
      button.click()
      print('Cookies aceptadas')
    except Exception as e:
      print('No se ha podido clicar el botón de cookies')
      print(e)      
  if download_html==True:
    try:
      html = driver.page_source
      print('html descargado')
      return html
    except Exception as e:
      print(e)      

driver = driver = webdriver.Chrome()