class Edades:

    def edad_alberto(edad_juan):
        return 2 * edad_juan / 3

    def edad_ana(edad_juan):
        return 4 * edad_juan / 3

    def edad_mama(edad_juan, edad_alberto, edad_ana):
        return edad_juan + edad_alberto + edad_ana


edad_juan = 9

edad_alberto = Edades.edad_alberto(edad_juan)
edad_ana = Edades.edad_ana(edad_juan)
edad_mama = Edades.edad_mama(edad_juan, edad_alberto, edad_ana)

print("Las edades son:")
print("ALberto:", int(edad_alberto))
print("Juan:", edad_juan)
print("Ana:", int(edad_ana))
print("Mamá:", int(edad_mama))
