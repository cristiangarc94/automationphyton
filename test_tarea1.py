
from unittest import TestCase
from tarea1 import mayuscula, numero_palabras

class Test(TestCase):

# Primera prueba unitaria de automatizacion
    #def txt_mayus(self):
     #   resultado = texto()
#        resultado_esperado = True
#        self.assertEquals(resultado,resultado_esperado)
      #  self.assertTrue(resultado) # Es lo mismo que las dos líneas anteriores (Asegurarse de que el resultado es True)

    def test_mayuscula_1(self):
        resultado = mayuscula("hola amigo")
        self.assertEqual(resultado, "HOLA AMIGO")

    def test_mayuscula_2(self):
        resultado = mayuscula("YA MAYUS")
        self.assertEqual(resultado, "YA MAYUS")

    def test_numero_palabras_1(self):
        resultado = numero_palabras(" ")
        self.assertEqual(resultado,0)

    def test_numero_palabras_2(self):
        resultado = numero_palabras("Aqui hay 4 palabras")
        self.assertEqual(resultado,4)