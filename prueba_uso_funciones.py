from aceptar_cookies import txt_botones_cookies_a_lista, cargar_ficheros_botones_cookies, aceptar_cookies
from consulta_palabras_relevantes import aceptar_cookies_y_guardar_htmls, html_a_texto, htmls_a_textos, cargar_stopwords, crear_matriz_tfidf, top_n_palabras_rel_tdidf, consulta_a_palabras_relevantes, consulta_a_nueva_consulta
from selenium import webdriver
from funciones_busqueda_SerApi import consulta_a_links

print('--------------------------------------------------------------------------------')
print("USO DE LA FUNCIÓN 'aceptar_cookies'")
driver = webdriver.Chrome()
url='https://cnnespanol.cnn.com/tag/nayib-bukele/'
aceptar_cookies(driver=driver, url=url, show_process=True)
driver.quit()

('--------------------------------------------------------------------------------')
print("USO DE LA FUNCIONES QUE ENGLOBA LA FUNCIÓN 'consulta_a_palabras_relevantes' ")
consulta_cafeina = 'cuál es el componente de la cafeína que actúa en el cerebro'
print("--------Función 'consulta_a_links' en ejecución--------")
urls_cafeina = consulta_a_links(consulta=consulta_cafeina)
print("--------Función 'aceptar_cookies_y_guardar_htmls' en ejecución--------")
htmls_cafeina = aceptar_cookies_y_guardar_htmls(urls=urls_cafeina)
print("--------Función 'htmls_a_textos' en ejecución--------")
textos_cafeina = htmls_a_textos(htmls=htmls_cafeina)
print("--------Función 'crear_matriz_tfidf' en ejecución--------")
matriz_tfidf_cafeina = crear_matriz_tfidf(text_files=textos_cafeina)
print("--------Función 'top_n_palabras_rel_tdidf' en ejecución--------")
palabras_rel_consulta_cafeina = top_n_palabras_rel_tdidf(tfidf=matriz_tfidf_cafeina)
print('Palabras relevantes de la consulta: ',palabras_rel_consulta_cafeina)

('--------------------------------------------------------------------------------')
print("USO DE LA FUNCIÓN 'consulta_a_palabras_relevantes'")
consulta = 'cuál es el componente de la cafeína que actúa en el cerebro'
consulta_a_palabras_relevantes(consulta)
