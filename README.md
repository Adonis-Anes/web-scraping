# INTRODUCCIÓN

Este proyecto trata de obtener las palabras relevantes de una consulta de Google. La obtención de estas palabras se realiza mediante la matriz TF-IDF. Los documentos que alimentan esta matriz son los htmls de las páginas web seleccionadas por la consulta hecha inicialmente. La selección de estas páginas es mediante SerApi. Una parte clave de este proyecto es la aceptación de cookies de las páginas. 

Web scraping program in Python using selenium library and SerApi for searches. Specifically focuses in accepting the cookies button in the websites, dowloading the html and finding the most relevant words across the websites using tfidf. These words will be used then for making a new search using SerApi.

# FICHEROS

- **cookies** (carpeta)
- **results** (carpeta): contiene los resultados de la ejecución de la(s) funcione(s).
    - **consultas** (carpeta): contiene el string de las consultas realizadas.
    - **htmls** (carpeta): contiene carpetas, las cuales cada una contienen los htmls de las páginas consultadas.
    - **matrices** (carpeta): contiene las matrices tfidf (guardados como .csv) generadas resultado de procesar el contenido de texto de los htmls de una consulta.
    - **output_funcion_acept_cookies** (carpeta): contiene la salida de la función ``aceptar_cookies`` para un conjunto de urls dada una consulta.
    - **palabras_rel** (carpeta): contiene las 10 palabras más relevantes según la matriz tfidf de cada consulta realizada.
    - **textos** (carpeta): contiene carpetas, las cuales cada una contienen los textos de las páginas consultadas (tras haber limpiado el texto del html).
    - **urls**: contiene ficheros de texto, las cuales contienen el conjunto de urls extraídas tras reallizar una consulta.
    - **métricas** (archivo csv): una tabla que contiene información acerca del número de botones de cookies clicados correctamente, urls extraídas, htmls descargados y otra información.
    - **tiempo_ejecución** (archivo csv): recoge el tiempo de ejecución de la función ``aceptar_cookies_sin_palalelizar`` y ``aceptar_cookies_paralelizado``.
  
- **test** (carpeta): contiene datos que sirven para realizar los test de las funciones.
- **example** (python notebook): contiene ejemplos de uso de las funciones.
- **functionsAccepCookies** (archivo python): contiene el conjunto de funciones que se encargan de encontrar y aceptar el botón de cookies y además de descargar el html de la página web.
- **functionsNLP** (archivo python): contiene el conjunto de funciones que se encargan de procesar el texto del html de las páginas web y extraer las palabras relevantes.
- **functionsReadWriteFiles** (archivo python): contiene el conjunto de funciones que leen y crean archivos en el directorio de carpetas.
- **functionsSerApi** (archivo python): contiene el conjunto de funciones encargadas de realizar consultas a SerApi y de conseguir el conjunto de links.
- **main** (archivo python): contiene la función principal.
- **stopwords** (archivo de texto): contiene el conjunto de stopwords utilizadas.
- **test** (archivo python): realiza un test de algunas funciones.

# EJEMPLOS DE USO

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

Véase el fichero example.ipynb

# ANÁLISIS DE RESULTADOS

  |          idConsulta |botonesClicados|botonesNoClicados|noHayBoton|htmlsDescargados| totalUrls|tEjNoParalelo| tEjParalelo|speedup
  ---------------------------------------------------------------------------------------------------------------------------------------
0 |         rascacielos |             0 |                7|         2|               9|        9 |       173.830|    72.171 |  2.408585
1 | animalesExtinguidos |             3 |                4|         2|               9|        9 |       356.284|    69.879 |  5.098585
2 |               bolsa |             2 |                5|         0|               7|        7 |       125.259|    28.600 |  4.379685
3 |              bolsa2 |             5 |                3|         0|               8|        8 |        80.385|    40.854 |  1.967616
4 |             cafeina |             4 |                5|         0|               9|        9 |       134.153|    50.597 |  2.651402
5 |                cena |             1 |                7|         0|               8|        8 |       178.739|    80.846 |  2.210858
6 |        introversion |             3 |                6|         0|               9|        9 |       162.473|    70.046 |  2.319519
7 | lumbarPropiocepcion |             1 |                4|         4|               9|        9 |        90.177|    59.184 |  1.523672
8 |               motor |             3 |                5|         0|               8|        8 |       116.876|    64.084 |  1.823794
9 |       musicaClasica |             2 |                3|         1|               6|        6 |       147.525|    65.496 |  2.252428
10|        plantasHogar |             2 |                6|         0|               8|        8 |       162.719|   128.117 |  1.270081
11|               pollo |             1 |                3|         5|               9|        9 |        84.837|    65.587 |  1.293503
12|             rodilla |             3 |                7|         0|              10|       10 |       164.980|    65.234 |  2.529049
13|       rusiaHistoria |             0 |                6|         2|               8|        8 |       132.287|    55.951 |  2.364337
14|              tigres |             2 |                6|         0|               8|        8 |       130.024|    86.855 |  1.497024
15|             tortugas |            2 |                6|         1|               9|        9 |       138.209|    51.573 |  2.679871



## Resumen
**Porcentaje medio de htmls descargados:** 100.0 %

**Porcentaje medio de botones de cookies encontrados clicados:** 25.623 %

**Speedup medio conseguido con ejecución paralela de la función aceptar_cookies:** 2.392 segundos

*Nota:* estos resultados se pueden ver al ejecutar el fichero métricas.py


# EXPLICACIÓN DEL CÓDIGO

## Funciones para aceptar el botón de cookies
Para aceptar las cookies se crea una función básica llamada `encontrar_elemento_y_clicar` que recibe como argumentos obligatorios una url y un xpath. Básicamente lo que hace es iniciar el driver, si no está pasado como parámetro, espera hasta un máximo de 3 segundos hasta encontrar un elemento clicable con el xpath pasado. Si lo encuentra lo clica.
Sobre esta función se construyen las demás. 
Dada una lista de candidatos a ser el botón de cookies de la página web, iteramos hasta que se alguno de estos coincida o agotemos la lista.


# POSIBLES MEJORAS Y LIMITACIONES
