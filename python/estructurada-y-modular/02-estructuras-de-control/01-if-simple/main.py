# Estructura if simple en Python

edad = 18

# Verificar si es mayor de edad
if edad >= 18:
    print("✅ Eres mayor de edad")
else:
    print("❌ Eres menor de edad")

print("\n--- Ejemplo 2: Calificación ---")

calificacion = 85

if calificacion >= 90:
    print("¡Excelente! Calificación: A")
elif calificacion >= 80:
    print("¡Muy bien! Calificación: B")
elif calificacion >= 70:
    print("¡Bien! Calificación: C")
elif calificacion >= 60:
    print("¡Aprobado! Calificación: D")
else:
    print("❌ Reprobado. Calificación: F")

print("\n--- Ejemplo 3: Login simple ---")

usuario_correcto = "admin"
password_correcto = "123456"

usuario = input("Usuario: ")
password = input("Contraseña: ")

if usuario == usuario_correcto and password == password_correcto:
    print("✅ ¡Acceso concedido! Bienvenido, admin.")
elif usuario != usuario_correcto:
    print("❌ Usuario incorrecto.")
else:
    print("❌ Contraseña incorrecta.")

print("\n--- Ejemplo 4: Par o Impar ---")

numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es PAR")
else:
    print(f"El número {numero} es IMPAR")
