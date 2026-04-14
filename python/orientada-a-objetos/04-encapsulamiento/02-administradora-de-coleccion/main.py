# Manejo de Objetos (Object Management) en Python
# Administrar coleiones de objetos usando listas

class AdminCirculos:
    def __init__(self):
        # Lista privada para guardar los círculos (no accesible directamente desde fuera)
        self._circulos = []

    def agregar(self, circulo):
        """Agrega un círculo a la colección"""
        self._circulos.append(circulo)
        return True

    def eliminar(self, circulo):
        """Elimina un círculo de la colección"""
        if circulo in self._circulos:
            self._circulos.remove(circulo)
            return True
        else:
            return False

    def buscar_por_area(self, area_max):
        """Busca círculos con área mayor a un valor"""
        encontrados = []
        for circulo in self._circulos:
            area = circulo.dame_area()
            if area > area_max:
                encontrados.append(circulo)
        return encontrados

    def buscar_por_color_borde(self, color):
        """Busca todos los círculos con un color de borde específico"""
        encontrados = []
        for circulo in self._circulos:
            if circulo.color_borde == color:
                encontrados.append(circulo)
        return encontrados

    def limpiar(self):
        """Elimina todos los círculos"""
        self._circulos.clear()
        return True

    def contar(self):
        """Regresa el número de círculos en la colección"""
        return len(self._circulos)


# Definición simple de la clase Circulo (para los ejemplos)
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def dame_area(self):
        """Calcula el área del círculo"""
        return 3.14159 * self.radio * self.radio


# Uso de la clase administradora
admin = AdminCirculos()

# Agregar algunos círculos
c1 = Circulo(5)
c2 = Circulo(10)
c3 = Circulo(15)

admin.agregar(c1)
admin.agregar(c2)
admin.agregar(c3)

print(f"Círculos agregados: {admin.contar()}")

# Buscar círculos con área > 200
grandes = admin.buscar_por_area(200)
print(f"Círculos con área > 200: {len(grandes)}")
for c in grandes:
    print(f"  - Área: {c.dame_area():.2f}")

# Eliminar un círculo
if admin.eliminar(c2):
    print("Círculo eliminado con éxito")
else:
    print("Error al eliminar círculo")

print(f"Círculos restantes: {admin.contar()}")
