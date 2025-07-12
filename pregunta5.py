
class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.nota = None

    def display(self):
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Número de registro: {self.registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.nota is not None:
            print(f"Nota: {self.nota}")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.nota = nota
