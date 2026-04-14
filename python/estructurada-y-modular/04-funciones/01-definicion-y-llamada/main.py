# Funciones en Python

# Definición de una función simple
def saludar():
    print("¡Hola desde la función!")

# Llamada a la función
print("--- Función simple ---")
saludar()

# Función con parámetro
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

print("\n--- Función con parámetro ---")
saludar_persona("Juan")
saludar_persona("María")

# Función con retorno
def suma(a, b):
    return a + b

print("\n--- Función con retorno ---")
resultado = suma(10, 5)
print(f"Suma de 10 + 5 = {resultado}")

# Función con múltiples parámetros y retorno
def calcular_promedio(num1, num2, num3):
    promedio = (num1 + num2 + num3) / 3
    return promedio

print("\n--- Calcular promedio ---")
promedio = calcular_promedio(85, 90, 78)
print(f"Promedio de 85, 90, 78 = {promedio:.2f}")

# Función con parámetro por defecto
def saludar_con_hora(nombre, hora="amigo"):
    print(f"¡Hola, {hora} {nombre}!")

print("\n--- Función con parámetro por defecto ---")
saludar_con_hora("Juan")
saludar_con_hora("María", "amiga")

# Función que verifica si un número es par
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print("\n--- Verificar si es par ---")
print(f"¿Es 4 par? {es_par(4)}")
print(f"¿Es 7 par? {es_par(7)}")
print(f"¿Es 10 par? {es_par(10)}")

# Función con múltiples retornos
def clasificar_edad(edad):
    if edad < 18:
        return "Menor de edad"
    elif edad < 30:
        return "Joven adulto"
    elif edad < 60:
        return "Adulto"
    else:
        return "Adulto mayor"

print("\n--- Clasificar edad ---")
print(f"Edad 15: {clasificar_edad(15)}")
print(f"Edad 25: {clasificar_edad(25)}")
print(f"Edad 45: {clasificar_edad(45)}")
print(f"Edad 70: {clasificar_edad(70)}")
