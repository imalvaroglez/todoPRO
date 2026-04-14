# Operadores aritméticos en Python

a = 10
b = 3

print(f"a = {a}, b = {b}")
print("\n--- Operadores Aritméticos ---")

# Suma (+)
resultado = a + b
print(f"Suma (a + b): {resultado}")

# Resta (-)
resultado = a - b
print(f"Resta (a - b): {resultado}")

# Multiplicación (*)
resultado = a * b
print(f"Multiplicación (a * b): {resultado}")

# División (/) - Resultado real
resultado = a / b
print(f"División (a / b): {resultado:.2f}")

# División entera (//) - Resultado entero sin decimales
resultado = a // b
print(f"División entera (a // b): {resultado}")

# Módulo (%) - Residuo de la división
resultado = a % b
print(f"Módulo (a % b): {resultado}")

# Potencia (**) - Elevar a una potencia
resultado = a ** 2
print(f"Potencia (a ** 2): {resultado}")

# Ejemplo práctico: Calcular cambio de compra
compra = 150
pagado = 200
cambio = pagado - compra

print(f"\n--- Ejemplo Práctico ---")
print(f"Compra: ${compra}")
print(f"Pagado: ${pagado}")
print(f"Cambio: ${cambio}")
