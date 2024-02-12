from selenium import webdriver

from .aceptar_cookies import *
from consulta_palabras_relevantes import *

def prueba_txt_botones_cookies_a_lista():
    salida_esperada = ['ej1', 'ej2', 'ej3', 'ej4']
    salida_obtenida = txt_botones_cookies_a_lista(file_dir='cookies/prueba_txt_botones_cookies_a_lista.txt')
    if salida_obtenida == salida_esperada:
        print("Prueba de la función 'txt_botones_cookies_a_lista' pasada correctamente")
    else:
        print("Prueba de la función 'txt_botones_cookies_a_lista' NO pasada correctamente")

def prueba_cargar_ficheros_botones_cookies():
    salida_esperada = (['didomi-notice-agree-button', 'onetrust-accept-btn-handler', 'ez-accept-all', 'hs-eu-confirmation-button', 'pea_cook_btn', 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll'], 
                       ['cdp-cookies-boton-cerrar', 'accept', 'fc-button fc-cta-consent fc-primary-button', 'btn btn-primary btn-sm', 'shareaholic-cookie-consent-button shareaholic-accept-button', 'mgbutton moove-gdpr-infobar-allow-all gdpr-fbo-0', 'cky-btn cky-btn-accept', 'CybotCookiebotDialogBodyButton'])
    salida_obtenida = cargar_ficheros_botones_cookies()
    if salida_obtenida == salida_esperada:
        print("Prueba de la función 'cargar_ficheros_botones_cookies' pasada correctamente")
    else:
        print("Prueba de la función 'cargar_ficheros_botones_cookies' NO pasada correctamente")

def prueba_aceptar_cookies_sin_descargar_html():
    url = 'https://www.sonymusic.es/playlist/2010-hits-decade/'
    driver = webdriver.Chrome()
    salida_esperada = 1
    salida_obtenida = aceptar_cookies(driver=driver, url=url)
    driver.quit()
    if salida_obtenida == salida_esperada:
        print("Prueba de la función 'aceptar_cookies' sin descargar html pasada correctamente")
    else:
        print("Prueba de la función 'aceptar_cookies' sin descargar html NO pasada correctamente")

def prueba_aceptar_cookies_descargando_html():
    url = 'https://www.sonymusic.es/playlist/2010-hits-decade/'
    driver = webdriver.Chrome()
    salida_obtenida = aceptar_cookies(driver=driver, url=url, download_html=True)
    driver.quit()
    if salida_obtenida != None:
        print("Prueba de la función 'aceptar_cookies' descargando html pasada correctamente")
    else:
        print("Prueba de la función 'aceptar_cookies' descargando html NO pasada correctamente")

def prueba_aceptar_cookies_y_guardar_htmls():
    urls = ['https://www.eluniverso.com/larevista/2021/01/17/nota/9491971/canciones-que-mas-escuchamos-decada-2010-2020/', 
            'https://www.sonymusic.es/playlist/2010-hits-decade/', 
            'https://neliosoftware.com/es/blog/como-crear-un-aviso-de-cookies-con-nelio-popups/']
    salida_obtenida = aceptar_cookies_y_guardar_htmls(urls=urls, show_process=False)
    if len(salida_obtenida) == 3:
        print("Prueba de la función 'aceptar_cookies_y_guardar_htmls'  pasada correctamente")
    else:
        print("Prueba de la función 'aceptar_cookies_y_guardar_htmls' NO pasada correctamente")
        

prueba_txt_botones_cookies_a_lista()
prueba_cargar_ficheros_botones_cookies()
#prueba_aceptar_cookies_sin_descargar_html()
#prueba_aceptar_cookies_descargando_html()
#prueba_aceptar_cookies_y_guardar_htmls()