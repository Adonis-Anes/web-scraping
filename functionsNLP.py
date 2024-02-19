# Librerías parte II
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from pandas import DataFrame
import re
from functionsReadWriteFiles import txt_a_lista

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
    return list(spacy_stopwords_es)+['cookie','cookies', 'cooki','etc', 'com', '\n', ' ']+spacy_stopwords_en

def crear_matriz_tfidf(text_files:list, max_df=0, min_df=0):
    """Genera una matriz tfid a partir de un conjunto de textos.
    Input: 
      - text_files: lista de textos.
    Output: matriz en forma de Dataframe de la tfidf con las 20 palabras más relevantes."""
    text_titles = list(range(len(text_files)))
    # Cargar las stopwords
    stop_words = txt_a_lista('stopwords.txt')
    # Llamar al objeto TfidfVectorizer
    if max_df == 0:
      max_df = len(text_files)
    if min_df==0:
      if len(text_files) > 6:
         min_df = (len(text_files)//2) + 1
      elif len(text_files) <= 6:
        min_df = (len(text_files)//2) + 2
    tfidf_vectorizer = TfidfVectorizer(input='content', stop_words=stop_words, max_features=30, strip_accents = 'unicode',
                                       min_df=min_df, max_df=max_df, token_pattern="[a-zA-Z]{2,}")
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
    if n<0 or n>30:
        return f'Número n={n} incorrecto, debe estar entre 1 y 30'
    top_n_words = tfidf.index[0:n]
    top_n_words = ' '.join(top_n_words)
    top_n_words = re.sub(' ano',' año', top_n_words)
    return top_n_words