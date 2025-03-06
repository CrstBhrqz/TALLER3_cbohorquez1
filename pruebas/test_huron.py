import unittest
from modelos.huron import Huron
from modelos.boa import Boa


# class TestHuron(unittest.TestCase):
#     def setUp(self):
#         print("iniciando setUp")
#         self.huron = Huron("Huron", 400, 5550, "Venezuela", 3.2)
#         print(self.huron.__dict__)

#     def test_hacer_ruido(self):
#         print("iniciando test_hacer_ruido")
#         self.assertEqual(self.huron.hacer_ruido(), print("¡Eek Eek!"))

#     def test_calcular_flete(self):
#         print("iniciando test_calcular_flete")
#         self.assertEqual(self.huron.calcular_flete(), 400*3.2)
    



# class TestBoa(unittest.TestCase):
#     def setUp(self):
#         self.boa = Boa("Boa_Test", 400, 5550, "Venezuela", 6)
#     def test_hacer_ruido(self):
#         print("iniciando test_hacer_ruido")
#         self.assertEqual(self.boa.hacer_ruido(), print("¡Tsss!"))

#     def test_calcular_flete(self):
#         print("iniciando test_calcular_flete")
#         self.assertEqual(self.boa.calcular_flete(), 400*6)
    
#     def test_comer_raton(self):
#         print("iniciando test_comer_raton")
#         ratones_comidos = 5
#         self.assertEqual(self.boa.comer_raton(ratones_comidos), print(f'Éxito'))
    
#     def test_muchos_ratones(self):
#         print("iniciando test_muchos_ratones")
#         ratones_comidos = 6
#         print(self.boa.ratones_comidos)
#         self.assertEqual(self.boa.comer_raton(ratones_comidos), print("Demasiados Ratones!"))


from modelos.guerderia import Guarderia
class TestGuarderia(unittest.TestCase):
    def setUp(self):
        print("iniciando setUp")
        mis_boas = [Boa("Boa_Test_1", 400, 5550, "Venezuela", 6), Boa("Boa_Test_2", 400, 5550, "Venezuela", 6)]
        mis_hurones = [Huron("Huron_A", 400, 5550, "Venezuela", 3.2), Huron("Huron_B", 400, 5550, "Venezuela", 3.2)]
        self.guarderia = Guarderia(mis_boas, mis_hurones)

    def test_buscar_boa_ali(self):
        print("iniciando test_buscar_boa_ali")
        ratones_comidos = 5
        self.assertEqual(self.guarderia.alimentar_boa("Boa_Test_1ss", ratones_comidos),print("Esta Boa no existe!"))


    def test_buscar_boa_llena(self):
        print("iniciando test_buscar_boa_llena")
        ratones_comidos = 10
        self.assertEqual(self.guarderia.alimentar_boa("Boa_Test_1", ratones_comidos),print("Esta Boa no existe!"))


