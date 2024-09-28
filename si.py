import os
from bannergrabing import banner_grabbing


print("Sistema para pruebas de seguridad informática")
print("Versión 1.0")
print("Desarrollado por: Dan Teran")

x = True
opcion = 0

os.system("cls")

while x:
    print("\nOpción 1: Encontrar subdominios.")
    print("Opción 2: Banner Grabbing.")
    print("Opción 3: Wad.")
    print("Opción 4: Escaneo de Puertos.")
    print("Opción 5: Salir.")
    
    try:
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            vistima = input("Ingrese el dominio: ")
            print("Encontrar subdominios")
            os.system("py programaEncontrarSubdominios.py -t " + vistima)
            input("Presione Enter para continuar...")
            os.system("cls")
        elif opcion == 2:
            vistima = input("Ingrese el dominio: ")
            puerto = input("Ingrese el puerto: ")
            print("Banner Grabbing")
            os.system(f"py bannergraby.py -t {vistima} -p {puerto}")
            input("Presione Enter para continuar...")
            os.system("cls")

        elif opcion == 3:
            print("Wad")
        elif opcion == 4:
            print("Escaneo de Puertos")
        elif opcion == 5:
            print("Saliendo del sistema...")
            x = False
        else:
            print("Opción no válida, intenta de nuevo.")
    
    except ValueError:
        print("Error: Ingrese un número válido.")