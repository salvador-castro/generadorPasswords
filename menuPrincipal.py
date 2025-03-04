from generador import generar_contrasenia
from utils import validar_longitud

def menu_principal():
    print("Generador de Contraseñas")
    nivel = input("Elige el nivel de seguridad (bajo, medio, alto): ").strip().lower()

    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            if validar_longitud(longitud):
                break
            else:
                print("❌ La longitud debe ser mayor a 0.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")

    contraseña = generar_contrasenia(nivel, longitud)
    print(f"🔐 Contraseña generada: {contraseña}")