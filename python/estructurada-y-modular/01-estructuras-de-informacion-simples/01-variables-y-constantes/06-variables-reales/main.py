# Variables reales (float) en Python
# Se usan para números con decimales

# Declaración de variables reales
precio = 19.99
altura = 1.75
peso = 70.5
pi = 3.14159

# Imprimir valores
print(f"Precio: ${precio}")
print(f"Altura: {altura} metros")
print(f"Peso: {peso} kg")
print(f"Valor de Pi: {pi}")

# Operaciones con reales
area = pi * (altura * altura)
imc = peso / (altura ** 2)
total_con_iva = precio * 1.16

print(f"\nÁrea (π * altura²): {area:.2f}")
print(f"IMC (peso / altura²): {imc:.2f}")
print(f"Precio con IVA (16%): ${total_con_iva:.2f}")
