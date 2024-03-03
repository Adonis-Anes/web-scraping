INTRODUCCIÓN

Este proyecto trata de obtener las palabras relevantes de una consulta de Google. La obtención de estas palabras se realiza mediante la matriz TF-IDF. Los documentos que alimentan esta matriz son los htmls de las páginas web seleccionadas por la consulta hecha inicialmente. La selección de estas páginas es mediante SerApi. Una parte clave de este proyecto es la aceptación de cookies de las páginas. 

Web scraping program in Python using selenium library and SerApi for searches. Specifically focuses in accepting the cookies button in the websites, dowloading the html and finding the most relevant words across the websites using tfidf. These words will be used then for making a new search using SerApi.

FICHEROS

- cookies (carpeta)
- results(carpeta): contiene los resultados de la ejecución de la(s) funcione(s).
- test (carpeta): contiene datos que sirven para realizar los test de las funciones.
- example (python notebook): contiene ejemplos de uso de las funciones.
- functionsAccepCookies (archivo python): contiene el conjunto de funciones que se encargan de encontrar y aceptar el botón de cookies y además de descargar el html de la página web.
- functionsNLP (archivo python): contiene el conjunto de funciones que se encargan de procesar el texto del html de las páginas web y extraer las palabras relevantes.
- functionsReadWriteFiles (archivo python): contiene el conjunto de funciones que leen y crean archivos en el directorio de carpetas.
- functionsSerApi (archivo python): contiene el conjunto de funciones encargadas de realizar consultas a SerApi y de conseguir el conjunto de links.
- main (archivo python): contiene la función principal.
- stopwords (archivo de texto): contiene el conjunto de stopwords utilizadas.
- test (archivo python): realiza un test de algunas funciones.

EJEMPLOS DE USO

Una de las funciones principales que se llama `consulta_a_palabras_relevantes` llama en su ejecución a un conjunto de funciones, que pueden ser invocadas por separado y dan el mismo resultado que llamar a esta función.
Veámoslo en el siguiente ejemplo. 

      # 0.- Definir la consulta
      consulta_cafeina = 'cuál es el componente de la cafeína que actúa en el cerebro'
      # 1.- Pasar de una consulta escrita a un conjunto de links
      urls_cafeina = consulta_a_links(consulta=consulta_cafeina)
      # 2.- Meternos en dichas páginas, aceptar las cookies y descargar el html
      htmls_cafeina = aceptar_cookies_y_guardar_htmls_paralelizado(urls=urls_cafeina)
      # 3.- Obtener el texto de los htmls
      textos_cafeina = htmls_a_textos(htmls=htmls_cafeina)
      # 4.- Crear la matriz tfidf de dichos textos
      matriz_tfidf_cafeina = crear_matriz_tfidf(text_files=textos_cafeina)
      # 5.- Mostrar en pantalla las n palabras relevantes extraídas por la matriz
      palabras_rel_consulta_cafeina = top_n_palabras_rel_tdidf(tfidf=matriz_tfidf_cafeina)
      print('Palabras relevantes de la consulta: ',palabras_rel_consulta_cafeina)

Estas líneas de código son equivalentes a llamar directamente a la función `consulta_a_palabras_relevantes(consulta=consulta_cafeina)`

También podemos guardar los resultados de la ejecución de cada función. Véase el fichero example.ipynb

Para aceptar las cookies se crea una función básica llamada `encontrar_elemento_y_clicar` que recibe como argumentos obligatorios una url y un xpath. Básicamente lo que hace es iniciar el driver, si no está pasado como parámetro, espera hasta un máximo de 3 segundos hasta encontrar un elemento clicable con el xpath pasado. Si lo encuentra lo clica.
Sobre esta función se construyen las demás. 
Dada una lista de candidatos a ser el botón de cookies de la página web, iteramos hasta que se alguno de estos coincida o agotemos la lista.

