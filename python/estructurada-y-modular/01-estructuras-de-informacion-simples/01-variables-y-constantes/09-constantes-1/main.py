# Constantes en Python
# Por convención, las constantes se escriben en MAYÚSCULAS
# Python no tiene verdaderas constantes, pero es una buena práctica

# Constantes definidas
PI = 3.14159
GRAVEDAD = 9.8
IVA = 0.16
MAX_ALUMNOS = 30
SALARIO_MINIMO = 207.44

# Uso de constantes
print("--- Constantes Definidas ---")
print(f"PI: {PI}")
print(f"GRAVEDAD: {GRAVEDAD} m/s²")
print(f"IVA: {IVA * 100}%")
print(f"MÁXIMO DE ALUMNOS: {MAX_ALUMNOS}")
print(f"SALARIO MÍNIMO: ${SALARIO_MINIMO}")

# Cálculos usando constantes
radio = 5
area = PI * (radio ** 2)

print(f"\n--- Cálculo de Área ---")
print(f"Radio: {radio}")
print(f"Área del círculo: {area:.2f}")

# Cálculo de precio con IVA
precio_sin_iva = 100
precio_con_iva = precio_sin_iva * (1 + IVA)

print(f"\n--- Cálculo de IVA ---")
print(f"Precio sin IVA: ${precio_sin_iva}")
print(f"Precio con IVA: ${precio_con_iva:.2f}")

# Validación usando constante
num_alumnos_actuales = 25

print(f"\n--- Validación ---")
print(f"Alumnos actuales: {num_alumnos_actuales}")
print(f"Máximo permitido: {MAX_ALUMNOS}")

if num_alumnos_actuales < MAX_ALUMNOS:
    cupos_disponibles = MAX_ALUMNOS - num_alumnos_actuales
    print(f"✅ Cupos disponibles: {cupos_disponibles}")
else:
    print("❌ Se ha alcanzado el máximo de alumnos")
