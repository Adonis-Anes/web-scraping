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

"""PARTE 0: LEER Y GUARDAR ARCHIVOS"""

def txt_a_string(dir_archivo):
   """
   Leer archivo txt y generar una variable tipo string donde se almacene el contenido del txt
   Input:
    - file_dir: dirección completa del archivo que queremos leer
    Output: nada
   """
   with open(dir_archivo, 'r',  encoding="utf-8") as f:
      return f.read()
   
def guardar_string_como_txt(string, dir_dest):
    """ 
    Guarda un objeto tipo string de Python en un fichero txt 
    Input:
      - text: objeto de Python tipo string que queremos guardar
      - dir_dest: dirección de destino del archivo
    Output: Nada
    """
    with open(dir_dest, 'w', encoding="utf-8") as f:
        f.write(string)
    f.close()

def txt_a_lista(dir_archivo):
    """
    Leer archivo txt y generar una variable lista donde cada línea del archivo 
    se convierte en un objeto de la lista.
    Input: 
      - dir_archivo: directorio donde se encuentra el archivo txt que queremos leer.
    Output: objeto tipo lista con el contenido del txt. 
    """
    lista = []
    with open(dir_archivo, 'r') as f:
        lista = [linea.rstrip() for linea in f]
    f.close()
    return lista

def guardar_lista_como_txt_por_lineas(lista, dir_dest):
    """ 
    Guarda un objeto tipo lista de Python en un fichero txt donde cada linea del txt 
    es un objeto de la lista.
    Input:
      - lista: lista que quermos guardar
      - dir_dest: dirección de destino del archivo
    Output: Nada
    """
    with open(dir_dest, 'w') as f:
        for line in lista:
            f.write(f"{line}\n")
    f.close()

def archivos_de_carpeta_a_lista(dir_comun, num_archivos):
    """
    Lee un directorio y carga los archivos contenidos en el en una variable lista 
    donde cada elemento de la lista es un archivo de la carpeta.
    Los archivos dentro de la carpeta deben de tener un nombre común.
    El formato de la parte variable debe ser {número}.txt
    Input: 
      - dir_comun: nombre común que identifica a los archivos contenidos en la carpeta.
      - num_archivos: número de archivos dentro de la carpeta
    Output: objeto tipo lista con el contenido del txt. 
    """
    lista = []
    for i in range(0,num_archivos):
        dir_completa = dir_comun + str(i)+ '.txt'
        lista.append(txt_a_string(dir_archivo=dir_completa))
    return lista

def guardar_cada_elem_de_lista_como_txt_diferente(lista, dir_dest_comun, nombre_comun_archivos):
    """ 
    Guarda un objeto tipo string de Python que contiene un html en un fichero txt 
    donde cada linea del txt es un objeto de la lista.
    Input:
      - dir_dest_comun: dirección de carpetas de destino de los archivos, 
        sin contener el nombre del archivo
      - nombre_comun_archivos: nombre base que compartirán los archivos, 
        sin la extensión .txt ya que luego se se le añadirá un número que les identificará
        según su posición en la lista
    Output: Nada
    """
    for i in range(len(lista)):
        dir_dest = dir_dest_comun + nombre_comun_archivos + str(i) + '.txt'
        guardar_string_como_txt(string=lista[i], dir_dest=dir_dest)

def csv_a_df(dir_archivo):
    return pd.read_csv(dir_archivo)

def guardar_df_como_csv(df, matrix_name):
    """
    Guardar un DataFrame como un csv. 
    Se guardan en la carpeta results/matrices/
    Solo es necesario proprocionar el nombre, el resto de la dirección se completa.
    Input:
      - df: El DataFrame que queremos guardar.
      - matrix_name: el nombre con que queremos guardar la matriz
    Output: Nada
    """
    df.to_csv(path_or_buf=f'results/matrices/{matrix_name}.csv', index_label="palabras")

"""-------------------------------------------------------------------------------------------------------------"""

"""PARTE I: ACEPTAR COOKIES Y DESCARGAR HTML"""
  
def cargar_ficheros_botones_cookies(cookies_base_dir='cookies/'):
    """Carga el fichero que contiene el texto html que identifica a las cookies.
    Input: 
      - cookies_base_dirdi: rectorio base donde se encuentran los ficheros de texto 
        que contienen los identificadores de los botones para aceptar las cookies.
        Por defecto es '/cookies'.
    Output: dos objetos tipo listas que contienen la anterior información.
    """
    cookie_button_by_class_dir = cookies_base_dir + "cookie_button_by_class.txt"
    cookie_button_by_id_dir = cookies_base_dir + "cookie_button_by_id.txt"
    button_class = txt_a_lista(dir_archivo=cookie_button_by_class_dir)
    button_id = txt_a_lista(dir_archivo=cookie_button_by_id_dir)

    return button_id, button_class

