'''Funciones que calculan el promedio de una serie arbitaria de números.'''

def promedio(*muestras):
    '''Calcula el promedio de la muestra correspondiente a todos los parámetros ingresados.'''
    if not muestras:
        return 0.0
    return sum(muestras)/len(muestras)
    
def promedio_titulo(titulo, *muestras):
    '''Calcula el promedio de la muestra correspondiente a todos los parámetros ingresados con excepción
       del primero, el cual será utilizado como título.'''
    if not muestras:
        print(f"{titulo}: No hay datos.")
        return
    p = sum(muestras)/len(muestras)
    print(f"{titulo}\nEl promedio de la muestra de {len(muestras)} elementos es {p:.3f}.")
        
if __name__ == "__main__":
    promedio_titulo("Muestra de demostración", 16, 15.5, 17.2, 18.6, 15.3, 16.7, 18, 16.1, 17.2)
