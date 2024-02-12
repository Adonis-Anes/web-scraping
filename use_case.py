from functions import *
from main import *
from selenium import webdriver
from SerApi_searches import consulta_a_links


#USO DE LA FUNCIÓN 'aceptar_cookies'
driver = webdriver.Chrome()
url='https://cnnespanol.cnn.com/tag/nayib-bukele/'
aceptar_cookies(driver=driver, url=url, show_process=True)
driver.quit()

# USO DE LA FUNCIONES QUE ENGLOBA LA FUNCIÓN 'consulta_a_palabras_relevantes'
consulta_cafeina = 'cuál es el componente de la cafeína que actúa en el cerebro'

# 1.- Pasar de una consulta escrita a un conjunto de links
urls_cafeina = consulta_a_links(consulta=consulta_cafeina)
# 2.- Meternos en dichas páginas, aceptar las cookies y descargar el html
htmls_cafeina = aceptar_cookies_y_guardar_htmls(urls=urls_cafeina)
# 3.- Obtener el texto de los htmls
textos_cafeina = htmls_a_textos(htmls=htmls_cafeina)
# 4.- Crear la matriz tfidf de dichos textos
matriz_tfidf_cafeina = crear_matriz_tfidf(text_files=textos_cafeina)
print("--------Función 'top_n_palabras_rel_tdidf' en ejecución--------")
# 5.- Mostrar en pantalla las n palabras relevantes extraídas por la matriz
palabras_rel_consulta_cafeina = top_n_palabras_rel_tdidf(tfidf=matriz_tfidf_cafeina)
print('Palabras relevantes de la consulta: ',palabras_rel_consulta_cafeina)

# Uso de la función 'consulta_a_palabras_relevantes'
consulta_a_palabras_relevantes(consulta=consulta_cafeina)
