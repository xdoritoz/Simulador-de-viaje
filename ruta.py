# ruta.py
class Ruta:
    def __init__(self, nombre, distancia, tiempo_estimado):
        self.nombre = nombre
        self.distancia = distancia
        self.tiempo_estimado = tiempo_estimado

    def __str__(self):
        return f"Ruta: {self.nombre}\nDistancia: {self.distancia} km\nTiempo estimado: {self.tiempo_estimado} minutos \n"
