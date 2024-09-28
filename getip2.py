import sys
import argparse
import os

parser = argparse.ArgumentParser(description="Ejecuta nslookup para obtener la IP de un objetivo.")
parser.add_argument("-t", "--target", help="Ingresa la URL sin HTTP", required=True)
args = parser.parse_args()

def ejecutar_nslookup(url):

    command = f"nslookup {url}"
    print(f"Ejecutando comando: {command}")
    
    respuesta = os.system(command)
    
    if respuesta == 0:
        print("El comando se ejecutó exitosamente.")
    else:
        print("Hubo un error al ejecutar el comando.")

def main():
    if args.target:
        ejecutar_nslookup(args.target)
    else:
        print("Ingrese una dirección sin HTTP")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupción por parte del usuario. Saliendo...")
        sys.exit()
