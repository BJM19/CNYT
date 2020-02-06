import unittest,calculadora

class TestCases(unittest.TestCase):
    def test_deberiaSumarDosNumerosComplejos(self):
        a=(-5,2)
        b=(4,-2)
        self.assertEqual(calculadora.suma(a,b),(-1,0))
    def test_deberiaRestarDosNumerosComplejos(self):
        a=(-5,2)
        b=(4,-2)
        self.assertEqual(calculadora.resta(a,b),(-9,4))
    def test_deberiaMultiplicarDosNumerosComplejos(self):
        a=(2,2)
        b=(-2,2)
        self.assertEqual(calculadora.producto(a,b),(-8,0))
    def test_deberiaDividirDosNumerosComplejos(self):
        a=(2,2)
        b=(-2,2)
        self.assertEqual(calculadora.division(a,b),(0.0,-1.0))
    def test_deberiaDarElOpuestoDeUnNumeroComplejo(self):
        a=(-2,-2)
        self.assertEqual(calculadora.opuesto(a),(2,2))
    def test_deberiaDarElConjugadoDeUnNumeroComplejo(self):
        a=(-2,-2)
        self.assertEqual(calculadora.conjugado(a),(-2,2))
    
    def test_deberiaDarElModuloDeUnNumeroComplejo(self):
        a=(2,2)
        self.assertEqual(calculadora.modulo(a),(2.8284271247461903))
    def test_deberiaPasarPolarACartesiano(self):
        a=(2,2)
        self.assertEqual(calculadora.polaresACartesianas(a),(1.9987816540381915, 0.06979899340500194))
    def test_deberiaPasarCartesianasAPolares(self):
        a=(1.9987816540381915, 0.06979899340500194)
        self.assertEqual(calculadora.cartesianasAPolares(a),(1024.0, 2.0))
    def test_deberiaDevolverLaFase(self):
        a=(2,2)
        self.assertEqual(calculadora.fase(a),(0.7853981633974483))
if __name__=="__main__":
    unittest.main()
