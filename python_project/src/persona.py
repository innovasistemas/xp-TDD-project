
class Persona():

    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.salario = 0

    def get_nombre(self) -> str:
        return self.nombre 
    
    def get_edad(self) -> int:
        return self.edad 
    
    def get_salario(self) -> float:
        return self.salario 

    def set_nombre(self, nombre) -> None:
        self.nombre = nombre

    def set_salario(self, salario) -> None:
        self.salario = salario
    
    def set_edad(self, edad) -> None:
        self.edad = edad

    def categoria_edad(self) -> str:
        if self.edad < 14:
            return "Niño"
        elif self.edad <= 28:
            return "Joven"
        else:
            return "Adulto"

    def verificar_mayoria_edad(self) -> bool:
        return self.edad >= 18

    def bonificacion_salario(self, bonificacion) -> float:
        if self.salario > 0:
            return bonificacion * 100 / self.salario
        return 0

