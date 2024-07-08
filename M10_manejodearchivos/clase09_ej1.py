import sys

def main():
    # Verificar que se han pasado exactamente 3 parámetros
    if len(sys.argv) != 4:
        print("Error: Se requieren exactamente 3 parámetros.")
        print("Uso: python clase09_ej1.py <param1> <param2> <param3>")
        return

    # Obtener los parámetros
    param1 = sys.argv[1]
    param2 = sys.argv[2]
    param3 = sys.argv[3]

    # Mostrar los parámetros recibidos
    print(f"Parámetros recibidos: {param1}, {param2}, {param3}")

if __name__ == "__main__":
    main()


