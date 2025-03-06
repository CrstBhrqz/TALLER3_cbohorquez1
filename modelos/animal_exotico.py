from modelos.animal import Animal

class AnimalExotico(Animal):
    
        
    def __init__(self,name:str, weight:float, age:int, pais_origen:str, impuesto:float):
        # Super hbala de la clase padre animal 
        super().__init__(name, weight, age) # parametros requeridos del padre 
        # parametro propios de la clase
        self.pais_origen = pais_origen
        self.impuesto = impuesto
        # print("Constructor de la clase AnimalExotico")
        # print(self.__dict__)
        
    def calcular_flete(self):
        return self.weight * self.impuesto
        