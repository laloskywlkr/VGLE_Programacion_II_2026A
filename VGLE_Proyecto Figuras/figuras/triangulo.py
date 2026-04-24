from figuras. abstracta import Figura

class Triangulo(Figura):
    def __init__(self, base, altura, lado_a, lado_b, lado_c):
        self.base = base
        self.altura = altura
        self.lados = [lado_a, lado_b, lado_c]

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return sum(self.lados)