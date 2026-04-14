# Clases y Objetos en Python

# Definición de una clase
class Persona:
    # Constructor (método __init__)
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad    # Atributo

    # Método para mostrar información
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    # Método para saludar
    def saludar(self):
        print(f"¡Hola, soy {self.nombre}!")

# Crear objetos de la clase Persona
print("--- Crear objetos ---")
persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)

# Usar los métodos de los objetos
print("\n--- Persona 1 ---")
persona1.mostrar_info()
persona1.saludar()

print("\n--- Persona 2 ---")
persona2.mostrar_info()
persona2.saludar()

# Ejemplo 2: Clase Rectángulo
print("\n--- Ejemplo Rectángulo ---")

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Crear un rectángulo
rectangulo1 = Rectangulo(5, 3)
rectangulo2 = Rectangulo(8, 4)

print("Rectángulo 1 (5 x 3):")
print(f"  Área: {rectangulo1.calcular_area()}")
print(f"  Perímetro: {rectangulo1.calcular_perimetro()}")

print("\nRectángulo 2 (8 x 4):")
print(f"  Área: {rectangulo2.calcular_area()}")
print(f"  Perímetro: {rectangulo2.calcular_perimetro()}")

# Ejemplo 3: Clase Estudiante
print("\n--- Ejemplo Estudiante ---")

class Estudiante:
    def __init__(self, nombre, matricula, calificacion):
        self.nombre = nombre
        self.matricula = matricula
        self.calificacion = calificacion

    def aprobo(self):
        return self.calificacion >= 60

    def mostrar_informacion(self):
        estado = "✅ APROBADO" if self.aprobo() else "❌ REPROBADO"
        print(f"Nombre: {self.nombre}")
        print(f"Matrícula: {self.matricula}")
        print(f"Calificación: {self.calificacion}")
        print(f"Estado: {estado}")

# Crear estudiantes
estudiante1 = Estudiante("Carlos", "A001", 75)
estudiante2 = Estudiante("Ana", "A002", 58)

print("Estudiante 1:")
estudiante1.mostrar_informacion()

print("\nEstudiante 2:")
estudiante2.mostrar_informacion()
