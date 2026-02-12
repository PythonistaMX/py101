import sys
from .promedios import promedio

def main():
    if len(sys.argv) > 1:
        try:
            datos = [float(x) for x in sys.argv[1:]]
            print(f"El promedio es: {promedio(*datos)}")
        except ValueError:
            print("Por favor ingrese solo números.")
    else:
        print("Uso: python -m paquete <numeros>")

if __name__ == "__main__":
    main()
