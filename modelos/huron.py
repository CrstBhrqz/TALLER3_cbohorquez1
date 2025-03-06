from modelos.animal_exotico import AnimalExotico

class Huron(AnimalExotico):
    
    def __init__(self, name:str, weight:float, age:int, pais_origen:str, impuesto:float):
        super().__init__(name, weight, age, pais_origen, impuesto)
        
    def hacer_ruido(self):
        return print("¡Eek Eek!")


