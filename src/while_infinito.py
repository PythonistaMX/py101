#! /usr/bin/python3
'''Este es un ciclo infinito, del cual solo se puede salir 
cuando se ingrese la cadena despedida.'''

suma = 0
while True:
    entrada = input("Clave:")
    if entrada == "despedida":
        break
    suma = suma + 1
    print("Intento %d. \n " % suma)
print("Tuviste %d intentos fallidos." % suma)