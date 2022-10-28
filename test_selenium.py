
from unittest import TestCase
from selenium_login2 import hacer_login


class Test(TestCase):
    RUTA_IMAGENES = '/Users/1531293/Pictures'
    def test_hacer_login_correcto(self):
        resultado = hacer_login('admin', '12345', 'correcto', Test.RUTA_IMAGENES)
        self.assertEqual(resultado,"WELCOME :)")

    def test_hacer_login_incorrecto_password(self):
        resultado = hacer_login('admin', 'MAL', 'password_incorrecto', Test.RUTA_IMAGENES)
        self.assertEqual(resultado,"ACCESS DENIED!")

    def test_hacer_login_incorrecto_usuario(self):
        resultado = hacer_login('MAL', '12345', 'usuario_incorrecto', Test.RUTA_IMAGENES)
        self.assertEqual(resultado,"ACCESS DENIED!")

    def test_hacer_login_incorrecto(self):
        resultado = hacer_login('admin1', '12345A', 'incorrecto', Test.RUTA_IMAGENES)
        self.assertEqual(resultado,"ACCESS DENIED!")

    def test_hacer_login_vacio(self):
        resultado = hacer_login('', '', 'vacio')
        self.assertEqual(resultado,"ACCESS DENIED!")