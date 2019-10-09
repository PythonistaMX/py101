#! /usr/bin/python3
'''Funciones que calculan número primos.'''

def esprimo(lista, numero):
    '''Valida si numero es divisible entre algún elemento de lista. De ocurrir, 
    regresa False. De lo contrario, regresa True.'''
    for primo in lista:
        if numero % primo == 0:
            return False
    return True


def lista_primos(limite):
    '''Genera una lista de los números primos comprendidos entre el 2 y el valor de limite.'''
    #La lista inicia con el número 2
    lista = [2]
    #Se realizará una iteración de cada número entero desde 3 hasta el valor de limite.
    for numero in range(3, limite + 1):
        #Si esprimo(numero) regresa True, añade el valor de numero a lista
        if esprimo(lista, numero):
            lista.append(numero)
    return lista


def gen_primos():
    """ Generador de números primos."""  
    contador = 1
    lista_primos=[]
    # Comienza una secuencia infinita.
    while True:
        primo = True
        contador += 1
        if len(lista_primos) > 0:
            primo = esprimo(lista_primos, contador)
        if primo:
            lista_primos.append(contador)
            yield contador         