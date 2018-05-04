#! /bin/bash/python3

'''Ejemplo de un script que puede ser importado como módulo y comportarse de forma diferenciada.'''

titulo = "Espacio muestral"
datos = (76, 81, 75, 77, 80, 75, 76, 79, 75)

def promedio(encabezado, muestra):
    '''Despliega el contenido de encabezado,así como el cálculo del promedio de muestra, 
    ingresado en una lista o tupla.'''  
    print("El promedio de %s con %d elementos es %f." % (titulo, len(muestra), sum(muestra) / len(muestra)))

if __name__ == "__main__": 
    promedio(titulo, datos)