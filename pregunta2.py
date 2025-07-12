def main():
    entrada = input("Ingrese calificaciones separadas por comas: ")
    calificaciones_str = entrada.split(",")
    calificaciones = []

    try:
        for nota in calificaciones_str:
            nota = nota.strip()  # elimina espacios en blanco
            calificaciones.append(int(nota))
        print("Calificaciones válidas:", calificaciones)
    except ValueError:
        print("Error: Asegúrese de ingresar solo números enteros separados por comas.")

main()