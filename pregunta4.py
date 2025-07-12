class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

rectangulo = RECTANGULO(6, 4)
print(f"Área del rectángulo: {rectangulo.calcular_area()}")

cuadrado = CUADRADO(5)
print(f"Área del cuadrado: {cuadrado.calcular_area()}")