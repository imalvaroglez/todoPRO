# Bucle for en Python

# Ejemplo 1: Imprimir números del 1 al 10
print("--- Números del 1 al 10 ---")
for i in range(1, 11):
    print(f"Número: {i}")

print("\n--- Números pares del 2 al 20 ---")
for i in range(2, 21, 2):  # range(inicio, fin, paso)
    print(f"Par: {i}")

# Ejemplo 2: Recorrer una lista
print("\n--- Recorrer lista de frutas ---")
frutas = ["manzana", "banana", "naranja", "uva", "mango"]

for fruta in frutas:
    print(f"Fruta: {fruta}")

# Ejemplo 3: Calcular suma de números
print("\n--- Calcular suma de números ---")
numeros = [10, 20, 30, 40, 50]
suma = 0

for num in numeros:
    suma += num
    print(f"Sumando {num} a la total... Total actual: {suma}")

print(f"\n✅ Suma total: {suma}")

# Ejemplo 4: Tabla de multiplicar
print("\n--- Tabla de multiplicar del 7 ---")
numero = 7

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Ejemplo 5: Encontrar el número mayor
print("\n--- Encontrar el número mayor ---")
numeros = [45, 12, 89, 34, 67, 23, 91]
mayor = numeros[0]

for num in numeros:
    if num > mayor:
        mayor = num

print(f"Lista: {numeros}")
print(f"✅ El número mayor es: {mayor}")
