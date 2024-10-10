# APP para hacer Cuestionarios
Para usar el programa, ejecute directamente desde la terminal el fichero 'main.py':

```python
python3 main.py
```

En la carpeta 'data' hay un fichero csv, puede cambiarlo con cualquier bloque de preguntas, siguiendo la estructura:

```csv
numero,tema,pregunta,respuestas,respuestas_correctas
```
- numero: indica el número de la pregunta (int)
- tema: indica el tema de la pregunta (int)
- pregunta: título de la pregunta (str)
- respuestas: respuestas con todos los caracteres escritos, deben de empezar por 'n)' y separadas por ';' (str)
- respuestas_correctas: respuestas correctas de la pregunta. Pueden escribirse como a;b;c, o con todo el texto: a) Me llamo Lucas;b) Filipinos
Ejemplo:
```csv
6,Tema 2,¿Cuáles son las características del ciclo de vida iterativo?,a) Los usuarios deben evaluar el producto en cada iteración;b) Las primeras versiones pueden ser prototipos desechables;c) No se permiten cambios en los requisitos;d) Se requiere una fase final para corregir errores;e) Las iteraciones suelen incluir cambios de equipo,a;b
```
