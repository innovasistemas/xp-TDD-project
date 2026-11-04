import sys
import os
# Detecta la carpeta raíz del proyecto y la agrega al buscador de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

# Intentar importar algo que todavía no existe de la caja negra llamada "Personas"
try:
    from clases.persona import Persona
except ImportError:
    verificar_mayoria_edad = None

class TestPersonaTDD(unittest.TestCase):

    def test_mayoria_edad(self):
        persona = Persona()
        # persona.agregar_persona("Ana Gil", 20, 200000)
        self.assertTrue(persona.verificar_mayoria_edad)
    
    def test_bonificacion_salario(self):
        persona = Persona()
        self.assertGreaterEqual(persona.bonificacion_salario("5%"), 0)

if __name__ == '__main__':
    unittest.main()