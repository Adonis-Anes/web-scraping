from funtcionsSerApi import consulta_a_links
from functionsAcceptCookies import *
from functionsNLP import *
from functionsReadWriteFiles import *

def consulta_a_palabras_relevantes(consulta:str, id_consulta, guardar_archivos=False):
    """Obtiene las palabras relevantes de la consulta realizada 
       resultado de aplicar tfidf sobre los htmls de las páginas.
    Input: 
        - consulta: variable tipo string con la consulta a realizar.
        - guardar_archivos: si quieres guardar los archivos generados en la consulta
        - id_consulta: palabra que identifica a la consulta con la que se nombrarán las carpetas
        - mostrar_proceso: 
    Output: palabras relevantes
    """
    print('0.- Realizando la consulta y obteniendo links')
    urls = consulta_a_links(consulta=consulta)
    print('1.- Aceptando cookies y extrayendo html')
    htmls = aceptar_cookies_y_extraer_htmls_concurrente(urls=urls)
    print('2.- Extrayendo texto limpio del html')
    textos = htmls_a_textos(htmls=htmls)
    print('3.- Creando la matriz tfidf')
    tfidf = crear_matriz_tfidf(text_files=textos)
    print('4.- Obteniendo palabras más relevantes')
    top_10_words = top_n_palabras_rel_tdidf(tfidf=tfidf)
    print('Las 10 palabras relevantes son:\n',top_10_words)
    if guardar_archivos == True:
        guardar_consulta(consulta=consulta, id_consulta=id_consulta)
        guardar_urls(urls=urls, id_consulta=id_consulta)
        #guardar htmls
        crear_carpeta(f'results/htmls/{id_consulta}/')
        guardar_htmls(htmls=htmls, id_consulta=id_consulta)
        #guardar textos
        crear_carpeta(f'results/textos/{id_consulta}/')
        guardar_textos(textos=textos, id_consulta=id_consulta)
        #guardar matriz tfidf
        guardar_tfidf(id_consulta=id_consulta)
        #guardar palabras relevantes
        guardar_palabras_rel(palabras=top_10_words, id_consulta=id_consulta)
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
