# Variables cadena (string) en Python

# Declaración de cadenas
nombre = "Juan"
apellido = 'Perez'
mensaje = "Hola, mundo!"

print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Mensaje: {mensaje}")

# Concatenación de cadenas
nombre_completo = nombre + " " + apellido
saludo = "Hola, " + nombre + "!"

print(f"\nConcatenación:")
print(f"Nombre completo: {nombre_completo}")
print(f"Saludo: {saludo}")

# f-strings (formato moderno en Python 3.6+)
edad = 25
ciudad = "Guadalajara"
info = f"Me llamo {nombre_completo}, tengo {edad} años y vivo en {ciudad}"

print(f"\nUsando f-strings:")
print(info)

# Operaciones con cadenas
frase = "programación en python es divertida"

print(f"\nFrase original: {frase}")
print(f"En mayúsculas: {frase.upper()}")
print(f"En minúsculas: {frase.lower()}")
print(f"Primera letra mayúscula: {frase.capitalize()}")

# Longitud de una cadena
longitud = len(frase)
print(f"\nLongitud de la frase: {longitud} caracteres")

# Acceder a caracteres específicos
primera_letra = frase[0]
ultima_letra = frase[-1]
print(f"Primera letra: {primera_letra}")
print(f"Última letra: {ultima_letra}")
