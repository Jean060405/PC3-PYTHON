def main():
    while True:
        try:
            fraccion = input("Ingrese la cantidad de combustible (X/Y): ")
            x, y = fraccion.strip().split("/")
            x = int(x)
            y = int(y)
            
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                print("Error: el numerador no puede ser mayor que el denominador.")
                continue

            porcentaje = round((x / y) * 100)
            if porcentaje <= 1:
                print("E")
            elif porcentaje >= 99:
                print("F")
            else:
                print(f"{porcentaje}%")
            break

        except ValueError:
            print("Error: solo se permiten números enteros con formato X/Y.")
        except ZeroDivisionError:
            print("Error: el denominador no puede ser cero.")

main()