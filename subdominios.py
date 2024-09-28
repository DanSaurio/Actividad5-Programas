'''
Programa para encontrar Subdominios de un sitio.
Explicar que hace este script.
Desarrollado por DanSaurio.com
'''

import requests
from os import path
import argparse
import sys

parse = argparse.ArgumentParser()
print(f'{parse}\n\n')
parse.add_argument('-t', '--target', help='indica el dominio de la victima')
parse = parse.parse_args()

def main():
    if parse.target:
        if path.exists('subdominios.txt'):
            with open('subdominios.txt', 'r') as wordlist:
                wordlist = wordlist.read().splitlines()  # Split by lines

            for subdominio in wordlist:
                url = "http://" + subdominio + "." + parse.target
                #print(url)

                try:
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        print("Se encontró un subdominio: " + url)
                except requests.ConnectionError:
                    pass  # Handle connection errors, e.g. subdomain doesn't exist
        else:
            print("No se encontró el archivo que contiene los subdominios a buscar")
    else:
        print("No se ha indicado un dominio objetivo")
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
