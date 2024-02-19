from selenium import webdriver
import unittest
from functionsReadWriteFiles import *
from functionsAcceptCookies import *

class TestCookieMethods(unittest.TestCase):

    def txt_a_string(self):
        salida_esperada = 'test función txt_a_string'
        salida_obtenida = txt_a_string('test/test_txt_a_string.txt')
        self.assertEqual(salida_obtenida, salida_esperada)

    def archivos_de_carpeta_a_lista(self):
        salida_esperada = ['file1','file2','file3']
        salida_obtenida = archivos_de_carpeta_a_lista('test/test_archivos_de_carpeta_a_lista/')
        self.assertEqual(salida_obtenida, salida_esperada)

    def test_txt_a_lista(self):
        salida_esperada = ['ej1', 'ej2', 'ej3', 'ej4']
        salida_obtenida = txt_a_lista('test/test_txt_a_lista.txt')
        self.assertEqual(salida_obtenida, salida_esperada)

    def test_buscar_boton_y_clicar(self):
        url = 'https://www.sostenibilidad.com/medio-ambiente/top-10-animales-extintos/'
        driver = iniciar_driver()
        salida_esperada = True
        xpath = "//*[contains(text(),'Acept')]"
        salida_obtenida = buscar_boton_y_clicar(url = url, xpath=xpath, driver=driver)
        driver.quit()
        self.assertEqual(salida_obtenida, salida_esperada)
    
if __name__ == '__main__':
    unittest.main()