# main.py
import time

from Simulacion.Vehiculo import Vehiculo
from Simulacion.Automovil import Automovil
from Simulacion.Conductor import Conductor
from Simulacion.destino import Destino, Ruta

def main():
    # Crear destinos y rutas
    destino1 = Destino("Playa")
    destino1.agregar_ruta(Ruta("Ruta Directa", 30, 20, 5))
    destino1.agregar_ruta(Ruta("Ruta Escénica", 40, 30, 8))

    destino2 = Destino("Montañas")
    destino2.agregar_ruta(Ruta("Ruta Rápida", 60, 40, 7))
    destino2.agregar_ruta(Ruta("Ruta Panorámica", 80, 50, 10))

    destino3 = Destino("Ciudad")
    destino3.agregar_ruta(Ruta("Ruta Principal", 20, 15, 3))
    destino3.agregar_ruta(Ruta("Ruta Alternativa", 25, 20, 5))

    destinos = [destino1, destino2, destino3]

    # Ejemplo de uso
    auto = Automovil("Toyota", "Corolla", "Rojo", 2023, 4, "Automática")
    conductor = Conductor("Juan", 30)

    print(auto)
    print(conductor)

    auto.encender()

    # Permitir al usuario personalizar el automóvil
    personalizar = input("¿Desea personalizar su automóvil? (Sí/No): ").lower()
    if personalizar == "si":
        auto.personalizar_automovil()

    # Permitir al usuario definir la velocidad
    velocidad_deseada = float(input("Ingrese la velocidad deseada (km/h): "))
    auto.acelerar(velocidad_deseada)

    # Mostrar destinos y rutas disponibles
    print("Destinos disponibles:")
    for i, destino in enumerate(destinos, 1):
        print(f"{i}. {destino.nombre}")

    # Permitir al usuario elegir el destino
    seleccion_destino = int(input("Seleccione el destino: "))
    destino_elegido = destinos[seleccion_destino - 1]

    print(f"\n{destino_elegido}\n")

    # Mostrar rutas disponibles para el destino elegido
    print("Rutas disponibles:")
    for i, ruta in enumerate(destino_elegido.rutas, 1):
        print(f"{i}. {ruta.nombre}")
        print(f"   {ruta}")

    # Permitir al usuario elegir la ruta
    seleccion_ruta = int(input("Seleccione la ruta: "))
    ruta_elegida = destino_elegido.rutas[seleccion_ruta - 1]

    # Calcular tiempo estimado de llegada con velocidad promedio de 30 km/h
    tiempo_estimado_promedio = ruta_elegida.calcular_tiempo_estimado(30)

    # Calcular tiempo total de viaje considerando la velocidad seleccionada por el usuario
    tiempo_estimado = ruta_elegida.calcular_tiempo_estimado(velocidad_deseada)

    # Mostrar detalles de la ruta y tiempo estimado de llegada
    print(f"\nRuta seleccionada: {ruta_elegida.nombre}")
    print(f"Distancia: {ruta_elegida.distancia} km")
    print(f"Tiempo estimado de llegada: {int(tiempo_estimado / 60)} horas ({int(tiempo_estimado)} minutos)")
    print(f"Porcentaje de accidentalidad: {ruta_elegida.porcentaje_accidentalidad}%")

    # Simulación de viaje con barra de progreso
    print("\nIniciando viaje...\n")
    tiempo_restante = min(tiempo_estimado, 5 * 60)  # Mínimo entre tiempo estimado y 5 minutos
    tiempo_transcurrido = 0

    while tiempo_transcurrido < tiempo_restante:
        time.sleep(1)  # Esperar 1 segundo
        tiempo_transcurrido += 1
        porcentaje_progreso = (tiempo_transcurrido / tiempo_restante) * 100
        print(f"Viajando... {porcentaje_progreso:.2f}% completado")

    print("\n¡Ha llegado a su destino!")
    tiempo_total_real = tiempo_estimado_promedio * (tiempo_transcurrido / tiempo_restante)
    tiempo_total_formato = time.strftime("%H:%M:%S", time.gmtime(tiempo_total_real))

    print(f"Porcentaje de accidentalidad durante el viaje: {ruta_elegida.porcentaje_accidentalidad}%")

    auto.apagar()

if __name__ == "__main__":
    main()
