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
    """
    Inicia un driver de Selenium con ciertas opciones específicas
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.pageLoadStrategy = 'eager'
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    return driver

def buscar_boton_y_clicar(url, xpath, driver, show_process=False):
    """
    Busca un elemento que pueda ser clicable dado un xpath y clica sobre él
    """
    try:
        driver.get(url)
        button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath)))
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


def aceptar_cookies_y_extraer_html(url:str, driver=None, show_process=True, extract_html=True):
  """
  Busca el tipo de botón que define el cuadro de aceptar cookies dentro de una página web
  sobre distintos tipos de botones dados en la lista de xpaths.
  Para ello, itera sobre la lista llamando a la función buscar_boton_y_clicar hasta que encuentra
  el botón o hasta que haya recorrido la lista entera
  """
  if driver is None: driver = iniciar_driver()
  found_cookie = False
  if 'wikipedia' in url or 'youtube' in url:
    if show_process: print(f'Esta página {url} no tiene cookies')
    found_cookie = True
    if extract_html: return driver.page_source  
  xpath_list = cargar_xpath_boton_cookies()
  idx = 0
  while not found_cookie and idx<len(xpath_list):
    found_cookie = buscar_boton_y_clicar(driver=driver, url=url, xpath=xpath_list[idx])       
    idx+= 1
  if not found_cookie and show_process: print('Botón de cookies no encontrada para la url', url)
  if extract_html: return driver.page_source  

def aceptar_cookies(url, driver=None):
    """Buscar y aceptar el botón de cookies dada una url"""
    aceptar_cookies_y_extraer_html(url=url, driver=driver, extract_html=False)

def aceptar_cookies_no_paralelizado(urls):
  """Buscar y aceptar el botón de cookies dada una lista de urls"""
  driver = iniciar_driver()
  for url in urls:
     aceptar_cookies(driver=driver, url=url)
  driver.quit()

def aceptar_cookies_y_extraer_htmls_no_paralelizado(urls):
    """Buscar y aceptar el botón de cookies y extraer el html de una lista de urls"""
    driver = iniciar_driver()
    htmls = []
    for url in urls:
        htmls.append(aceptar_cookies_y_extraer_html(url=url, driver=driver))
    driver.quit()
    return htmls
        
def paralelizar_funcion(func, arg):
    with ThreadPoolExecutor() as executor:
        return list(executor.map(func, arg))

def aceptar_cookies_paralelizado(urls):
    return paralelizar_funcion(aceptar_cookies, urls)

def aceptar_cookies_y_extraer_htmls_paralelizado(urls):
    return paralelizar_funcion(aceptar_cookies_y_extraer_html, urls)

"""-------------------------------------------------------------------------------------------------------------"""