def aceptar_cookies(driver, url:str, get_html=False, show_process=False):
  """Pincha en el botón aceptar del cuadro de diálogo que informa sobre la recopilación de cookies.
  Input: 
    - driver: un objeto COMPLETAR.
    - url: un enlace de una página web.
    - dowload_html: una variable de tipo booleano que nos permite indicar si. 
      queremos descargar el html de la página o no.
    - show_process: una variable de tipo booleano que nos permite indicar si 
      queremos mostrar el proceso de ejecución de la función.
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
  if get_html==True:
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
    """Acepta las cookies de una lista de páginas web y guarda los htmls en una variable.
    Input: 
      - urls: lista de urls.
      - show_process: una variable de tipo booleano que nos permite indicar si 
        queremos mostrar el proceso de ejecución de la función.
    Output: lista de htmls.
    """
    htmls=[]
    driver = webdriver.Chrome()
    for url in urls:
        if show_process == True:
            print("SCRAPEANDO PÁGINA", url)
        try:
            htmls.append(aceptar_cookies(driver=driver, url=url, get_html=True))
        except Exception as e:
            print(e)
    driver.quit()
    return htmls

"""-------------------------------------------------------------------------------------------------------------"""


"""PARTE II: EXTRAER Y PROCESAR EL TEXTO DE LAS PÁGINAS WEB PARA DETERMINAR LAS PALABRAS RELEVANTES"""
def html_a_texto(html:str):
  """Extrae el texto de un archivo escrito en lenguaje html. Pensado para páginas web.
  Input: 
    - html: un objeto de texto que esté escrito en lenguaje html.
  Output: el texto limpio del html, objeto tipo string."""
  soup = BeautifulSoup(html, features="html.parser")
  return soup.get_text()

def htmls_a_textos(htmls:list):
    """Extrae el texto de un conjunto de htmls contenidos en una lista.
  Input: 
    - htmls: lista con los htmls.
  Output: lista de textos."""
    texts=[]
    for html in htmls:
        texts.append(html_a_texto(html=html))
    return texts

def cargar_stopwords():
    """Carga las stopwords que se van a necesitar para crear la matriz tfidf.
    Input: nada
    Output: una lista de palabras, que son las stopwords."""
    spacy.load("es_core_news_sm")
    spacy_stopwords_es = list(spacy.lang.es.stop_words.STOP_WORDS)
    spacy_stopwords_en = list(STOP_WORDS)
    return list(spacy_stopwords_es)+['cookie','cookies', 'configuración', 'datos']+spacy_stopwords_en

def crear_matriz_tfidf(text_files:list):
    """Genera una matriz tfid a partir de un conjunto de textos.
    Input: 
      - text_files: lista de textos.
    Output: matriz en forma de Dataframe de la tfidf con las 20 palabras más relevantes."""
    text_titles = list(range(len(text_files)))
    # Cargar las stopwords
    stop_words = cargar_stopwords()
    # Llamar al objeto TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer(input='content', stop_words=stop_words, max_features=30, 
                                       min_df=5, strip_accents='ascii', token_pattern="[a-zA-Z]{2,}")
    # Crear la matriz
    tfidf_vector = tfidf_vectorizer.fit_transform(text_files)
    # Convertir la matriz a un objeto tipo DataFrame
    tfidf = pd.DataFrame(tfidf_vector.toarray(), index=text_titles, columns=tfidf_vectorizer.get_feature_names_out())
    # Añadir una coulumna que es el recuento de en cuantos documentos aparece esa palabra
    tfidf.loc['total doc freq'] = (tfidf > 0).sum()
    # Transponer el Dataframe y devolverlo
    return tfidf.T

def top_n_palabras_rel_tdidf(tfidf:DataFrame, n=10):
    """Obtiene las n palabras más relevantes del DataFrame tfidf.
    Input: 
        - tfidf: matriz tfidf en forma de Dataframe.
        - n: número de palabras relevantes, por defecto 10.
    Output: cadena de texto con las palabras más relevantes."""
    if n<0 or n>20:
        return f'Número n={n} incorrecto, debe estar entre 1 y 20'
    top_n_words = tfidf.index[0:n]
    return ' '.join(top_n_words)