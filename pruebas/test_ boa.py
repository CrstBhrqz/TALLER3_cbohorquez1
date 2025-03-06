import unittest
from modelos.boa import Boa


class TestBoa(unittest.TestCase):
    def setUp(self):
        self.boa = Boa("Boa_Test", 400, 5550, "Venezuela", 6)
    def test_hacer_ruido(self):
        print("iniciando test_hacer_ruido")
        self.assertEqual(self.boa.hacer_ruido(), print("¡Tsss!"))

    def test_calcular_flete(self):
        print("iniciando test_calcular_flete")
        self.assertEqual(self.boa.calcular_flete(), 400*6)
    
