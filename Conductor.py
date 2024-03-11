# conductor.py
class Conductor:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Conductor: {self.nombre}, Edad: {self.edad}"
