from functions import txt_a_string
import os

consultas = os.listdir('results/consultas/')
palabras_rel = os.listdir('results/palabras_rel/')
for i in range(len(consultas)):
    consulta = txt_a_string('results/consultas/'+consultas[i])
    print('Consulta realizada: ', consulta)
    palabra_rel = txt_a_string('results/palabras_rel/'+palabras_rel[i])
    print('Palabras relevantes extraídas: ', palabra_rel)
    print('----------------------------------------------------------------')