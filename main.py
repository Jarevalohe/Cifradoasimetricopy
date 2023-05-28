from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generar las claves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Exponente público 65537 por defecto
    key_size=2048  # Tamaño de la clave en bits
)

public_key = private_key.public_key()

# Cifrado
mensaje = b"Mensaje a codificar"

# Cifrar el mensaje utilizando la clave pública
cifrado = public_key.encrypt(
    mensaje,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Algoritmo de generación de máscara
        algorithm=hashes.SHA256(),  # Algoritmo hash
        label=None  # Etiqueta opcional
    )
)

# Descifrado
# Descifrar el mensaje utilizando la clave privada correspondiente
descifrado = private_key.decrypt(
    cifrado,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Imprimir los resultados
print("Mensaje original:", mensaje)
print("Mensaje cifrado:", cifrado)
print("Mensaje descifrado:", descifrado)
