'''Funciones que calculan el promedio de una serie arbitaria de números.'''

def promedio(*muestras):
    '''Calcula el promedio de la muestra correspondiente a todos los parámetros ingresados.'''
    print(promedio = sum(muestras)/len(muestras))
    
def promedio_titulo(titulo, *muestras):
    '''Calcula el promedio de la muestra correspondiente a todos los parámetros ingresados con excepción
       del primero, el cual será utilizado como título.'''
    promedio = sum(muestras)/len(muestras)
    print(titulo)
    print('El promedio de la muestra de %d elementos es %.3f.' %(len(muestras), promedio))
    
print(__name__)
    
if __name__ == "__main__":
    promedio_titulo("Muestra de demostración", 16, 15.5, 17.2, 18.6, 15.3, 16.7, 18, 16.1, 17,2)  