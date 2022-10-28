
from unittest import TestCase
from Prueba import es_impar

class Test(TestCase):

# Primera prueba unitaria de automatizacion
    def test_es_impar(self):
        resultado = es_impar(5)
#        resultado_esperado = True
#        self.assertEquals(resultado,resultado_esperado)
        self.assertTrue(resultado) # Es lo mismo que las dos líneas anteriores (Asegurarse de que el resultado es True)

    def test_es_impar2(self):
        resultado = es_impar(-1)
        self.assertTrue(resultado)

    def test_no_es_impar(self):
        resultado = es_impar(4)
        self.assertFalse(resultado)