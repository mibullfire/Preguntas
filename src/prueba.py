from preguntas import *
from soluciones import *
from collections import namedtuple
import random
import csv

soluciones = namedtuple('Soluciones', 'numero, pregunta, respuestas, correctas')

def leer_fichero(ruta):
    res = []
    with open(ruta, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)
        for numero, pregunta, respuestas, correctas in lector:
            res.append(soluciones(int(numero), pregunta, respuestas.split(';'), correctas.split(';')))

    return res

def pregunta(lista):
    numero = random.randint(1, len(lista))
    for i in lista:
        if i.numero == numero:
            print(i.pregunta)
            for j in i.respuestas:
                print(j)
            respuesta = input('Respuesta: ')
            respuestas = respuesta.split(',')
    
    for i in lista:
        if i.numero == numero:
            for x in respuestas:
                if x in i.correctas:
                    print(f'\n {x} es correcta!')
                else:
                    print(f'\n {x} es incorrecto!')
    
    if sorted(respuestas) == sorted(i.correctas):
        print('\nHas acertado todo!')
    else:
        print('\nTodas las respuestas correctas eran: ', i.correctas)

#print(leer_fichero('data/solucionario.csv'))
pregunta(leer_fichero('data/solucionario.csv'))