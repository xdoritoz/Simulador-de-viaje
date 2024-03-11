# vehiculo.py
class Vehiculo:
    def __init__(self, marca, modelo, color, anio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.encendido = False
        self.velocidad = 0

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nAño: {self.anio}"

    def encender(self):
        if not self.encendido:
            print("El vehículo está encendido.")
            self.encendido = True
        else:
            print("El vehículo ya está encendido.")

    def apagar(self):
        if self.encendido:
            print("El vehículo está apagado.")
            self.encendido = False
            self.velocidad = 0
        else:
            print("El vehículo ya está apagado.")

    def acelerar(self, velocidad):
        if self.encendido:
            self.velocidad += velocidad
            print(f"El vehículo está acelerando a {self.velocidad} km/h.")
        else:
            print("No puedes acelerar, el vehículo está apagado.")

    def frenar(self):
        if self.velocidad > 0:
            print("El vehículo está frenando.")
            self.velocidad = max(0, self.velocidad - 10)
        else:
            print("El vehículo ya está detenido.")

    def obtener_velocidad(self):
        return self.velocidad

