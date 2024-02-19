from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from functionsReadWriteFiles import *
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver

"""PARTE I: ACEPTAR COOKIES Y DESCARGAR HTML"""

def iniciar_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.pageLoadStrategy = 'eager'
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    return driver

def extraer_html(driver, show_error=True):
    try:
        html = driver.page_source
        if html is not None: return html
    except Exception as e:
        if show_error: print('Error al extraer el html', e)

def buscar_boton_y_clicar(url, xpath, driver, show_process=False):
    try:
        driver.get(url)
        button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        if show_process: print(f'Elemento con xpath:{xpath}, encontrado para url {url}')
        #Solo si se ha encontrado el elemento probamos a clicar
        try:
            button.click()
            print(f'Elemento con xpath:{xpath}, encontrado y clicado para url {url}')
            return True
        except ElementNotInteractableException:
            if show_process: print('ElementNotInteractableException')
        except Exception as e:
           if show_process: print(e)
    except TimeoutException:
        if show_process: print('Elemento no encontrado')
        if show_process: print('TimeOutException')
    except Exception as e:
           if show_process: print(e)


def aceptar_boton_cookies_lista_xpath_y_extraer_html(url:str, driver=None, show_process=True):
  if driver is None: driver = iniciar_driver()
  if 'wikipedia' in url or 'youtube' in url:
    if show_process: print(f'Esta página {url} no tiene cookies')
    return extraer_html(driver=driver)
  xpath_list = cargar_xpath_boton_cookies()
  found_cookie = False
  idx = 0
  while not found_cookie and idx<len(xpath_list):
    xpath = xpath_list[idx]
    found_cookie = buscar_boton_y_clicar(driver=driver, url=url, xpath=xpath)       
    idx+= 1
  if not found_cookie and show_process: print('Botón de cookies no encontrada para la url', url)
  return extraer_html

def aceptar_cookies_y_extraer_htmls_no_concurrente(urls):
  driver = iniciar_driver()
  htmls = []
  for url in urls:
     htmls.append(aceptar_boton_cookies_lista_xpath_y_extraer_html(driver=driver, url=url))
  driver.quit()
  return htmls
    
def paralelizar_funcion(func, arg):
    with ThreadPoolExecutor() as executor:
        return list(executor.map(func, arg))

def aceptar_cookies_y_extraer_htmls_concurrente(urls):
    return paralelizar_funcion(aceptar_boton_cookies_lista_xpath_y_extraer_html, urls)

"""-------------------------------------------------------------------------------------------------------------"""
