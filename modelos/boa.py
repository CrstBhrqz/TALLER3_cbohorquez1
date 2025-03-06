from modelos.animal_exotico import AnimalExotico

class Boa(AnimalExotico):
    def __init__(self, name, weight, age, pais_origen, impuesto):
        super().__init__(name, weight, age, pais_origen, impuesto)
        self.ratones_comidos = 0
        # print("Constructor de la clase Boa")
        # print(self.__dict__)
        
    
    def hacer_ruido(self):
        return print("¡Tsss!")
    
    def comer_raton(self, ratones_comidos):
        
        self.ratones_comidos += ratones_comidos

        if self.ratones_comidos >= 10:
            return print("Demasiados Ratones!")
        
        return "Éxito"
    
    def contar_ratones_comidos(self):
        return print(f"El animal {self.name} ha comido {self.ratones_comidos} ratones.")
    