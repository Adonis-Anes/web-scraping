from functionsAcceptCookies import *
from functionsNLP import *
from functionsReadWriteFiles import *

id_consultas = ["tortugas","animalesExtinguidos", "bolsa", "bolsa2", "cafeina", "cena",
               "introversion", "lumbarPropiocepcion", "motor", "musicaClasica", "rascacielos", 
               "rodilla", "rusiaHistoria", "tigres"]

for id in id_consultas:
    textos = cargar_textos(id_consulta=id)
    matriz = crear_matriz_tfidf(text_files=textos)
    guardar_tfidf(matriz, id_consulta=id)
    palabras = top_n_palabras_rel_tdidf(matriz)
    guardar_palabras_rel(palabras=palabras, id_consulta=id)