from functions import *
from SerApi_searches import consulta_a_links

def consulta_a_palabras_relevantes(consulta:str, guardar_archivos=False, id_consulta='', mostrar_proceso=False):
    """Obtiene las palabras relevantes de la consulta realizada 
       resultado de aplicar tfidf sobre los htmls de las páginas.
    Input: 
        - consulta: variable tipo string con la consulta a realizar.
        - guardar_archivos: si quieres guardar los archivos generados en la consulta
        - id_consulta: palabra que identifica a la consulta con la que se nombrarán las carpetas
        - mostrar_proceso: 
    Output: palabras relevantes
    """
    proceso = 5*[""]
    if mostrar_proceso == True:
        proceso = ['0.- Realizando la consulta y obteniendo links', '1.- Aceptando cookies y extrayendo html', 
                    '2.- Extrayendo texto limpio del html', '3.- Creando la matriz tfidf',
                    '4.- Obteniendo palabras más relevantes'] 
    proceso[0]
    urls = consulta_a_links(consulta=consulta)
    proceso[1]
    htmls = aceptar_cookies_y_guardar_htmls(urls=urls)
    proceso[2]
    textos = htmls_a_textos(htmls=htmls)
    proceso[3]
    tfidf = crear_matriz_tfidf(text_files=textos)
    proceso[4]
    top_10_words = top_n_palabras_rel_tdidf(tfidf=tfidf)
    print('10 palabras más relevantes en todas las consultas:\n',top_10_words)
    if guardar_archivos == True:
        if id_consulta == '':
            id_consulta = top_10_words[0:5]
        #guardar consulta
        guardar_string_como_txt(consulta, f'results/consultas/consulta_{id_consulta}.txt')
        #guardar urls
        guardar_lista_como_txt_por_lineas(urls, f'results/urls/urls_{id_consulta}.txt')
        #guardar htmls
        crear_carpeta(f'results/htmls/{id_consulta}/')
        guardar_cada_elem_de_lista_como_txt_diferente(lista=htmls, dir_dest_comun=f'results/htmls/{id_consulta}/html_{id_consulta}')
        #guardar textos
        crear_carpeta(f'results/textos/{id_consulta}/')
        guardar_cada_elem_de_lista_como_txt_diferente(lista=htmls, dir_dest_comun=f'results/textos/{id_consulta}/texto_{id_consulta}')
        #guardar matriz tfidf
        guardar_df_como_csv(tfidf,f'tfidf_{id_consulta}')
        #guardar palabras relevantes
        guardar_string_como_txt(top_10_words, f"results/palabras_rel/palabras_rel_{id_consulta}.txt")
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
