from selenium import webdriver
import unittest

from aceptar_cookies import *

class TestCookieMethods(unittest.TestCase):

    def test_txt_botones_cookies_a_lista(self):
        salida_esperada = ['ej1', 'ej2', 'ej3', 'ej4']
        salida_obtenida = txt_botones_cookies_a_lista(file_dir='cookies/prueba_txt_botones_cookies_a_lista.txt')
        self.assertEqual(salida_obtenida, salida_esperada)

    def test_cargar_ficheros_botones_cookies(self):
        salida_esperada = (['didomi-notice-agree-button', 'onetrust-accept-btn-handler', 'ez-accept-all', 'hs-eu-confirmation-button', 'pea_cook_btn', 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll'], 
                        ['cdp-cookies-boton-cerrar', 'accept', 'fc-button fc-cta-consent fc-primary-button', 'btn btn-primary btn-sm', 'shareaholic-cookie-consent-button shareaholic-accept-button', 'mgbutton moove-gdpr-infobar-allow-all gdpr-fbo-0', 'cky-btn cky-btn-accept', 'CybotCookiebotDialogBodyButton'])
        salida_obtenida = cargar_ficheros_botones_cookies()
        self.assertEqual(salida_obtenida, salida_esperada)

    def test_aceptar_cookies(self):
        url = 'https://www.sonymusic.es/playlist/2010-hits-decade/'
        driver = webdriver.Chrome()
        salida_esperada = 1
        salida_obtenida = aceptar_cookies(driver=driver, url=url)
        driver.quit()
        self.assertEqual(salida_obtenida, salida_esperada)

    def test_aceptar_cookies_y_guardar_htmls(self):
        urls = ['https://www.eluniverso.com/larevista/2021/01/17/nota/9491971/canciones-que-mas-escuchamos-decada-2010-2020/', 
                'https://www.sonymusic.es/playlist/2010-hits-decade/']
        salida_obtenida = aceptar_cookies_y_guardar_htmls(urls=urls, show_process=False)
        self.assertEqual(len(salida_obtenida), len(urls))  

if __name__ == '__main__':
    unittest.main()