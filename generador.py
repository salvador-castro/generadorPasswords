import random
import string

def generar_contrasenia(nivel, longitud):
    if nivel == "bajo":
        caracteres = string.ascii_lowercase
    elif nivel == "medio":
        caracteres = string.ascii_letters + string.digits
    elif nivel == "alto":
        caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Nivel de seguridad no válido. Usa: bajo, medio o alto.")
    
    return "".join(random.choice(caracteres) for _ in range(longitud))