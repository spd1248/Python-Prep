import csv
import datetime
import sys


def registrar_datos(temperatura, humedad, llovio):
    archivo = 'clase09_ej2.csv'
    tiempo_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(archivo, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tiempo_actual, temperatura, humedad, llovio])


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python clase09_ej2.py2 <temperatura> <humedad> <llovio>")
        sys.exit(1)

    temperatura = float(sys.argv[1])
    humedad = float(sys.argv[2])
    llovio = sys.argv[3].lower() in ['true', '1', 't', 'y', 'yes']

    registrar_datos(temperatura, humedad, llovio)
    print("Datos registrados correctamente.")
