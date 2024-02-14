INTRODUCCIÓN

Este proyecto trata de obtener las palabras relevantes de una consulta de Google. La obtención de estas palabras se realiza mediante la matriz TF-IDF. Los documentos que alimentan esta matriz son los htmls de las páginas web seleccionadas por la consulta hecha inicialmente. La selección de estas páginas es mediante SerApi. Una parte clave de este proyecto es la aceptación de cookies de las páginas. 

Web scraping program in Python using selenium library and SerApi for searches. Specifically focuses in accepting the cookies button in the websites, dowloading the html and finding the most relevant words across the websites using tfidf. These words will be used then for making a new search using SerApi.

EJEMPLOS DE USO

      driver = webdriver.Chrome()
      url='https://cnnespanol.cnn.com/tag/nayib-bukele/'
      aceptar_cookies(driver=driver, url=url, show_process=True)
      driver.quit()


Una de las funciones principales que se llama `consulta_a_palabras_relevantes` llama en su ejecución a un conjunto de funciones, que pueden ser invocadas por separado y dan el mismo resultado que llamar a esta función.
Veámoslo en el siguiente ejemplo. 

      # 0.- Definir la consulta
      consulta_cafeina = 'cuál es el componente de la cafeína que actúa en el cerebro'
      # 1.- Pasar de una consulta escrita a un conjunto de links
      urls_cafeina = consulta_a_links(consulta=consulta_cafeina)
      # 2.- Meternos en dichas páginas, aceptar las cookies y descargar el html
      htmls_cafeina = aceptar_cookies_y_guardar_htmls(urls=urls_cafeina)
      # 3.- Obtener el texto de los htmls
      textos_cafeina = htmls_a_textos(htmls=htmls_cafeina)
      # 4.- Crear la matriz tfidf de dichos textos
      matriz_tfidf_cafeina = crear_matriz_tfidf(text_files=textos_cafeina)
      # 5.- Mostrar en pantalla las n palabras relevantes extraídas por la matriz
      palabras_rel_consulta_cafeina = top_n_palabras_rel_tdidf(tfidf=matriz_tfidf_cafeina)
      print('Palabras relevantes de la consulta: ',palabras_rel_consulta_cafeina)

Estas líneas de código son equivalentes a llamar directamente a la función `consulta_a_palabras_relevantes(consulta=consulta_cafeina)`

También podemos guardar los resultados de la ejecución de cada función. Véase el fichero example.ipynb

DESCRIPCIÓN DETALLADA
La descripción detallada se puede consultar en el siguiente documento.

