import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()

    fuente_usuario = input("Ingrese el nombre de la fuente (o presione Enter para elegir una aleatoria): ").strip()

    if fuente_usuario == "":
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Fuente aleatoria seleccionada: {fuente_seleccionada}")
    elif fuente_usuario in fuentes_disponibles:
        fuente_seleccionada = fuente_usuario
    else:
        print("Fuente no válida. Se usará una fuente aleatoria.")
        fuente_seleccionada = random.choice(fuentes_disponibles)

    figlet.setFont(font=fuente_seleccionada)

    texto = input("Ingrese el texto que desea imprimir: ")
    print("\n" + figlet.renderText(texto))

if __name__ == "__main__":
    main()
