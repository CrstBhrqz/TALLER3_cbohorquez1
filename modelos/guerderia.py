
from modelos.huron import Huron
from modelos.boa import Boa

class Guarderia:


    def __init__(self, lista_boas: list[Boa], lista_hurones: list[Huron]):
        self.boas = lista_boas
        self.hurones = lista_hurones

    def alimentar_boa(self, boa, ratones_comidos):
   
        try:

            for animal in self.boas:
  
                if animal.name == boa:
                    return animal.comer_raton(ratones_comidos)
            
            return print("Esta Boa no existe!")
            
        except ValueError as e:
            return print(e)