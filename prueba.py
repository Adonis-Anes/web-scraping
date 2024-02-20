from functionsAcceptCookies import *
from functionsReadWriteFiles import *
import time

id_consulta = 'rodilla'
urls = cargar_urls(id_consulta=id_consulta)
inicio = time.time()
htmls = aceptar_cookies_y_extraer_htmls_paralelizado(urls=urls)
fin = time.time()
print((fin-inicio))
#print(htmls)
guardar_htmls(htmls=htmls, id_consulta=id_consulta)
