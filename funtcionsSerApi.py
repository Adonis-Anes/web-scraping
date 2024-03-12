# !pip install google-search-results
from serpapi import GoogleSearch

def txt_a_consulta_SerApi(txt_file):
  """
  DESCRIPCIÓN: lee un txt con un formato específico (especificado abajo),
  limpia el texto, quitándo lo no es válido para los parámetros de búsqueda de SerApi
  y transforma los idiomas al formato estándar de Google.
  ENTRADA: un fichero txt con el siguiente formato:
    (1) CONSULTA: <valor>
    (2) IDIOMAS DE LAS PÁGINAS: <valor>
    ---Ejemplo:----------------------------------------------
    (1) CONSULTA: moda estilo ropa
    (2) IDIOMAS DE LAS PÁGINAS: español inglés catalán
  SALIDA: dos variables: consulta e idiomasm en formato específico para introducirlo
  directamente en los parámetros de búsqueda de SerApi
  """
  file = open(txt_file)
  consulta = file.readline()
  idiomas = file.readline()
  consulta = consulta.replace("(1) CONSULTA: ", "")
  consulta = consulta.replace("\n", "")
  idiomas = idiomas.replace("(2) IDIOMAS DE LAS PÁGINAS: ", "")
  idiomas = idiomas_a_formato_google_supported_languagues(idiomas)
  return consulta, idiomas

def idiomas_a_formato_google_supported_languagues(idiomas):
  """
  DESCIPCIÓN: tranforma idiomas escritos en español al formato estándar de Google
  para las búsquedas.
  ENTRADA: una cadena de texto (string) de idiomas escritos en español separados por espacios
  SALIDA: cadena de texto con los idiomas en el formato estándar de Google
  para las búsquedas.

  """
  a_reemplazar = ["español", "catalán","catalan","inglés", "ingles", "vasco", "euskera", "gallego", "francés", "alemán", "aleman"]
  reemplazo = ["lang_es", "lang_ca", "lang_ca", "lang_en","lang_en", "lang_eu","lang_eu","lang_ga","lang_fr","lang_de","lang_de" ]
  for i in range(len(a_reemplazar)):
    idiomas=idiomas.replace(a_reemplazar[i], reemplazo[i])
  return idiomas

# 1 QUERY --> ORGANIC RESULTS
def consulta_a_organic_results(consulta :str,
                               idiomas_pags :str = "" ,
                               idioma_google :str = "" ,
                               pais_google :str = "" ,
                               origen_busqueda :str = ""):
  """
  DESCRIPCIÓN: a partir de una consulta obtener los organic results de SerApi
  ENTRADA:
   - consulta: conjunto de palabras que definen la búsqueda (obligatorio)
   - idiomas_pags: el idioma en el que están las páginas que se quieren encontrar (opcional)
   - idioma_google: lenguaje que usa Google para buscar (opcional)
   - pais_google: país desde donde busca Google (opcional)
   - origen_busqueda: desde donde se realiza la búsqueda (opcional)
  SALIDA: organic results de SerApi
  """
  secret_api_key = SECRET_API_KEY
  params = {
    "engine": "google",
    "q": consulta,
    "api_key": secret_api_key,
    "lr": idiomas_pags, #language result: one or multiple languages to limit the search to (OPTIONAL)
    # Geographic Location ------------------------------------------------------------------
    "location": origen_busqueda, #from where you want the search to originate (OPTIONAL)
    # Localization --------------------------------------------------------------------------
    "hl": idioma_google, #language to use for the Google search (OPTIONAL)
    "gl": pais_google, #google location: country to use for the Google search (OPTIONAL)
  }
  search = GoogleSearch(params)
  results = search.get_dict()
  organic_results = results["organic_results"]
  return organic_results

# 2 ORGANIC RESULTS --> LINKS
def extraer_links_de_organic_results(organic_results):
  urls_retrieved = []
  for res in organic_results:
    urls_retrieved.append(res['link'])
  return urls_retrieved

# 1 y 2 junto
def consulta_a_links(consulta:str, idiomas_pags:str="", idioma_google:str="", pais_google:str="", origen_busqueda:str=""):
  """
  DESCIPCIÓN: recibe una consulta completa y devuelve un conjunto links relevantes a esa consulta
  ENTRADA:
   - consulta (obligatorio)
   - resto de variables opcional (ver descipción completa en la función "consulta_a_organic_results")
  SALIDA: lista de links rastreados por SerApi resultado de la consulta hecha

  """
  # Función que dada una query devuelve un conjunto de links que ha recogido SerApi
  organic_results = consulta_a_organic_results(consulta, idiomas_pags="", idioma_google="", pais_google="", origen_busqueda="")
  links = extraer_links_de_organic_results(organic_results)
  return links

# TODO JUNTO
def txt_a_links(txt):
  """
  DESCIPCIÓN: recibe un txt que contiene la consulta completa y devuelve un conjunto links relevantes a esa consulta
  ENTRADA: fichero txt que contenga la consuta a realizar
  con formato especificado en la función "txt_a_consulta_SerApi"
  SALIDA: lista de links rastreados por SerApi resultado de la consulta hecha

  """
  consulta, idiomas_pags=txt_a_consulta_SerApi(txt)
  organic_results = consulta_a_organic_results(consulta, idiomas_pags="", idioma_google="", pais_google="", origen_busqueda="")
  links = extraer_links_de_organic_results(organic_results)
  return links
