class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        if edad <18: 
            raise MenorEdadException
        else:
            self.edad = edad

class MenorEdadException(Exception):
    def __init__(self, message="La persona es menor de edad"):
        super().__init__(message)
