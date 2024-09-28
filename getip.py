"""
Primera Forma: nslookup (url)
Segunda Forma: nslookup.io
Tercera Forma: nxtoolbox.com
Cuarta Forma: script pythonoso
"""


import sys
import argparse
import socket 


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="Ingresa la URL sin HTTP", required=True)
args = parser.parse_args()

def get_ip_lokochon(url):
    try:
        ip = socket.gethostbyname(url)
        print(f"La dirección IP de {url} es: {ip}")
    except Exception as e:
        print(f"No se pudo obtener la IP: {e}")

def main():
    if args.target:
        get_ip_lokochon(args.target)
    else:
        print("Ingrese una dirección sin HTTP")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
