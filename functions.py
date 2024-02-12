# Librerías parte I
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import csv

# Librerías parte II
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from pandas import DataFrame

"""PARTE I: ACEPTAR COOKIES Y DESCARGAR HTML"""

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
    button_class = txt_botones_cookies_a_lista(file_dir=cookie_button_by_class_dir)
    button_id = txt_botones_cookies_a_lista(file_dir=cookie_button_by_id_dir)
    return button_id, button_class

def aceptar_cookies(driver, url, download_html=False, show_process=False):
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
      if show_process==True:
        print(f"Buscando botón de cookies con atributo: {atribute_type}={cookie} ({idx+1}/{len(cookies_button_list)})")
        print("Cambiando el tipo de cookies a buscar...")
      idx+= 1        
  if found_cookie:
    try:
      button.click()
      if show_process==True:
        print(f'Cookies aceptadas (tipo {atribute_type}={cookie})')
    except Exception as e:
      if show_process==True:
        print('No se ha podido clicar el botón de cookies')
      print(e)      
  else:
    if show_process==True:
        print('Búsqueda del botón de cookies finalizada sin éxito')
  if download_html==True:
    try:
      html = driver.page_source
      if show_process==True:
        print('html descargado')
      return html
    except Exception as e:
      print(e) 
  else:
    return 1 #Para el test 
  
def aceptar_cookies_y_guardar_htmls(urls:list, show_process=True):
    """Acepta las cookies de una lista de páginas web y guarda los htmls en una variable
    Input: lista de urls
    Output: lista de htmls
    """
    if len(urls)<=1:
        print('La lista debe contener más de una url, sino usar la función aceptar_cookies_y_guardar_html del fichero aceptar_cookies.py')
        return None
    htmls=[]
    driver = webdriver.Chrome()
    for url in urls:
        if show_process == True:
            print("SCRAPEANDO PÁGINA", url)
        try:
            htmls.append(aceptar_cookies(driver=driver, url=url, download_html=True))
        except Exception as e:
            print(e)
    driver.quit()
    return htmls


"""PARTE II: EXTRAER Y PROCESAR EL TEXTO DE LAS PÁGINAS WEB PARA DETERMINAR LAS PALABRAS RELEVANTES"""
def html_a_texto(html:str):
  """Extrae el html del texto
  Input: html
  Output: texto, objeto tipo string"""
  soup = BeautifulSoup(html, features="html.parser")
  return soup.get_text()

def htmls_a_textos(htmls:list):
    """Extrae el html del texto
  Input: lista de htmls
  Output: lista de textos"""
    texts=[]
    for html in htmls:
        texts.append(html_a_texto(html=html))
    return texts

def cargar_stopwords():
    """Carga las stopwords que se van a necesitar para crear la matriz tfidf
    Input: nada
    Output: lista de palabras que son las stopwords"""
    spacy.load("es_core_news_sm")
    spacy_stopwords_es = list(spacy.lang.es.stop_words.STOP_WORDS)
    spacy_stopwords_en = list(STOP_WORDS)
    return list(spacy_stopwords_es)+['cookie','cookies']+spacy_stopwords_en

def crear_matriz_tfidf(text_files:list):
    """Generar matriz tfid a partir de un conjunto de textos, en este caso, htmls
    Input: lista de textos
    Output: matriz en forma de Dataframe de la tfidf con las 20 palabras más 'relevantes'"""
    text_titles = list(range(len(text_files)))
    # Cargar las stopwords
    stop_words = cargar_stopwords()
    # Llamar al objeto TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer(input='content', stop_words=stop_words, max_features=20)
    # Crear la matriz
    tfidf_vector = tfidf_vectorizer.fit_transform(text_files)
    # Convertir la matriz a un objeto tipo DataFrame
    tfidf_df = pd.DataFrame(tfidf_vector.toarray(), index=text_titles, columns=tfidf_vectorizer.get_feature_names_out())
    # Añadir una coulumna que es el recuento de en cuantos documentos aparece esa palabra
    tfidf_df.loc['00_Document Frequency'] = (tfidf_df > 0).sum()
    # Transponer el Dataframe y devolverlo
    return tfidf_df.T

def top_n_palabras_rel_tdidf(tfidf:DataFrame, n=10):
    """Obtener las n palabras más relevantes del DataFrame tfidf
    Input: 
        tfidf: matriz tfidf en forma de Dataframe
        n: número de palabras relevantes, por defecto 10
    Output: cadena de texto con las palabras más relevantes"""
    if n<0 or n>20:
        return f'Número n={n} incorrecto, debe estar entre 1 y 20'
    top_n_words = tfidf.index[0:n]
    return ' '.join(top_n_words)