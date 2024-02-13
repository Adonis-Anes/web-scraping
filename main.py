from functions import aceptar_cookies_y_guardar_htmls, htmls_a_textos, crear_matriz_tfidf, top_n_palabras_rel_tdidf
from SerApi_searches import consulta_a_links

def consulta_a_palabras_relevantes(consulta:str):
    """Obtiene las palabras relevantes de la consulta realizada 
       resultado de aplicar tfidf sobre los htmls de las páginas.
    Input: 
        - consulta: variable tipo string con la consulta a realizar.
    Output: palabras relevantes
    """
    urls = consulta_a_links(consulta=consulta)
    htmls = aceptar_cookies_y_guardar_htmls(urls=urls)
    textos = htmls_a_textos(htmls=htmls)
    matriz = crear_matriz_tfidf(text_files=textos)
    top_10_words = top_n_palabras_rel_tdidf(tfidf=matriz)
    print('10 palabras más relevantes en todas las consultas:\n',top_10_words)
    return top_10_words
    
def consulta_a_nueva_consulta(consulta:str):
    """Dada una consulta, vuelve a realizar otra consulta nueva con las palabras relevantes de la primera consulta. 
       Estas palabras relevantes son obtenidas aplicando tfidf sobre los htmls de las páginas.
    Input: 
        - consulta: variable tipo string con la consulta a realizar.
    Output: lista de urls.
    """
    new_query = consulta_a_palabras_relevantes(consulta=consulta)
    nuevos_urls = consulta_a_links(consulta=new_query)
    return nuevos_urls
