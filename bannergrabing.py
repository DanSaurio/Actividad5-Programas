import socket
import sys

def banner_grabbing(dominio, puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((dominio, int(puerto)))
        sock.settimeout(5)
        banner = sock.recv(1024)
        
        print(f"Banner recibido desde {dominio}:{puerto}:\n{banner.decode().strip()}")
    
    except socket.timeout:
        print(f"Timeout: No se pudo recibir el banner desde {dominio}:{puerto}.")
    
    except Exception as e:
        print(f"Error al conectar con {dominio}:{puerto}. Detalles: {e}")
    
    finally:
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python3 bannergraby.py -t <dominio> -p <puerto>")
        sys.exit(1)
    
    dominio = ""
    puerto = 0
    
    for i in range(len(sys.argv)):
        if sys.argv[i] == "-t":
            dominio = sys.argv[i+1]
        elif sys.argv[i] == "-p":
            puerto = sys.argv[i+1]
    
    banner_grabbing(dominio, puerto)