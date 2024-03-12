from functionsAcceptCookies import *
from functionsNLP import *
from functionsReadWriteFiles import *
import time
import pandas as pd
import os

ids = ['rascacielos', 'animalesExtinguidos', 'bolsa','bolsa2', 'cafeina', 'cena', 'introversion', 'lumbarPropiocepcion',
      'motor','musicaClasica', 'plantasHogar', 'pollo', 'rodilla', 'rusiaHistoria','tigres', 'tortugas']

df = pd.DataFrame(columns=['idConsulta', 'botonesClicados', 'botonesNoClicados',
                           'noHayBoton','htmlsDescargados','totalUrls'])
for id in ids:
    outputs = txt_a_lista(f"results/output_funcion_acept_cookies/resParalelo_{id}.txt")
    total_urls = len(cargar_urls(id_consulta=id))
    num_elementos = len(os.listdir(f"results/textos/{id}"))
    botones_clicados = 0
    botones_no_clicados = 0
    no_hay_boton = 0
    for output in outputs:
        if "encontrado y clicado" in output:
            botones_clicados += 1
        if "no encontrada" in output:
            botones_no_clicados +=1
        if "no tiene cookies" in output:
            no_hay_boton +=1
    nueva_fila = {'idConsulta': id, 'botonesClicados': botones_clicados, 
                  'botonesNoClicados': botones_no_clicados, 'noHayBoton': no_hay_boton,
                  'htmlsDescargados':num_elementos, 'totalUrls': total_urls}
    df = df._append(nueva_fila, ignore_index=True)

t_ej = pd.read_csv("results/tiempo_ejecucion.csv")
df['tEjNoParalelo'] = t_ej['tiempo_ejecucion_no_paralelo']
df['tEjParalelo'] = t_ej['tiempo_ejecucion_paralelo']
df['speedup'] = df['tEjNoParalelo']/ df['tEjParalelo']
print(df)
pct_botones_clicados = df['botonesClicados']/df['totalUrls']
print('-----------------------------------------------------------------------')
pct_htmls_no_descargados = df['totalUrls']/df['totalUrls']
print('Porcentaje medio de htmls descargados', pct_htmls_no_descargados.mean()*100,'%')
print('Porcentaje medio de botones de cookies encontrados clicados', round(pct_botones_clicados.mean()*100,3),'%')
print('Speedup medio conseguido con ejecución paralela de la función aceptar_cookies', round(df['speedup'].mean(),3), 'segundos')
df.to_csv("results/metricas.csv", index=False)

cargar