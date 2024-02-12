from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from pandas import DataFrame


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