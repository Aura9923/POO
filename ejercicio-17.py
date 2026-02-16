import math
class Circulo:

    def area(radio):
        return math.pi * radio ** 2

    def perimetro(radio):
        return 2 * math.pi *radio

radio = 3
print("Area:", Circulo.area(radio))
print("Perimetro:", Circulo.perimetro(radio))