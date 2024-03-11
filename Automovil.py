# automovil.py
from Simulacion.Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color, anio, num_puertas, tipo_transmision):
        super().__init__(marca, modelo, color, anio)
        self.num_puertas = num_puertas
        self.tipo_transmision = tipo_transmision

    def __str__(self):
        return super().__str__() + f"\nNúmero de puertas: {self.num_puertas}\nTipo de transmisión: {self.tipo_transmision}"

    def personalizar_automovil(self):
        print("Personalizar automóvil:")
        self.marca = input("Nueva marca: ")
        self.modelo = input("Nuevo modelo: ")
        self.color = input("Nuevo color: ")
        self.anio = int(input("Nuevo año: "))
        self.num_puertas = int(input("Número de puertas: "))
        self.tipo_transmision = input("Tipo de transmisión: ")

        print("Automóvil personalizado con éxito!")
