# Librerías parte 0
import os
import errno
import pandas as pd

"""PARTE 0: LEER Y GUARDAR ARCHIVOS"""
def crear_carpeta(dir_carpeta):
  try:
      os.mkdir(dir_carpeta)
  except OSError as e:
      if e.errno != errno.EEXIST:
          pass

def txt_a_string(dir_archivo):
   """
   Leer archivo txt y generar una variable tipo string donde se almacene el contenido del txt
   Input:
    - file_dir: dirección completa del archivo que queremos leer
    Output: nada
   """
   with open(dir_archivo, 'r',  encoding="utf-8") as f:
      return f.read()

def cargar_palabras_rel(id_consulta):
    return txt_a_string(f"results/palabras_rel/palabrasRel_{id_consulta}.txt")

def guardar_string_como_txt(string, dir_dest):
    """ 
    Guarda un objeto tipo string de Python en un fichero txt 
    Input:
      - text: objeto de Python tipo string que queremos guardar
      - dir_dest: dirección de destino del archivo
    Output: Nada
    """
    with open(dir_dest, 'w', encoding="utf-8") as f:
        f.write(string)
    f.close()

def guardar_consulta(consulta, id_consulta):
    guardar_string_como_txt(consulta, f'results/consultas/consulta_{id_consulta}.txt')

def guardar_palabras_rel(palabras, id_consulta):
    guardar_string_como_txt(palabras, f"results/palabras_rel/palabrasRel_{id_consulta}.txt")

def txt_a_lista(dir_archivo):
    """
    Leer archivo txt y generar una variable lista donde cada línea del archivo 
    se convierte en un objeto de la lista.
    Input: 
      - dir_archivo: directorio donde se encuentra el archivo txt que queremos leer.
    Output: objeto tipo lista con el contenido del txt. 
    """
    lista = []
    with open(dir_archivo, 'r') as f:
        lista = [linea.rstrip() for linea in f]
    f.close()
    return lista

def cargar_xpath_boton_cookies():
    return txt_a_lista('cookies/xpath_cookies')
    

def cargar_urls(id_consulta):
    return txt_a_lista(f"results/urls/urls_{id_consulta}.txt")

def guardar_lista_como_txt_por_lineas(lista, dir_dest):
    """ 
    Guarda un objeto tipo lista de Python en un fichero txt donde cada linea del txt 
    es un objeto de la lista.
    Input:
      - lista: lista que quermos guardar
      - dir_dest: dirección de destino del archivo
    Output: Nada
    """
    with open(dir_dest, 'w') as f:
        for line in lista:
            f.write(f"{line}\n")
    f.close()

def guardar_urls(urls:list, id_consulta):
    guardar_lista_como_txt_por_lineas(urls, f'results/urls/urls_{id_consulta}.txt')

def archivos_de_carpeta_a_lista(dir_carpeta):
    """
    Lee un directorio y carga los archivos contenidos en el en una variable lista 
    donde cada elemento de la lista es un archivo de la carpeta.
    Los archivos dentro de la carpeta deben de tener un nombre común.
    El formato de la parte variable debe ser {número}.txt
    Input: 
      - dir_comun: nombre común que identifica a los archivos contenidos en la carpeta.
      - num_archivos: número de archivos dentro de la carpeta
    Output: objeto tipo lista con el contenido del txt. 
    """
    nombres_archivos = os.listdir(dir_carpeta)
    lista = []
    for nombre_archivo in nombres_archivos:
        dir_completa = dir_carpeta + nombre_archivo
        lista.append(txt_a_string(dir_archivo=dir_completa))
    return lista

def cargar_htmls(id_consulta):
    return archivos_de_carpeta_a_lista(f'results/htmls/{id_consulta}/')

def cargar_textos(id_consulta):
    return archivos_de_carpeta_a_lista(f'results/textos/{id_consulta}/')

def guardar_cada_elem_de_lista_como_archivo_diferente(lista, dir_dest_comun, extension='.txt'):
    """ 
    Guarda un objeto tipo string de Python que contiene un html en un fichero txt 
    donde cada linea del txt es un objeto de la lista.
    Input:
      - dir_dest_comun: dirección de carpetas de destino de los archivos y nombre base 
        que compartirán los archivos, sin la extensión .txt ya que luego se se le añadirá 
        un número que les identificará según su posición en la lista
    Output: Nada
    """
    for i in range(len(lista)):
        dir_dest = dir_dest_comun + str(i) + extension
        guardar_string_como_txt(string=lista[i], dir_dest=dir_dest)

def guardar_htmls(htmls, id_consulta):
    guardar_cada_elem_de_lista_como_archivo_diferente(lista= htmls, dir_dest_comun=f'results/htmls/{id_consulta}/html_{id_consulta}', extension='.html')    

def guardar_textos(textos, id_consulta):
    guardar_cada_elem_de_lista_como_archivo_diferente(lista= textos, dir_dest_comun=f'results/textos/{id_consulta}/texto_{id_consulta}')

def csv_a_df(dir_archivo):
    return pd.read_csv(dir_archivo)

def cargar_tfidf(id_consulta):
    return csv_a_df(f"results/matrices/tfidf_{id_consulta}.csv")

def guardar_df_como_csv(df, dir_dest):
    """
    Guardar un DataFrame como un csv. 
    Se guardan en la carpeta results/matrices/
    Solo es necesario proprocionar el nombre, el resto de la dirección se completa.
    Input:
      - df: El DataFrame que queremos guardar.
      - dir_dest: el nombre con que queremos guardar la matriz
    Output: Nada
    """
    df.to_csv(path_or_buf=dir_dest, index_label="palabras")

def guardar_tfidf(tfidf, id_consulta):
    dir_dest = f'results/matrices/tfidf_{id_consulta}.csv'
    guardar_df_como_csv(tfidf, dir_dest=dir_dest)
"""-------------------------------------------------------------------------------------------------------------"""



