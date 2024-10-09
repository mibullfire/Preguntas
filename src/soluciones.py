from collections import namedtuple

soluciones = namedtuple('Soluciones', 'numero, correctas')

lista_soluciones = [soluciones(numero=1, correctas=['a', 'c', 'd', 'e']),
                    soluciones(numero=2,correctas=['a'])]
