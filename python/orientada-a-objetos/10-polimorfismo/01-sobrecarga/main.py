# Sobrecarga de Métodos (Function Overloading) en Python

# Python no tiene sobrecarga de métodos como C++, pero podemos lograr
# funcionalidad similar usando argumentos con valores por defecto

class Empleado:
    # Constantes de clase
    SALARIO_BASE = 10000
    EDAD_MINIMA = 18

    def __init__(self, nombre, edad, salario=None):
        self.nombre = nombre
        self.edad = edad
        # Si no se proporciona salario, usa el salario base
        self.salario = salario if salario is not None else self.SALARIO_BASE

    def fijar_datos(self, nombre):
        """Sobrecarga 1: solo nombre"""
        self.nombre = nombre

    def fijar_datos_completo(self, nombre, edad):
        """Sobrecarga 2: nombre y edad"""
        self.fijar_datos(nombre)
        self.edad = edad

    def fijar_datos_todo(self, nombre, edad, salario):
        """Sobrecarga 3: nombre, edad y salario"""
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def dame_info(self):
        """Método para obtener información del empleado"""
        return f"---Datos del empleado---\nNombre: {self.nombre}\nEdad: {self.edad}\nSalario: ${self.salario:.2f}"


# Crear empleados usando diferentes combinaciones de parámetros
print("--- Creación con diferentes parámetros ---")

emp1 = Empleado("Juan", 25)
print(emp1.dame_info())

emp2 = Empleado("María", 30, 35000)
print(emp2.dame_info())

emp3 = Empleado("Carlos", 28)
print(emp3.dame_info())
