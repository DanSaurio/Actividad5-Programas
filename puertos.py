import socket
import sys
import argparse
import os

parser = argparse.ArgumentParser(description="Script para buscar puertos abiertos en un dominio.")
parser.add_argument("-t", "--target", help="Indica el dominio del objetivo", required=True)
parser = parser.parse_args()

def main():
    target = parser.target

    if not os.path.exists("puertos.txt"):
        print("El archivo 'puertos.txt' no existe.")
        return

    with open("puertos.txt", "r") as wordlist:
        puertos = wordlist.read().splitlines()

        if not puertos:
            print("El archivo 'puertos.txt' está vacío.")
            return

        for puerto_str in puertos:
            try:
                puerto = int(puerto_str)  
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1) 
                resultado = s.connect_ex((target, puerto))

                if resultado == 0:
                    print(f"El puerto {puerto} está abierto y puede estar en uso.")
                else:
                    print(f"El puerto {puerto} está cerrado o no responde.")

                s.close()
            except ValueError:
                print(f"El valor '{puerto_str}' no es un número de puerto válido.")
            except Exception as e:
                print(f"Ocurrió un error al escanear el puerto {puerto}: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupción por parte del usuario. Saliendo...")
        sys.exit()
