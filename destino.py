# destino.py
class Destino:
    def __init__(self, nombre):
        self.nombre = nombre
        self.rutas = []

    def agregar_ruta(self, ruta):
        self.rutas.append(ruta)

    def __str__(self):
        return f"Destino: {self.nombre}\nRutas disponibles:\n{', '.join([str(r) for r in self.rutas])}"

class Ruta:
    def __init__(self, nombre, distancia, tiempo_base, porcentaje_accidentalidad_base):
        self.nombre = nombre
        self.distancia = distancia
        self.tiempo_base = tiempo_base  # Tiempo base sin considerar la velocidad
        self.porcentaje_accidentalidad_base = porcentaje_accidentalidad_base
        self.porcentaje_accidentalidad = 0

    def calcular_tiempo_estimado(self, velocidad):
        tiempo_estimado = (self.tiempo_base / velocidad) * 60  # Convertir minutos a horas
        self.porcentaje_accidentalidad = self.porcentaje_accidentalidad_base + velocidad / 10  # Ajustar accidentalidad
        return tiempo_estimado

    def __str__(self):
        return f"Ruta: {self.nombre}\nDistancia: {self.distancia} km\nTiempo base estimado: {self.tiempo_base} minutos\nPorcentaje base de accidentalidad: {self.porcentaje_accidentalidad_base}%"
