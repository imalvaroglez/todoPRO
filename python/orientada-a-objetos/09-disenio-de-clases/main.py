# Diseño de Clases: Composición vs Herencia (Class Design)
# Ejemplo de elegir entre composición y herencia para resolver un problema

# ==================== PROBLEMA ====================
# Queremos representar vehículos con:
# - Motor (atributos comunes: tipo, potencia, consumo)
# - Comportamientos específicos según el tipo de vehículo

# ==================== OPCIÓN A: COMPOSICIÓN ====================
# Composición: un objeto contiene otros objetos
# "Un vehículo TIENE UN motor"
# El motor es independiente y se puede reutilizar

class Motor:
    def __init__(self, tipo, potencia, consumo):
        self.tipo = tipo
        self.potencia = potencia  # en HP
        self.consumo = consumo # en L/100km

    def descripcion(self):
        return f"Motor {self.tipo} - {self.potencia}HP, {self.consumo}L/100km"

    def arrancar(self):
        return f"⚙️ Motor {self.tipo} arrancando..."

    def apagar(self):
        return f"🔴 Motor {self.tipo} apagado"


class VehiculoComposicion:
    """Vehículo usando COMPOSICIÓN - tiene un motor"""
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor  # COMPOSICIÓN: tiene un motor

    def mostrar_info(self):
        print(f"=== {self.marca} (Composición) ===")
        print(self.motor.descripcion())
        print(self.motor.arrancar())

    def conducir(self):
        return f"Conduciendo {self.marca} con composición"


# ==================== OPCIÓN B: HERENCIA ====================
# Herencia: una clase especializa comportamiento de otra
# "Un vehículo ES UN tipo de motor"
# Crear clases separadas para cada tipo de motor

class MotorBase:
    """Clase base para motores (usando herencia)"""
    def __init__(self, tipo):
        self.tipo = tipo

    def descripcion(self):
        return f"Motor base de tipo: {self.tipo}"

    def arrancar(self):
        return f"🔧 Motor {self.tipo} arrancando..."


class MotorElectrico(MotorBase):
    """Motor eléctrico especializado"""
    def __init__(self, tipo, potencia):
        super().__init__(tipo)
        self.potencia = potencia

    def descripcion(self):
        return f"Motor eléctrico - {self.potencia}HP"

    def arrancar(self):
        return f"⚡ Motor eléctrico zumbando..."


class MotorGasolina(MotorBase):
    """Motor de gasolina especializado"""
    def __init__(self, tipo, cilindros):
        super().__init__(tipo)
        self.cilindros = cilindros

    def descripcion(self):
        return f"Motor de gasolina - {self.cilindros} cilindros"

    def arrancar(self):
        return f"🔧 Motor de gasolina encendido..."


class VehiculoHerencia(VehiculoComposicion):
    """Vehículo usando HERENCIA - ES un tipo de motor específico"""
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor  # HERENCIA: es un tipo específico de motor

    def mostrar_info(self):
        print(f"=== {self.marca} (Herencia) ===")
        print(self.motor.descripcion())
        print(self.motor.arrancar())

    def conducir(self):
        return f"Conduciendo {self.marca} con herencia"


# ==================== DEMOSTRACIÓN ====================
print("\n" + "="*50)
print("COMPOSICIÓN vs HERENCIA")
print("="*50)

# Crear motores reutilizables
motor_v8 = Motor("V8", 200, 8.5)
motor_v6_elec = MotorElectrico("V6 Eléctrico", 150, 7.0)
motor_v4_gas = MotorGasolina("V4 Gas", 120, 6)

# Vehículo con COMPOSICIÓN (puede cambiar de motor fácilmente)
toyota_comp = VehiculoComposicion("Toyota Yaris", motor_v8)
print(toyota_comp.mostrar_info())
print()

# Cambiar de motor (fácil con composición)
print("\nCambando motor en Toyota Yaris (Composición)...")
toyota_comp.motor = motor_v6_elec
print(toyota_comp.mostrar_info())

# Vehículo con HERENCIA (el tipo de motor es fijo)
tesla_herencia = VehiculoHerencia("Tesla Model 3", MotorElectrico("Motor Eléctrico", 450, 5.0))
print(tesla_herencia.mostrar_info())

# Intentar cambiar de motor en Tesla (difícil con herencia)
print("\nIntentando cambiar motor en Tesla Model 3 (Herencia)...")
# tesla_herencia.motor = MotorGasolina("V4 Gas", 120, 6)  # Esto no funciona bien
# tesla_herencia.mostrar_info()

print("\n" + "="*50)
print("COMPOSICIÓN: Más flexible, reutiliza motores, cambio fácil")
print("HERENCIA: Más estricto, define tipo exacto, cambio difícil")
print("="*50)
