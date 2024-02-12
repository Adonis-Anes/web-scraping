from aceptar_cookies import aceptar_cookies_y_guardar_htmls
from busqueda_SerApi import consulta_a_links
from procesar_textos import htmls_a_textos, crear_matriz_tfidf, top_n_palabras_rel_tdidf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

def consulta_a_palabras_relevantes(consulta:str):
    """Obtiene las palabras relevantes de la consulta realizada 
    resultado de aplicar tfidf sobre los htmls de las páginas
    Input: consulta
    Output: palabras relevantes
    """
    urls = consulta_a_links(consulta=consulta)
    htmls = aceptar_cookies_y_guardar_htmls(urls=urls)
    textos = htmls_a_textos(htmls=htmls)
    matriz = crear_matriz_tfidf(text_files=textos)
    top_10_words = top_n_palabras_rel_tdidf(tfidf=matriz)
    print('10 palabras más relevantes en todas las consultas:\n',top_10_words)
    return top_10_words
    
def consulta_a_nueva_consulta(consulta):
    """Dada una consulta, vuelve a realizar otra consulta nueva con las palabras relevantes de la primera consulta. 
    Estas palabras releventes son obtenidas aplicando tfidf sobre los htmls de las páginas
    Input: consulta
    Output: urls
    """
    new_query = consulta_a_palabras_relevantes(consulta=consulta)
    nuevos_urls = consulta_a_links(consulta=new_query)
    return nuevos_urls
