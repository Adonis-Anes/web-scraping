from functionsAcceptCookies import aceptar_cookies_y_extraer_htmls_concurrente, aceptar_cookies_y_extraer_htmls_no_concurrente
from functionsReadWriteFiles import *
import time
import numpy

ids_consultas = ['animalesExtinguidos', 'bolsa', 'bolsa2', 'caballitos', 'cafeina', 'cena', 'introversion', 
               'lumbarPropiocepcion', 'motor', 'musicaClasica', 'plantasHogar', 'pollo', 'rascacielos', 
               'rodilla', 'rusiaHistoria', 'tigres', 'tortugas']

lista_urls = []
for id_consulta in ids_consultas:
    lista_urls.append(cargar_urls(id_consulta=id_consulta))


tiempos_ejecucion_con = []
tiempos_ejecucion_no = []

i=0

inicio_ej_con = time.time()
aceptar_cookies_y_extraer_htmls_concurrente(urls=lista_urls[i])
fin_ej_con = time.time()
tiempos_ejecucion_con.append(fin_ej_con - inicio_ej_con)
print(tiempos_ejecucion_con)
guardar_lista_como_txt_por_lineas(tiempos_ejecucion_con, 'tiempos_ejecucion_con.txt')

#
inicio_ej_no = time.time()
aceptar_cookies_y_extraer_htmls_no_concurrente(urls=lista_urls[i])
fin_ej_no = time.time()
tiempo_ejucion_no = fin_ej_no - inicio_ej_no
tiempos_ejecucion_no.append(fin_ej_no - inicio_ej_no)
print(tiempos_ejecucion_no)
guardar_lista_como_txt_por_lineas(tiempos_ejecucion_no, 'tiempos_ejecucion_no.txt')
