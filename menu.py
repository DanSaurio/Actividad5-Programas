import os
import argparse
import sys
import subprocess

def buscar_subdominios(target):
    if os.path.exists('subdominios.txt'):
        with open('subdominios.txt', 'r') as wordlist:
            subdominios = wordlist.read().splitlines()

        for subdominio in subdominios:
            url = f"http://{subdominio}.{target}"
            print(f"Probando subdominio: {url}")
      
    else:
        print("El archivo 'subdominios.txt' no existe.")

def ejecutar_comando_python(script, target):
    try:
        subprocess.run(['python', script, '-t', target], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar {script}: {e}")

def menu_principal():
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Limpia la consola
        
        print("Sistema Para Pruebas De Seguridad Informático")
        print("Versión 1.0 Desarrollado por Angel Nava")
        print("1. Búsqueda de subdominios")
        print("2. Banner grabbing (getip.py)")
        print("3. Información adicional (getip2.py)")
        print("4. Escaneo de puertos")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            vistima = input("Por favor, indique el dominio objetivo: ")
            buscar_subdominios(vistima)
        elif opcion == "2":
            vistima = input("Por favor, indique el dominio objetivo: ")
            ejecutar_comando_python('getip.py', vistima)
        elif opcion == "3":
            vistima = input("Por favor, indique el dominio objetivo: ")
            ejecutar_comando_python('getip2.py', vistima)
        elif opcion == "4":
            print("Escaneo de puertos aún no implementado.")
            input("Presiona Enter para volver al menú...")
        elif opcion == "5":
            print("Saliendo...")
            sys.exit()
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu_principal()
