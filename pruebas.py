from functionsAcceptCookies import *
from functionsNLP import *
from functionsReadWriteFiles import *
import time

id = 'cafeina'
urls = cargar_urls(id_consulta=id)
ini = time.time()
aceptar_cookies_paralelizado(urls=urls)
fin = time.time()
print(fin-ini)